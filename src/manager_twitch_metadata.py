import os
from twitch import TwitchHelix
from multiprocessing import Pool                                                                                                 

def twitch_chat_metadata_scraper(channel_name):
    print('getting metadata for channel: ' + channel_name + '\n')
    log_path = '../chat_log_data/'
    log_file_name = log_path + channel_name + '_stream_metadata.txt'

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
    pool.map(twitch_chat_metadata_scraper, processes)





