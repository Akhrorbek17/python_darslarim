# Funksiya va Ro'yxat
# 21-dars


# def bahola (ismlar):
#     baholar = {}
#     while ismlar:
#         ism = ismlar.pop()
#         baho = input(f"Talaba {ism.title()}ning bahosini kiriting:")
#         baholar[ism]=int(baho)
#     return baholar

# talabalar = ['hasan', 'husan', 'olim', 'shamshod']
# baholar = bahola(talabalar[:])
# print(baholar)
# print(talabalar)

# def katta_harf(ism):
#     ism = ism[:]
#     for i in range(len(ism)):
#         ism[i]=ism[i].title()
#     return ism
        
# ismlar = ['ali','vali','hasan','husan']
# katta_harf(ismlar)
# yangi_ismlar=katta_harf(ismlar[:])
# print(ismlar)
# print(yangi_ismlar)


def bahola (ismlar):
    baholar = {}
    for ism in ismlar:
        baho = input(f"Talaba {ism.title()}ning bahosini kiriting:")
        baholar[ism]=int(baho)
    return baholar

talabalar = ['hasan', 'husan', 'olim', 'shamshod']
baholar = bahola(talabalar)
print(baholar)
print(talabalar)
