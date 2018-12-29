#!/usr/bin/env python
#!-*- coding:utf-8 -*-

'''
invite=["zhangsan","lisi","wanger","zhouyi"] #创建一个列表
print(invite) #打印列表
print("lisi not come") #打印李四无法参加
invite[1]="wuwu" #修改列表第二个为wuwu
print(invite) #打印修改后的列表
invite.append("lisa")#在列表最后添加lisa
invite.append("wuso")#在列表最后添加wuso
invite.insert(0,"ksks")#在列表最前面插入ksks
invite.insert(4,"psao")#在列表第五位后面插入psao
print(invite)#打印当前修改后的列表
del invite[3]#删除列表第四个元素
print(invite)#打印删除后的元素
invite.pop()#删除列表最后一个元素
print(invite)#打印已删除的列表元素
a=invite.pop()#赋值a为当前删除的列表元素
print(a+" "+"sorry!")#打印a
b=invite.pop()
print(b+" "+"sorry!")
=======
# /usr/bin/env python
# coding:utf-8
'''
invite=["zhangsan","lisi","wanger","zhouyi"]
print(invite)
print("lisi not come")
invite[1]="wuwu"
print(invite)
invite.append("lisa")
invite.append("wuso")
invite.insert(0,"ksks")
invite.insert(4,"psao")
print(invite)
del invite[3]
print(invite)
invite.pop()
print(invite)
a=invite.pop()
print(a+" "+"sorry!")
b=invite.pop()
print(b+" "+"sorry!")
c=invite.pop()
print(c+" "+"sorry!")
d=invite.pop()
print(d+" "+"sorry!")
print(invite)
print(invite[0]+" "+"welcome!")
print(invite[1]+" "+"welcome!")
del invite[0]#删除列表第一个元素
print(invite)
print(len(invite))#打印当前元素长度
num=[1,8,6,4,2,3,7,9,54]
num.sort()#对元素进行排序
del invite[0]
print(invite)
print(len(invite))
num=[1,8,6,4,2,3,7,9,54]
num.sort()
print(num)

travel=["bq2","cq3","aq1","eq5","dq4"]
print(travel)
print(sorted(travel))
print(travel)
travel.reverse()
print(travel)
travel.reverse()
print(travel)
travel.sort()
print(travel)
print(len(travel))

'''
<<<<<<< Updated upstream
'''
y=list(range(2,11,2))#创建一个2到10的偶数列表
import cursor as cursor

