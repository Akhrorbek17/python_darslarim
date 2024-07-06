# 18-dars
# Ro'yxatlar bilan ishlash



# print("Yaqin do'stlaringizni ro'yxatini tuzamiz.")
# ismlar = []
# n=1
# while True:
#     savol = f"{n}-do'stngiz ismini kiriting: "
#     ism  = input(savol)
#     ismlar.append(ism)
#     takrorlash = input("Yana ism qo'shasizmi ?)(ha/yo'q) ")
#     n+=1
#     if takrorlash != 'ha':                
#         break

# print("Do'stlaringiz ro'yxati:")
# for ism in ismlar:
#     print(ism.title())


# print("Do'stlaringizni yoshini saqlaymiz:")
# dostlar = {}
# ishora =True
# while ishora:
#     ism = input("Do'stingizni ismini kiriting: ")
#     yosh = input(f"{ism.title()}ning yoshini kiriting: ")
#     dostlar[ism]=int(yosh)

#     javob = input("Yana ma'lumot qo'shasizmi? (ha/yo'q)")
#     if javob == 'yo\'q':
#         ishora = False
        
# for ism,yosh in dostlar.items():
#     print(f"{ism.title()} {yosh} yoshida")  


# cars = ['lacetti','nexia','toyota','nexia','audi','malubi','nexia']
# while 'nexia' in cars:
#     cars.remove('nexia')
# print(cars)

# talabalar = ['hasan','hasan','olim','botir']
# baholangan_talabalar ={}
# while talabalar:
#     talaba = talabalar.pop()
#     baho =input(f"{talaba.title()}ning bahosini kiriting:")
#     print(f"{talaba.title()} baholandi" )
#     baholangan_talabalar[talaba]=int(baho)
    
# print(baholangan_talabalar)

# print("Buyurtma qabul qiluvchi dastur:")
# mahsulotlar = []
# n=1
# while True:
#     savol = f"{n}-chi mahsulot: "
#     mahsulot1 = input(savol)
#     mahsulotlar.append(mahsulot1)
#     buyurtma =input("Yana mahsulot buyurtma qilasizmi?(ha/yo'q)")
#     n+=1
#     if buyurtma  != 'ha':
#         break
# print("Buyurtmalar ro'yxati:")      
# for mahsulot1 in mahsulotlar:
#     print(mahsulot1)

# print("E-bozor uchun dastur")
# mahsulotlar = {}
# ishora = True
# while ishora:
#     nomi = input("Mahsulotni nomini yozing: ")
#     narh= input(f"{nomi.title()}ning narhi nech pul ?")
#     mahsulotlar[nomi] = float(narh)
#     javob = input("Yana mahsulot qo'shish:(ha/yo'q)")
#     if javob == 'yo\'q':
#         ishora = False
        
# for nomi,narh in mahsulotlar.items():
#     print(f"{nomi.title()} {narh} so'm")

buyurtmalar = ['olma','non','shashlik', 'shakar']
mahsulotlar = {'olma':10000,
               'uzum':3000,
               'shashlik':15000,
               'tarvuz': 12000}


while buyurtmalar :
    buyurtma = buyurtmalar.pop()
    if buyurtma in mahsulotlar.keys():
        narh = mahsulotlar[buyurtma]
        print(f"{buyurtma.title()}-{narh} so'm")
    else:
        print(f"Bizda {buyurtma} yo'q")











