#coding=utf-8
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import random

# 随机字母
def getChar():
    return chr(random.randint(65,97))

# 随机颜色
def getColor():
    return (random.randint(32,127),random.randint(32,127),random.randint(32,127))

def getColor2():
    return (random.randint(64,255),random.randint(64,255),random.randint(64,255))

# 300*60
width = 300
height = 60
image = Image.new("RGB",(width,height),(255,255,255))

# 字体
font = ImageFont.truetype("C:\Windows\Fonts\simsun.ttc",36)

# draw
draw = ImageDraw.Draw(image)

# 填充像素
for x in range(width):
    for y in range(height):
        draw.point((x,y),fill=getColor2())
        
# 填充文字
for z in range(4):
    draw.text( (60*z+10,10), getChar(), font=font, fill=getColor())

# 模糊
image = image.filter(ImageFilter.BLUR)
image.save("check.jpg","jpeg")

