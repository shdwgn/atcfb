# ------------[ AUTO CREATE FACEBOOK ACCOUNTS ]-------------- #
# ------------[ IMPORT ]-------------- #
import os
import sys
import re
import time
import json
import random
import string
import hashlib
from datetime import datetime
try:
    import requests
    from faker import Faker
    from bs4 import BeautifulSoup
except ImportError:
    os.system('pip install requests faker beautifulsoup4')
    import requests
    from faker import Faker
    from bs4 import BeautifulSoup
# ------------[ COLORS ]-------------- #
W = '\033[97;1m'
R = '\033[91;1m'
G = '\033[92;1m'
Y = '\033[93;1m'
B = '\033[94;1m'
P = '\033[95;1m'
S = '\033[96;1m'
N = '\x1b[0m'
PURPLE ='\x1b[38;5;46m'
RED = '\033[1;91m'
WHITE = '\033[1;97m'
GREEN = '\033[1;32m'
YELLOW = '\033[1;33m'
BLUE = '\033[1;34m'
ORANGE = '\033[1;35m'
CYAN = '\033[1;36m'
BLACK="\033[1;30m"
EXTRA ='\x1b[38;5;208m'
RESET = '\033[0m'
# ------------[ BANNER ]-------------- #
run_count = 0
status_list = ['ONLINE', 'ACTIVE', 'BUSY', 'AWAY', 'DO NOT DISTURB']
random_status = random.choice(status_list)
# ------------[ LOGO ]-------------- #
logo=(f"""{GREEN}
                     █████╗ ████████╗ ██████╗
                    ██╔══██╗╚══██╔══╝██╔════╝
                    ███████║   ██║   ██║     
                    ██╔══██║   ██║   ██║     
                    ██║  ██║   ██║   ╚██████╗
                    ╚═╝  ╚═╝   ╚═╝    ╚═════╝
{WHITE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
OWNER        : BRYX ANTON GRAYSON && JAHRA
STATUS       : {random_status}
FACEBOOK     : https://www.facebook.com/bryxxxpogi
TOOL         : PAID/PREMIUM 
VERSION      : {GREEN}[0.4]
{WHITE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
OK IDS SAVE IN    :\033[1;32m /sdcard/BRYX-CREATE-FB-NEW-OK.txt\033[1;37m
{WHITE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━""")
# ------------[ HELPERS ]-------------- #
def clear():
    os.system('clear')
    print(logo)
# ------------[ LINEX ]-------------- #
def linex():
    print('\033[1;37m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
# ------------[ GENERATE RANDOM STRING ]-------------- #
def generate_random_string(length):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))
# ------------[ USERAGENT UA ]-------------- #
def user_agent():
    devices = [
        "[FBAN/FB4A;FBAV/323.0.0.46.119;FBBV/298672707;FBDM/{density=2.75,width=1080,height=2168};FBLC/ru_RU;FBRV/299927973;FBCR/MTS RUS;FBMF/Xiaomi;FBBD/Redmi;FBDV/Redmi Note 9 Pro;FBSV/10]",
        "[FBAN/FB4A;FBAV/316.0.0.54.116;FBBV/287519012;FBDM/{density=2.75,width=1080,height=2134};FBLC/cs_CZ;FBRV/289140577;FBCR/O2.CZ;FBMF/Xiaomi;FBBD/Redmi;FBDV/Redmi Note 8 Pro;FBSV/10]",
        "[FBAN/FB4A;FBAV/305.1.0.40.120;FBBV/272401209;FBDM/{density=2.0,width=720,height=1456};FBLC/it_IT;FBRV/273474118;FBCR/I TIM;FBMF/OPPO;FBBD/OPPO;FBDV/CPH1931;FBSV/10]",
        "[FBAN/FB4A;FBAV/435.0.0.42.112;FBBV/523162189;FBDM/{density=3.0,width=1080,height=2165};FBLC/it_IT;FBRV/526139383;FBCR/TIM;FBMF/OnePlus;FBBD/OnePlus;FBDV/LE2113;FBSV/13]",
        "[FBAN/FB4A;FBAV/221.0.0.48.102;FBBV/154683427;FBDM/{density=2.75,width=1080,height=2030};FBLC/en_GB;FBRV/155327069;FBCR/Banglalink;FBMF/Xiaomi;FBBD/xiaomi;FBDV/Redmi Note 5;FBSV/8.1.0]"
    ]
    prefix = "[FBAN/FB4A;FBAV/" + str(random.randint(11, 80)) + ".0.0." + str(random.randint(9, 49)) + "." + str(random.randint(11, 77)) + ";FBBV/" + str(random.randint(11111111,99999999)) + ";"
    ua = prefix + random.choice(devices)
    return ua
# ------------[ BANNER ]-------------- #
def lock_checker(user_id):
    try:
        response = requests.get(f'https://graph.facebook.com/{user_id}/picture?type=normal')
        if 'Photoshop' in response.text:
            return 'Active'
        else:
            return 'Locked'
    except Exception as e:
        print(f"{RED}ERROR CHECKING ACCOUNT STATUS: {e}{RESET}")
        return 'Error'
