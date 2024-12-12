# 🔐 Code Guessing Tool

## 📝 Description
This tool is designed to discover whether an email is associated with an account on the target website by attempting to guess the verification codes associated with accounts using various methods. It can be used to test how the system handles verification codes in account recovery pages.

## ⚠️ Legal Disclaimer
- **Use of the Tool Legally**: You must ensure that you are using this tool in a test environment with explicit permission from the website owner.
- **Ethical Use**: Ensure that you use the tool ethically for research or educational purposes only.
- **Compliance with Local Laws**: Before using the tool on any website, make sure you have permission to test it.
  
**Warning**: Unauthorized use of this tool on any website without explicit permission is illegal and unethical. You are solely responsible for your actions when using this tool.

## 🛠️ How to Use

### Requirements:
- Python 3.x
- Required Python libraries:
  ```bash
  pip install requests beautifulsoup4
  ```

### Setup Steps:
1. **Download the Tool**:
   - Clone the repository or download the source files directly from GitHub.

2. **Prepare the Email File**:
   - Create a text file (`emails.txt`) containing the list of emails you want to test. Each email should be on a new line.

3. **Configure the Tool**:
   - In the script, modify the `url` and `headers` variables to match the target website's settings. Make sure to set the correct target URL and adjust any necessary headers like User-Agent, Content-Type, etc.

4. **Run the Tool**:
   - Run the script via the following command in your terminal:
     ```bash
     python code_guessing_tool.py
     ```

### Viewing Results:
- When the tool finds valid codes for any email, it will display results like this:
  ```
  [SUCCESS] Valid code found:
  Email: example@example.com, Valid Code: 1234
  ```
  
- If no valid codes are found, the output will indicate failure:
  ```
  [FAILED] No valid code found.
  ```

### Important Messages:
- **[INFO]**: General information or status messages.
- **[ERROR]**: Errors encountered, such as connection issues or invalid responses.
- **[VALID CODE FOUND]**: A valid code has been found for an email address.
- **[INVALID]**: The guessed code is invalid for the given email.
- **[NO RESPONSE]**: The target server did not respond as expected for a particular guess.

## 📋 Key Functions in the Code:

1. **`check_code()`**:
   - This function checks the validity of a guessed code for a given email by sending a POST request to the target website. If a valid response is received (e.g., JSON response with success or error messages), it processes and prints the result accordingly.

2. **`guess_codes()`**:
   - This function manages the code-guessing process. It attempts every code from 1000 to 9999, sending requests for each code to the target URL and checking the response. If a valid code is found, it is added to the list of valid codes and printed.

3. **`check_website()`**:
   - Verifies that the target website is up and running. It sends a simple GET request to the specified URL and checks if the response status is 200 (OK). If the website is down or inaccessible, the script will exit.

4. **`load_emails_from_file()`**:
   - This function loads the emails from a text file (`emails.txt`). It reads each line as a separate email address and stores them in a list for further processing. If the file is not found or cannot be read, an error is printed.

## 🏆 Tool Results:
- If valid codes are found, the email and the valid code will be displayed in the terminal:
  ```
  [SUCCESS] Valid code found:
  Email: example@example.com, Valid Code: 1234
  The web page code will be shown to you
  ```

- If no valid codes are found after all attempts, a failure message will be displayed:
  ```
  [FAILED] No valid code found.
  ```

## 🤝 Contributing:
---

**Note**: This tool was developed using Python and leverages libraries such as `requests` and `BeautifulSoup` to parse the website's responses. It is essential to use this tool responsibly and only on systems that you have explicit permission to test.

---

Thank you for using this tool, and feel free to provide feedback or ask questions via the Issues section of the repository.

---

# 🔐 أداة تخمين الرموز

## 📝 الوصف
تم تصميم هذه الأداة لاكتشاف ما إذا كان الإيميل مرتبطًا بحساب على الموقع المستهدف من خلال محاولة تخمين الرموز المرتبطة بالحسابات باستخدام طرق مختلفة. يمكن استخدامها لاختبار كيفية تعامل النظام مع الرموز في صفحات استرجاع الحساب.

## ⚠️ التنبيه القانوني
- **استخدام الأداة بشكل قانوني**: يجب التأكد من أنك تستخدم هذه الأداة في بيئة اختبار وبإذن صريح من مالك الموقع.
- **الاستخدام الأخلاقي**: تأكد من استخدام الأداة بطريقة أخلاقية لأغراض البحث أو التعليم فقط.
- **الامتثال للقوانين المحلية**: قبل استخدام الأداة على أي موقع، تأكد من أنك حصلت على إذن لاختباره.

**تحذير**: الاستخدام غير المصرح به لهذه الأداة على أي موقع دون إذن صريح هو غير قانوني وغير أخلاقي. أنت المسؤول الوحيد عن أفعالك عند استخدام هذه الأداة.

