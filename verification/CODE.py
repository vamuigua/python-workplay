name = raw_input("Please write your name...")
openfile = open("test.txt", "r")
if name not in file.readline():
    file.write(name)
    file.close()
    print ("Success!")
else:
    print ('Name not found')