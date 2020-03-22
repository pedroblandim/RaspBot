import socket
import telepot
import psutil

TOKEN = '1113352697:AAG5giiZwUq-TQJwcDZNApYvRe5rfsiyDNA'
#GROUP_ID = 643741476
GROUP_ID = -427127900

def getIp():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    ip = s.getsockname()
    s.close()
    return ip

def handle(bot, ip, request):
    # Possible requests:
    # ip
    # cpu <intervals=1> <each=False>

    request =  request['message']['text'].lower().split(' ')
    command =  request[0]  
    print(f'req: {request} com:{command}')
    

    # ip 
    if command == 'ip':
        response = ip
       

    # cpu usage
    elif command == 'cpu':
        try: 
            intervals = int(request[1]) if int(request[1]) > 0 else 1
        except:
            intervals = 1 # default value, in case intervals is not given
        
        cpus = len(psutil.cpu_percent(percpu=True)) # number of cores
        response = "CPU USAGE IN %\n\n"
        try:
            each = request[2]
        except:
            each = False

        if each:
            for i in range(intervals):
                usage = psutil.cpu_percent(interval=0.1, percpu=True)
                for i in range(cpus):
                    if i == cpus//2:
                        response += '\n'
                    response += f'Cpu{i}: {usage[i]}   '
                response += '\n\n'

        else:
            for i in range(intervals):
                usage = psutil.cpu_percent(interval=0.1)
                response += f'Cpu: {usage}\n'
        
    bot.sendMessage(GROUP_ID, response)
    return response
        




def listen(bot, ip):

    upId = bot.getUpdates()[-1]['update_id']
    while True:
        lastUp = bot.getUpdates()[-1] # last update

        # upId saves the id of the last update answered, except when initializing
        # if the last update answered is equal to the last update, there's nothing to be done
        if upId != lastUp['update_id']: # new msg
            upId = lastUp['update_id']
            handle(bot, ip, lastUp)



if __name__ == "__main__":
    bot = telepot.Bot(TOKEN)
    ip = getIp()[0]
    listen(bot, ip)

