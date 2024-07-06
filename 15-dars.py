# 15-dars.py


#Dasturlash asoslari

# .items()

# talaba_0 = {
#     'ism':'alijon',       
#     'familya':'shamshiyev',
#     'yosh':22, 
#     'faklutet':'matematika',
#     'kurs':4 , 
#     }

# print(talaba_0.items())


# for key , value in talaba_0.items():
#     print(f"Kalit: {key}")
#     print(f"Qiymat: {value} \n")



# telefonlar = {
#     'ali':'iphone x',
#     'vali':'galaxy s9',
#     'olim':'mi 10 pro',
#     'orif': 'nokia 3310'
#     }

# for k, q in telefonlar.items():
#     print(f"{k.title()}ning telefoni {q}")

mahsulotlar = {
    'olma':10000,
    'anor':20000,
    'uzum':40000,
    'anjir':25000,
    'shaftoli':30000
    }

# print(mahsulotlar.keys())

# print("Do'kondagi mahsulotlar")
# for mahsulot in mahsulotlar.keys():
#     print(mahsulot.title())


# print('Do\'kondagi mahsulotlar:')
# for mahsulot in mahsulotlar:
#     print(mahsulot.title())

# bozorlik = ['anor','uzum','non','baliq']
# for mahsulot in mahsulotlar:
#     if mahsulot in bozorlik:
#         print(f"{mahsulot.title()} {mahsulotlar[mahsulot] } so'm ")
        

# for buyum in bozorlik:
#     if buyum not in mahsulotlar:
#         print(f"Iltimos, do'koningizga {buyum} ham olib keling")
    
        
        
# print(telefonlar.values())

# print("Foydalanuvchilar quyidagi telefonlarni ishlatishadi:")
# for tel in telefonlar.values():
#     print(tel)
    
# telefonlar = {
#     'ali':'iphone x',
#     'vali':'galaxy s9',
#     'olim':'mi 10 pro',
#     'orif': 'nokia 3310',
#     'hamida':'galaxy s9',
#     'tohir':'iphone x',
#     'maryam':'huawei p 30',
#     'umar':'iphone x'
#     }    
    
# # set 
# print("Foydalanuvchilar quyidagi telefonlarni ishlatishadi: ")    
# for tel in set(telefonlar.values()) :
#     print(tel)

# toys = {'ball', 'car', 'bear', 'car', 'ball'}
# print(toys)


# python_dics = {
#     'int':'butun son',
#     'float':'o\'nlik son',
#     'for':'biror amalni qayta bajarish tsikli',
#     'if':'Shartlarni tekshirish operatori',
#     'Boolean':'Mantiqiy qiymat',
#     'str':'matnli so\'z',
#     }
# for key, value in sorted(python_dics.items()):
#     print(f"{key.title()} - {value}")


davlat = {
    'AQSH':'Washington',
    'QIRGIZISTON':'Bishkek',
    'MALAYZIYA':'Kuala-Lumpur',
    'QOZOGIZTON':'Astana',
    'ROSSIYA':'Moskva',
    'SINGAPUR':'Singapur',
    'TOJIKISTON':'Dushanbe',
    'ITALIYA':'Rim'
    }
# print("Dunyo davlatlari:")
# for d in davlat:
#     print(d)

# print("Davlatlarning poytaxti:")


# country =input("Qaysi davlatning poytaxtini bilishni istaysiz ?:").lower()
# capital = davlat.get(country)
# if capital == None:
#     print("Kechirasiz, bizda bu haqida ma\'lumot yo\'q")
# else:
#     print(f"{country.upper()}ning poytaxti {capital.title()} shahri")


menu = {
        'osh':12000,
        'mastava':10000,
        'qozonkabob':15000,
        'sho\'rva':10000,
        'do\'lma':13000,
        'shashlik':6000,
        'lag\'mon':9000,
        'somsa':3000,
        'uyg\'ur lagmon':10000,
        'chuchvara' :10000
        }

print("3 ta taom buyurtma bering.")
buyurtmalar = []
for n  in range(3):
    buyurtmalar.append(input(f"{n+1}-taom:").lower())

for buyurtma in buyurtmalar:
    if buyurtma in menu:
        print(f"{buyurtma.title()} {menu[buyurtma]} so'm")
    else:
        print(f"Kechirasiz, bizda {buyurtma} yo'q")    


