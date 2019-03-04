import random,string,datetime
"""手机号"""
def Number():
    number=random.randint(14000000000,14099999999)
    return number
    print(number)
"""微信ID"""
def Wxid():
    wxid=random.sample(string.ascii_lowercase,5)
    fh=''.join(wxid)
    return fh
    print(fh)
"""用户名"""
def Name():
    name = random.sample(string.ascii_lowercase, 3)
    fh=''.join(name)
    return fh
    print(fh)
"""用户昵称"""
def Nickname():
    nickname = random.sample(string.ascii_lowercase, 4)
    fh = ''.join(nickname)
    return fh
    print(fh)
"""单据编号"""
def Billmoduleid():
    billmoduleid=random.randint(9006666,9999999)
    return billmoduleid
    print(billmoduleid)
"""开始日期"""
def Sdate():
    i = datetime.datetime.now()
    sdate= ("%s-%s-%s" % (i.year,i.month,i.day))
    return sdate
"""结束日期"""
def Edate():
    i = (datetime.datetime.now()+datetime.timedelta(days=15))
    edate=("%s-%s-%s" % (i.year,i.month,i.day))
    return edate
"""制单时间"""
def Inputdate():
    inputdate=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    return inputdate
    print(inputdate)
shj=Number()
wx=Wxid()
yhm=Name()
yhnc=Nickname()
djbh=Billmoduleid()
ks=Sdate()
js=Edate()
sj=Inputdate()
#随机生成整数

numI=random.randint(0,999)
print(numI)
#随机生成小数
numF=random.uniform(0,999)
no=round(numF,2)
print(no)
#随机生成大写字母
S= string.ascii_uppercase
R= random.choice(S)
print(R)
#随机生成小写字母
s=string.ascii_lowercase
r=random.choice(s)
print(r)
#随机生成符号
seed = "~!@#$%^&*()-_=+[]{},.?"
fh=random.choice(seed)
print(fh)
#随机生成汉字
def GB2312():
    head = ''.join(random.randint(0x4E00, 0x9FA5))
    return head
for i in range(100):
    s=chr(GB2312())
print(s)
#颜文字
for i in range(0x1f600,0x1f650):
    print(chr(i),end=" ")
    if i%16==15:
        print()