'''
y=list(range(2,11,2))
>>>>>>> Stashed changes
print(y)
print(min(y))
for i in range(0,10):
    print(i)
'''
'''
pizzas=["orange","apple","durian"]
print(pizzas)
for pizza in pizzas:
    print("I like" +' '+ pizza + ' '+"pizza")
print("I relly love pizza")


animals=["cat","dog","pig"]
for animal in animals:
    print("A"+' '+animal.title()+' '+"would make a great pet")
print("These animals all have legs")

for i in range(0,21):
    print(i)

numbers=list(range(1,1000001))
print(min(numbers))
print(max(numbers))
<<<<<<< Updated upstream
print(sum(numbers))#总和

OddNumber=list(range(1,21,2)) #创建一个1-20的奇数列表
for odd in OddNumber:
    print(odd)

mupitle=list(range(3,31,3))#创建一个能整除3的列表
for mup in mupitle:
    print(mup)

cubes=[]#创建一个空列表
for a in range(1,11):
    cube=a**3 #赋值cube的立方
    cubes.append(cube)#把值添加到列表
print(cubes)

cubee=[b**3 for b in range(1,11,2)]#列表解析将FOR循环和创造新元素的代码合在了一起
=======
print(sum(numbers))
OddNumber=list(range(1,21,2)) 
for odd in OddNumber:
    print(odd)

mupitle=list(range(3,31,3))
for mup in mupitle:
    print(mup)

cubes=[]#
for a in range(1,11):
    cube=a**3 
    cubes.append(cube)
print(cubes)

cubee=[b**3 for b in range(1,11,2)]
>>>>>>> Stashed changes
print(cubee)


ListTest=["1","2","3","4"]
TEST=2
if TEST in ListTest:
    print("hava in")
else:
    print("not in")

a="Cat"
print(a.lower())

<<<<<<< Updated upstream
age=int(input("请输入的年龄:"))
if age<4:
    print("免费")
elif 4<=age<18:
    print("收费5元")
else:
    print("收费10元")
=======
age=int(input("请输入你的年龄:"))
if age<4:
    print("小学生")
elif 4<=age<18:
    print("幼儿园")
else:
    print("垃圾")
>>>>>>> Stashed changes


alien_color=["yellow","green","red"]
align_01="gerrn"

if align_01 in alien_color:
    print("you have the five mark")
elif align_01 not in alien_color:
    print("you have the ten mark")


alien_01="red"
if alien_01 =="green":
    print("you have the five mark")
elif alien_01 =="yellow":
    print("you have the ten mark")
elif alien_01 == "red":
    print("you have the fiften mark")


age=int(input("请输入你的年龄："))
if age <2:
    print("it's baby")
elif 2<=age<4:
    print("He is a bady and learning to walk")
elif 4<=age<13:
    print("He is children")
elif 13<=age<20:
    print("He is teenger")
elif 20<=age<65:
    print("He is adult")
else:
    print("He is the aged")


users=["admin","lqp","fsy","zs","wr"]
for user in users:
    if user=="admin":
        print("Hello"+" "+user.title()+","+"would you like to see a status report?")
    else:
        print("Hello"+" "+user.title()+","+"thank you for logging in again")

num=(list(range(0,10)))
for num_01 in num:
    if num_01 == 1:
        print(str(num_01)+"st")
    elif num_01 ==2:
        print(str(num_01)+"nd")
    elif num_01 ==3:
        print(str(num_01)+"rd")
    elif num_01 ==4:
        print(str(num_01)+"th")
    elif num_01 ==5:
        print(str(num_01)+"th")
    elif num_01 ==6:
        print(str(num_01)+"th")
    elif num_01 ==7:
        print(str(num_01)+"th")
    elif num_01 ==8:
        print(str(num_01)+"th")
    elif num_01 ==9:
        print(str(num_01)+"th")

friend={
<<<<<<< Updated upstream
    "first_name":"李",
    "last_name":"大哥",
    "age":"18",
    "city1":"重庆",
    "city":"重庆"
=======
    "first_name":"王",
    "last_name":"小二",
    "age":"18",
    "city1":"china",
    "city":"mocswo"
>>>>>>> Stashed changes
}
for a in set(friend.values()):
    print(a)

rivers={
    "Yangtze River":"china",
    "the Nile":"Nimule",
    "Amazon":"Andes",
    "nile":"egypt"
}
<<<<<<< Updated upstream
rivers["changjiang"]="china"#增加字典键、值
rivers["nile"]="china"#修改字典值
del rivers["the Nile"]#删除字典键、值
=======
rivers["changjiang"]="china"
rivers["nile"]="china"
del rivers["the Nile"]
>>>>>>> Stashed changes
print(rivers)
for river in rivers.keys():
    for city in rivers.values():
        print(river.title()+" "+"runs though"+" "+city.title())

<<<<<<< Updated upstream
#字典嵌套
=======

>>>>>>> Stashed changes
people={
    'zhang':{
        'first_name':'zhang',
        'last_name':'zhang1',
        'age':'15'
         },
    'li':{
        'first_name':'li',
        'last_name':'li1',
        'age':'16'
         },
    'wang':{
        'first_name':'wang',
        'last_name':'wang1',
        'age':'14'
        }
}

for i,j in people.items():
    print("\nname:"+" "+i)
    print("first_name:"+j['first_name'])
    print("last_name:"+j["last_name"])
    print("age:"+j["age"])


<<<<<<< Updated upstream
money=(input("请问你们多少人用餐："))
if money == 8:
    print("有空位")
else:
    print("没有空位")

numbe=int(input("请输入一个数字："))
if numbe%10 == 0:
    print("输入的数字是10的整数倍")
elif numbe%10 !=0:
    print("输入的数字不是10的整数倍")
=======
money=(input("请输入你的金额"))
if money == 8:
    print("对了")
else:
    print("错了")

numbe=int(input("请输入你猜测的数字："))
if numbe%10 == 0:
    print("猜对了")
elif numbe%10 !=0:
    print("猜错了")
>>>>>>> Stashed changes
'''
'''
a = True
while a:
<<<<<<< Updated upstream
    ps = input("请输入你的配料：")
=======
    ps = input("请输入你猜测的数字：")
>>>>>>> Stashed changes
    if ps == 8:
        break
    else:
        print(ps)

age =1
while age:
<<<<<<< Updated upstream
    age_1=int(input("请输入你的年龄："))
    if 0<age_1 <3:
        print("免费")
    elif 3<= age_1 < 12:
        print("收费10$")
    elif age_1>12:
        print("收费15$")
=======
    age_1=int(input("请输入你的年龄"))
    if 0<age_1 <3:
        print("小学生")
    elif 3<= age_1 < 12:
        print("幼儿园")
    elif age_1>12:
        print("垃圾")
>>>>>>> Stashed changes
    else:
        break

a=1
while a<=5:
    print(a)

sandwich_orders=["first","scoend","third"]
finished_sandwiches=[]
for i in sandwich_orders:
    print("I made your "+i)
finished_sandwiches+=sandwich_orders
print(finished_sandwiches)

def a():
    print("hello")
a()

def make_shirt(size,font=" i love python"):
<<<<<<< Updated upstream
    print("这件体恤型号"+size+","+"这件体恤印有字体"+font)
=======
    print("这件衣服"+size+","+"和我"+font)
>>>>>>> Stashed changes

make_shirt("big size")


def city_country(city_name,country_name):
    print(city_name.title()+","+country_name.title())

city_country("chongqing","china")
city_country("now york","america")
city_country("paris","france")


def make_album(name,album_name, num = ""):
    zidian = {'name': name, 'album name': album_name }
#    print(zidian)
    if num:
        zidian['num']=num
    print(zidian)

#make_album("jay","heiye",num=23)


while 1:
<<<<<<< Updated upstream
    a = raw_input("请输入你的名字：")
    if a == "q":
        break
    b = raw_input("请输入你的专辑名：")
    c = raw_input("请输入你的歌曲数：")
=======
    a = raw_input("请输入你猜测的数字：")
    if a == "q":
        break
    b = raw_input("璇疯緭鍏ヤ綘鐨勪笓杈戝悕锛�")
    c = raw_input("璇疯緭鍏ヤ綘鐨勬瓕鏇叉暟锛�")
>>>>>>> Stashed changes
    d=make_album(a,b,num=c)
    print(d)




def show_magicians(magic):
    for ma in magic:
        print(ma)

magician=["li","zhang","wang"]

show_magicians(magician)


def pizzas(*name):
    for pizza in name:
<<<<<<< Updated upstream
        print("点的配料是"+pizza)
=======
        print("鐐圭殑閰嶆枡鏄�"+pizza)
>>>>>>> Stashed changes


pizzas("lajiao")
pizzas("xiangcai","dasuan")
pizzas("1","2","3","4")


<<<<<<< Updated upstream
def build_pofile(first,last,**user_info):#定义一个函数，**user_info一个空列表的形参
=======
def build_pofile(first,last,**user_info):#瀹氫箟涓�涓嚱鏁帮紝**user_info涓�涓┖鍒楄〃鐨勫舰鍙�
>>>>>>> Stashed changes
    my_pofile={}
    my_pofile={
        'first_name':first,
        'last_name':last,
    }
    for key,value in user_info.items():
        my_pofile[key]=value
    print(my_pofile)

build_pofile("li","qing",xing="peng",gender="boy")


import time

print(time.time())


from test_01 import  build_pofile as bp

bp("li","qing")

'''

