'''
Modes:
r -> if the not exists then we will get the FileNotFoundError. otherwise we will be able
     to read the file content
w   -> If the file does not exists then it will create the file and start writing into it.
        if the file exists then it will clean up the file and start writing as a new file.
a   -> if file does not exists then it will create a file and start writing into it
        if the file exists it will continue to append along with the existing content.
r+  -> read file content and write into ti
w+  -> write first and read whatever has been written into it
rb -> read special file such as image file, video file, audio file
wb  -> write the special file as above
'''
"""
#to read : read(), readline(), readlines()
with open('days.txt','r') as fh:
    #print(fh.read())
    #print(fh.readline(),end='')
    #print(fh.readline())
    print(fh.readlines()[2:5])


#to write : write, writelines
with open('myfile.txt','w') as wfh:
    #wfh.write("PYTHON PROGRAMMING")
    wfh.writelines(["Python\n",'Java\n','AWS'])

#append : write, writelines
with open('myfile.txt','a') as afh:
    #afh.write('\nSnowflake\n')
    afh.writelines(["India\n","USA\n","Canada\n","Singapore\n","Japan\n"])

with open('myfile.txt','r+') as rwfh:
    print(rwfh.read())
    rwfh.write("-----END OF THE LINE -----\n")

with open('myfile.txt','w+') as fh:
    fh.writelines(['Chennai\n','Newyork\n','Dearborn'])
    fh.seek(0,0)
    print(fh.read())
"""
with open(r'C:\Users\RaghulRamesh\Pictures\puppy.jpg','rb') as fo:
    with open(r'C:\Users\RaghulRamesh\Pictures\puppy_new.jpg','wb') as wo:
        wo.write(fo.read())
