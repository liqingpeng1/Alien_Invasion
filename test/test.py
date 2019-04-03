
#!/usr/bin/env python
# !-*- coding:utf-8 -*-

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

# /usr/bin/env python
# coding:utf-8

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



y=list(range(2,11,2))#创建一个2到10的偶数列表
import cursor as cursor


y=list(range(2,11,2))

print(y)
print(min(y))
for i in range(0,10):
    print(i)

pizzas=["orange","apple","durian"]
print(pizzas)
for pizza in pizzas:
    print("I like" +' '+ pizza + ' '+"pizza")
print("I relly love pizza")


animals = ["cat","dog","pig"]
for animal in animals:
    print("A"+' '+animal.title()+' '+"would make a great pet")
print("These animals all have legs")

for i in range(0,21):
    print(i)

numbers=list(range(1,1000001))
print(min(numbers))
print(max(numbers))
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
print(cubee)


ListTest=["1","2","3","4"]
TEST=2
if TEST in ListTest:
    print("hava in")
else:
    print("not in")

a="Cat"
print(a.lower())

age=int(input("请输入的年龄:"))
if age<4:
    print("免费")
elif 4<=age<18:
    print("收费5元")
else:
    print("收费10元")
age=int(input("请输入你的年龄:"))
if age<4:
    print("小学生")
elif 4<=age<18:
    print("幼儿园")
else:
    print("垃圾")


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
    "first_name":"李",
    "last_name":"大哥",
    "age":"18",
    "city1":"重庆",
    "city":"重庆",
    "first_name":"王",
    "last_name":"小二",
    "age":"18",
    "city1":"china",
    "city":"mocswo"
}
for a in set(friend.values()):
    print(a)

rivers={
    "Yangtze River":"china",
    "the Nile":"Nimule",
    "Amazon":"Andes",
    "nile":"egypt"
}
rivers["changjiang"]="china"#增加字典键、值
rivers["nile"]="china"#修改字典值
del rivers["the Nile"]#删除字典键、值
rivers["changjiang"]="china"
rivers["nile"]="china"

print(rivers)
for river in rivers.keys():
    for city in rivers.values():
        print(river.title()+" "+"runs though"+" "+city.title())

#字典嵌套
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

a = True
while a:
    ps = input("请输入你的配料：")
    ps = input("请输入你猜测的数字：")
    if ps == 8:
        break
    else:
        print(ps)

age =1
while age:
    age_1=int(input("请输入你的年龄："))
    if 0<age_1 <3:
        print("免费")
    elif 3<= age_1 < 12:
        print("收费10$")
    elif age_1>12:
        print("收费15$")
    age_1=int(input("请输入你的年龄"))
    if 0<age_1 <3:
        print("小学生")
    elif 3<= age_1 < 12:
        print("幼儿园")
    elif age_1>12:
        print("垃圾")
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
    print("这件体恤型号"+size+","+"这件体恤印有字体"+font)

    print("这件衣服"+size+","+"和我"+font)


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
    a = str(input("请输入你的名字："))
    if a == "q":
        break
    b = str(input("请输入你的专辑名："))
    c = str(input("请输入你的歌曲数："))
    a = str(input("请输入你猜测的数字："))
    if a == "q":
        break
    b = str(input("璇疯緭鍏ヤ綘鐨勪笓杈戝悕锛�"))
    c = str(input("璇疯緭鍏ヤ綘鐨勬瓕鏇叉暟锛�"))
    d = make_album(a,b,num=c)
    print(d)




def show_magicians(magic):
    for ma in magic:
        print(ma)

magician=["li","zhang","wang"]

show_magicians(magician)


def pizzas(*name):
    for pizza in name:
        print("点的配料是"+pizza)
        print("鐐圭殑閰嶆枡鏄�"+pizza)

pizzas("lajiao")
pizzas("xiangcai","dasuan")
pizzas("1","2","3","4")


def build_pofile(first,last,**user_info):#定义一个函数，**user_info一个空列表的形参

    my_pofile = {
        'first_name':first,
        'last_name':last,
    }
    for key,value in user_info.items():
        my_pofile[key]=value
    print(my_pofile)

build_pofile("li","qing",xing="peng",gender="boy")


import time

print(time.time())


from test import  build_pofile as bp

bp("li","qing")

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
        print("当前用户登陆了" + str(self.login_attempts) + "次")

    def reset_login_attempts(self):
        self.login_attempts = 0
        print("用户登陆次数已被重置为:" + str(self.login_attempts) + "次")



    def reset_login_attempts(self):
        self.login_attempts = 0
        print("用户登陆次数已被重置为:" + str(self.login_attempts) + "次")



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



FlseTest="guest.txt"

with open(FlseTest, 'a') as FT:
    FT.write("请输入你的名字："+str(input("请输入你的名字：")))

FlseTest="guest.txt"

