from colorama import Fore, Back, Style
from fake_useragent import UserAgent
import threading 
import requests 
import argparse

banner = """


___________         ___.   .__    .___  .___           __________                       
\_   _____/_________\_ |__ |__| __| _/__| _/____   ____\______   \_____    ______ ______
 |    __)/  _ \_  __ \ __ \|  |/ __ |/ __ |/ __ \ /    \|     ___/\__  \  /  ___//  ___/
 |     \(  <_> )  | \/ \_\ \  / /_/ / /_/ \  ___/|   |  \    |     / __ \_\___ \ \___ \ 
 \___  / \____/|__|  |___  /__\____ \____ |\___  >___|  /____|    (____  /____  >____  >
     \/                  \/        \/    \/    \/     \/               \/     \/     \/   v1.0
by c0d3Ninja

"""

print(Fore.CYAN + banner)

parser = argparse.ArgumentParser()
group = parser.add_mutually_exclusive_group()

group.add_argument('-p', '--path', action='store',
                    type=str, help='path to check',
                    metavar='domain.com')

parser.add_argument('-d', '--domains', action='store',
                   help="domains to check",
                   metavar="filename.txt")

parser.add_argument('-t', '--target', action='store',
                   help="domain to check",
                   metavar="site.com")

args = parser.parse_args()

ua = UserAgent()
header = {'User-Agent':str(ua.chrome)}

def start():
    if args.domains:
        if args.path:
            print(Fore.CYAN + "Checking domains to bypass....")
            try:
                with open(f"{args.domains}", "r") as f:
                    checklist = f.readlines()
            except IOError:
                print(f"File {args.domains} not found!")

            with open("bypasses.txt", "r") as b:
                bypass = b.readlines()
                for lines in checklist:
                    for bypasslist in bypass:
                        getbypass = bypasslist.strip()
                        lines = lines.strip()
                        path = f"{args.path}"
                        links = lines + "/" + path + getbypass
                        r = requests.get(links, stream=True, headers=header)
                        print(Fore.WHITE + links + Fore.GREEN + " [{}]".format(r.status_code))
        else:
            print(Fore.CYAN + "Checking domains to bypass....")
            try:
                with open(f"{args.domains}", "r") as f:
                    checklist = f.readlines()
            except IOError:
                print(f"File {args.domains} not found!")

            with open("bypasses.txt", "r") as b:
                bypass = b.readlines()
                for lines in checklist:
                    for bypasslist in bypass:
                        getbypass = bypasslist.strip()
                        lines = lines.strip()
                        links = lines + getbypass
                        r = requests.get(links, stream=True, headers=header)
                        print(Fore.WHITE + links + Fore.GREEN + " [{}]".format(r.status_code))            
    if args.target:
        if args.path:
            print(Fore.GREEN + f"Checking {args.target}...")
            try:
                with open("bypasses.txt", "r") as f:
                    bypasslines = f.readlines()
            except IOError:
                print(f"File not found!")

            for lines in bypasslines:
                lines = lines.strip()
                target = f"{args.target}"
                path = f"{args.path}"
                links = target + "/" + path + lines
                r = requests.get(links, headers=header)
                print(Fore.WHITE + links + Fore.GREEN + " [{}]".format(r.status_code))
        else:
            print(Fore.GREEN + f"Checking {args.target}...")
            try:
                with open("bypasses.txt", "r") as b:
                    bypasslines2 = b.readlines()
            except IOError:
                print(f"File not found!")

            for lines in bypasslines2:
                lines = lines.strip()
                target = f"{args.target}"
                links = target + lines
                r = requests.get(links, headers=header)
                print(Fore.WHITE + links + Fore.GREEN + " [{}]".format(r.status_code))            


t = threading.Thread(target=start)
t.start()
    
