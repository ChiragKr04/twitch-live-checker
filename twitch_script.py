import time

import requests
from bs4 import BeautifulSoup
import json
from application import open_chrome


def run_twitch_script(url: str):

    url = "https://www.twitch.tv/"+url

    is_live = False

    while True:
        time.sleep(2)
        print("running")
        page = requests.get(url)

        soup = BeautifulSoup(page.content, 'html.parser')

        my_live_json = soup.find_all('script')

        print(my_live_json[0].get_text('script'))
        if is_live:
            continue
        try:
            y = json.loads(my_live_json[0].get_text('script'))
            print("We are live", y[0]["publication"]["isLiveBroadcast"])
            is_live = True
            open_chrome(url)
            break

        except Exception as e:
            print("Not Live", e.__class__.__name__)

        time.sleep(20)
