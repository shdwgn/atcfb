import os, sys, re, time, json, platform
import requests, bs4, random, string
from faker import Faker
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

def load_proxies():
    proxy_url = "https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all"
    try:
        response = requests.get(proxy_url)
        if response.status_code == 200:
            return [proxy.strip() for proxy in response.text.splitlines()]
    except requests.exceptions.RequestException:
        pass
    return []

proxies_list = load_proxies()

def get_random_proxy():
    if proxies_list:
        return {"http": random.choice(proxies_list)}
    return None

purple = "\033[1;35m"
violet_chu = "\033[1;35m"
darkblue = "\033[34m"
green = "\033[1;32m"
red = "\033[1;31m"
yellow = "\033[1;33m"
skyblue = "\033[1;36m"
blue = "\033[1;34m"
lightblue = "\033[38;5;81m"
hotpink = "\033[38;5;197m"
light_magenta = "\033[38;5;174m"
white = "\033[1;37m"
lavender = "\033[38;5;189m"
rasp = "\033[38;5;22m"
darkblue = "\033[34m"
green = "\033[1;32m"
red = "\033[1;31m"
yellow = "\033[1;33m"
skyblue = "\033[1;36m"
blue = "\033[1;34m"
lightblue = "\033[38;5;81m"
white = "\033[1;37m"
gh ="\x1b[38;5;196m"
gh2 = "\x1b[38;5;197m"
gh3 = "\x1b[38;5;198m"
gh4 = "\x1b[38;5;199m"
gh5  = "\x1b[38;5;200m"
gh6 = "\x1b[38;5;201m"
rb = "\x1b[38;5;190m"
rb2 = "\x1b[38;5;191m"
rb3 = "\x1b[38;5;192m"
rb4 = "\x1b[38;5;193m"
rb5 = "\x1b[38;5;194m"
rb6 = "\x1b[38;5;195m"
C = "\x1b[38;5;202m"
C2 = "\x1b[38;5;203m"
C3 = "\x1b[38;5;204m"
C4 = "\x1b[38;5;205m"
C5 = "\x1b[38;5;206m"
C6 = "\x1b[38;5;207m"
Q = "\x1b[38;5;118m"
Q2 = "\x1b[38;5;119m"
Q3 = "\x1b[38;5;120m"
Q4 = "\x1b[38;5;121m"
Q5 = "\x1b[38;5;122m"
Q6 = "\x1b[38;5;123m"

ua = UserAgent()
def ugenX():
    ualist = [ua.random for _ in range(50)]
    return str(random.choice(ualist))

def fake_name():
    first = Faker().first_name()
    last = Faker().last_name()
    return first, last

def fake_nama():
    first = Faker("id_ID").first_name()
    last = Faker("id_ID").last_name()
    return first,last

def extractor(data):
    soup = BeautifulSoup(data, "html.parser")
    data = {}
    for inputs in soup.find_all("input"):
        name = inputs.get("name")
        value = inputs.get("value")
        if name:
            data[name] = value
    return data

folder_path = '/sdcard/AUTO-CREATE-BRYX/create/'
try:
    os.makedirs(folder_path, exist_ok=True)
except:
    pass

from datetime import datetime
import time
now = datetime.now()
formatted_time = now.strftime("%Y-%m-%d %H:%M:%S")
current_date = now.date()
current_time = now.time()
timestamp = time.time()


def banner(): 
    clear_screen()
    print(f"""\033[1;32m
          ███████╗██████╗░██████╗░░█████╗░██████╗░
          ██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗
          █████╗░░██████╔╝██████╔╝██║░░██║██████╔╝
          ██╔══╝░░██╔══██╗██╔══██╗██║░░██║██╔══██╗
          ███████╗██║░░██║██║░░██║╚█████╔╝██║░░██║
          ╚══════╝╚═╝░░╚═╝╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝
\033[1;34m──────────────────────────────────────────────────────────────\033[1;37m
\033[1;37m[\033[1;32m✓\033[1;37m] \033[1;32mOWNER\033[1;37m    : \033[1;32mBRYXPOGI && JAHRAPRETTY
\033[1;37m[\033[1;32m✓\033[1;37m] \033[1;32mTOOL\033[1;37m     : \033[1;32mAUTO CREATE FACEBOOK TOOL
\033[1;37m[\033[1;32m✓\033[1;37m] \033[1;32mSTATUS\033[1;37m   : \033[1;32mPREMIUM
\033[1;37m[\033[1;32m✓\033[1;37m] \033[1;32mDATE\033[1;37m     : \033[1;32m{current_date}
\033[1;37m[\033[1;32m✓\033[1;37m] \033[1;32mVERSION\033[1;37m  : \033[1;32m0.2
\033[1;34m──────────────────────────────────────────────────────────────\033[1;37m""")

