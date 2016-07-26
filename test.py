print "Hello, Welcome to Python!"

name =input('Please write you name...')
age =input('What is your age?')
if age <18:
    print ('You are not allowed to enter!')
elif age>=18:
    print ('Enjoy yourself!')
elif age>=30:
    print ('Too old for this!')
else:
    print ('Invalid input...Try again!')

raw_input("\n\nPress the enter key to exit.")
