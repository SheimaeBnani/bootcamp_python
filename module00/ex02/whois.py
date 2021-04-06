import sys

if(len(sys.argv)<=1):
        sys.exit(1)
a=int(sys.argv[1])

if(len(sys.argv)>2):
        print("ERROR")
else:
        if(a%2==0 and a!=0):
                print("I am Even")
        if(a%2!=0):
                print("I am Odd")
        if(a==0):
                print("I am Zero")