def clear_screen():
    if 'termux' in platform.system().lower():
        os.system('clear')
    elif platform.system().lower() == 'windows':
        os.system('cls')
    else:
        os.system('clear')

def linex():
    print(f"\033[1;34m──────────────────────────────────────────────────────────────\033[1;37m")

used_numbers = set()
min_number = 500

domain_groups = {
    'common': ['linshiyouxiang.net','besttempmail.com']
}

def generate_unique_number():
    while True:
        number = random.randint(min_number, 1000000 + min_number)
        if number not in used_numbers:
            used_numbers.add(number)
            return number

def generate_random_emails(group='common', length=10, count=1, use_unique_number=False):
    domains = domain_groups.get(group, domain_groups['common'])
    emails = []
    for _ in range(count):
        prefix_length = length - 6 if use_unique_number else length
        prefix = ''.join(random.choices(string.ascii_lowercase + string.digits, k=prefix_length))
        if use_unique_number:
            prefix += str(generate_unique_number())
        domain = random.choice(domains)
        emails.append(f"{prefix}@{domain}")
    return emails if count > 1 else emails[0]

oks=[]
cps=[]
pcp=[]
id=[]
uid=[]
cid=[]
user_id=[]
tokenku=[]
ugenx=[]

def main():
    banner()
    print("[1] AUTO CREATE FB WITH COOKIE METHOD 1")
    print("[2] AUTO CREATE FB WITH PROXY METHOD 2")
    linex()
    method = input(f"\033[1;37m[\033[1;32m✓\033[1;37m] \033[1;37mCHOOSE METHOD : ")
    if method == '1':
    	createfb_method_1()
    if method == '2':
    	createfb_method_2()

def createfb_method_1():
    uid=[]
    global make,oks,cps
    banner()
    print("[1] NAME FILIPINO PHILIPPINES")
    print("[2] NAMA BAHASA INDONESIA")
    linex()
    name = input(f"\033[1;37m[\033[1;32m✓\033[1;37m] \033[1;37mCHOOSE NAME : ")
    linex()
    num = int(input("HOW MANY ACCOUNT : "))
    linex()
    pww = input("ENTER CUSTOM PASSWORD : ")
    linex()
    for make in range(num):
        sys.stdout.write(f"\r\033[1;37m[CREATE]\033[1;37m[\033[1;36m{make + 1}\033[1;37m|\033[1;31m{num}\033[1;37m]\033[1;37m[\033[1;32mOK:-{len(oks)}\033[1;37m]\033[1;37m")
        sys.stdout.flush()
        ses = requests.Session()
        response = ses.get("https://x.facebook.com/reg")
        form = extractor(response.text)
        if name == '1':
        	firstname, lastname = fake_name()
        if name == '2':
        	firstname, lastname = fake_nama()
        email2 = generate_random_emails()
        payload = {
            'ccp': "2",
            'reg_instance': form.get("reg_instance", ""),
            'submission_request': "true",
            'reg_impression_id': form.get("reg_impression_id", ""),
            'ns': "1",
            'logger_id': form.get("logger_id", ""),
            'firstname': firstname,
            'lastname': lastname,
            'birthday_day': str(random.randint(1, 28)),
            'birthday_month': str(random.randint(1, 12)),
            'birthday_year': str(random.randint(1992, 2009)),
            'reg_email__': email2,
            'sex': "2",
            'encpass': '#PWD_BROWSER:0:{}:{}'.format(str(time.time()).split('.')[0], pww),
            'submit': "Sign Up",
            'fb_dtsg': form.get("fb_dtsg", ""),
            'jazoest': form.get("jazoest", ""),
            'lsd': form.get("lsd", "")
        }

        headers = {
            "Host": "m.facebook.com",
            "Connection": "keep-alive",
            "User-Agent": ugenX(),
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "en-US,en;q=0.9"
        }

        reg_url = "https://www.facebook.com/reg/submit/"
        reg_submit = ses.post(reg_url, data=payload, headers=headers)
        login_coki=ses.cookies.get_dict()
        if "c_user" in login_coki:
            coki=";".join([key+"="+value for key,value in ses.cookies.get_dict().items()])
            uid = login_coki["c_user"]
            ckk=f"https://graph.facebook.com/{uid}/picture?type=normal"
            respns=requests.get(ckk).text
            print(f"\r\033[1;37m[\033[1;32m✓\033[1;37m] \033[1;32mNAME   : \033[1;32m{firstname} {lastname}")
            print(f"\r\033[1;37m[\033[1;32m✓\033[1;37m] \033[1;32mEMAIL  : \033[1;32m{email2}")
            print(f"\r\033[1;37m[\033[1;32m✓\033[1;37m] \033[1;32mUID    : {uid}")
            print(f"\r\033[1;37m[\033[1;32m✓\033[1;37m] \033[1;32mPASS   : {pww}")
            print(f"\r\033[1;37m[\033[1;32m✓\033[1;37m] \033[1;32mCOOKIE : {coki}")
            linex()
            open('/sdcard/AUTO-CREATE-BRYX/create/NEWACCOUNT-ALIVE.txt', 'a').write(uid+'|'+pww+'\n')
            open('/sdcard/AUTO-CREATE-BRYX/create/EMAILS.txt', 'a').write(email2+'\n')
            open('/sdcard/AUTO-CREATE-BRYX/create/COOKIE-ALIVE.txt', 'a').write(coki+'\n')
            os.system('espeak -a 300 "HEY,  YOU,  GOT,  OK,  ID"')
            oks.append(uid)
        else:
            print(f"\r\033[1;37m[\033[1;32m✓\033[1;37m] \033[1;31mAIRPLANE MODE OR CHECKPOINT")
            os.system('espeak -a 300 "ACCOUNT SUSPENDED"')
            cps.append(uid)
            linex()

