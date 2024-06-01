# 07-dars "for" bilan tanishuv


# mehmonlar = [ "Ali", 'Vali', 'Hasan', 'Husan', 'Olim']
# for mehmon in mehmonlar:
#     print("Salom ", mehmon)

# mehmonlar = ["Ali", 'Vali', 'Hasan', 'Husan', 'Olim']
# for mehmon in mehmonlar:
#     print(
# f"Hurmatli {mehmon}, sizni 20 Dekabr kuni nahorgi oshga taklif qilamiz")
#     print("Hurmat bilan , Palonchievlar oilasi\n")

# sonlar = list(range(1,11))
# for son in sonlar:
#     print(f"{son} ning kubi {son**3} ga teng")

# sonlar = list(range(11))# 1 dan 10 gacha sonlar ro'yxati
# sonlar_kvadrati=[] # bo'sh ro'yxat yaratamiz
# for son in sonlar: # sonlardagi har bir son uchun
#     sonlar_kvadrati.append(son**2) # uning kvadratini xisoblab sonlar_kvadratiga qoshadi

# print(sonlar)
# print(sonlar_kvadrati)

# dostlar = [] # bo'sh ro'yxat
# print("5 ta eng yaqin do'stingiz kim ?")
# for  n in range(5):# n bu yerda 0 dan 4 gacha qiymatlar oladi
#     dostlar.append(input(f"{n+1}- do'stingizning ismini kiriting:"))
# print(dostlar)

# ismlar = ['Xojiakbar', 'Ammoriddin', 'Sardorbek', 'Abdulaziz', 'Ismoiljon']
# for ism in ismlar:
#     print(f"Qalesan ishlar joyidami {ism} , kecha nimaga kontrga chiqmading\n")


# ismlar = ['Xojiakbar', 'Ammoriddin', 'Sardorbek', 'Abdulaziz', 'Ismoiljon']
# for ism in ismlar:
#     print("Salom ", ism)
    
    
# print(f"Kod {len(ismlar)} marta takrorlandi")


# toq_sonlar = list(range(11,100,2))
# for toq_son in toq_sonlar:
#     print(toq_son**3)

# kinolar = []
# print("Sevimli kinoyingiz qaysi ?")
# for kino in range(5):
#     kinolar.append(input(f"{kino+1} - eng sevimli kinoyingizni kiriting:\n"))
# print(kinolar)



n_people = int(input("Bugun necha kishi bn suhbat qildingiz?>>>"))
ismlar = []
for n in range(n_people):
    ismlar.append(input(f"{n+1}-suhbat qilgan odamingiz kim edi: "))
print(ismlar)






