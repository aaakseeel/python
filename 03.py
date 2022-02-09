#h03
#a. ratt
#03.02.22

#palindroom
#sisestus
palin=input('sisesta palindroom:')
print([::-1])

#tundide ajad
start=input('algusaeg:')
lopp=input('lõpuaeg: ')
#tükeldus
hh1,mm1=start.split(':')
hh2,mm2=lopp.split(':')
#teisendamine minutiks
minutid=int(hh1)*60+int(mm1)
minutid2=int(hh2)*60+int(mm2)
#absoluutväärtus
ajavahe=abs(minutid-minutid2)
#teisendamine hh:mm
hh=ajavahe // 60 #täisarvuline jagamine
mm=ajavahe%60 #jääk
#lause formindamine format abil
print(f'õpilaste päeva pikkus on {hh}:{mm}')

#emaili kontroll
#true/false, in/not in
email=input('sinu meil:')
print("@" in email)

#vandumine
vanne=input('ära kurat ütle:')
vanne=vanne.lower().replace('kurat','***')
print(vanne)

#korralik kasutajanimi
nimi=input('sisesta nimi:')
nimi=nimi.capitalize().strip()
print('tere '+nimi+'!')
