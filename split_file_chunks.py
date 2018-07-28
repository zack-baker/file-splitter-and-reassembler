from sys import argv
import os

#Set initial variables

MBYTE_MULT=1024*1024
filepath = argv[1]
block_size = int(argv[2])
filesize = os.path.getsize(filepath)
passes=0

f_obj = open(filepath,"rb")

#for each full block,
while filesize>block_size*MBYTE_MULT:
	#get the output block name from the file name + the pass #
	dest_name = argv[1] + "_" + str(passes)
	passes+=1
	#open the output block file for writing
	dest_obj = open(dest_name,"wb")

	#read in a blocks worth of data from the original file
	temp_contents = f_obj.read(block_size*MBYTE_MULT)

	#write the block to the file
	dest_obj.write(temp_contents)

	#close the output file
	dest_obj.close()

	#reduce the tracker keeping track of the amount of file we have left to read
	filesize-=block_size*MBYTE_MULT


#repeat the looped process, but only read to the end of the file, not an entire blocks worth, because we dont have that many bytes anymore
dest_name = argv[1] + "_" + str(passes)
dest_obj = open(dest_name,"wb")
temp_contents = f_obj.read(filesize)
dest_obj.write(temp_contents)
dest_obj.close()




