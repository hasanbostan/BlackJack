import random


def blackjack():

    def kart_cek(deste_sayılar, deste_semboller,kart, oyuncunun_kartları, dagıtıcının_kartları):
        cekilen_sayı=deste_sayılar[random.randint(0,12)]
        cekilen_sembol=deste_semboller[random.randint(0,3)]
        kart.extend([cekilen_sembol+" "+cekilen_sayı])
        while kart[0] in oyuncunun_kartları or kart[0] in dagıtıcının_kartları:
            kart.clear()
            cekilen_sayı=deste_sayılar[random.randint(0,12)]
            cekilen_sembol=deste_semboller[random.randint(0,3)]
            kart.extend([cekilen_sembol+" "+cekilen_sayı])
        oyuncunun_kartları.extend(kart)
        kart.clear()
        return oyuncunun_kartları


    def toplam_bul(oyuncunun_kartları,değer,toplam,eksilt=0):
        for i in oyuncunun_kartları:
            for x in değer:
                if x in i:
                    toplam+=değer[x]
        toplam-=eksilt
        return toplam

    def yazdır(oyuncunun_kartları):
        for i in oyuncunun_kartları:
            print(i,", ",end="")

    cevap="e"
    while cevap=="e":
        deste_sayılar=["As","İkili","Üçlü","Dörtlü","Beşli","Altılı","Yedili","Sekizli","Dokuzlu","Onlu","Vale","Kız","Papaz"]
        deste_semboller=["Kupa","Karo","Maça","Sinek"]
        değer={"As":11,"İkili":2,"Üçlü":3,"Dörtlü":4,"Beşli":5,"Altılı":6,"Yedili":7,"Sekizli":8,"Dokuzlu":9,"Onlu":10,"Vale":10,"Kız":10,"Papaz":10}
        kart=[]
        oyuncunun_kartları=[]
        dagıtıcının_kartları=[]
        toplam=0
        a=0
        for i in range(2):  #İlk kart çekimi!
            kart_cek(deste_sayılar,deste_semboller,kart,oyuncunun_kartları,dagıtıcının_kartları)
            kart_cek(deste_sayılar,deste_semboller,kart,dagıtıcının_kartları,oyuncunun_kartları)

        print("Dağıtıcının açık kağıdı:",dagıtıcının_kartları[0])
        print("Oyuncunun kağıtları: ",end="")
        yazdır(oyuncunun_kartları)
        if toplam_bul(oyuncunun_kartları,değer,toplam)!=21:
            for i in oyuncunun_kartları:
                if "As" in i:
                    print("Toplamı:",toplam_bul(oyuncunun_kartları,değer,toplam),"Ya da",toplam_bul(oyuncunun_kartları,değer,toplam)-10)
                    break
                else:
                    print("Toplamı:",toplam_bul(oyuncunun_kartları,değer,toplam))
                    break

        else:
            print("BLACKJACK!")
            print("Oyuncu Blackjack yaptı. Sıra dağıtıcıda")

            print("Dağıtıcının kağıtları: ",end="")
            yazdır(dagıtıcının_kartları)
            if toplam_bul(dagıtıcının_kartları,değer,toplam)!=21:
                print("Toplamı:",toplam_bul(dagıtıcının_kartları,değer,toplam))
                print("Oyuncu kazandı!")
            else:
                print("BLACKJACK!")
                print("Dağıtıcı Blackjack yaptı.")
                print("Berabere!")
            break

        karar=input("(K)art mi? (P)as mi?")
        karar=karar.lower()
        while karar=="k":
            while not karar in "kp":
                karar=input("Hatalı giriş yaptınız. Tekrar oynamak ister misiniz?(K/P)")
            kart_cek(deste_sayılar,deste_semboller,kart,oyuncunun_kartları,dagıtıcının_kartları)
            toplam_puan=toplam_bul(oyuncunun_kartları,değer,toplam)
            if toplam_bul(oyuncunun_kartları,değer,toplam)>21:
                for i in oyuncunun_kartları:
                    if "As" in i:
                        a+=1
                if a>0:
                    while toplam_puan>21 and a>0:
                            a=a-1
                            toplam_puan-=10
                    print("Oyuncunun Kartları: ",end="")
                    yazdır(oyuncunun_kartları)
                    print("Toplamı:",toplam_puan)
                    while toplam_puan<21:
                        karar=input("(K)art mi? (P)as mi?")
                        if karar=="p":
                            break
                        kart_cek(deste_sayılar,deste_semboller,kart,oyuncunun_kartları,dagıtıcının_kartları)
                        toplam_puan=toplam_bul(oyuncunun_kartları,değer,toplam)
                        if toplam_bul(oyuncunun_kartları,değer,toplam)>21:
                            for i in oyuncunun_kartları:
                                if "As" in i:
                                    a+=1
                            if a>0:
                                while toplam_puan>21 and a>0:
                                    a=a-1
                                    toplam_puan-=10
                            print("Oyuncunun Kartları: ",end="")
                            yazdır(oyuncunun_kartları)
                            print("Toplamı:",toplam_puan)


                    if toplam_puan==21:
                        print("Sıra dağıtıcıda.")
                        print("Dağıtıcının kartları: ",end="")
                        yazdır(dagıtıcının_kartları)
                        print("Toplamı:",toplam_bul(dagıtıcının_kartları,değer,toplam))
                        toplam_puan_d=toplam_bul(dagıtıcının_kartları,değer,toplam)
                        while toplam_puan_d<=16:
                            kart_cek(deste_sayılar,deste_semboller,kart,dagıtıcının_kartları,oyuncunun_kartları)
                            toplam_puan_d=toplam_bul(dagıtıcının_kartları,değer,toplam)
                            if toplam_bul(dagıtıcının_kartları,değer,toplam)>21:
                                for i in dagıtıcının_kartları:
                                    if "As" in i:
                                        a+=1
                        else:
                            if toplam_puan>toplam_puan_d:
                                print("Oyuncu Kazandı!")
                            elif toplam_puan==toplam_puan_d:
                                print("Berabere!")
                            else:
                                print("Dağıtıcı Kazandı!")


                    elif toplam_puan>21:
                        print("Oyuncunun Kartlari: ",end="")
                        yazdır(oyuncunun_kartları)
                        print("Toplamı:",toplam_puan)
                        print("Oyuncu battı!")

                    elif toplam_puan<21:
                        print("Sıra dağıtıcıda.")
                        print("Dağıtıcının kartlari: ",end="")
                        yazdır(dagıtıcının_kartları)
                        print("Toplamı:",toplam_bul(dagıtıcının_kartları,değer,toplam))
                        toplam_puan_d=toplam_bul(dagıtıcının_kartları,değer,toplam)
                        while toplam_puan_d<=16:
                            kart_cek(deste_sayılar,deste_semboller,kart,dagıtıcının_kartları,oyuncunun_kartları)
                            toplam_puan_d=toplam_bul(dagıtıcının_kartları,değer,toplam)
                            if toplam_bul(dagıtıcının_kartları,değer,toplam)>21:
                                for i in dagıtıcının_kartları:
                                    if "As" in i:
                                        a+=1







                            if a>0:
                                while toplam_puan_d>21 and a>0:
                                    a=a-1
                                    toplam_puan_d-=10
                            print("Dağıtıcının kağıtları: ",end="")
                            yazdır(dagıtıcının_kartları)
                            print("Toplamı:",toplam_puan_d)
                else:
                    print("Oyuncunun Kartları: ",end="")
                    yazdır(oyuncunun_kartları)
                    print("Toplamı:",toplam_puan)
                    print("Oyuncu battı!")
                    break

                break

            elif toplam_bul(oyuncunun_kartları,değer,toplam)==21:
                print("Oyuncunun Kartları: ",end="")
                yazdır(oyuncunun_kartları)
                print("Toplamı:",toplam_puan)
                print("Sıra dağıtıcıda.")
                print("Dağıtıcının kartları:",end="")
                yazdır(dagıtıcının_kartları)
                toplam_puan_d=toplam_bul(dagıtıcının_kartları,değer,toplam)
                while toplam_puan_d<=16:
                    kart_cek(deste_sayılar,deste_semboller,kart,dagıtıcının_kartları,oyuncunun_kartları)
                    toplam_puan_d=toplam_bul(dagıtıcının_kartları,değer,toplam)
                    if toplam_bul(dagıtıcının_kartları,değer,toplam)>21:
                        for i in dagıtıcının_kartları:
                            if "As" in i:
                                a+=1
                    if a>0:
                        while toplam_puan_d>21 and a>0:
                            a=a-1
                            toplam_puan_d-=10
                    print("Dağıtıcının kağıtları: ",end="")
                    yazdır(dagıtıcının_kartları)
                    print("Toplamı:",toplam_puan_d)

                    if toplam_puan>toplam_puan_d:
                        print("Oyuncu Kazandı!")
                    elif toplam_puan==toplam_puan_d:
                        print("Berabere!")
                    else:
                        print("Dağıtıcı Kazandı!")



            else:
                print("Oyuncunun Kartları: ",end="")
                yazdır(oyuncunun_kartları)
                print("Toplamı:",toplam_puan)
                karar=input("(K)art mi? (P)as mi?")
                karar=karar.lower()


        else:
            toplam_puan=toplam_bul(oyuncunun_kartları,değer,toplam)
            print("Oyuncunun puanı:",toplam_puan)
            print("Sıra dağıtıcıda")
            print("Dağıtıcının kartları: ",end="")
            yazdır(dagıtıcının_kartları)
            print("Toplamı:",toplam_bul(dagıtıcının_kartları,değer,toplam))
            toplam_puan_d=toplam_bul(dagıtıcının_kartları,değer,toplam)
            while toplam_puan_d<=16:
                    kart_cek(deste_sayılar,deste_semboller,kart,dagıtıcının_kartları,oyuncunun_kartları)
                    toplam_puan_d=toplam_bul(dagıtıcının_kartları,değer,toplam)
                    if toplam_bul(dagıtıcının_kartları,değer,toplam)>21:
                        for i in dagıtıcının_kartları:
                            if "As" in i:
                                a+=1
                    if a>0:
                        while toplam_puan_d>21 and a>0:
                            a=a-1
                            toplam_puan_d-=10
                    print("Dağıtıcının kağıtları: ",end="")
                    yazdır(dagıtıcının_kartları)
                    print("Toplamı:",toplam_puan_d)
            if toplam_puan_d>21:
                print("Dağıtıcı battı!")
            if len(dagıtıcının_kartları)==2 and toplam_puan_d==21:
                print("Dağıtıcı BLACKJACK yaptı!")
            elif toplam_puan==toplam_puan_d:
                print("Berabere!")
            elif toplam_puan_d>toplam_puan and toplam_puan_d<21:
                print("dağıtıcı Kazandı!")
            elif toplam_puan>toplam_puan_d and toplam_puan<21:
                print("oyuncu Kazandı!")

        cevap=input("Tekrar oynamak istiyor musunuz?(e/E/h/H)")
        cevap=cevap.lower()
        while not cevap in "eh":
            cevap=input("Hatali veri girisi yaptiniz. Tekrar oynamak istiyor musunuz?(e/E/h/H)")






