#h05
#aksel ratt
#15.02.22

#Tärnid
arvud=[16,17,18,19,20]

print(arvud)
for x in range(sum(arvud)):
    print('*'*arvud[x])

'''
#Vanused
vanused=[16,17,18,19,20]

print(vanused)
print(min(vanused),max(vanused))
print(sum(vanused)/len(vanused)) #olen geenius

#Duplikaadid
opilased=['Juhan','Kati','Mario','Mario','Mati','Mati']
opilased=sorted(set(opilased))
print(opilased)

#Õpilased
opilased=['Juhan','Kati','Maarja','Mario','Mati']
print('vali nime nr, mida tahad kustutada: ')
for x in range(len(opilased)):
    print(f'{x+1}.{opilased[x]}')
valik=int(input('sisesta nr: '))
valik=valik-1
del opilased[valik]

nimi=input('sisesta uus nimi: ')
opilased.insert(valik, nimi)
print(opilased)

#Nimede lisamine loendisse
nimed=[]

for x in range(5):
    nimi=input('lisa nimi: ')
    nimed.append(nimi)
nimed.sort()
print(nimed)
'''