## 🛠️ كيفية الاستخدام

### المتطلبات:
- Python 3.x
- المكتبات المطلوبة:
  ```bash
  pip install requests beautifulsoup4
  ```

### خطوات الإعداد:
1. **تنزيل الأداة**:
   - قم باستنساخ المستودع أو تحميل ملفات المصدر مباشرة من GitHub.

2. **تحضير ملف الإيميلات**:
   - قم بإنشاء ملف نصي (`emails.txt`) يحتوي على قائمة الإيميلات التي ترغب في اختبارها. يجب أن يكون كل إيميل في سطر جديد.

3. **تكوين الأداة**:
   - في السكربت، قم بتعديل متغيرات `url` و `headers` لتتناسب مع إعدادات الموقع المستهدف. تأكد من تعيين الرابط الصحيح وضبط أي رؤوس ضرورية مثل `User-Agent` و `Content-Type` إلخ.

4. **تشغيل الأداة**:
   - قم بتشغيل السكربت عبر الأمر التالي في الطرفية:
     ```bash
     python code_guessing_tool.py
     ```

### مشاهدة النتائج:
- عندما تجد الأداة الرموز الصالحة لأي إيميل، ستعرض النتائج على النحو التالي:
  ```
  [SUCCESS] تم العثور على رمز صالح:
  البريد الإلكتروني: example@example.com، الرمز الصالح: 1234
  ```

- إذا لم يتم العثور على أي رموز صالحة، ستعرض الأداة رسالة فشل:
  ```
  [FAILED] لم يتم العثور على أي رمز صالح.
  ```

### الرسائل الهامة:
- **[INFO]**: رسائل معلوماتية أو حالة.
- **[ERROR]**: الأخطاء التي تم اكتشافها، مثل مشاكل الاتصال أو الاستجابات غير الصالحة.
- **[VALID CODE FOUND]**: تم العثور على رمز صالح لإيميل.
- **[INVALID]**: الرمز الذي تم تخمينه غير صالح للإيميل المحدد.
- **[NO RESPONSE]**: لم تستجب الخوادم المستهدفة بالطريقة المتوقعة في تخمين معين.

## 📋 الوظائف الرئيسية في الكود:

1. **`check_code()`**:
   - تقوم هذه الوظيفة بالتحقق من صلاحية الرمز المخمن لإيميل معين من خلال إرسال طلب POST إلى الموقع المستهدف. إذا تم الحصول على استجابة صالحة (على سبيل المثال، استجابة JSON تحتوي على رسائل نجاح أو خطأ)، يتم معالجتها وطباعتها وفقًا لذلك.

2. **`guess_codes()`**:
   - تقوم هذه الوظيفة بإدارة عملية تخمين الرموز. تحاول كل رمز من 1000 إلى 9999، وتقوم بإرسال طلبات لكل رمز إلى الرابط المستهدف وتتحقق من الاستجابة. إذا تم العثور على رمز صالح، تتم إضافته إلى قائمة الرموز الصالحة ويتم طباعته.

3. **`check_website()`**:
   - تتحقق من أن الموقع المستهدف يعمل بشكل صحيح. يتم إرسال طلب GET بسيط إلى الرابط المحدد والتحقق من أن حالة الاستجابة هي 200 (OK). إذا كان الموقع غير متاح أو لا يمكن الوصول إليه، سيتم إنهاء السكربت.

4. **`load_emails_from_file()`**:
   - تقوم هذه الوظيفة بتحميل الإيميلات من ملف نصي (`emails.txt`). تقرأ كل سطر كعنوان إيميل منفصل وتخزنه في قائمة للمعالجة اللاحقة. إذا لم يتم العثور على الملف أو لم يتمكن من قراءته، سيتم طباعة رسالة خطأ.

## 🏆 نتائج الأداة:
- إذا تم العثور على رموز صالحة، سيتم عرض الإيميل والرمز الصالح في الطرفية:
  ```
  [SUCCESS] تم العثور على رمز صالح:
  البريد الإلكتروني: example@example.com، الرمز الصالح: 1234
  ```سيتم عرض رمز صفحة الويب لك 

- إذا لم يتم العثور على أي رموز صالحة بعد كل المحاولات، سيتم عرض رسالة فشل:
  ```
  [FAILED] لم يتم العثور على أي رمز صالح.
  ```

## 🤝 المساهمة:
---

**ملاحظة**: تم تطوير هذه الأداة باستخدام Python وتستفيد من مكتبات مثل `requests` و `BeautifulSoup` لتحليل استجابات الموقع. من المهم استخدام هذه الأداة بشكل مسؤول وفقط على الأنظمة التي لديك إذن لاختبارها.

---

شكرًا لاستخدامك هذه الأداة، ولا تتردد في تقديم تعليقاتك أو طرح أسئلتك عبر قسم المشاكل في المستودع.
