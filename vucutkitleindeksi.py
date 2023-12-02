boy=float(input("Boyunuzu metre cinsinden giriniz: "))
kilo=float(input("Kilonuzu kilogram cinsinden giriniz: "))
vki= float(kilo/boy**2)
print(f"Vücut kitle indeksiniz {vki}")

if vki>=0 and vki<=18.5:
    print("Kilo almalısın.")

elif vki>=18.5 and vki<=24.9:
    print("İdeal kilodasın,formunu koru.")

elif vki>=25 and vki<=29.9:
    print("Kilon fazla,bir diyetisyen eşliğinde daha sağlıklı olabilirsin.")

elif vki>=30 and vki<=34.9:
    print("Birinci dereceden obezsin.")

else :
    print("Hesaplayamadım :D")

enazidealkilo=(18.5*boy**2)

if vki>24.9 :
    idealkilo=(24.9*boy**2)
elif vki>18.5 :
    enazidealkilo=(18.5*boy**2)
elif vki<18.5 :
    idealkilo=(18.5*boy**2)

vgk= kilo-idealkilo
eavgk=kilo-enazidealkilo
print(f"En az vermeniz gereken kilo {vgk}, En fazla vermeniz gereken kilo {eavgk}")












