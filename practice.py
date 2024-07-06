# AMALIYOT


# otam = {'ism':'Abrorbek', 'yil':1978, 'viloyat':'Andijon'}
# onam = {'ism':'Nilufarhon', 'yil':1981, 'viloyat':'Andijon'}
# ukam = {'ism':'Asrorbek', 'yil':2005, 'viloyat':'Andijon'}
# print(f"Otamning ismi {otam['ism']}, {otam['yil']}-yilda ,\
#   {otam['viloyat']}da tug'ilgan")
# print(f"Onamning ismi {onam['ism']}, {onam['yil']}-yilda ,\
#   {onam['viloyat']}da tug'ilgan")
# print(f"Ukamning ismi {ukam['ism']}, {ukam['yil']}-yilda ,\
#   {ukam['viloyat']}da tug'ilgan")


# sevimli_taom = {'Dadam':'osh','Onam':'manti','ukam':'grechka', 'murodil':'qozonkabob','xojiakbar':'lag\'mon'}
# print(f"Ukamning sevimli taomi {sevimli_taom['ukam']}")
# print(f"Murodilning sevimli taomi {sevimli_taom['murodil']}")
# print(f"Xojiakbarning sevimli taomi {sevimli_taom['xojiakbar']}")


python_izohli_lugati ={
    'integer':'Butun son',
    'float':"O'nlik son",
    'string':'matn',
    'list':'Ro\'yxat',
    'tuple':"o'zgarmas ro'yxat"}

kalit = input("Kalit so'z kiriting:").lower()
print(python_izohli_lugati.get(kalit,"Bunday so'z mavjud emas"))

kalit = input("Kalit so'z kiriting: ").lower()
tarjima=python_izohli_lugati.get(kalit)
if tarjima == None:
    print("Bunday so'z mavjud emas")
else:
    print(f"{kalit.title()} so'zi {tarjima} deb tarjima qilinadi")    
    
    
    
    
    
    
    
    
    
    
    