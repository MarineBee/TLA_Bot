import requests
from error_logging import err_logging

# get channel data from twitch.
def twitch_check(streamer_id, app_key, auth_token):
    stream_headers = {'client-id': app_key, 'Authorization': auth_token}
    try:
        stream_req = requests.get(f"https://api.twitch.tv/helix/search/channels?query={streamer_id}", headers=stream_headers)
    except requests.exceptions.ConnectionError as err:
        err_logging(err)
        print("req error : twitch 연결 실패\n???")
        return None, None, None

    stream_data_json = stream_req.json()["data"]

    # check for specific streamer
    i = 0
    category = ""
    title = ""
    is_live = False  # refreshing variable is_live
    while i < len(stream_data_json):
        stream_data = stream_data_json[i]
        if stream_data["broadcaster_login"] == streamer_id:
            is_live = stream_data["is_live"]
            category = stream_data["game_name"]
            title = stream_data["title"]
            print(stream_data["display_name"])
            break
        else:
            i += 1

    if is_live:
        print("online")
    else:
        print("offline")

    return is_live, category, title
