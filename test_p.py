import wavefile
import sys

# returns the contents of the wav file as a double precision float array
def wav_to_floats(filename = 'test1.wav'):
    w = wavefile.load(filename)
    return w[1][0]

signal = wav_to_floats(sys.argv[1])
print "read "+str(len(signal))+" frames"
print  "in the range "+str(min(signal))+" to "+str(max(signal))