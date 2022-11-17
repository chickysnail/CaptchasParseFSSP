import requests
from bs4 import BeautifulSoup as bs
import json
import urllib

capatchaAmount = 10000
id = 0
dir = "Captchas10000"
while id!=capatchaAmount:
    captchaUrl = "https://is.fssp.gov.ru/ajax_search?system=ip&is%5Bextended%5D=1&nocache=1&is%5Bvariant%5D=1&is%5Bregion_id%5D%5B0%5D=&is%5Blast_name%5D=surname&is%5Bfirst_name%5D=name&is%5Bdrtr_name%5D=&is%5Bip_number%5D=&is%5Bpatronymic%5D=midname&is%5Bdate%5D=07.01.2022&is%5Baddress%5D=&is%5Bid_number%5D=&is%5Bid_type%5D%5B0%5D=&is%5Bid_issuer%5D=&is%5Binn%5D="
    captchaRequest = requests.get(captchaUrl)
    if captchaRequest.status_code!=200:
        continue
    captchaRequestJson = json.loads(captchaRequest.text)
    captchaPage = captchaRequestJson["data"]
    captchaSoup = bs(captchaPage, "html.parser")
    imgTag = captchaSoup.find_all('img', id="capchaVisual")
    captcha_path = imgTag[0].attrs["src"]

    #saving image
    urllib.request.urlretrieve(captcha_path, f"{dir}\captcha-{id}.jpg")
    print(f"{id+1}: captcha-{id}.jpg")
    id+=1
print("DONE!")