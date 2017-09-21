from PIL import Image,ImageDraw,ImageFont,ImageFilter

import random
'''
自动生成240*60的验证码
'''
#随机字母
def ranChar():
    return chr(random.randint(65,90))

#color1
def ranColor():
    return (random.randint(64,255),random.randint(32,255),random.randint(64,255))

#color2
def ranColor2():
    return (random.randint(32,127),random.randint(32,127),random.randint(32,127))

width = 60 * 4
height=60
image=Image.new('RGB',(width,height),(255,255,255))
#创建Font对象
font=ImageFont.truetype('ariali.ttf',36)

#创建Draw对象
draw=ImageDraw.Draw(image)

#填充每个像素
for x in range(width):
    for y in range(height):
        draw.point((x,y),fill=ranColor())

d=list()
dd=''

#输出文字
for t in range(4):
    mChar=ranChar()
    d.append(mChar)
    dd=dd+mChar
    draw.text((60*t+10,10),mChar,font=font,fill=ranColor2())

print(d)
print(dd)

#模糊
image=image.filter(ImageFilter.BLUR)
image.save('code.jpg','jpeg')
image.show()#打开图片
