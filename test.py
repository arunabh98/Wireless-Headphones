import requests
import wavefile
import time
import sys
import wave
import struct

wrd=wave.open('/home/pranav/Documents/my_projects/Wireless-Headphones/music/piano2.wav',"r")

fin = open("/home/pranav/Documents/my_projects/Wireless-Headphones/music/piano2.wav","rb") # Read wav file, "r flag" - read, "b flag" - binary 
ChunkSizeString=fin.read(4) # Total Size of File in Bytes - 8 Bytes
ChunkSize=struct.unpack('I',ChunkSizeString) # 'I' Format is to to treat the 4 bytes as unsigned 32-bit inter
TotalSize=ChunkSize[0]+8 # The subscript is used because struct unpack returns everything as tuple
print("TotalSize=",TotalSize)
DataSize=TotalSize-44 # This is the number of bytes of data
print("DataSize=",DataSize)


for i in range(1000):           #iteration over entire data. issue: the data is so big that we need to send it in chunks									                     
 	SString=wrd.readframes(1) 
	S=struct.unpack_from('h',SString)
	print(S[0])                #data type is int 




# def chunks(l, n):
#     n = max(1, n)
#     return [l[i:i+n] for i in xrange(0, len(l), n)]

# chunked_signals = chunks(signal, 1000)
'''
for x in signal:
	r = requests.post('http://192.168.0.112/login', data = {'CHARACTER':str(100*x)})
	time.sleep(0.0000226757);
'''
# for chunked_signal in chunked_signals:
#     r = requests.post('http://192.168.0.112/login', data = {'CHARACTER':chunked_signal})