#raise [exception [, args[, tracebac]]]
'''try:
    num=11
    print(num)
    raise ValueError
except:
    print("Exception occured")'''

try:
    print("Raising Exception")
    raise ValueError
finally:
    print("performing clean-up in finally")
    