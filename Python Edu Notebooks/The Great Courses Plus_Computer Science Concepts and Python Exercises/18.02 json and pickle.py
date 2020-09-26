# JSON utility
import json

myfile = open("filename", "w")

json_string = json.dumps(data)
myfile.write(json_string+'\n')

json_string = myfile.readline()
data = json.loads(json_string)

myfile.close()
# ============================
length = 34
width = 2

outfile = open("datafile.json", "w")

json_string = json.dumps(length)
outfile.write(json_string+'\n')
json_string = json.dumps(width)
outfile.write(json_string+'\n')
json_string = json.dumps("data for an example")
outfile.write(json_string+'\n')

outfile.close()
# ============================
infile = open("datafile.json", "w")
json_string = infile.readline()
l = json.loads(json_string)
json_string = infile.readline()
w = json.loads(json_string)
json_string = infile.readline()
description = json.loads(json_string)
infile.close()

print(description)
print(l*w)
#=================================================

# PICKLE
import pickle

infile = open("pickleFile", "rb")
data = pickle.load(infile)

account = pickle.load(infile)
owner = pickle.load(infile)
balance = pickle.load(infile)

infile.close()

outfile = open("pickleFile", "wb") # write binary
# outfile = open("pickleFile", "wr") # write binary
# outfile = open("pickleFile", "wa") # append binary

pickle.dump(data, outfile)

outfile.close()

# or store entire objects and retrieve them as such
class MyBigObj:
    stuff = 3


fullObj1 = MyBigObj()
fullObj2 = MyBigObj()

outfile = open("pickleFile", "wb") # write binary
pickle.dump(fullObj1, outfile)
pickle.dump(fullObj2, outfile)

outfile.close()

infile = open("pickleFile", "rb")
newFullObj1 = pickle.load(infile)
newFullObj2 = pickle.load(infile)

infile.close()