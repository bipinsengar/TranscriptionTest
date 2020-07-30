Objective:
To Test the transcription accuracy of Dialpad Call, for various english accent

Environment Setup:
1. 2 Dialpad System (For making calls)
2. AudioCable (software to mimic mic and play  the same over speaker)
3. Python interprator with project specific packages

How we are doing it??
1. Python script will send first 300 mp3 files and then collect transcription summary.
2. Then with same script send remaining mp3 files and collect transcription summary as csv.
3. Process both transcription and mapped them against mp3 file sent.
4. With help of python fuzzy module which uses Levenshtein Distance algorithem to get the percentage of accuracy.
https://www.datacamp.com/community/tutorials/fuzzy-string-python
5. Test score of all mp3 files against 80 % accuracy.

Report Link:
https://vigorous-hamilton-9a8d0e.netlify.app/


Improvements:-
