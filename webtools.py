import requests
from colorama import Fore, Style, Back, init
import threading
import hashlib
import whois
import ssl
import socket
from urllib.parse import urlparse

# تفعيل مكتبة colorama
init(autoreset=True)

# معلومات المبرمج
programmer_name = "Ayham Alwdy"
programmer_phone = "/00963938627021"
programmer_facebook = "Ayham Alwdy"
programmer_email = "ayhamalwdy2024@gmail.com"
programmer_github = "https://github.com/ayhamalwdy2024/webtools-"
syrian_flag = "🇸🇾"  # رمز علم سوريا
programmer_nationality = "Syrian"
programmer_location = "Germany"
programmer_study = "Cybersecurity at Technical University of Berlin"
program_description = (
    "Hello, I am Ayham from Syria, currently residing in Germany and studying Cybersecurity at the Technical University of Berlin. "
    "I designed this tool to scan websites for security vulnerabilities. Please note that neither I nor this tool are responsible for any illegal use."
)

# وظيفة لعرض بيانات المبرمج بشكل احترافي
def display_programmer_info():
    print(Fore.GREEN + Style.BRIGHT + "*" * 50)
    print(Fore.YELLOW + Style.BRIGHT + "       Programmer Information " + syrian_flag + Style.RESET_ALL)
    print(Fore.GREEN + Style.BRIGHT + "*" * 50)
    print(Fore.CYAN + Style.BRIGHT + f"Name: {programmer_name}")
    print(Fore.CYAN + Style.BRIGHT + f"Phone: {programmer_phone}")
    print(Fore.CYAN + Style.BRIGHT + f"Facebook: {programmer_facebook}")
    print(Fore.CYAN + Style.BRIGHT + f"Email: {programmer_email}")
    print(Fore.CYAN + Style.BRIGHT + f"GitHub: {programmer_github}")
    print(Fore.CYAN + Style.BRIGHT + f"Nationality: {programmer_nationality}")
    print(Fore.CYAN + Style.BRIGHT + f"Location: {programmer_location}")
    print(Fore.CYAN + Style.BRIGHT + f"Study: {programmer_study}")
    print(Fore.CYAN + Style.BRIGHT + f"Description: {program_description}")
    print(Fore.GREEN + Style.BRIGHT + "*" * 50 + Style.RESET_ALL)
    print()  # إضافة سطر فارغ لتحسين العرض

# وظيفة لعرض المعلومات في جدول احترافي
def display_table(title, rows):
    print(Fore.GREEN + Style.BRIGHT + "*" * 50)
    print(Fore.YELLOW + Style.BRIGHT + title + Style.RESET_ALL)
    print(Fore.GREEN + Style.BRIGHT + "*" * 50)
    for row in rows:
        print(Fore.CYAN + Style.BRIGHT + f"{row}")
    print(Fore.GREEN + Style.BRIGHT + "*" * 50 + Style.RESET_ALL)
    print()  # إضافة سطر فارغ لتحسين العرض

# فحص رؤوس HTTP
def check_http_headers(url):
    try:
        response = requests.get(url)
        headers = response.headers
        security_headers = [
            'Strict-Transport-Security',
            'Content-Security-Policy',
            'X-Content-Type-Options',
            'X-Frame-Options',
            'X-XSS-Protection'
        ]
        missing_headers = [header for header in security_headers if header not in headers]
        rows = [f"Header: {header} - {headers.get(header, 'Not found')}" for header in security_headers]
        if missing_headers:
            rows.append(f"Missing security headers: {', '.join(missing_headers)}")
        else:
            rows.append("All recommended security headers are present.")
    except requests.exceptions.RequestException as e:
        rows = [f"Error checking HTTP headers: {e}"]

    display_table("   HTTP Headers Analysis", rows)

# فحص الثغرات المعروفة (Placeholder)
def check_known_vulnerabilities(url):
    rows = ["Placeholder: Implement known vulnerability scanning"]
    display_table("   Known Vulnerabilities Check", rows)

# اختبار تصاريح الوصول (Placeholder)
def check_access_control(url):
    rows = ["Placeholder: Implement access control checks"]
    display_table("   Access Control Testing", rows)

# فحص تكوينات الخادم (Placeholder)
def check_server_configuration(url):
    rows = ["Placeholder: Implement server configuration checks"]
    display_table("   Server Configuration Checks", rows)

