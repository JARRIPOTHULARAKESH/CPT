from collections import Counter
text=input("Enter a text:")
counter=Counter(text)
print("Characters frequencies:",dict(counter))