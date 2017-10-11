# LSTMDrumGenerator
Drum pattern generator based on character generator

# Current status
First posting I am doing of this is for a simple one drum example. I have visualised this as a snare drum. 

Create a text file with the pattern of the snare drum, as 1 and 0 (hit or no hit). I have done with 16ths in mind so I have every 4 characters as a beat. So for a snare hit on the 2's it would be 0000000100000001

The model will generate a new sequence for you with the length of the seq_length that you tell it. I have it set to 16 so it will produce 1 bar of snare. Current snare.tct file is just made up on the fly, not a song.

# Further work
My plan is to extend this so that it has instead of just one LSTM, it will have 8, one for each drum and cymbal in a standard kit. At first all 8 LSTM models will predict their own new sequence but as long as they are fed from text files that follow the same conventions ie. same songs in the same order with 16ths as their timing then this should work.

Longterm it may be beneficial to try and use a merge layer to predict them in conjunction with one another as in music of course playing one drum and one cymbal often times is something that you do together for a reason. They are not always played as independant drums.

