import os
import time
import socket
import logging
from emoji import demojize

class twitch_chat_scraper():
    def __init__(self):
        pass
        
    def scraper(self):
        server = 'irc.chat.twitch.tv'
        port = 6667
        nickname = 'gCapstone2'
        token = os.environ.get('TWITCH_OAUTH_TOKEN')

        channel = '#'+input('Enter Channel Name: ')
        print('Getting twitch chat data for channel ' + channel)
        log_path = '../chat_log_data/'
        log_file_name = log_path + channel[1:] + '_chat.log'

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

        print(resp)

        time.sleep(1)

        while True:
            counter+=1
            resp = sock.recv(2048).decode('utf-8')
        #     print(counter, resp)

            if resp.startswith('PING'):
                sock.send("PONG\n".encode('utf-8'))

            elif len(resp) > 0:
        #         logging.info(demojize(resp))
                logging.info(resp)

            if (counter < 5):
                print('printing ' + str(counter) + " " + resp)

if __name__ == "__main__":
    t = twitch_chat_scraper()
    t.scraper()