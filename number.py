'''随机密码生成器V1.1'''
import random
import string
import traceback
import subprocess
print("欢迎使用密码随机生成器！\n")
# count=0
seed = "ABCDEFGHIJKLMNOPQRSTUVWXYZ,abcdefghijklmnopqrstuvwxyz.1234567890!@#$%&*-_="
sa = []
def main():
    num = int(input("请输入要生成的密码数量：\n"))
    i = 0
    while i != num:
        for j in range(8):
            sa.append(random.choice(seed))
        salt = ''.join(random.sample(string.ascii_letters + string.digits, 8))
        print("以下为随机生成的密码：", salt)
        try:
            FILE = open("F:/code/Auto/Loginfo/Password.txt", "a", encoding="utf-8")
            FILE.write(salt)
            FILE.write("\n")
            FILE.close
        except:
            traceback.print_exc()
        i = i + 1
if __name__ == '__main__':
    main()
res = subprocess.Popen('pause', shell=True, stdout=subprocess.PIPE)
# while count<10:
#     for j in range(8):
#         sa.append(random.choice(seed))
#     salt = ''.join(random.sample(string.ascii_letters + string.digits, 8))
#     print("以下为随机生成的密码：",salt)
#     count+=1