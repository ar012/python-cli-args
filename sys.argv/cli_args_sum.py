from sys import argv

args = argv[1: ]
# print(args)

sum = 0

for x in args:
  sum=sum+int(x)
  
print("Result ", sum)

