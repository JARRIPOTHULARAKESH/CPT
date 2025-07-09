'''import sys
print("Script name:",sys.argv[0])
print("All args:",sys.argv[1:])
print("Number of items:",len(sys.argv))
print("Included file name:",sys.argv)
if len(sys.argv)>1:
    print("First arg:",sys.argv[1])
else:
    print("No arguments provided")'''

'''num1=int(sys.argv[1])
num2=int(sys.argv[2])
num3=int(sys.argv[3])
print("product:",num1*num2*num3)'''

import argparse
parser=argparse.ArgumentParser(description="Simple Calculator.")
parser.add_argument("--x", type=int,required=True, help="First number")

parser.add_argument("--y", type=int,required=True, help="Second number")
parser.add_argument("--opt", type=str,required=True, choices=["add","sub","mul","div"], help="Operation to perform")
args=parser.parse_args()
if args.opt=="add":
    result=args.x+args.y
elif args.opt=="sub":
    result=args.x-args.y
elif args.opt=="mul":
    result=args.x*args.y
elif args.opt=="div":
    result=args.x/args.y
print("Result is:",result)