def fal_bakma_oyunu():

    deste_puan={}
    niyet=input("Niyetinizi tuttunuz mu?(e/E/h/H):")
    niyet=niyet.lower()
    while not(niyet=="e" or niyet=="h"):
        niyet=input("Hatali veri girisi yaptiniz. Niyetinizi tuttunuz mu?(e/E/h/H):")
        niyet=niyet.lower()
    while niyet=="e":
        sayac=puan=0
        deste_sayılar=["As","İkili","Üçlü","Dörtlü","Beşli","Altılı","Yedili","Sekizli","Dokuzlu","Onlu","Vale","Kız","Papaz"]
        deste_semboller=["Kupa","Karo","Maça","Sinek"]
        kart=[]
        yerdeki_kartlar=[]
        cıkarılan_kartlar=[]
        puan_kartları=[]
        while len(cıkarılan_kartlar)+len(puan_kartları)+len(yerdeki_kartlar)!=52:
            sayac=sayac%13
            cekilen_sayı=deste_sayılar[random.randint(0,12)]
            cekilen_sembol=deste_semboller[random.randint(0,3)]
            kart=[cekilen_sembol,cekilen_sayı]
            while kart in yerdeki_kartlar or kart in cıkarılan_kartlar or kart in puan_kartları:
                cekilen_sayı=deste_sayılar[random.randint(0,12)]
                cekilen_sembol=deste_semboller[random.randint(0,3)]
                kart=[cekilen_sembol,cekilen_sayı]
            else:
                yerdeki_kartlar.append(kart)
                print(sayac+1,".Kart:",kart[0],kart[1])
                a=input()
            if deste_sayılar.index(cekilen_sayı)==sayac:
                print(kart[0],kart[1],"Kartı eşleşti! Saymaya yeniden başlanıyor!")
                puan_kartları.append(kart)
                yerdeki_kartlar.clear()
                sayac=-1
                a=input()
            if len(yerdeki_kartlar)==13:
                print("Eşleşme olmadı! Saymaya yeniden başlanıyor!")
                cıkarılan_kartlar.extend(yerdeki_kartlar)
                yerdeki_kartlar.clear()
                a=input()
            sayac+=1
        for i in puan_kartları:
            if i[1]=="As":
                puan+=1
            elif i[1]=="İkili":
                puan+=2
            elif i[1]=="Üçlü" :
                puan+=3
            elif i[1]=="Dörtlü" :
                puan+=4
            elif i[1]=="Beşli" :
                puan+=5
            elif i[1]=="Altılı":
                puan+=6
            elif i[1]=="Yedili" :
                puan+=7
            elif i[1]=="Sekizli" :
                puan+=8
            elif i[1]=="Dokuzlu" :
                puan+=9
            elif i[1]=="Onlu" :
                puan+=10
            elif i[1]=="Vale" :
                puan+=10
            elif i[1]=="Kız" :
                puan+=10
            elif i[1]=="Papaz" :
                puan+=10
        print("Toplam Puanınız:",puan)
        print("Niyetiniz %",puan,"Oranında gerçekleşecek.")
        niyet=input("Tekar oynamak istiyor musunuz?(e/E/h/H):")
        niyet=niyet.lower()
        while not(niyet=="e" or niyet=="h"):
            niyet=input("Hatalı giriş yaptınız. Tekrar oynamak istiyor musunuz?(e/E/h/H):")
            niyet=niyet.lower()

def menu_goruntule():
    print("         MENU      ")
    print("1. Fal Bakma Oyunu")
    print("2. Blackjack(21) Oyunu")
    print("3. Çıkış")
def sayi_al(alt_sinir,ust_sinir):
    sayi=int(input())
    while sayi<alt_sinir or sayi>ust_sinir:
        sayi=int(input("hatali veri girisi, lutfen tekrar giriniz:"))
    return sayi
def menu():
    cikis='h'
    while cikis=='H' or cikis=='h':
       menu_goruntule()
       print("Seciminizi giriniz [1-3]:",end="")
       secim=sayi_al(1,3)
       if secim==1:
           fal_bakma_oyunu()

       elif secim==2:
           blackjack()

       elif secim==3:
           cikis=input("Cikmak istediginize emin misiniz(e/E/h/H)?:")
           while cikis not in ['e', 'E', 'h', 'H']:
               cikis=input("hatali veri girisi, lutfen tekrar giriniz:")



menu()