# ------------[ GMAIL FILE MAKE ]-------------- #
def load_gmail_list(filename):
    if not os.path.isfile(filename):
        print(f"{RED}GMAIL LIST FILE NOT FOUND: {filename}{RESET}")
        sys.exit()
    with open(filename, 'r') as f:
        emails = f.read().splitlines()
    return emails
# ------------[ EMAIL ADDRESS ]-------------- #
def generate_random_emails(length=10, domains=None, count=1):
    if domains is None:
        domains = ["gmail.com"]
    emails = []
    for _ in range(count):
        prefix = ''.join(random.choices(string.ascii_lowercase + string.digits, k=length))
        domain = random.choice(domains)
        emails.append(f"{prefix}@{domain}")
    return emails if count > 1 else emails[0]
# ------------[ ACCOUNT CREATOR ]-------------- #
def register_account(fake, email, password):
    session = requests.Session()
    api_key = '882a8490361da98702bf97a021ddc14d'
    secret = '62f8ce9f74b12f84c123cc23437a4a32'

    first_name = fake.first_name()
    last_name = fake.last_name()
    birthday = fake.date_of_birth(minimum_age=18, maximum_age=90)
    gender = random.choice(['M', 'F'])

    payload = {
        'api_key': api_key,
        'attempt_login': True,
        'birthday': birthday.strftime('%Y-%m-%d'),
        'client_country_code': 'US',
        'fb_api_caller_class': 'com.facebook.registration.protocol.RegisterAccountMethod',
        'fb_api_req_friendly_name': 'registerAccount',
        'firstname': first_name,
        'format': 'json',
        'gender': gender,
        'lastname': last_name,
        'email': email,
        'locale': 'en_US',
        'method': 'user.register',
        'password': password,
        'reg_instance': generate_random_string(32),
        'return_multiple_errors': True
    }

    sorted_req = sorted(payload.items(), key=lambda x: x[0])
    sig_str = ''.join(f'{k}={v}' for k, v in sorted_req)
    payload['sig'] = hashlib.md5((sig_str + secret).encode()).hexdigest()

    headers = {'User-Agent': user_agent()}
    response = session.post('https://b-api.facebook.com/method/user.register', data=payload, headers=headers)
    
    try:
        reg = response.json()
    except:
        print(f"{RED}FAILED TO PARSE RESPONSE{RESET}")
        return

    user_id = reg.get('new_user_id')
    token = reg.get('session_info', {}).get('access_token')
    
    if user_id:
        status = lock_checker(user_id)
        if status == 'Locked':
            print(f"{RED}ACCOUNT LOCKED{RESET}")
        else:
            FbLink=f"https://www.facebook.com/profile.php?id={user_id}"
            print(f"{GREEN}ACCOUNT CREATED SUCCESSFULLY!{RESET}")
            print(f"{WHITE}EMAIL    : {email}")
            print(f"ID       : {user_id}")
            print(f"PASSWORD : {password}")
            print(f"NAME     : {first_name} {last_name}")
            print(f"BIRTHDAY : {birthday}")
            print(f"FB LINK  : {FbLink}{RESET}")

            cookies = session.cookies.get_dict()
            cookie_str = "; ".join([f"{key}={value}" for key, value in sorted_req])

            with open("/sdcard/BRYX-CREATE-FB-NEW-OK.txt", "a") as f:
                f.write(f"{user_id}|{password}|{cookie_str}\n")
            print(f"{GREEN}COOKIES SAVED!{RESET}")

            time.sleep(random.uniform(3,6))  # Random sleep for realistic behavior
    else:
        print(f"{YELLOW}ACCOUNT CREATION FAILED OR BLOCKED{RESET}")
# ------------[ MAIN MENU ]-------------- #
if __name__ == "__main__":
    clear()
    print(f"{WHITE}[1] AUTOMATIC FACEBOOK ACCOUNT CREATION{RESET}")
    print(f"{WHITE}[0] EXIT TOOL{RESET}")
    linex()
    choice = input(f"{WHITE}CHOOSE NUMBER : {RESET}")
    linex()
    
    if choice == '1':
        #gmail_file = input(f"{WHITE}ENTER GMAIL LIST FILE NAME (EXAMPLE : gmail_list.txt): {RESET}")
        #gmail_list = load_gmail_list(gmail_file)
        fake = Faker()
        num = int(input(f"{WHITE}ENTER NUMBER OF ACCOUNT TO CREATE : {RESET}"))
        password = input(f"{WHITE}ENTER CUSTOMER PASSWORD : {RESET}")
        linex()
        for _ in range(num):
            email = generate_random_emails()
            print(f"{GREEN}CREATING ACCOUNT WITH {email}...{RESET}")
            register_account(fake, email, password)
            linex()

    else:
        print(f"{YELLOW}EXITING...{RESET}")
        sys.exit()