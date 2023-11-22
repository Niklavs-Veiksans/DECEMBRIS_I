datne = input("datne:")
garums = input("garums")
garint = str(garums)
if not garums == garint:
    print('pedodiet jusu vertiba nav skaitlis')
with open(datne,'rb') as datne:
    saturs = datne.read()



print(len(saturs))

print(saturs[:10])
print(saturs[:1],saturs[-1:])

if garint == len(saturs):
    print('wow tu esi tik gudrs uzmineju teksta garumu')
    print(saturs)
elif garint > len(saturs):
    print('wow tu esi tik negudrs tur tak tik daudz nav dumikit')
elif garint < len(saturs):
    print(saturs[:garint])