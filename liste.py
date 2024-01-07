# listele in python pot sa curpinda elemente de tipuri diferite
# au dimeniune dinamica

fructe = ['mar', 'banana', 'portocala', 3, True, 3]

# afisam  o lista
print (fructe)

# accesam un element in f de index
print (fructe[1])

# adaugam un nou element
fructe.append('rosie')

# suprascirem un element
fructe[0] = 'para'

# afisam lista
print(fructe)

# aflam dimensiunea
print(len(fructe))

# scoate si ne returneaza ultimul element
last = fructe.pop()
print (last)
print (fructe)

# de cate ori apare un elem?
print(fructe.count(3))

fructe_exotice = ['ananas', 'kiwi']
fructe.extend(fructe_exotice)
print(fructe)
