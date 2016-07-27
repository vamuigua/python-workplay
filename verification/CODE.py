name = raw_input("Please write your name...")
openfile = open("names.txt", "r+")
if name not in openfile.readline():
    openfile.write(name)
    openfile.close()
    print ("Success!")
else:
    print ('Name not found')
    openfile.close()