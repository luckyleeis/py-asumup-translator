import requests
import time
from stem import Signal
from stem.control import Controller


DEEPL = 'deepl'
POND = 'pond'

headers = {
    DEEPL: {
        "Accept": "*/*",
        "Accept-Language": "en-US,en;q=0.5",
        "Accept-Encoding": "gzip, deflate, br",
        "Referer": "https://www.deepl.com/",
        "Content-type": "application/json",
        "Origin": "https://www.deepl.com",
        "Connection": "keep-alive",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "no-cors",
        "Sec-Fetch-Site": "same-site",
        "Pragma": "no-cache",
        "Cache-Control": "no-cache",
        "TE": "trailers",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; rv:91.0) Gecko/20100101 Firefox/91.0"
    },
POND: {
        "Accept": "*/*",
        "Accept-Language": "en-US,en;q=0.5",
        "Accept-Encoding": "gzip, deflate, br",
        "Referer": "https://en.pons.com/",
        "Content-type": "application/json",
        "Origin": "https://en.pons.com",
        "Connection": "keep-alive",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-site",
        "Pragma": "no-cache",
        "Cache-Control": "no-cache",
        "TE": "trailers",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; rv:91.0) Gecko/20100101 Firefox/91.0"
    }
}


def get_session():
    session = requests.session()
    session.proxies = {}
    session.proxies['http']='socks5h://localhost:9050'
    session.proxies['https']='socks5h://localhost:9050'
    return session

def post(type, url, json, retries=0):

    if retries > 0:
        if (retries > 3):
            return 'error'
        renew_tor_ip()

    header = headers[type]
    session = get_session()
    response = session.post(url, json=json, headers=header)

    try:
        response.raise_for_status()
        res = response.json()
        if 'error' not in res:
            return res
    except:
        pass

    post(type, url, json, retries + 1)



def get_current_ip():
    session = get_session()

    try:
        r = session.get('http://httpbin.org/ip')
    except Exception as e:
        print (str(e))
    else:
        return r.json()
    

def renew_tor_ip():
    ip = get_current_ip()['origin']

    with Controller.from_port(port = 9051) as controller:
        controller.authenticate(password="luckyleeisinthehouse")
        controller.signal(Signal.NEWNYM)
    
    time.sleep(2)
    second_ip = get_current_ip()['origin']    
    while ip == second_ip:
        time.sleep(1)
        continue