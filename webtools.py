import requests
from colorama import Fore, Style, Back, init
import threading
import hashlib
import whois
from urllib.parse import urlparse
import ssl
import socket

# تفعيل مكتبة colorama
init(autoreset=True)

# معلومات المبرمج
programmer_name = "Ayham Alwdy"
programmer_phone = "/00963938627021"
programmer_facebook = "Ayham Alwdy"
programmer_email = "ayhamalwdy2024@gmail.com"
programmer_github = "https://github.com/ayhamalwdy2024/webtools-"

# وظيفة لعرض بيانات المبرمج بشكل احترافي
def display_programmer_info():
    print(Fore.GREEN + Style.BRIGHT + "*" * 50)
    print(Fore.YELLOW + Style.BRIGHT + "       Programmer Information" + Style.RESET_ALL)
    print(Fore.GREEN + Style.BRIGHT + "*" * 50)
    print(Fore.CYAN + Style.BRIGHT + f"Name: {programmer_name}")
    print(Fore.CYAN + Style.BRIGHT + f"Phone: {programmer_phone}")
    print(Fore.CYAN + Style.BRIGHT + f"Facebook: {programmer_facebook}")
    print(Fore.CYAN + Style.BRIGHT + f"Email: {programmer_email}")
    print(Fore.CYAN + Style.BRIGHT + f"GitHub: {programmer_github}")
    print(Fore.GREEN + Style.BRIGHT + "*" * 50 + Style.RESET_ALL)
    return_to_menu()

# إضافة وظيفة العودة إلى القائمة الرئيسية
def return_to_menu():
    print(Fore.MAGENTA + Style.BRIGHT + "[*] Returning to main menu..." + Style.RESET_ALL)
    # افترض أنك هنا تقوم بإعادة عرض القائمة الرئيسية
    main_menu()

# وظيفة للعرض قائمة الخيارات الرئيسية
def main_menu():
    print(Fore.BLUE + Style.BRIGHT + "Main Menu:" + Style.RESET_ALL)
    print(Fore.GREEN + "1. Scan Website" + Style.RESET_ALL)
    print(Fore.GREEN + "2. DoS Attack" + Style.RESET_ALL)
    print(Fore.GREEN + "3. Encrypt IP" + Style.RESET_ALL)
    print(Fore.GREEN + "4. Check SQL Injection" + Style.RESET_ALL)
    print(Fore.GREEN + "5. Check XSS" + Style.RESET_ALL)
    print(Fore.GREEN + "6. Gather Info" + Style.RESET_ALL)
    print(Fore.GREEN + "7. Load Test" + Style.RESET_ALL)
    print(Fore.GREEN + "8. Check Encryption & Security" + Style.RESET_ALL)
    print(Fore.GREEN + "9. Check Parameter Vulnerabilities" + Style.RESET_ALL)
    print(Fore.GREEN + "10. Programmer Info" + Style.RESET_ALL)
    choice = input(Fore.BLUE + "Enter your choice: " + Style.RESET_ALL)
    if choice == "10":
        display_programmer_info()
    else:
        # تنفيذ باقي الخيارات بناءً على الاختيار
        pass

# هنا يتم بدء التطبيق
if __name__ == "__main__":
    main_menu()
