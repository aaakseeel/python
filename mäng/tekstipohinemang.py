# tekstipõhine mäng
# aksel ratt
# it21

# moodulid
import random

# stat'id
elud = 100 # su elud
dmg = random.randint(20, 50) # kahju mida teed
xp = 0 # puntkid, mida näed mängu lõpus
lvl = 0 # su tase
velud = 100 # vaenlase elud
vdmg = random.randint(10, 30) # kahju mida vaenlane teeb

# menüü
print('kalevipoeg ja igavene narkomaania')
print()
print('lugu ja progemine: aksel ratt')
print()
algus = int(input('(1) alusta (2) anna alla '))
print()

# kakluse funktsioon
def kaklus(velud, elud):
    global algus
    while elud >= 0 and velud >= 0:
        velud -= dmg
        elud -= vdmg
        print(f'tegid {dmg} kahju')
        print()
        print(f'vaenlane tegi {vdmg} kahju')
        print()
        print(f'sinu elud: {elud}')
        print(f'vaenlase elud: {velud}')
    
    if velud <= 0:
        print('võit')
        algus = 2
    else:
        print('surid')
        algus = 2
        
if algus == 1:
    kn = input('nimi: ')
    while algus == 1:
        print(algus)
        kaklus(elud, velud)
elif algus == 2:
    exit()

# nime valik
print(f'jou, {kn}! sinu eesmärk: tapa ära sibul, et saada narkot')
print()

# mäng
while elud >= 0:
    print('lvl 1: sibul')
    print()
    print('sibul: kakleme')
    print()
    print('kalevipoeg: teeme nii')
    print()
    
    kaklus(elud, velud)
