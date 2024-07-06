# 16-dars
# Nesting



car0 = {
        'model':'lacetti',
        'rang':'oq',
        'yil':2018,
        'narh':13000,
        'km':50000,
        'korobka':'avtomat'
        }

car1 = {
        'model':'nexia 3',
        'rang':'qora',
        'yil':2015,
        'narh':9000,
        'km':89000,
        'korobka':'mexanika'
        }

car2 = {
        'model':'gentra',
        'rang':'qizil',
        'yil':2019,
        'narh':15000,
        'km':20000,
        'karobka':'mexanika'
        }
# car = car0
# print(f"{car['model'].title()}, "
#       f"{car['rang']} rang, "
#       f"{car['yil']}-yil, {car['narh']}$")

# car = car1
# print(f"{car['model'].title()}, "
#       f"{car['rang']} rang, "
#       f"{car['yil']}-yil, {car['narh']}$")

# car = car2
# print(f"{car['model'].title()}, "
#       f"{car['rang']} rang, "
#       f"{car['yil']}-yil, {car['narh']}$")


# cars = [car0 , car1 , car2]
# for car in cars:
#     print(f"{car['model'].title()}, "
#           f"{car['rang']} rang, "
#           f"{car['yil']}-yil, {car['narh']}$


malibus = []
for n in range(10):
    new_car = {
        'model':'malibu',
        'rang':None,
        'yil':2020,
        'narh':None,
        'km':0,
        'korobka':'avto'
        }
    malibus.append(new_car)

# for malibu in malibus:
#     print(malibu)
    
for malibu in malibus[:3]:
    malibu['rang'] = 'qizil'    

# for malibu in malibus:
#     print(malibu)

for malibu in malibus[3:6]:
    malibu['rang'] = 'qora'
    
for malibu in malibus[6:]:
    malibu['rang'] = 'kulrang'
    malibu['korobka'] = 'mexanika'


# for malibu in malibus:
#     print(malibu)


# for malibu in malibus:
#     if malibu['korobka']=='avto':
#         malibu['narh'] = 25000
#     else:
#         malibu['narh']= 20000

# for malibu in malibus:
#     print(malibu)
    
dasturchilar = {
    'ali':['python','c++'],
    'vali':['html','css','js'],
    'hasan':['php','sql'],
    'husan':['python', 'php'],
    'maryam':['c++','c#']
    }

# for ism , tillar in dasturchilar.items():
#     print(f"\n{ism.title()} quyidagi dasturlash tillarini biladi")
#     for till in tillar:
#         print(till.upper())


# for ism , tillar in dasturchilar.items():
#     print(f"\n{ism.title()} quyidagi dasturlash tillarini biladi")
#     for till in tillar:
#         print(f"{till.upper()} ", end='')


# hamkasblar = {
#     'ali':{'familya':'valiyev',
#            'tyil':1995,
#            'malumot':'oliy',
#            'tillar':['python', 'c++']
#            },
#     'vali':{'familya':'aliyev',
#             'tyil':2001,
#             'malumot':"o'rta-maxsus",
#             'tillar':['html','css', 'js']},
#     'hasan':{'familya':'husanov',
#              'tyil':1999,
#              'malumot':'maxsus',
#              'tillar':['python', 'php']}
# }


# for ism , info in hamkasblar.items():
#     print(f"\n{ism.title()} {info['familya'].title()},"
#           f"{info['tyil']} - yilda tug'gilgan."
#           f"Malumoti: {info['malumot']}. \n"
#           "Quyidagi dasturlash tillarini biladi:")
#     for til in info['tillar']:
#         print(til.upper())


# Amaliyot


