#Ten program wyswietli szesc losowych i niepowtarzajacych sie liczb z zakresu od 1 do 49.
from random import randint
print "Oto szesc losowych i niepowtarzajacych sie liczb z zakresu od 1 do 49:"
x=range(1,50)
i=0
lista=[]
while len(lista)<6:
    i+=1
    x=randint(1,49)
    if x not in lista:
        lista+=[x]
lista.sort()
for j in lista:
    print j,
print "."
y=i-6
print "Podczas losowania doszlo do:",y,
if y==0:
    print "powtorzen."
elif y==1:
    print "powtorzenia."
else:
    print "powtorzen."
print "Powodzenia w losowaniu lotto! :D"
