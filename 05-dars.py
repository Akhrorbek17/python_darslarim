# 05 dars Lists (Ro'yxatlar)




# mevalar = ['olma', 'anjir', 'shaftoli', "o'rik"]
# narhlar = [12000 , 18000, 10900, 22000, 25000, 36000, -25, 63.7]
# sonlar = ['bir', 'ikki', 3, 4, 5]
# ismlar = []


# .append()

# mevalar =['olma', 'anjir', 'shaftoli', "o'rik"]
# mevalar.append("tarvuz") # mevalarga tarvuz qo'shamiz
# print(mevalar)



# .insert(index, object)

# cars = ['Lacetti', "Nexia 3", "Cobalt"]
# cars.insert(0, 'Malibu 2')
# print(cars)
# cars.insert(2, 'Damas')
# print(cars)


# del list[]

# cars = ['Lacetti',"Damas", "Malibu", "Onix" ]
# del cars[1]
# print(cars)

# .remove()

# hayvonlar = ['it', 'mushuk', 'sigir', "qo'y", 'quyon', 'mushuk']
# hayvonlar.remove('mushuk')
# print(hayvonlar)

# .pop()

# bozorlik = ["yog", 'un', 'piyoz', 'banan', 'go\'sht']
# mahsulot = bozorlik.pop(2)
# print("Men " + mahsulot + "sotib oldim")
# print("Olinmagan mahsulotlar:" , bozorlik)

# Topshiriq

# ismlar = ['Abdulaziz', 'Ammoriddin', 'Xojiakbar']
# print("Salom " + ismlar[0] + ", bugun choyxona bormi ?")
# print( ismlar[1] , ", choyxonaga boramizmi ? ")
# print("Bugun nimaga " + ismlar[2] + " choyxonaga kemadiz ?")

# sonlar = [21000, 3200, -34, 45.5, 12000, 65, -34]
# numbers = sonlar.pop(3)
# sonlar.append(34)
# del sonlar[3]
# print(sonlar)

# t_shaxslar = ['Alisher Navoiy', 'Mirzo Ulugbek', 'Al- Xorazmiy', 'Mirzo Ulugbek']
# z_shaxslar = ['Abdulla Oripov', 'Xudoyberdi To\'xtaboev', "Temur Malik", 'Abdulla Qodiriy']
# t_shaxslar1 = t_shaxslar.pop(0)
# z_shaxslar1 = z_shaxslar.pop(2)
# print('Men tarixiy shaxslardan ' + t_shaxslar1 + " bilan,\nzamonaviy shaxslardan esa " + z_shaxslar1 + " bilan suhbat qilisni istar edim") 

# friends = []
# friends.append("Xojiakbar")
# friends.append("Abdulaziz")
# friends.append("Maqsud")
# friends.append("Ammoriddin")
# friends.append("Muhammad yusuf")
# friends.append("Asilbek")
# # print(friends)
# friends.remove("Maqsud")
# friends.remove("Xojiakbar")
# friends.remove("Asilbek")
# # print(friends)
# friends.insert(0, "Sarvar")
# friends.insert(2, 'Eldor')
# friends.insert(3, "Qori" )
# print(friends)

# mehmonlar = []
# mehmonlar.append(friends.pop(1))
# mehmonlar.append(friends.pop(4))
# mehmonlar.append(friends.pop(2))
# print("Kelgan mehmonlar :" , mehmonlar)



        


