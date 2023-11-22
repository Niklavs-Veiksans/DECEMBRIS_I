datne = input("datne:")
garums = input("garums")

with open(datne,'rb') as datne:
    saturs = datne.read()

print(len(saturs))

print(saturs[:10])
print(saturs[:1],saturs[-1:])

if garums == len(saturs):
    print('wow tu esi tik gudrs uzmineju teksta garumu')
    print(saturs)
elif garums > len(saturs):
    print('wow tu esi tik negudrs tur tak tik daudz nav dumikit')
elif garums < len(saturs):
    print(saturs[:garums])