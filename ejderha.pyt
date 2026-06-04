import random

#Değişkenler
oyuncu_hp = 100
ejder_hp = 100
iksir_sayisi = 2
print("\n ------\n Ejderhanın Karşısındasın Al Gardını\n ------ ")

while oyuncu_hp>0 and ejder_hp>0:
    print(f"\n Senin Canın: {oyuncu_hp} Ejderhanın Canı:{ejder_hp} İksir Sayın: {iksir_sayisi} ")
    hamle= input("\n Saldırmak İçin= 1 \\ İksir İçmek İçin= 2 \\ Kaçmak İçin= 3 Tuşuna Basın ")


    if hamle == ("1"):
        ejdere_hasar = random.randint(15,30)
        ejder_hp -= ejdere_hasar
        print(f"\n Ejdere Bir Kılıç Darbesi İndirdin Ona {ejdere_hasar} Hasar verdin.")
    elif hamle == ("2"):
        if iksir_sayisi>0:
            oyuncu_hp+= 40
            iksir_sayisi-= 1 
            if oyuncu_hp>100:
                oyuncu_hp=100
                print("İksir Kullandın Canın (40) miktarda arttı")
        else :
             print("iksirin kalmamış zort")

    elif hamle ==("3"):
        şans = random.choice([True,False])
        if şans:
            print("Kaçmayı Başardın Rezil Herif")
            break
        else:
            print("Ejderha yolunu kesti savaşmak istiyor")
    
    else :
        print("Heycandan donun kaldın")
    
    if ejder_hp>0 and hamle!= "3":
        ejderin_hasar = random.randint(10,25)
        oyuncu_hp -= ejderin_hasar

    secilen_saldırı = random.choice([

        f"Ejderha Sana pençe darbesi vurdu ve {ejderin_hasar} hasar verdi.",
        f"Ejderha Sana nefesi ile ateş üfledi ve {ejderin_hasar} hasar verdi."
    ])
    print(f"\n {secilen_saldırı}")

    



#bitiriş konuşması 

print("Oyun Bitti")
if oyuncu_hp<=0:
    print("\n Ejderha Seni yendi Kaybettin")
if ejder_hp <=0:
    print("Tebrikler Ejderhayı yendin Kazandın")               