'''
>>>>>>> Stashed changes
class User:

    def __init__(self, first_name, last_name, age, gender):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gender = gender
        self.login_attempts = 0

    def describe_user(self):
        print("Your are first_name:" + self.first_name.title())
        print("Your are last_name:" + self.last_name.title())
        print("Your age is:" + str(self.age))
        print("Your gender is:" + self.gender)

    def greet_user(self):
        print("Hello" + " " + self.first_name.title() + "!")

    def increment_login_attempts(self):
        self.login_attempts += 1
<<<<<<< Updated upstream
        print("当前用户登陆了" + str(self.login_attempts) + "次")

    def reset_login_attempts(self):
        self.login_attempts = 0
        print("用户登陆次数已被重置为:" + str(self.login_attempts) + "次")




    print("褰撳墠鐢ㄦ埛鐧婚檰浜�" + str(self.login_attempts) + "娆�")

    def reset_login_attempts(self):
        self.login_attempts = 0
        print("鐢ㄦ埛鐧婚檰娆℃暟宸茶閲嶇疆涓�:" + str(self.login_attempts) + "娆�")



user1 = User("jake", "kangkang", 18, "boy")
user1.describe_user()
user1.greet_user()
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.reset_login_attempts()
<<<<<<< Updated upstream
'''

