# 14-Lugat bilan tanishish
 


# car_0 ={'model':'ferrari', 'rang':'qizil'}
# print(car_0['model'])
# print(car_0['rang'])

# en_uz = {'apple':'olma','apricot':"o'rik",'banana':"banan"}

# mevalar= {'olma':10000,'tarvuz':8000,'qovun':10000}
# print(f"Olma narhi {mevalar['olma']} so'm")

#  

# talaba_1 = {}
# talaba_1['ism'] = 'qobil rasulov'
# talaba_1['kurs'] = 3
# talaba_1['yosh'] = 24
# print(talaba_1)

# talaba_1['kurs'] = 4
# print(f"Talaba {talaba_1['ism'].title()} {talaba_1['kurs']}-kurs")


# talaba_0 = {'ism':'murod olimov', 'yosh':20, 't_yil':2000}
# del talaba_0['yosh']
# print(talaba_0)

telefonlar = {
    'ali':'iphone x',
    'vali':'galaxy s9',
    'olim':'mi 10 pro',
    'orif':'nokia 3310',
    'anvar':'pixel 3xl'
    }
phone = telefonlar.get('ali','Bunday ism mavjud emas')
print(phone)

phone = telefonlar.get('hasan')
print(phone)


