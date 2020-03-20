import socket
import telepot

TOKEN = '1113352697:AAG5giiZwUq-TQJwcDZNApYvRe5rfsiyDNA'
#GROUP_ID = 643741476
GROUP_ID = -427127900

def getIp():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    ip = s.getsockname()
    s.close()
    return ip

def handle(bot, upId, ip):
    while True:
        up = bot.getUpdates()[-1]

        if upId != up['update_id']: # new msg
            upId = up['update_id']
            if up['message']['text'].lower() == 'ip':
                bot.sendMessage(GROUP_ID, ip)


if __name__ == "__main__":
    bot = telepot.Bot(TOKEN)
    ip = getIp()[0]
    upId = 0
    handle(bot, upId, ip)