def createfb_method_2():
    uid=[]
    global make,oks,cps
    banner()
    print("[1] NAME FILIPINO PHILIPPINES")
    print("[2] NAMA BAHASA INDONESIA")
    linex()
    name = input(f"\033[1;37m[\033[1;32m✓\033[1;37m] \033[1;37mCHOOSE NAME : ")
    linex()
    num = int(input("HOW MANY ACCOUNT : "))
    linex()
    pww = input("ENTER CUSTOM PASSWORD : ")
    linex()
    for make in range(num):
        sys.stdout.write(f"\r\033[1;37m[CREATE]\033[1;37m[\033[1;36m{make + 1}\033[1;37m|\033[1;31m{num}\033[1;37m]\033[1;37m[\033[1;32mOK:-{len(oks)}\033[1;37m]\033[1;37m")
        sys.stdout.flush()
        ses = requests.Session()
        response = ses.get("https://x.facebook.com/reg")
        form = extractor(response.text)
        if name == '1':
        	firstname, lastname = fake_name()
        if name == '2':
        	firstname, lastname = fake_nama()
        email2 = generate_random_emails()
        payload = {
            'ccp': "2",
            'reg_instance': form.get("reg_instance", ""),
            'submission_request': "true",
            'reg_impression_id': form.get("reg_impression_id", ""),
            'ns': "1",
            'logger_id': form.get("logger_id", ""),
            'firstname': firstname,
            'lastname': lastname,
            'birthday_day': str(random.randint(1, 28)),
            'birthday_month': str(random.randint(1, 12)),
            'birthday_year': str(random.randint(1992, 2009)),
            'reg_email__': email2,
            'sex': "2",
            'encpass': '#PWD_BROWSER:0:{}:{}'.format(str(time.time()).split('.')[0], pww),
            'submit': "Sign Up",
            'fb_dtsg': form.get("fb_dtsg", ""),
            'jazoest': form.get("jazoest", ""),
            'lsd': form.get("lsd", "")
        }

        headers = {
            "Host": "m.facebook.com",
            "Connection": "keep-alive",
            "User-Agent": ugenX(),
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "en-US,en;q=0.9"
        }

        proxy = get_random_proxy()
        reg_url = "https://www.facebook.com/reg/submit/"
        reg_submit = ses.post(reg_url, data=payload, headers=headers, proxies=proxy, timeout=30)
        login_coki=ses.cookies.get_dict()
        if "c_user" in login_coki:
            coki=";".join([key+"="+value for key,value in ses.cookies.get_dict().items()])
            uid = login_coki["c_user"]
            ckk=f"https://graph.facebook.com/{uid}/picture?type=normal"
            respns=requests.get(ckk).text
            print(f"\r\033[1;37m[\033[1;32mERROR-OK\033[1;37m]\033[1;32m {uid} | {pww}")
            open('/sdcard/AUTO-CREATE-BRYX/create/NEWACCOUNT-ALIVE.txt', 'a').write(uid+'|'+pww+'\n')
            open('/sdcard/AUTO-CREATE-BRYX/create/EMAILS.txt', 'a').write(email2+'\n')
            open('/sdcard/AUTO-CREATE-BRYX/create/COOKIE-ALIVE.txt', 'a').write(coki+'\n')
            os.system('espeak -a 300 "HEY,  YOU,  GOT,  OK,  ID"')
            oks.append(uid)
        else:
            cps.append(uid)


if __name__ == "__main__":
    main()