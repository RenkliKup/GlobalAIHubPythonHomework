import random as rnd
'''
Kurallar:
5 hak veriliyor buldun buldun :D
'''
name=input("please enter yourself name:")
words=["a b i l i t y"] 
letter=""
ayni=[]
game=rnd.choice(words)
game=game.split(" ")
count=0
deneme=5
print(f"Hello {name}")
while True:

    letter=input("lütfen bir harf girin:")
    if(letter in ayni):
        print("bu harfi daha önce girdiniz")
        pass
    else:
        for a in range(0,len(game)):
            if letter==game[a]:
                ayni.append(letter)
                cnt=len(game)-1
                print(f"güzel {letter} harfini buldun. şimdi {cnt} harf kaldı")
                count+=1
                while True:
                    try:
                        game.remove(letter)
                    except ValueError:
                        break
                break
        if(deneme <1):
            print("oyun bitti")
            break

        if(count==0):
            deneme-=1
            print(f"deneme {deneme} kaldı ")
        if(count>0 and deneme>0):
            count=0
        if(len(game)==0):
            print("tebrikler oyunu kazandın")
            print("Bulduğunuz kelime:",words)
            break


    
