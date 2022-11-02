from twitch_chat_irc import twitch_chat_irc


async def send_chat(twitch_bot_data_path, channel):
    username = 'TtTB_'
    oauth_data = open(twitch_bot_data_path, 'r', encoding='utf-8')
    oauth = oauth_data.read()
    oauth_data.close()
    connection = twitch_chat_irc.TwitchChatIRC(username, oauth)

    message = '테스트용 채팅입니다.'
    connection.send(channel, message)
    connection.close_connection()
