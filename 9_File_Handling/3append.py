# append an existing file ganesh.txt and insert some data

f = open("ganesh.txt","a")

x = "\nHey this content is added using append"

f.write(x)

f.close()