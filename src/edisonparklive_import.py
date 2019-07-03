import pandas as pd
import time
import datetime

data_file = '../chat_log_data/edisonparklive_445273558.txt'

def create_df(data_file):
    print("creating df...\n")
    df = pd.DataFrame(columns=['timestamp', 'user', 'chat_msg']) #initializes the dataframe
    
    with open(data_file, "r") as f:
        line_counter = 0
        for line in f:
            timestamp = line[1:6]
            user = line[15:][:line[15:].find(':')]
            chat = line[15:][line[15:].find(':')+2:-1]
            df.loc[line_counter] = (timestamp, user, chat)
            line_counter += 1
    print('df complete!')
    return df
        
start_time = time.time()
df = create_df(data_file)
print("\n\n--- the process took %s seconds ---" % (time.time() - start_time))

df['timestamp'][0] = '00:00'
df['timestamp'] = df['timestamp'].apply(lambda x: datetime.datetime.strptime(x, '%H:%M').time())