# mashxur_shaxs = {
#     'Abu Abdulloh':{'familya':'Muhammad ibn Ismoil',
#                     'tyil':810,
#                     'viloyat':'Buxoro',
#                     'yashagan':60},
#     'Abdulla':{'familya':'Qodiriy',
#                'tyil':1894,
#                'viloyat':'Toshkent',
#                'yashagan':44},
#     'Erkin':{'familya':'Vohidov',
#                'tyil':1936,
#                'viloyat':'Farg\'onada',
#                'yashagan':80},
#     'Alisher':{'familya':'Navoiy',
#                'tyil':1441,
#                'viloyat':'Xirot',
#                'yashagan':60}
#     }
# for ism, info in mashxur_shaxs.items():
#     print(f"{ism.title()} {info['familya'].title()},"
#           f"{info['tyil']}-yilda {info['viloyat'].title()}da tavallud topgan."
#           f" {info['yashagan']} yil umr ko'rgan.")
    
    
# buxoriy = {'ism':'Abu Abdulloh Muhammad ibn Ismoil',
#             'tyil':810,
#             'vyil':870,
#             'tjoy':'Buxoro',
#             'asarlar':["Al-jome' as-sahih", 'Al-adab al-mufrad', "At-tarix al kabir",
#   "At-tarix as-sag'ir"]
#     }    
    
# qodiriy = {'ism':'Abdulla Qodiriy',
#             'tyil':1894,
#             'vyil':1938,
#             'tjoy':'Toshkent',
#             'asarlar':["O'tkan kunlar", 'Mehrobdan Chayon', "Obid ketmon"]
#     }       

# vohidov = {'ism':'Erkin  Vohidov',
#             'tyil':1936,
#             'vyil':2016,
#             'tjoy':'Farg\'ona',
#             'asarlar':["Tong nafasi", 'Qo\'shiqlarim sizga', "O'zbegim", "Qiziquvchan Matmusa"]
#             }       
# navoiy = {'ism':'Alisher Navoiy',
#             'tyil':1441,
#             'vyil':1501,
#             'tjoy':'Toshkent',
#             'asarlar':["Xamsa", 'Lison ut-Tayr', "Mahbub Al-Qulub"]
#         }

# shaxslar = ['buxoriy', 'qodiriy','vohidov', 'navoiy']

# for shaxs in shaxslar:
#     ism = shaxs['ism']
#     asarlar = shaxs['asarlar']
#     print(f"\n{ism} ning mashxur asarlari: ")
#     for asar in asarlar:
#         print(asar)
    
    
    
# kinolar = {
#     'ali':['Terminator','Rambo','Titanic'],
#     'vali':['Tenet','Inception','Interstellar'],
#     'hasan':['Abdullajon','Bomba','Shaytanat'],
#     'husan':['Mahallada duv-duv gap','John Wick']
#     }
# for ism, kinolar in kinolar.items():
#     print(f"\n{ism.title()}ning sevimli kinolari:")
#     for kino in kinolar:
#         print(kino)
    
    

davlatlar = {
    'O\'zbekiston':{'poytaxt':'Toshkent',
           'hududi':448978,
           'aholisi':33000000,
           "pul":'so\'m'
           },
    'Rossiya':{'poytaxt':'Moskva',
           'hududi':17098246,
           'aholisi':144000000,
           "pul":'rubl'
           },
    'AQSH':{'poytaxt':'Vashington',
           'hududi':9631418,
           'aholisi':327000000,
           "pul":'dollar'
           },
    'Malayziya':{'poytaxt':'Kuala-Lumpur',
           'hududi':329750,
           'aholisi':25000000,
           "pul":'rinngit'
           }
    }
# for davlat,info in davlatlar.items():
#     print(f"\n{davlat}ning poytaxti {info['poytaxt']}"
#           f"\nHududi: {info['hududi']} kv.km "
#           f"\nAholisi: {info['aholisi']}"
#           f"\nPul birligi: {info['pul']}")    
        
davlat = input("Dvlat nomini kiriting:").lower()    
if davlat in davlatlar:
    info = davlatlar[davlat]
    print(f"\n{davlat.capitalize()}ning poytaxti {info['poytaxt'].title()}"
          f"\nHududi: {info['hududi']} kv.km "
          f"\nAholisi: {info['aholisi']}"
          f"\nPul birligi: {info['pul']}")    
else:
    print("Bizda bu davlat xaqida malumot mavjud emas")
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    















