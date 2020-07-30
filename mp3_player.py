import os
import time
import pandas as pd
from pydub import AudioSegment
from pydub.playback import play

# ####Configurations###########
base_dir = os.getcwd()
input_folder = os.path.join(base_dir, 'speech_sam/')
# sound = AudioSegment.from_wav('1to10.wav')
# sound = AudioSegment.from_mp3('test.mp3')
# play(sound)
cnt=0
mp3_played_ordered_list = []
for files in os.listdir(input_folder):
    # Inside First Folder. For example Under sample1
    mp3s_parent_path = input_folder + files
    for mp3s in os.listdir(mp3s_parent_path)[:300]:
        mp3s_abs_path = mp3s_parent_path + '/' + mp3s
        print (f"{cnt} playing {mp3s} . . . ")
        sound = AudioSegment.from_mp3(mp3s_abs_path)
        mp3_played_ordered_list.append(mp3s)
        play(sound)
        time.sleep(25)
        cnt = cnt+1

# dictionary of lists  
dict_to_csv = {'file_name': mp3_played_ordered_list}

df = pd.DataFrame(dict_to_csv)

# saving the dataframe 
df.to_csv('csvs/mp3_played_order_579.csv')