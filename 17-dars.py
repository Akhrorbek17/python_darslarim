# 17-dars 
# While tsikli

# #input
# ism = input("Ismingiz nima? ")
# savol = f"Salom, {ism.title()}. Yoshingiz nechida ?" 
# yosh = input(savol)
# yosh= int(yosh)
# height = input("Bo'yingiz necha metr ?")
# height = float(height)


# while
# son = 1
# while son<=5:
#     print(son , end=' ')
#     son+=1
# print(" Dastur tugadi !")    

# while input

# print("Kiritilgan sonni kvadratini qaytaruvchi dastur.")
# savol = "Istalgan sonni kiriting:"
# savol +="(dasturni to'xtatish uchun 'exit' deb yozing):"
# qiymat = ' '
# while qiymat !='exit':
#     qiymat= input(savol)
#     if qiymat != 'exit':
#         print(float(qiymat)**2)
# print("Dastur tugadi !")

#ishora
# print("Kiritilgan sonning kvadratini qaytaruvchi dastur.")
# savol = "Istalgan son kiriting"
# savol += "(dasturni to'xtatish uchun 'exit deb yozing'): "
# ishora = True
# while ishora:
#     qiymat = input(savol)
#     if qiymat == 'exit':
#         ishora = False
#     else:
#         print(float(qiymat)**2)
# print("Dastur tugadi !")


# break
# print("Kiritilgan sonning kvadratini qaytaruvchi dastur.")
# savol = "Istalgan son kiriting"
# savol += "(dasturni to'xtatish uchun 'exit deb yozing'): "

# while True:
#     qiymat = input(savol)
#     if qiymat == 'exit':
#         break
#     else:
#         print(float(qiymat)**2)
# print('Dastur tugadi')

# sonlar = list(range(1,11))
# for son in sonlar:
#     if son == 5:
#         break
#     print(f"{son} ning kubi {son**3} ga teng")

# sonlar = list(range(1,11))
# for son in sonlar:
#     if son == 5:
#         continue
#     print(f"{son} ning kvadrati {son**2} ga teng")


#  # Continue while
# son = 0
# while son<10:
#     son+=1
#     if son%2 != 0:
#         continue
#     else:
#        print(son) 

# Infinity Loop
# son = 0
# while son<10:
#     #son +=1
#     if son%2 !=0:
#         continue
#     else:
#         print(son)
    
# son= 1
# while son>0:
#     son+=1
#     if son%2 !=0:
#         continue
#     else:
#         print(son)

# savol = input("Foydali kitoblarni kiriting:")
# savol += "(barcha kitoblarni kiritib 'stop' so'zini yozing: )"

# while True:
#     kitob = input(savol)
#     if kitob != 'stop':
#       break
# print("Thanks !")


# savol = "Nechcha yoshdasiz ?:"


# while True:
#     qiymat = input(savol)
#     if qiymat =='exit' or qiymat == 'quit':
#         break
#     yosh = int(qiymat)
    
#     if yosh <7:
#         narh = 2000
#     elif 7<=yosh <18:
#         narh = 3000
#     elif 18<=yosh<65:
#         narh = 10000
#     else: narh = 0
    
#     if narh == 0:
#         print("Sizga chipta bepul")
#     else:    
#         print(f"Chipta {narh} so'm")

# savol ="Kiritilgan sonning ildizini qaytaruvchi dastur.\n"
# savol += "Musbat son kiriting "
# savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "

# while True:
#     qiymat = input(savol)
#     if qiymat == 'exit':
#        break
#     elif float(qiymat)<0:
#        continue
#     else:
#         ildiz = float(qiymat)**(0.5)
#         print(f"{qiymat} ning ildizi {ildiz} ga teng")









