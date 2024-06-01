# 09-dars
# if-elif=else

# son = 50
# if son>0:
#     print("Musbat son")
# else:
#     print("Manfiy son")    
    

# yosh = int(input("Yoshingiz nechida ? >>>"))    
# if yosh <=4:
#     narh = 0    
# elif yosh <=12:  
#     narh = 5000
# elif yosh <=18:
#     narh = 8000    
# else:
#     narh = 10000    
   
# print(f"Sizga kirish {narh} so'm")
    
    
# kun = input("Bugun nima kun ?>>>")    
# if kun.lower() == "shanba" or kun.lower() == 'yakshanba':
#     print("Bugun dam olish kuni.")    
# else:
#     print("Bugun ish kuni.")    
    
# kun = input("Bugun nima kun ?")    
# harorat = float(input("Havo hororati qanday ?"))    
    
# if kun.lower() == 'yakshanba' and harorat>=30:
#     print("Cho'milgani ketdik!")    
# elif kun.lower()== 'yakshanba' and harorat<30: 
#     print("Uyda dam olamiz!")
    
    
# kun = input("Bugun nima kun ?")    
# harorat = float(input("Havo hororati qanday ?"))    
    
# if (kun.lower() == 'yakshanba' or kun.lower()== 'shanba') and harorat>=30:
#     print("Cho'milgani ketdik!")    
# elif (kun.lower() == 'yakshanba' or kun.lower()== 'shanba') and harorat>=30:
#     print("Uyda dam olamiz!")    
    
# narh = 15000
# choy = True
# salat = False

# if choy and salat:
#     narh= narh + 10000
# elif choy or salat:
#     narh = narh + 5000

# print(f"Jami {narh} so'm")    
    
    
# narh = 15000
# choy = True
# salat = False
# non = True
# kompot = True
# assorti =False

# if choy:
#     print("Mijoz choy oldi.")
#     narh = narh + 3000
# if salat:
#     print("Mijoz salat oldi. ")
#     narh = narh + 6000
# if non:
#     print("Mijoz non oldi.")    
#     narh = narh + 3000
# if kompot:
#     print("Mijoz kompot oldi.")    
#     narh = narh + 5000
# if assorti:
#     print("Mijoz assorti oldi.")    
#     narh = narh + 15000
    
# print(f"Jami {narh} so'm boldi.")    


# menu = ['osh', 'qozonkabob', 'shashlik', 'norin', 'somsa']
# 'manti' in menu


# menu = ['osh', 'qozonkabob', 'shashlik', 'norin', 'somsa']
# ovqat = input('Nima ovqat yeysiz?>>>')
# if ovqat.lower()in menu:
#     print('Buyurtma qabul qilindi.')
# else:
#     print("Afsuski bizda bunday ovqat yo'q")

# menu = ['osh', 'qozonkabob', 'shashlik', 'norin', 'somsa']
# ovqat = input('Nima ovqat yeysiz?>>>')
# if ovqat.lower() not in menu:
#     print("Afsuski bizda bunday ovqat yo'q")
# else:
#     print('Buyurtma qabul qilindi.')

# menu = ['osh', 'qazonkabob', 'shashlik', 'norin', 'somsa'] 
# buyurtmalar = ["osh", 'somsa', 'manti', 'shashlik']

# for taom in buyurtmalar:
#     if taom in menu:
#         print(f"Menuda {taom} bor")
#     else:
#         print(f"Kechirasiz, menuda {taom} yo'q")

#Consoleda yoziladi
# if buyurtmalar:
#     print(f"ro'yxatda {len(buyurtmalar)} ta taom bor")
# else:
#     print(f"Kechirasiz, menuda (taom) yo'q")

menu = ['osh', 'qazonkabob', 'shashlik', 'norin', 'somsa'] 
buyurtmalar = ["osh", 'somsa', 'manti', 'shashlik']

if buyurtmalar:
    for taom in buyurtmalar:
        if taom in menu:
            print(f"Menuda {taom} bor")
        else:
            print(f"Kechirasiz, menuda {taom} yo'q")
else:
    print("Savatchangiz bo'sh!")










   
    
    
    
    