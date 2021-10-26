count = dict()
fhand = input("Enter file:")
hand = open(fhand)
for line in hand:
    words = line.split()
    for word in words:
        count[word] = count.get(word,0)+1

#The most important part for this program
Bigcount = None
Bigword = None
for word,count in count.items():
    if Bigcount is None or count > Bigcount:
        Bigword = word
        Bigcount = count
print(Bigword,':',Bigcount)
