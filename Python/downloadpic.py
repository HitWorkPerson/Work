import requests
import time
import json
import re
import base64
from requests.packages.urllib3.exceptions import InsecureRequestWarning


class DownLoadPic:
    def __init__(self):
        self.millis = int(round(time.time() * 1000))
        self.url = "https://kyfw.12306.cn/passport/captcha/captcha-image64?login_site=E&module=login&rand=sjrand&{0}&callback=jQuery19109128043507846153_1622098990632&_=1622098990633".format(
            self.millis)
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36"
        }

    def downloadpic(self, i):
        try:
            requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
            r = requests.get(url=self.url, headers=self.headers, verify=False)
        except Exception as e:
            print(e)
            return
        re_text = re.search('\{.*\}', r.text, re.M | re.S).group(0)
        json_text = json.loads(re_text)
        if json_text["result_message"] == "生成验证码成功" and json_text["result_code"] == "0":
            img = str.encode(json_text["image"])
            with open('./pic/verify{}.png'.format(i), 'wb') as f:
                f.write(base64.b64decode(img))
                print("下载图片成功")
        else:
            print("生成验证码失败")


if __name__ == '__main__':
    d = DownLoadPic()
    for i in range(1, 10000):
        d.downloadpic(i)