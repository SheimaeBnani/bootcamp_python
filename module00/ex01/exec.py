import sys

m = len(sys.argv)
Strng =""
for i in range(1, m):
        Strng+=" "+sys.argv[i]
Str_case = Strng.swapcase()
print(''.join(reversed(Str_case)))

