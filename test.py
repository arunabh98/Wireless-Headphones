import requests
import wavefile
import time
import sys
import wave
import struct

wrd=wave.open('/home/pranav/Documents/my_projects/Wireless-Headphones/music/test1.wav',"r")

fin = open("/home/pranav/Documents/my_projects/Wireless-Headphones/music/test1.wav","rb") # Read wav file, "r flag" - read, "b flag" - binary 
ChunkSizeString=fin.read(4) # Total Size of File in Bytes - 8 Bytes
ChunkSize=struct.unpack('I',ChunkSizeString) # 'I' Format is to to treat the 4 bytes as unsigned 32-bit inter
TotalSize=ChunkSize[0]+8 # The subscript is used because struct unpack returns everything as tuple
print("TotalSize=",TotalSize)
DataSize=TotalSize-44 # This is the number of bytes of data
print("DataSize=",DataSize)

data_len = 1000000                             #one time data length                       

for i in range(TotalSize/data_len):       
	for j in range(data_len): 
		SString = wrd.readframes(1)
		if struct.calcsize('B') < len(SString):
			break
		else:
			S=struct.unpack_from('B',SString)
			print(S[0])
			#r = requests.post('http://192.168.0.112/login', data = {'CHARACTER':S[0]}) 
			#time.sleep(0.0000226757);
print('1000000 integers sent')	
	
for i in range(TotalSize%data_len):           #iteration over entire data. issue: the data is so big that we need to send it in chunks									                      
	SString = wrd.readframes(1)
	if struct.calcsize('B') < len(SString):
		break
	else:
		S=struct.unpack_from('B',SString)
		print(S[0])
		#r = requests.post('http://192.168.0.112/login', data = {'CHARACTER':S[0]}) 
		#time.sleep(0.0000226757);
print('remaining data sent')
	