with open(FlseTest, 'a') as FT:
    FT.write("璇疯緭鍏ヤ綘鐨勫悕瀛楋細"+str(input("璇疯緭鍏ヤ綘鐨勫悕瀛楋細")))
    print(FT)
    FT.close()

Filetest="guest_book.txt"


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
            f.close()

import datetime

print(datetime.datetime.now())
datetime.datetime.now().replace(minute=3, hour=2)



import random

num = random.randint(1, 9)

while True:
    num1 = int(input("请输入你猜测的数字："))
    if num == num1:
        print("猜对了！")
        break
    elif num != num1:
        print("猜错了再猜！")
    num1 = int(input("请输入你猜测的数字:"))



import random
AuthCode = ""

a = str(random.randint(0, 9))
b = str(random.randint(0, 9))
c = str(random.randint(0, 9))
d = str(random.randint(0, 9))
e = str(random.randint(0, 9))
f = str(random.randint(0, 9))

AuthCode = a + b + c + d + e + f

print(AuthCode)

import easygui, random
num = random.randint(1,3)
numbers = 0
feavl = easygui.msgbox("现在开始一个猜数字游戏且只有五次机会")
# easygui.msgbox("你选择的是" + feavl)
# feavl = easygui.choicebox("请选择你要的口味",choices=["蓝莓","草莓","树莓"])//按钮选择
# feavl = easygui.enterbox("请输入你要的口味",default="草莓")//一个输入框
# feavl = easygui.mulenterbox(""你的名字是,"你的年龄是")//可支持同页面多输入框
while True and numbers < 5:
    feavl = easygui.integerbox("请输入你猜测的数字")#输入的是整数型
    if feavl == num:
        easygui.msgbox("你猜对了")
        break
    elif feavl != num:
        easygui.msgbox("你猜错了")
    numbers += 1


import easygui
easygui.msgbox("现在开始收集你的信息")
first_name = easygui.enterbox("请输入你的名字")
num = easygui.integerbox("请输入你的房间号")
city = easygui.enterbox("请输入你的城市")
postcode = easygui.enterbox("请输入你的邮编")
easygui.msgbox("你的地址是："+"\n"+ first_name+"\n"+str(num)+"\n"+city+"\n"+str(postcode))

import easygui as g
g.msgbox("招聘足球训练生", title="报名", ok_button ="确定")
gender = str(g.choicebox("请输入你的性别", choices=["男", "女"]))
age = g.integerbox("请输入你年龄", lowerbound=0, upperbound=100)
if gender == "女" and 10 <= age and age <= 12:
    g.msgbox("恭喜你,合格了", title="招聘", ok_button="确定")
else:
    g.msgbox("对不起你不合要求", title="招聘", ok_button="确定")

import easygui
password = "111111"
username = "111111"
title = "登陆"
name = ["*登录账号", "*登录密码"]
user=easygui.multenterbox("请输入你登录账号和密码", title, name)
print(user)
if user[0] == username and user[1] == password:
    easygui.msgbox("登陆成功")
elif user[0] != username and user[1] == password:
    easygui.buttonbox("登陆账号错误", choices=["重新登录", "退出"])
else:
    easygui.buttonbox("登陆密码错误", choices=["重新登录", "退出"])

import time
def timesleep(timem):
    for i in range(timem,0,-1):
        print(str(i) + "s")
        time.sleep(1)
    print("over")

timesleep(3)

import random
import time
list1 = []
for i in range(0,6):
    f = random.randint(0, 21)
    list1.append(str(f))
    print(list1)

for i in range(30, 0, -3):
    num = random.random() * 10
    print(num)
    time.sleep(3)

import pygame,random
from pygame.color import THECOLORS
screen = pygame.display.set_mode([740, 580])
screen.fill([255,255,255])
for i in range(0,100):
    width = random.randint(0,150)
    height = random.randint(0,100)
    colors_name = random.choice(THECOLORS.keys())
    color = THECOLORS(colors_name)
    top = random.randint(0,600)
    left = random.randint(0,490)
    pygame.draw.rect(screen,color,[left,top,left,height],1)
pygame.display.flip()
running = True
while running:
    for event in pygame.event.get():
        if event.type ==pygame.QUIT:
            running = False
pygame.quit()

from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.get("http://www.baidu.com")
driver.maximize_window()
size = driver.get_window_position()
print(size)
hendle = (driver.current_window_handlent)
print(hendle)
driver.find_element_by_id("kw").send_keys("python")
driver.find_element_by_id("su").click()
time.sleep(5)
driver.quit()

import xlrd
elcel = xlrd.open_workbook(u"test.xlsx")
table = elcel.sheet_by_index(0)
nrows = table.nrows
a = table.row_values(0, 0)
b = table.col_values(0, 2)
# print(a,b)
values = table.cell(0, 0).value
print(values)


