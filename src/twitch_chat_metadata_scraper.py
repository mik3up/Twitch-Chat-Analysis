# # Scraping Twitch Channel Metadata
# 
# ### Uses Twitch API / Python client to extract data
# 
# The following code runs and logs data until manually stopped


# specify channel data and text file name
channel_name = input('Enter channel name: ')
# channel_name = 'singsing'
print('getting metadata for channel: ' + channel_name)
log_path = '../chat_log_data/'
log_file_name = log_path + channel_name + '_stream_metadata.txt'

#Twitch API calls
from itertools import islice
from twitch import TwitchHelix
import os

client = TwitchHelix(client_id=os.environ.get('TWITCH_CLIENT_KEY'))

f = open(log_file_name,"a+")
f.close()

#writes to time and data to file
import time
starttime=time.time()
import datetime

while True:
    #gets current channel metadata
    streams_iterator = client.get_streams(user_logins=channel_name)
    stream_data = streams_iterator.next()
    
    #gets current datetime
    now = str(datetime.datetime.now().isoformat())
    
    #prints current time output
#     print ("tick- ",now)
    
    #writes time and channel metadata to file
    data = str(now+str(stream_data)+"\n")
    f = open(log_file_name,"a+")
    f.write(data)
    print(data)
    f.close()

    time.sleep(60.0 - ((time.time() - starttime) % 60.0))