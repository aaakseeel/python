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
    
def kera(r):
    v=round(4*3.14*r**2)
    return v

if valik==2:
    print('Ahah, nii kõva mees...')
    r=int(input('Sisesta kera raadius r = '))
    print(kera(r))
    
def koonus(r,h):
    v=round(4*3.14*r**2)
    return v

if valik==3:
    print('Olgu. Teeme ära!')
    h=int(input('Sisesta koonuse kõrgus h = '))
    r=int(input('Sisesta koonuse raadius r = '))
    print(koonus(r,h))
    
def silinder(r,h):
    v=round(3.14*r**2*h)
    return v

if valik==4:
    print('Davai!')
    r=int(input('Sisesta silindri raadius r: '))
    h=int(input('Sisesta silindri kõrgus h: '))
    print(koonus(r,h))
    
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