import os
import pandas as pd

# configuration
base_dir = os.getcwd()
ordered_file_name_csv = os.path.join(base_dir, 'csvs/mp3_played_order_579.csv')
transcription_csv = os.path.join(base_dir, 'csvs/transcript_579.csv')
df1 = pd.read_csv(transcription_csv)
# assigning unique name to variables
transripted_speech_list = [text for text in df1['content']]
df2 = pd.read_csv(ordered_file_name_csv)
# assigning unique name to variables
ordered_file_name_list = [text for text in df2['file_name']]
dict_to_csv = {'${file_name}': ordered_file_name_list,'${transripted_speech}': transripted_speech_list}

df = pd.DataFrame(dict_to_csv)

# saving the dataframe
df.to_csv('csvs/transripted_speech_579.csv', sep=";")
