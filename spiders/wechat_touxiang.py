from numpy import *
import itchat
import PIL.Image as Image
from os import listdir

def get_imgs():
    itchat.auto_login(hotReload=True)
    friends = itchat.get_friends(update=True)[100:325]
    num = 0
    for i in friends:
        img = itchat.get_head_img(userName=i["UserName"])
        fileImage = open( "./user/" + str(num) + ".jpg",'wb')
        fileImage.write(img)
        fileImage.close()
        num += 1
def get_big_img():
    pics = listdir("user")
    numPic = len(pics)
    print(numPic)
    toImage = Image.new("RGB", (450, 450))
    x = 0
    y = 0
    for i in pics:
        try:
            img = Image.open("user/{}".format(i))
        except IOError:
            print("Error: 没有找到文件或读取文件失败",i)
        else:
            img = img.resize((30, 30), Image.ANTIALIAS)
            toImage.paste(img, (x * 30, y * 30))
            x += 1
            if x == 15:
                x = 0
                y += 1
    toImage.save("user/" +"touxiang.jpg")
    itchat.send_image("user/" +"touxiang.jpg", 'filehelper')

get_imgs()
get_big_img()
