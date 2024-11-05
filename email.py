contenido = list()
listo = list()
count = 0
fname = input("Enter file name: ")
if len(fname) < 1:
    fname = "mbox-short.txt"

fh = open(fname)
for line in fh:
    if line.startswith('From: '):
        continue
    elif line.startswith('From '):
        contenido = line.split()
        listo.append(contenido[1])
        count = count + 1

#print(listo)
for saltos in listo:
    print(saltos.rstrip())
print("There were", count, "lines in the file with From as the first word")

