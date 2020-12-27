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
print("Öğrenci Kaydınız Başarılı.")
name_surname_control=True

obje=s_s_s(name,surname)
print("Öğrenci Girişini Yapın Lütfen")
for control in range(0,3):
    name=input("Lütfen Adınızı Giriniz:")
    surname=input("Lütfen soyadınızı giriniz:")
    if((obje.name==name and obje.surname==surname)):
        print("Giriş Yapıldı")
        name_surname_control=True
        break
    else:
        name_surname_control=False
if(not name_surname_control):
    print("Yanlış Ad veya Soyad girdiniz programa giriş yapılmadı")
    pass
else:
    
    kontrol=True
    while kontrol:
        print(f"Merhaba {obje.name} {obje.surname}")
        for x in case.values():
            if x in "Yanlış Tuş Girişi":
                pass
            else:
                print(x)
        switch=int(input("please enter someone:"))
    
        if switch==1:
            if(obje.count>0):
                yeniad=input(f"{obje.count} defa adınızı ve soyadınızı değiştirebilirsiniz Yeni Ad Giriniz:")
                yeniSoyad=input(f"{obje.count} defa adınızı ve soyadınızı değiştirebilirsiniz Yeni Soyad Giriniz:")
                obje.adDegistir(yeniad,yeniSoyad)
                print(f"Adınız ve soyadınız {obje.name} {obje.surname} olarak değiştirildi")
            else:
                print("Hakkınız bitti")
        elif switch==2:
            if(obje.dersSayisi>5):
                print("Daha Fazla Ders Giremezsiniz")
            else:
                dersAdi=input("Ders Adını Giriniz:")
                vize=int(input("Vize Notunu Girniz:"))
                final=int(input("Final Notunu Girniz:"))
                proje=int(input("Proje Notunu Giriniz:"))
                obje.dersTanimla(dersAdi,vize,final,proje)
                print("Ders Kaydınız Başarılı")
        elif switch==3:
            if(obje.dersSayisi>2):
                obje.dersNotHesapla()
            else:
                print(f"Ders sayınız en az 3 olmalı. sizin ders sayınız: {obje.dersSayisi}")
        elif switch==4:
            if(obje.dersSayisi>0):
                obje.dersKayiKeys()
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
        
                
                
            
    