import urllib.request
import urllib.parse
import time
from bs4 import BeautifulSoup

class ZhiLianSpider(object):
    def __init__(self, jl, kw, start_page, end_page):
        # 保存到成员属性中，这样在其他的方法中就可以直接使用
        self.jl = jl
        self.kw = kw
        self.start_page = start_page
        self.end_page = end_page

        self.items = []

    def handle_request(self, page):
        url = 'https://sou.zhaopin.com/jobs/searchresult.ashx?'
        data = {
            'jl': self.jl,
            'kw': self.kw,
            'p': page,
        }
        query_string = urllib.parse.urlencode(data)
        # 拼接url
        url += query_string
        # print(url)
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
        }
        return urllib.request.Request(url=url, headers=headers)

    def parse_content(self, content):
        # 生成soup对象
        soup = BeautifulSoup(content, 'lxml')
        # 首先找到所有的table
        table_list = soup.find_all('table', class_='newlist')[1:]
        # print(table_list)
        # print(len(table_list))
        # 遍历所有的table，依次提取每一个工作的信息
        for table in table_list:
            # 职位名称
            zwmc = table.select('.zwmc a')[0].text.strip('\xa0')
            # 公司名称
            gsmc = table.select('.gsmc a')[0].text
            # 职位月薪
            zwyx = table.select('.zwyx')[0].text
            # 工作地点
            gzdd = table.select('.gzdd')[0].text
            # print(gzdd)
            # exit()
            item = {
                '职位名称': zwmc,
                '公司名称': gsmc,
                '职位月薪': zwyx,
                '工作地点': gzdd,
            }
            self.items.append(item)

    def run(self):
        # 搞个循环
        for page in range(self.start_page, self.end_page + 1):
            print('正在爬取第%s页......' % page)
            #　拼接url的过程，构建请求对象
            request = self.handle_request(page)
            content = urllib.request.urlopen(request).read().decode('utf8')
            # 给我请求对象，解析并且提取内容
            self.parse_content(content)
            print('结束爬取第%s页' % page)
            time.sleep(2)

        # 将所有的工作保存到文件中
        string = str(self.items)
        with open('work.txt', 'w', encoding='utf8') as fp:
            fp.write(string)

def main():
    # 输入工作地点
    jl = input('请输入工作地点:')
    # 输入工作关键字
    kw = input('请输入关键字:')
    # 输入起始页码
    start_page = int(input('请输入起始页码:'))
    # 输入结束页码
    end_page = int(input('请输入结束页码:'))
    zhilian = ZhiLianSpider(jl, kw, start_page, end_page)
    zhilian.run()

if __name__ == '__main__':
    main()

import urllib.request
import urllib.parse
from bs4 import BeautifulSoup
import time

# 给我一个url，返回一个请求对象
def handle_request(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
    }
    return urllib.request.Request(url=url, headers=headers)

def parse_first_page(url):
    request = handle_request(url)
    # 发送请求，获取响应
    content = urllib.request.urlopen(request).read().decode('utf8')
    time.sleep(2)
    # 使用bs解析内容,生成soup对象
    soup = BeautifulSoup(content, 'lxml')
    # print(soup)
    # 查找所有的章节链接对象
    a_list = soup.select('.book-mulu > ul > li > a')
    # print(ret)
    # print(len(ret))
    # 打开文件
    fp = open('三国演义.txt', 'w', encoding='utf8')
    # 遍历所有的a对象
    for oa in a_list:
        # 取出这个a的内容
        title = oa.string
        # 取出a的href属性
        href = 'http://www.shicimingju.com' + oa['href']

        print('正在下载%s......' % title)
        # 向href发送请求，直接获取到解析之后的内容
        neirong = get_neirong(href)
        print('结束下载%s' % title)
        time.sleep(2)
        string = '%s\n%s' % (title, neirong)
        # 将string写入到文件中
        fp.write(string)

    fp.close()

def get_neirong(href):
    # 向href发送请求，获取响应，解析响应，返回内容
    request = handle_request(href)
    content = urllib.request.urlopen(request).read().decode('utf8')
    # 生成soup对象，提取章节内容
    soup = BeautifulSoup(content, 'lxml')
    # 找包含章节内容的div
    odiv = soup.find('div', class_='chapter_content')
    neirong = odiv.text
    return neirong

def main():
    url = 'http://www.shicimingju.com/book/sanguoyanyi.html'
    # 解析第一个页面，返回所有的章节列表
    chapter_list = parse_first_page(url)

if __name__ == '__main__':
    main()


import requests
url='http://www.baidu.com'
req = requests.get(url)
if (req.status_code == requests.status_codes.ok):#返回的状态码等于200就打印ok
    print('ok')

a=bin(2)#返回字符的二进制字符串
print(a)#0b10
c=format(2,'b')#返回不需要0b前缀
print(c)#10
'''
