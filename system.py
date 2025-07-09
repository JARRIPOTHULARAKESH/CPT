import sys
print("Script name:",sys.argv[0])
print("All args:",sys.argv[1:])
if len(sys.argv)>1:
    print("First arg:",sys.argv[1])
else:
    print("No arguments provided")