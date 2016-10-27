import requests
import wavefile
import sys

# returns the contents of the wav file as a double precision float array
def wav_to_floats(filename = 'test1.wav'):
    w = wavefile.load(filename)
    return w[1][0]

signal = wav_to_floats('test1.wav')

def chunks(l, n):
    n = max(1, n)
    return [l[i:i+n] for i in xrange(0, len(l), n)]

chunked_signals = chunks(signal, 1000)

for chunked_signal in chunked_signals:
    r = requests.post('http://192.168.0.112/login', data = {'CHARACTER':str(chunked_signal)})
