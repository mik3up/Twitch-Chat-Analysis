import os
from twitch import TwitchHelix                                                                
from multiprocessing import Pool                                                                       

import time
import socket
import logging
from emoji import demojize

def twitch_chat(channel):
    server = 'irc.chat.twitch.tv'
    port = 6667
    nickname = 'gCapstone2'
    token = os.environ.get('TWITCH_OAUTH_TOKEN')

    channel = '#' + channel
    print('Getting twitch chat data for channel ' + channel)
    log_path = '../chat_log_data/'
    log_file_name = log_path + channel[1:] + '_chat.log'
    print('printing chat to ' + log_file_name)

    sock = socket.socket()
    sock.connect((server, port))

    time.sleep(1)

    sock.send(f"PASS {token}\n".encode('utf-8'))
    sock.send(f"NICK {nickname}\n".encode('utf-8'))
    sock.send(f"JOIN {channel}\n".encode('utf-8'))

    resp = sock.recv(2048).decode('utf-8')
    print(resp)

    time.sleep(1)

    resp = sock.recv(2048).decode('utf-8')
    print(resp)

    time.sleep(1)

    counter=0
    
    logging.basicConfig(level=logging.DEBUG,
                        format='%(asctime)s —— %(message)s',
                        datefmt='%Y-%m-%d_%H:%M:%S',
                        handlers=[logging.FileHandler(log_file_name, encoding='utf-8')])

    time.sleep(1)

    logging.info(resp)
    
    time.sleep(1)

    while True:
        counter+=1
        print(str(counter) + ' ' + channel + ': ' + resp)
        resp = sock.recv(2048).decode('utf-8')

        if resp.startswith('PING'):
            sock.send("PONG\n".encode('utf-8'))

        elif len(resp) > 0:
            logging.info(resp)

if __name__ == "__main__": 
    
    client = TwitchHelix(client_id=os.environ.get('TWITCH_CLIENT_KEY'))

    get_streams = client.get_streams(page_size=100)[1:]
    top_50_channel_list = []

    for stream in get_streams:
        if(stream['language'] == 'en'):
            top_50_channel_list.append(stream['user_name'])

    my_list = top_50_channel_list[0:5]

    processes = my_list
    pool = Pool(processes=len(my_list))                                                        
    pool.map(twitch_chat, processes)