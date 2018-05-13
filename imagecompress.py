from PIL import Image
import os
import time

size=0
qua=100
stepsize=5 #stepsize initially set to 5, change it to any integer, 5 does the job though

a=input("Enter image path\n")
p=Image.open(a)

b=input("Enter save path\n")
inputsize=input("Enter desired size\nNOTE: Put space after size and mention type like: B or KB or MB or GB)\n")
inputsize=inputsize.split(' ')
if(inputsize[1].upper()=="B"):
    desiredsize=int(float(inputsize[0]))
elif(inputsize[1].upper()=="KB"):
    desiredsize=int(float(inputsize[0])*1024)
elif(inputsize[1].upper()=="MB"):
    desiredsize=int(float(inputsize[0])*1024*1024)
elif(inputsize[1].upper()=="GB"):
    desiredsize=int(float(inputsize[0])*1024*1024*1024)

size=os.path.getsize(a)
if(size<desiredsize):
    print("Size of file is already smaller than desired size!\n")
    exit()

while size>desiredsize:
    if(qua>0):
        p.save(b,quality=qua)
        qua=qua-stepsize
        time.sleep(1)
        size=os.path.getsize(b)
    else:
        print("Unable to process the image to a smaller one, the smallest possible is being stored\n")
        break

print("Scripted by Ankan Das, UEM-Kolkata\n")
time.sleep(5)
