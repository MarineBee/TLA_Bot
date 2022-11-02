# libraries required
import asyncio
import requests
import time

# functions from other .py
from twitter_main import twitter_main
from read_list import read_list
from twitch_chat import send_chat
from twitch_check import twitch_check

# paths that hold important information
app_data_path = "D:/TereBin/TtTB/data/twitch_app_data.txt"
streamer_json_path = "D:/TereBin/TtTB/data/streamer_list.json"
twitch_bot_data_path = 'D:/TereBin/TtTB/data/twitch_bot_data.txt'
err_log_path = 'D:/TereBin/TtTB/data/err_log.txt'

# -------------------------------------------------- non-repeated part (초기 설정 부분)
# get twitch api key/api secret from local data
with open(app_data_path) as app_data_txt :
    app_data = app_data_txt.read().splitlines()
    app_key = app_data[0]
    app_secret = app_data[1]

# get access_token and token_type from twitch oauth2
auth_req = requests.post('https://id.twitch.tv/oauth2/token?client_id=' + app_key + '&client_secret=' + app_secret + '&grant_type=client_credentials')
auth_req_json = auth_req.json()
# parsing token and headers to create auth_token
auth_token = auth_req_json["token_type"][0].upper() + auth_req_json["token_type"][1:] + " " + auth_req_json["access_token"]

# -------------------------------------------------- required part (작동부분에서 불러올 부분)
# class of Streamer. one class per one user
class Streamer:
    def __init__(self, dict_num):
        self.num = dict_num

    #def run(self):

# function that uses the Streamer class
async def main():
    await asyncio.gather(twitter_main(streamer_json_path, app_data_path), send_chat(twitch_bot_data_path, 'terebin_420'))
    return

# -------------------------------------------------- repeated part (실제 작동 부분)
while True:
    start = time.time()
    print(time.strftime('%y/%m/%d %H:%M', time.localtime(time.time())), "\n")
    # make streamer_dict from streamer_list.json
    streamer_dict = read_list(streamer_json_path)
    # check each streamer
    num = 1 # 0 is standard data
    while num < len(streamer_dict):
        streamer_data = streamer_dict[str(num)]
        is_live, category, title = twitch_check(streamer_data["1_twitch_id"], app_key, auth_token)
        if is_live is None:
            pass
        else:
            pass


        num = num + 1


    asyncio.run(main())
    print("실행시간 :", str(round(time.time() - start, 2)) + "초")
    print("-"*50)
    time.sleep(20)
