# 19-dars
# Function 


# print("Assalomu alaykum !")

# def salom_ber():
#     """ Salom beruvchi funksiya """
#     print("Assalomu alaykum!")

# salom_ber()


# def salom_ber (ism):
#     """ Foydalanuvchi ismini qabul qilib,
#     unga salom beruvchi funksiya"""
#     print(f"Assalomu alaykum, hurmatli {ism.title()}!")

# salom_ber('hasan')
# salom_ber("g'ulom")


# def toliq_ism(ism, familiya):
#     """Foydalanuvchi ism va familiyasini jamlab chiqaruvchi funksiya"""
#     print(f"Foydalanuvchi ismi:{ism.title()}\n"
#           f"Foydalanuvchi familiyasi: {familiya.title()}")
    
# toliq_ism('olim', 'hakimov')    
    
    
# def yosh_hisobla(ism, tugilgan_yil):
#     """ Foydalanuvchi yoshini hisoblaydigan dastur"""
#     print(f"{ism.title()} {2024-tugilgan_yil} yoshda")    
    
# # yosh_hisobla('olim', 1995)
# yosh_hisobla(ism='olim', tugilgan_yil=1995)
    
    
# def yosh_hisobla(tugilgan_yil,joriy_yil=2020):
#     """Foydalanuvchi tug'ilgan yilidan uning yoshini hisoblaydi"""
#     print(f"Siz {joriy_yil-tugilgan_yil} yoshdasiz")    
    
# yosh_hisobla(1995,2020)    
    

# def ism_tugilgan_yil (ism , yosh, joriy_yil=2024):
#     """Foydalanuvchi ismi va tugilgan yilini hisoblaydigan dastur"""
#     print(f"{ism.title()}ning tugilgan yili {joriy_yil- yosh}")
    
# ism_tugilgan_yil('hasan',23)    
    
    
# def kub_kv_xisoblash (son):    
#     """Foydalanuvchidan son olib kub va kvadratini xisoblash"""
#     print(f"kvadratni xisoblaymiz: {son**2}\n"
#           f"kubini xisoblaymiz:{son**3}")
    
# kub_kv_xisoblash(2)    

# def juft_toq_son (son):   
#     """Foydalanuvchidan son olib toq va juft sonni chiqaruvchi dastur"""
#     if son%2:
#         print(f"{son} toq son")
#     else:
#         print(f"{son} juft son")
    
# juft_toq_son(8) 
# juft_toq_son(37)   
    
# def katta_son (son1, son2):   
#     """Foydalanuvchi kiritgan sonlarni katta kichikligini xisoblaydigan dastur:"""
#     if son1>son2:
#        print(f"{son1} katta son")
#     elif son2>son1:
#        print(f"{son2} katta son")
#     else:
#        print("Sonlar teng")

# katta_son(233, 23)    
  

# def daraja (x,y=2):
#     print(f"{x} ning {y} darajasi {x**y} ga teng")

# daraja(5,2)
# daraja(3,5)
# daraja(6)

def qoldiqsiz (son):
    """Foydalanuvchi kiritgan sonni 2 va 10 oraligi sonlarga qoldiqsiz bolinishi ni tekshiruvchi dastur"""
    for n in range(2,11):
     if not son%n:
       print(f"{son} {n} ga qoldiqsiz bo'linadi")


qoldiqsiz(25)









  
    