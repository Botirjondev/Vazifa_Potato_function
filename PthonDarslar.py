# def linear_Search(list, item):
#     for i in range(len(list)):
#         if list[i]==item:
#             return i
#         return 0
    
#     def binary_Search(list,item):
#         low=0
#         high=len(list)-1
#         while low <= high:
#             mid=(low+high)//2
#             guess=list[mid]
#             if guess==item:
#                 return mid
#             if guess>item:
#                 high=mid-1
#             else:
#                 low=mid+1
                
#                 return None
#             mylist1 = [1,2,3,5,4,7,81,256,95,945,548]
#             print(binary_Search(mylist1, 256))
#             print(linear_Search(mylist1, 7))
#             print("hello world")

# mylist = []
# for mehmon in range(0, 5):
#     print(mehmon)

# mylist = [5,6,25,321,257,154]
# for i in mylist:
    
#     print(i)


# mehmonlar = ["ali","vali","Gani","olim"]
# for mehmon in mehmonlar:
#     print("Salom",mehmon.capitalize(),"bayramga xush kelibsiz !!")
    
# sonlar = list(range(11))
# print(sonlar)
# sonlar_kvadrati = []
# for i in sonlar:
#     sonlar_kvadrati.append(i**2)
#     print(sonlar_kvadrati)
    
# son2 = list(range(11))
# print(son2)    


ismlar = ["Bilol","Ali","Aziz","Vali","Guli"]
n=0
for i in ismlar:
    n=n+1
    print(f"Salom {i}")
print(f"Kod {n} marta takrorlandi")
    
sonlar = list(range(9,100,2))
print(sonlar)
for i in range(1,6):
    Kino = input("Yoqtirgan filmlaringizni kiriting >>>\n")
    print(f"{i} inchi kino {Kino}")

suhbat =int(input("Bugun nechta odam bilan gaplashdingiz>>>\n"))
od=[]
for i in range(suhbat):
        odam = input(f"{i+1} suhbatlashgan odamingiz kim edi?>>>") 
        od.append(odam.capitalize())
print(od)       
    
cars=["audi","bmw","mersides","honda"]
for i in cars:
    if i=="bmw":
        print(i.upper())
    else:
        print(i.title())



ism = input("Ismingiz nima >>>")
if ism.lower() != "ali":
    print(f"Uzur {ism.title()} biz Alini kutyapmiz")
else:
    print(f"Salom {ism.title()}")

javob = float(input("12*6 necchi bo`ladi>>>"))
if javob != 72:
    print("Javob xato")
              
yosh = int(input("Yoshingiz nechchida>>>"))
if yosh <18:
    print("Uzur sizga mumkin emas")
else:
    print("Xush kelibsiz")    
              
login = input("Yangi login tallang!!!>>")
if len(login) <7:
    print("Sonlar kam to`liqroq kiriting")
else:
    print("Siz muvofaqyatli tarzda o`ttingiz")

x, y = 25, 50 # x=25 va y=50
print("x>y") if x>y else print("x<y")
              
cars = ["audi","toyota","gm","ford"]
for i in cars:
    if i=="gm":
        print(i.upper())
    else:
        print(i.title()) 

cars = ["audi","toyota","gm","ford"]
for i in cars:
    if i =="gm":
        print(i.upper())
    else:
        print(i.title())

sonlar = []
    
              
    
    