# تحليل نقاط الضعف في تطبيقات الويب
def check_web_application_vulnerabilities(url):
    rows = []
    # إضافة فحوصات مختلفة
    payloads = [
        "' OR '1'='1",
        "<script>alert('XSS')</script>",
        "admin' --"
    ]
    for payload in payloads:
        try:
            response = requests.get(url + "?q=" + payload)
            if payload in response.text:
                rows.append(f"Potential vulnerability with payload: {payload}")
        except requests.exceptions.RequestException as e:
            rows.append(f"Error checking web application vulnerabilities: {e}")
    
    if not rows:
        rows.append("No vulnerabilities found.")
    
    display_table("   Web Application Vulnerabilities", rows)

# فحص الأمان في شبكات التواصل الاجتماعي (Placeholder)
def check_social_engineering(url):
    rows = ["Placeholder: Implement social engineering checks"]
    display_table("   Social Engineering Checks", rows)

# اختبار أداء الشبكة
def network_performance_testing(url):
    rows = []
    # تجميع أوقات الاستجابة واختبار التحمل يمكن أن يتطلب أدوات أكثر تخصصًا
    rows.append(f"Placeholder: Implement network performance testing for {url}")
    display_table("   Network Performance Testing", rows)

# فحص أمان شهادات SSL/TLS
def check_ssl_cert(domain):
    try:
        conn = ssl.create_default_context().wrap_socket(socket.socket(), server_hostname=domain)
        conn.connect((domain, 443))
        cert = conn.getpeercert()
        rows = [str(cert)]
    except Exception as e:
        rows = [f"Error checking SSL certificate: {e}"]

    display_table("   SSL Certificate Details", rows)

# فحص ملفات التكوين
def check_configuration_files(url):
    rows = ["Placeholder: Implement configuration file scanning"]
    display_table("   Configuration Files Check", rows)

# توليد تقرير أمني شامل (Placeholder)
def generate_comprehensive_report(url):
    rows = ["Placeholder: Implement comprehensive security report"]
    display_table("   Comprehensive Security Report", rows)

# فحص الأمان للمكونات الإضافية (Placeholder)
def check_plugin_security(url):
    rows = ["Placeholder: Implement plugin security checks"]
    display_table("   Plugin Security Checks", rows)

# اختبار هجمات التلاعب بالجلسات (Placeholder)
def check_session_hijacking(url):
    rows = ["Placeholder: Implement session hijacking checks"]
    display_table("   Session Hijacking Tests", rows)

# القائمة الرئيسية
def display_menu():
    print(Fore.GREEN + Style.BRIGHT + "*" * 50)
    print(Fore.YELLOW + Style.BRIGHT + "         Web Tools Menu" + Style.RESET_ALL)
    print(Fore.GREEN + Style.BRIGHT + "*" * 50)
    print(Fore.CYAN + "[1] Scan for admin pages" + Style.RESET_ALL)
    print(Fore.CYAN + "[2] Check CSRF vulnerability" + Style.RESET_ALL)
    print(Fore.CYAN + "[3] Perform DoS attack" + Style.RESET_ALL)
    print(Fore.CYAN + "[4] Encrypt IP address" + Style.RESET_ALL)
    print(Fore.CYAN + "[5] Check SQL Injection vulnerability" + Style.RESET_ALL)
    print(Fore.CYAN + "[6] Check XSS vulnerability" + Style.RESET_ALL)
    print(Fore.CYAN + "[7] Gather domain information" + Style.RESET_ALL)
    print(Fore.CYAN + "[8] Load test" + Style.RESET_ALL)
    print(Fore.CYAN + "[9] Check SSL certificate" + Style.RESET_ALL)
    print(Fore.CYAN + "[10] Check HTTP headers" + Style.RESET_ALL)
    print(Fore.CYAN + "[11] Check known vulnerabilities" + Style.RESET_ALL)
    print(Fore.CYAN + "[12] Check access control" + Style.RESET_ALL)
    print(Fore.CYAN + "[13] Check server configuration" + Style.RESET_ALL)
    print(Fore.CYAN + "[14] Check web application vulnerabilities" + Style.RESET_ALL)
    print(Fore.CYAN + "[15] Check social engineering" + Style.RESET_ALL)
    print(Fore.CYAN + "[16] Network performance testing" + Style.RESET_ALL)
    print(Fore.CYAN + "[17] Check configuration files" + Style.RESET_ALL)
    print(Fore.CYAN + "[18] Generate comprehensive report" + Style.RESET_ALL)
    print(Fore.CYAN + "[19] Check plugin security" + Style.RESET_ALL)
    print(Fore.CYAN + "[20] Check session hijacking" + Style.RESET_ALL)
    print(Fore.CYAN + "[0] Exit" + Style.RESET_ALL)
    print(Fore.GREEN + Style.BRIGHT + "*" * 50)

