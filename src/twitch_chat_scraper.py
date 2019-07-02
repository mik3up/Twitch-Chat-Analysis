import os
import time
import socket
import logging
from emoji import demojize

class twitch_chat_scraper:
    def __init__(self, channel):
        self.channel_name = channel
        
    def scraper(self, channel_name):
        server = 'irc.chat.twitch.tv'
        port = 6667
        nickname = 'gCapstone2'
        token = os.environ.get('TWITCH_OAUTH_TOKEN')


        #specify the channel and log file name
        # channel = '#'+input('Enter Channel Name: ')
#         channel = '#edisonparklive'
        channel = '#' + channel_name
        print('Getting twitch chat data for channel ' + channel)
        log_path = '../chat_log_data/'
        log_file_name = log_path + channel[1:] + '_chat.log'

        #To establish a connection to Twitch IRC we'll be using Python's socket library. First we need to instantiate a socket:

        sock = socket.socket()
        sock.connect((server, port))

        time.sleep(1)

        #Once connected, we need to send our token and nickname for authentication, and the channel to connect to over the socket.

        # With sockets, we need to send() these parameters as encoded strings:

        sock.send(f"PASS {token}\n".encode('utf-8'))
        sock.send(f"NICK {nickname}\n".encode('utf-8'))
        sock.send(f"JOIN {channel}\n".encode('utf-8'))

        # Now we have successfully connected and can receive responses from the channel we subscribed to. To get a single response we can call .recv() and then decode the message from bytes:

        resp = sock.recv(2048).decode('utf-8')
        print(resp)

        time.sleep(1)

        # Note: running this the first time will show a welcome message from Twitch. Run it again to show the first message from the channel.

        # The 2048 is the buffer size in bytes, or the amount of data to receive. The convention is to use small powers of 2, so 1024, 2048, 4096, etc. Rerunning the above will receive the next message that was pushed to the socket.

        resp = sock.recv(2048).decode('utf-8')
        print(resp)

        time.sleep(1)

        # Writing messages to a file
        # Right now, our socket is being inundated with responses from Twitch but we have two problems:

        # We need to continuously check for new messages
        # We want to log the messages as they come in
        # To fix, we'll use a loop to check for new messages while the socket is open and use Python's logging library to log messages to a file.

        # First, let's set up a basic logger in Python that will write messages to a file:

        # saves to the specified log file name
        counter=0
        class ContextFilter(logging.Filter):
            def filter(self, record):
                record.count = counter
                return True

        logging.basicConfig(level=logging.DEBUG,
                            format='%(asctime)s —— %(count)s —— %(message)s',
                            datefmt='%Y-%m-%d_%H:%M:%S',
                            handlers=[logging.FileHandler(log_file_name, encoding='utf-8')])
        logging = logging.getLogger(__name__)
        logging.addFilter(ContextFilter())

        time.sleep(1)

        logging.info(resp)
        print(resp)

        time.sleep(1)

        # Continuous message writing
        # Now on to continuously checking for new messages in a loop.

        # When we're connected to the socket, Twitch (and other IRC) will periodically send a keyword — "PING" — to check if you're still using the connection. We want to check for this keyword, and send an appropriate response — "PONG".

        # One other thing we'll do is parse emojis so they can be written to a file. To do this, we'll use the emoji library that will provide a mapping from emojis to their meaning in words. For example, if a 👍 shows up in a message it'll be converted to :thumbs_up:.

        # The following is a while loop that will continuously check for new messages from the socket, send a PONG if necessary, and log messages with parsed emojis:

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
                print('printing ' + counter + " " + resp)

        # This will keep running until you stop it. To see the messages in real-time open a new terminal, navigate to the log's location, and run tail -f chat.log.

if __name__ == "__main__":
    twitch_chat_scraper.scraper(self.channel_name)