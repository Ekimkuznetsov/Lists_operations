# LIsts operations
# For each line, split the line into a list of words using the split() method
fname = input("Enter file name: ")
fh = open(fname)
fst = list()
for line in fh:
    x = line.split()
    for word in x:
        if word not in fst:
            fst.append(word)  
fst.sort()
print(fst)