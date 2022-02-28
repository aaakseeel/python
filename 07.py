#h07
#aksel ratt
#28.02.22

#ruumalade leidmise programm
print('********** LEIAME RUUMALA **********')
print('Choose your fighter: 1. Kuup, 2. Kera, 3. Koonus, 4. Silinder')
valik=int(input('Vali kujundi nr: '))

def kuup(a):
    v=a**3
    return v

if valik==1:
    print('Tark otsus...')
    a=int(input('Sisesta kuubi külje pikkus a = '))
    print(kuup(a))
    
def kera(d):
    s=3,14*d**2
    return s

if valik==2:
    print('Ahah, nii kõva mees...')
    d=int(input('Sisesta kera diameeter d = '))
    print(kera(d))

'''
#1 ja 2
def tervita(n,keel='de'):
    if keel=='et':
        print('tere',n)
    elif keel=='en':
        print('hi',n)
    else:
        print('hallo',n)
        
n=input('nimi: ')
k=input('vali keel (et/en/de): ')
tervita(n,k)
'''