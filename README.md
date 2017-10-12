# LSTMDrumGenerator
Drum pattern generator based on character generator

# Current status
First posting I am doing of this is for a simple one drum example. I have visualised this as a snare drum. 

Create a text file with the pattern of the snare drum, as 1 and 0 (hit or no hit). I have done with 16ths in mind so I have every 4 characters as a beat. So for a snare hit on the 2's it would be 0000000100000001

The model will generate a new sequence for you with the length of the seq_length that you tell it. I have it set to 16 so it will produce 1 bar of snare. Current snare.txt file is just made up on the fly, not a song.

# Further work
To expand this further I believe it would be beneficial to develop a dictionary mapping all combinations of drums being played to numerical values. For example:

0 : None
1 : Hi-Hat only
2 : Hi-Hat & Snare
3 : Hi-Hate & Bass Drum

etc.....

This would allow for any combination of drums being played at once to be represented.

This is a quick and dirty way to tie all the drums together in processing through one LSTM model.

For the short term we could do this for a few songs manually from tabs to test the idea. In the long term if we end up liking this idea we should try and create a function to read in standard format tabs and do this task for us.

