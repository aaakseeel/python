import random
#h04
#aksel ratt
#03.02.22

#ruutude ja kuupide tabel

#pank
konto=0
raha=int(input('summa: '))
aastad=int(input('aastad: '))
intress=0.05
konto=konto+raha

print
for a in range(aastad):
    kasum=konto*intress
    print(konto,kasum,konto+kasum)
    konto=konto+kasum


#arvamismäng

#viiskud

#paaris ja paaritu

#pisike korrutustabel

#loto
for a in range(1,6):
    print(random.randint(0, 9),end='')
'''
#tärnid
arv=5
for i in range(1,6):
    print('* '*arv)
    arv=arv-1

for i in range(1,6):
    print('* '*5)

for i in range(1,6):
    print('* '*i)

#jalgpalli meeskond
sugu=input('sisesta sugu: ')

if sugu=='mees':
    vanus=int(input('sisesta vanus: '))
    if vanus>=16 and vanus<=18:
        print('sobid meeskonda')
    else:
        print('ei sobi meeskonda')
    
#matemaatika
arv1=('')
arv2=('')
tehe=input('vali tehe:\n1) liitmine\n2) lahutamine jne')

if tehe==1:
    teen seda
elif tehe==2:
    teen seda
elif= tehe==3:
    teen seda
else:
    teen

#ruudu kontroll
a=int(input('sisesta ruudu üks külg:'))
b=int(input('sisesta ruudu teine külg:'))
if a==b:
    print('tegemist on ruuduga')
else:
    print('risttahukas')

#juubel
sunnipaev=input('kirjuta sünnipäev pp.kk.aaaa: ')
a=2022
pp,kk,aaaa=sunnipaev.split('.')

vanus=a-int(aaaa)

a=5
jaak = a%2
 
if jaak==0:
    print('juubel')
else:
    print('pole juubel')

#müük
hind=int(input('toote hind: '))

if hind>10:
    ale=0.1
else:
    ale=0.2
    
vastus=(hind*ale)
print(vastus)
'''