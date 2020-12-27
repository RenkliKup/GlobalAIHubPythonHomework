class s_s_s:
    dersKayit={}
    dersSayisi=0
    dersOrtalama=0
    dersNotlari={}
    count=3
    def __init__(self,name="",surname=""):
        self.name=name;
        self.surname=surname
    def adDegistir(self,yeniAd,yenisoyad):
        self.count-=1
        self.name=yeniAd
        self.surname=yenisoyad
    def dersNotHesapla(self):
        for x,y in self.dersKayit.items():
            if (y[0]*0.3+y[1]*0.5+y[2]*0.2)>=90:
                self.dersNotlari[x]="AA ile Geçtin"
            elif 70<=int(y[0]*0.30+y[1]*0.5+y[2]*0.2)<90:
                self.dersNotlari[x]="BB ile Geçtin"
            elif 50<=int(y[0]*0.30+y[1]*0.5+y[2]*0.2)<70:
                self.dersNotlari[x]="CC ile Geçtin"
            elif 30<=int(y[0]*0.30+y[1]*0.5+y[2]*0.2)<50:
                self.dersNotlari[x]="DD ile Geçtin"
            elif int(y[0]*0.30+y[1]*0.5+y[2]*0.2)<30:
                self.dersNotlari[x]="FF ile Kaldın"
        for x,y in self.dersNotlari.items():
            print(f"Ders Adi:{x},Ders Notu:{y}")
        
    def dersTanimla(self,dersAdi,midterm,final,project):
        self.dersSayisi+=1
        self.dersAdi=dersAdi
        self.midterm=midterm
        self.final=final
        self.project=project
        self.dersKayit[self.dersAdi]=[self.midterm,self.final,self.project]
        

    def dersKayitYazdir(self):
    
        return self.dersKayit
    def dersKayiKeys(self):
        count=1
        for x in self.dersKayit.keys():
            print(f"Ders {count}:{x}")
            count+=1

case={
1:"1-Ad Değiştir",
2:"2-Ders Kaydı",
3:"3-Ders Notu Hesapla",
4:"4-Dersleri Göster",
"Default":"Yanlış Tuş Girişi"}
 
print("Öğrenci Kaydınızı Yapın Lütfen")
name=input("Lütfen Adınızı Giriniz:")
surname=input("Lütfen soyadınızı giriniz:")
baris=s_s_s(name,surname)
print("Öğrenci Kaydınız Başarılı.")
kontrol=True
while kontrol:
    print(f"Merhaba {baris.name} {baris.surname}")
    for x in case.values():
        if x in "Yanlış Tuş Girişi":
            pass
        else:
            print(x)
    bar=int(input("please enter someone:"))
   
    if bar==1:
        if(baris.count>0):
            yeniad=input(f"{baris.count} defa adınızı ve soyadınızı değiştirebilirsiniz Yeni Ad Giriniz:")
            yeniSoyad=input(f"{baris.count} defa adınızı ve soyadınızı değiştirebilirsiniz Yeni Soyad Giriniz:")
            baris.adDegistir(yeniad,yeniSoyad)
            print(f"Adınız ve soyadınız {baris.name} {baris.surname} olarak değiştirildi")
        else:
            print("Hakkınız bitti")
    elif bar==2:
        if(baris.dersSayisi>5):
            print("Daha Fazla Ders Giremezsiniz")
        else:
            dersAdi=input("Ders Adını Giriniz:")
            vize=int(input("Vize Notunu Girniz:"))
            final=int(input("Final Notunu Girniz:"))
            proje=int(input("Proje Notunu Giriniz:"))
            baris.dersTanimla(dersAdi,vize,final,proje)
            print("Ders Kaydınız Başarılı")
    elif bar==3:
        if(baris.dersSayisi>2):
              baris.dersNotHesapla()
        else:
            print(f"Ders sayınız en az 3 olmalı. sizin ders sayınız: {baris.dersSayisi}")
    elif bar==4:
        if(baris.dersSayisi>0):
            baris.dersKayiKeys()
        else:
            print("Dersiniz Yok Lütfen ders ekleyin")
    else:
        case["Default"]
    kontrol=input("Devam Etmek İstiyor musunz E/H")
    if kontrol=="e" or kontrol=="E":
        kontrol=True
    else:
        kontrol=False
        print("Tekrar Bekleriz")
    
            
            
        
   