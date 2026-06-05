import random

def oyun_durumu(oyuncu_hp, ejder_hp, iksir_sayisi):
    print(f"\n{"="*30}")
    print(f"\n Senin Canın: {oyuncu_hp} Ejderhanın Canı:{ejder_hp} İksir Sayın: {iksir_sayisi} ")
    print(f"\n{"="*30}")

def oyuncu_saldirisi (ejder_hp): # 1 
    ejdere_hasar = random.randint(15,30)
    ejder_hp -= ejdere_hasar

    oyuncu_saldırısı = random.choice([
        f"Ejderhaya kılıç darbesi indirdin ve {ejdere_hasar} hasar verdin.",
        f"Ejderhaya ok attın ve {ejdere_hasar} hasar verdin."
    ])
    print(f"\n {oyuncu_saldırısı}")
    return max(0, ejder_hp)

def oyuncu_iksir(oyuncu_hp, iksir_sayisi): # 2
    if iksir_sayisi>0:
        oyuncu_hp+= 40
        iksir_sayisi-= 1 
        if oyuncu_hp>100:
            oyuncu_hp=100
        print("İksir Kullandın Canın (40) miktarda arttı")
    else :
         print("iksirin kalmamış zort")
    return oyuncu_hp, iksir_sayisi

def oyuncu_kacis(): # 3
    şans = random.choice([True,False])
    if şans:
        print("Kaçmayı Başardın Rezil Herif")
        return True
    else:
        print("Ejderha yolunu kesti savaşmak istiyor")
        return False

def ejderha_saldirisi(oyuncu_hp):
    ejderin_hasar = random.randint(10,25)
    oyuncu_hp -= ejderin_hasar
    secilen_saldırı = random.choice([
        f"Ejderha Sana pençe darbesi vurdu ve {ejderin_hasar} hasar verdi.",
        f"Ejderha Sana nefesi ile ateş üfledi ve {ejderin_hasar} hasar verdi."
    ])
    print(f"\n {secilen_saldırı}")
    return max(0, oyuncu_hp)

#Değişkenler
oyuncu_hp = 100
ejder_hp = 100
iksir_sayisi = 2
print("\n ------\n Ejderhanın Karşısındasın Al Gardını\n ------ ")

while oyuncu_hp>0 and ejder_hp>0:
    oyun_durumu(oyuncu_hp, ejder_hp, iksir_sayisi)
    hamle = input("\n Ne Yapmak İstersin? \n 1- Saldır \n 2- İksir Kullan \n 3- Kaç \n Seçimin: ")
    print(f"\n{"="*30}")

    if hamle == ("1"):
        ejder_hp = oyuncu_saldirisi(ejder_hp)

    elif hamle == ("2"):
        oyuncu_hp, iksir_sayisi = oyuncu_iksir(oyuncu_hp, iksir_sayisi)

    elif hamle ==("3"):
        if oyuncu_kacis():
            break
    else :
        print("Heycandan donun kaldın") 
    
    if ejder_hp>0: 
        oyuncu_hp = ejderha_saldirisi(oyuncu_hp)
    
#bitiriş konuşması 

print("Oyun Bitti")
if oyuncu_hp<=0:
    print("\n Ejderha Seni yendi Kaybettin")
if ejder_hp <=0:
    print("Tebrikler Ejderhayı yendin Kazandın")               