# وظيفة للعودة إلى القائمة الرئيسية
def return_to_menu():
    input(Fore.YELLOW + Style.BRIGHT + "Press Enter to return to the menu...")

# القائمة الرئيسية
def main():
    display_programmer_info()
    
    while True:
        display_menu()
        choice = input(Fore.YELLOW + Style.BRIGHT + "Choose an option: ")
        
        if choice == "1":
            target_url = input("Enter the URL to scan for admin pages: ")
            # تنفيذ وظيفة فحص صفحات الإدارة (Placeholder)
            print("Scanning for admin pages...")
            return_to_menu()
        elif choice == "2":
            target_url = input("Enter the URL to check CSRF vulnerability: ")
            # تنفيذ وظيفة فحص ثغرات CSRF (Placeholder)
            print("Checking for CSRF vulnerabilities...")
            return_to_menu()
        elif choice == "3":
            # تنفيذ اختبار DoS (Placeholder)
            print("Performing DoS attack...")
            return_to_menu()
        elif choice == "4":
            target_ip = input("Enter the IP address to encrypt: ")
            # تنفيذ وظيفة تشفير عنوان IP (Placeholder)
            print("Encrypting IP address...")
            return_to_menu()
        elif choice == "5":
            target_url = input("Enter the URL to check SQL Injection vulnerability: ")
            # تنفيذ وظيفة فحص ثغرات SQL Injection (Placeholder)
            print("Checking for SQL Injection vulnerabilities...")
            return_to_menu()
        elif choice == "6":
            target_url = input("Enter the URL to check XSS vulnerability: ")
            # تنفيذ وظيفة فحص ثغرات XSS (Placeholder)
            print("Checking for XSS vulnerabilities...")
            return_to_menu()
        elif choice == "7":
            domain = input("Enter the domain to gather information: ")
            # تنفيذ وظيفة جمع المعلومات عن النطاق
            domain_info = whois.whois(domain)
            rows = [f"Domain: {domain_info.domain_name}", f"Registrar: {domain_info.registrar}"]
            display_table("   Domain Information", rows)
            return_to_menu()
        elif choice == "8":
            target_url = input("Enter the URL for load test: ")
            network_performance_testing(target_url)
            return_to_menu()
        elif choice == "9":
            domain = input("Enter the domain to check SSL certificate: ")
            check_ssl_cert(domain)
            return_to_menu()
        elif choice == "10":
            target_url = input("Enter the URL to check HTTP headers: ")
            check_http_headers(target_url)
            return_to_menu()
        elif choice == "11":
            target_url = input("Enter the URL to check known vulnerabilities: ")
            check_known_vulnerabilities(target_url)
            return_to_menu()
        elif choice == "12":
            target_url = input("Enter the URL to check access control: ")
            check_access_control(target_url)
            return_to_menu()
        elif choice == "13":
            target_url = input("Enter the URL to check server configuration: ")
            check_server_configuration(target_url)
            return_to_menu()
        elif choice == "14":
            target_url = input("Enter the URL to check web application vulnerabilities: ")
            check_web_application_vulnerabilities(target_url)
            return_to_menu()
        elif choice == "15":
            target_url = input("Enter the URL to check social engineering: ")
            check_social_engineering(target_url)
            return_to_menu()
        elif choice == "16":
            target_url = input("Enter the URL for network performance testing: ")
            network_performance_testing(target_url)
            return_to_menu()
        elif choice == "17":
            target_url = input("Enter the URL to check configuration files: ")
            check_configuration_files(target_url)
            return_to_menu()
        elif choice == "18":
            target_url = input("Enter the URL to generate a comprehensive report: ")
            generate_comprehensive_report(target_url)
            return_to_menu()
        elif choice == "19":
            target_url = input("Enter the URL to check plugin security: ")
            check_plugin_security(target_url)
            return_to_menu()
        elif choice == "20":
            target_url = input("Enter the URL to check session hijacking: ")
            check_session_hijacking(target_url)
            return_to_menu()
        elif choice == "0":
            print(Fore.RED + Style.BRIGHT + "Exiting...")
            break
        else:
            print(Fore.RED + "Invalid choice. Please enter a number between 0 and 20.")

if __name__ == "__main__":
    main()
