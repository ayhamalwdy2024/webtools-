import requests
import argparse
import subprocess
import webbrowser

# معلومات المبرمج
programmer_name = "Ayham Alwdy"
programmer_phone = "+00963938627021"
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

# ألوان ساطعة في الـ VS Code
HEADER_COLOR = "\033[95m"
OKBLUE = "\033[94m"
OKGREEN = "\033[92m"
WARNING = "\033[93m"
FAIL = "\033[91m"
ENDC = "\033[0m"

def print_banner():
    print(f"{HEADER_COLOR}--- Web Vulnerability Scanner ---{ENDC}")
    print(f"{HEADER_COLOR}{syrian_flag} Programmer Information {syrian_flag}{ENDC}")
    print(f"Name: {programmer_name}")
    print(f"Phone: {programmer_phone}")
    print(f"Facebook: {programmer_facebook}")
    print(f"Email: {programmer_email}")
    print(f"GitHub: {programmer_github}")
    print(f"Nationality: {programmer_nationality}")
    print(f"Location: {programmer_location}")
    print(f"Study: {programmer_study}")
    print(f"{program_description}")
    print("-" * 50)

def gather_info(url):
    print(f"{OKBLUE}[INFO] Gathering Information for {url}{ENDC}")
    try:
        response = requests.get(url)
        print(f"{OKGREEN}[INFO] HTTP Headers:{ENDC}")
        for header, value in response.headers.items():
            print(f"{OKBLUE}{header}: {value}{ENDC}")
    except requests.RequestException as e:
        print(f"{FAIL}[ERROR] {e}{ENDC}")

def check_sql_injection(url):
    print(f"{OKBLUE}[INFO] Checking for SQL Injection at {url}{ENDC}")
    try:
        subprocess.call(['sqlmap', '-u', url, '--batch'])
    except FileNotFoundError:
        print(f"{FAIL}[ERROR] sqlmap not found. Make sure sqlmap is installed.{ENDC}")

def check_xss(url):
    print(f"{OKBLUE}[INFO] Checking for XSS at {url}{ENDC}")
    # منطق فحص XSS هنا
    # يمكن إضافة تحليل مخصص لمكتبات مثل OWASP ZAP

def check_lfi(url):
    print(f"{OKBLUE}[INFO] Checking for LFI at {url}{ENDC}")
    lfi_payloads = ["../../../../etc/passwd", "../etc/passwd"]
    for payload in lfi_payloads:
        lfi_url = f"{url}/{payload}"
        try:
            response = requests.get(lfi_url)
            if "root:x" in response.text:
                print(f"{FAIL}[VULNERABLE] LFI Detected with payload: {payload}{ENDC}")
            else:
                print(f"{OKGREEN}[SAFE] No LFI with payload: {payload}{ENDC}")
        except requests.RequestException as e:
            print(f"{FAIL}[ERROR] {e}{ENDC}")

def check_csrf(url):
    print(f"{OKBLUE}[INFO] Checking for CSRF at {url}{ENDC}")
    # منطق فحص CSRF هنا
    # يمكن استخدام أدوات مثل OWASP CSRFTester

def run_nmap(target):
    print(f"{OKBLUE}[INFO] Running nmap on {target}{ENDC}")
    try:
        subprocess.call(['nmap', '-sV', target])
    except FileNotFoundError:
        print(f"{FAIL}[ERROR] nmap not found. Make sure nmap is installed.{ENDC}")

def open_webpage(url):
    print(f"{OKBLUE}[INFO] Opening {url} in web browser{ENDC}")
    webbrowser.open(url)

def find_admin_pages(url):
    print(f"{OKBLUE}[INFO] Searching for Admin Page at {url}{ENDC}")
    admin_paths = [
        'admin/', 'admin/login/', 'admin/admin.php', 'admin.php',
        'administrator/', 'administrator/index.php', 'adminpanel/', 'user/login/',
        'admin/login.php', 'admin_area/', 'login/', 'admin1/', 'admin2/', 
        'cpanel/', 'controlpanel/', 'admincontrol/', 'adminarea/'
    ]
    
    for path in admin_paths:
        full_url = f"{url.rstrip('/')}/{path}"
        try:
            response = requests.get(full_url)
            if response.status_code == 200:
                print(f"{OKGREEN}[FOUND] Admin page found at: {full_url}{ENDC}")
            else:
                print(f"{WARNING}[NOT FOUND] Tried: {full_url}{ENDC}")
        except requests.RequestException as e:
            print(f"{FAIL}[ERROR] {e}{ENDC}")

def main():
    parser = argparse.ArgumentParser(description="Web Vulnerability Scanner")
    parser.add_argument("url", help="Target URL")
    parser.add_argument("--nmap", help="Run nmap on target", action="store_true")
    parser.add_argument("--sqlmap", help="Run SQLMap on target", action="store_true")
    parser.add_argument("--open", help="Open target in web browser", action="store_true")
    parser.add_argument("--admin", help="Search for admin pages", action="store_true")
    args = parser.parse_args()

    print_banner()
    gather_info(args.url)

    if args.sqlmap:
        check_sql_injection(args.url)
    
    check_xss(args.url)
    check_lfi(args.url)
    check_csrf(args.url)

    if args.nmap:
        run_nmap(args.url)
    
    if args.open:
        open_webpage(args.url)

    if args.admin:
        find_admin_pages(args.url)

if __name__ == "__main__":
    main()
