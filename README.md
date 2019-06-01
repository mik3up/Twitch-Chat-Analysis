# Twitch Chat Analysis
![twitch_logo](https://github.com/mik3up/Twitch-Chat-Analysis/blob/master/images/twitch_logo.png =25x25)

### Table of Contents
0. [Contents](#contents)
1. [Motivation](#motivation)
2. [Powerpoint](#Powerpoint)
3. [Hypothesis_test](#Hypothesis_test)
4. [Getting_data](#Getting_data)
5. [EDA_analysis](#EDA_analysis)
6. [Future_work](#Future_work)
 

<!-- add background on what twitch -->

## Motivation ![pogchamp](https://github.com/mik3up/Twitch-Chat-Analysis/blob/master/images/pogchamp.jpg) ![pogchamp](https://github.com/mik3up/Twitch-Chat-Analysis/blob/master/images/pogchamp.jpg) ![pogchamp](https://github.com/mik3up/Twitch-Chat-Analysis/blob/master/images/pogchamp.jpg)

* The world of eSports is experiencing amazing growth, technology has enabled a new category and platform to rise, and allows fans to become integrated in with the larger community.
* Having been a gamer for my whole life and also working in the field of data, I was surprised at the lack of analysis despite the scale of eSports
* I want to better understand the coorelation between how effective these platforms are in engaging the audience
    * What drives engagement?
    * What does engagement translate to in the business case (more ads? predicting better content?)
    * What determines good content? Can this be learned through data?
* Twitch was an ideal platform to use, with an average of 15 million daily Twitch viewers who watch and average of 95 minutes per day, Twitch has the scale, and depth in better understanding this coorelation.

## Powerpoint

Powerpoint presentation: [link](https://drive.google.com/file/d/1v_HMjvs2c6H-bqARwmNgRTE1vPNxhU1k/view?usp=sharing)

## Hypothesis_test

Null Hypothesis: The frequency of Twitch chat will not results in more viewers staying in the channel.

## Getting_data

A typical trend in analyzing data is that 60-80% of effort goes towards finding and cleaning the data.

My case was no different, a large part of my time was spent on learning more about the Twitch platform, learning to use the API, and then being able to extract the relevant fields that I identifed into a useable dataframe for further data analysis.

* [twitch_chat_metadata_scraper.ipynb](https://github.com/mik3up/Twitch-Chat-Analysis/blob/master/src/twitch_chat_metadata_scraper.ipynb) imports channel metadata from a specifed channel every minute, outputs results to a .txt file

*sample output*
```
2019-05-31T09:48:21.891992{'id': '34347046624', 'user_id': '30816637', 'user_name': 'AdmiralBulldog', 'game_id': '29595', 'community_ids': [], 'type': 'live', 'title': 'Secret vs OG || [A] @AdmiralBulldog', 'viewer_count': 6429, 'started_at': datetime.datetime(2019, 5, 31, 12, 2, 41), 'language': 'en', 'thumbnail_url': 'https://static-cdn.jtvnw.net/previews-ttv/live_user_admiralbulldog
```

* [twitch_chat_scraper.ipynb](https://github.com/mik3up/Twitch-Chat-Analysis/blob/master/src/twitch_chat_scraper.ipynb) uses Twitch API to retrieve Twitch chat in real-time and outputs to a .log file as they occur live

*sample output*
```
2019-05-31_09:49:44 — :gandor87!gandor87@gandor87.tmi.twitch.tv PRIVMSG #admiralbulldog :Pog

2019-05-31_09:49:44 — :jeffdack!jeffdack@jeffdack.tmi.twitch.tv PRIVMSG #admiralbulldog :OMEGALUL OMEGALUL OMEGALUL OMEGALUL OMEGALUL OMEGALUL

2019-05-31_09:49:44 — :asmodeuszx!asmodeuszx@asmodeuszx.tmi.twitch.tv PRIVMSG #admiralbulldog :POGGIES

2019-05-31_09:49:45 — :mastah85!mastah85@mastah85.tmi.twitch.tv PRIVMSG #admiralbulldog :MingLUL
```

The data was sampled from on 5/31/2019 from ~10AM thru ~1PM PST.
Sampled 6 channels across the gaming category (hearthstone/dota2)

## EDA_analysis

* [twitch_chat_EDA.ipynb](https://github.com/mik3up/Twitch-Chat-Analysis/blob/master/src/twitch_chat_EDA.ipynb) loads the .log and .txt files from the twitch data scrapers into a pandas dataframe

A few infographics of the EDA performed

![alt text](https://github.com/mik3up/Twitch-Chat-Analysis/blob/master/images/bar_chat_count.png "channel v chat count")

Word Clouds by Streamer
![alt text](https://github.com/mik3up/Twitch-Chat-Analysis/blob/master/images/[DOTA]_admiralbulldog_word_cloud.png =250x250)
![alt text](https://github.com/mik3up/Twitch-Chat-Analysis/blob/master/images/[DOTA]_dota2ruhub_word_cloud.png =250x250)
![alt text](https://github.com/mik3up/Twitch-Chat-Analysis/blob/master/images/[HS]_playhearthstone_word_cloud.png =250x250)
![alt text](https://github.com/mik3up/Twitch-Chat-Analysis/blob/master/images/[HS]_solaryhs_word_cloud.png =250x250)


## Future_work

No meaningful conclusions could be drawn from the EDA that was done so far, however the data exploration phase opened even more questions and raised more interest.

Following up on this, I would like to...

* Understand the correlation between chat activity vs viewership, and perhaps even content
* NLP / Sentiment analysis on Twitch chat
* Content analysis - can chat tell when content is becoming relevant and we can generate a clip?
* Improve the data workflow so it takes one python file, currently I need to run 2 python files per channel (not scalable)