class Restaurant():
    def __init__(self):
        pass

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 25

    def describe_restaurant(self):
        print("\n该店铺名称是：" + self.restaurant)
        print("\n该店铺烹饪方法是：" + self.cuisine_type)

    def open_restaurant(self):
        print("\n该店铺正在营业")

    def rest_numer_served(self):
        print("\n现在用餐人数是:" + str(self.number_served))

    def increment_number_served(self, miles):
        self.number_served += miles
        print("\n该店最多接纳顾客位数是:" + str(self.number_served))


# restaurant_1 = Restaurant('希尔顿酒店', '川菜')
        print("\n该店铺名称是：" + self.restaurant)
        print("\n该店铺菜系是：" + self.cuisine_type)

    def open_restaurant(self):
        print("\n璇ュ簵閾烘鍦ㄨ惀涓�")

    def rest_numer_served(self):
        print("\n鐜板湪鐢ㄩ浜烘暟鏄�:" + str(self.number_served))

    def increment_number_served(self, miles):
        self.number_served += miles
        print("\n璇ュ簵鏈�澶氭帴绾抽【瀹綅鏁版槸:" + str(self.number_served))


# restaurant_1 = Restaurant('甯屽皵椤块厭搴�', '宸濊彍')
# restaurant_1.describe_restaurant()
# restaurant_1.open_restaurant()
# restaurant_1.rest_numer_served()
# restaurant_1.increment_number_served(300)

class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type):
        super.mro()
        self.__init__(restaurant_name, cuisine_type)
        self.flavors = (list(range(0, 15, 2)))

    def a_flavors(self):
        print(self.flavors)


# ice=IceCreamStand("希尔顿酒店", "冷饮店")
# ice=IceCreamStand("甯屽皵椤块厭搴�", "鍐烽ギ搴�")
# ice.describe_restaurant()
# ice.a_flavors()


class Admin(User):
    def __init__(self, first_name, last_name, age, gender):
        super.__init__(first_name, last_name, age, gender)
        self.privileges = ["can add post", "can delete post", "can ban user"]


# admin1=Admin("jake", "kangkang", 18, "boy")
# admin1.describe_user()
# admin1.show_privileges()


''''
FlseTest="guest.txt"

with open(FlseTest, 'a') as FT:
    FT.write("请输入你的名字："+str(input("请输入你的名字：")))
=======

FlseTest="guest.txt"

with open(FlseTest, 'a') as FT:
    FT.write("璇疯緭鍏ヤ綘鐨勫悕瀛楋細"+str(input("璇疯緭鍏ヤ綘鐨勫悕瀛楋細")))
>>>>>>> Stashed changes
    print(FT)
    FT.close()


Filetest="guest_book.txt"

<<<<<<< Updated upstream
print("输入quit退出输入")

while True:
    with open(Filetest, "a") as f:
        ipt = input("\n请输入你的名字：")
        if ipt == "quit":
            break
        try:
            f.write("\n你输入的姓名是："+str(ipt))
            print(ipt+" "+"你好！")
        except AttributeError:
            print("\n输入有误，请重新输入")
=======
print("杈撳叆quit閫�鍑鸿緭鍏�")

while True:
    with open(Filetest, "a") as f:
        ipt = input("\n璇疯緭鍏ヤ綘鐨勫悕瀛楋細")
        if ipt == "quit":
            break
        try:
            f.write("\n浣犺緭鍏ョ殑濮撳悕鏄細"+str(ipt))
            print(ipt+" "+"浣犲ソ锛�")
        except AttributeError:
            print("\n杈撳叆鏈夎锛岃閲嶆柊杈撳叆")
>>>>>>> Stashed changes
            f.close()
'''
'''
import datetime

print(datetime.datetime.now())
datetime.datetime.now().replace(minute=3, hour=2)
'''

import random

'''
num = random.randint(1, 9)

while True:
<<<<<<< Updated upstream
    num1 = int(input("请输入你猜测的数字："))
    if num == num1:
        print("猜对了！")
        break
    elif num != num1:
        print("猜错了再猜！")
=======
    num1 = int(input("璇疯緭鍏ヤ綘鐚滄祴鐨勬暟瀛楋細"))
    if num == num1:
        print("鐚滃浜嗭紒")
        break
    elif num != num1:
        print("鐚滈敊浜嗗啀鐚滐紒")
>>>>>>> Stashed changes
'''

AuthCode = ""

a = str(random.randint(0, 9))
b = str(random.randint(0, 9))
c = str(random.randint(0, 9))
d = str(random.randint(0, 9))
e = str(random.randint(0, 9))
f = str(random.randint(0, 9))

AuthCode = a + b + c + d + e + f

print(AuthCode)

