#h04
#a. "hitler" ratt
#03.02.1945

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

#jalgpalli meeskond
vanus=16-18