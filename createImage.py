import time
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw 

def createIMG(*args):
    pass

w, h = 800, 800
sizeText = 16
start_pos = (sizeText*4, sizeText*4)

img = Image.new("P", (w,h), 'white')
draw = ImageDraw.Draw(img)

font = ImageFont.truetype('/home/danila/codes/python/fonts/UbuntuMono-R.ttf', sizeText)

# Одинаковые по размеру ячейки
# step = [
#     (w - start_pos [0]*2)//n, 
#     (h - start_pos [1]*2)//(m+1)
#     ]

# for i in range(start_pos[0], w - start_pos[0] - step[0], step[0]):
#     for j in range(start_pos[1], h - start_pos[1] - step[1], step[1]):
#         draw.rectangle([(i, j), (i + step[0], j + step[1])], outline='black')
#         draw.text((i + step[0]/4, j + step[1]/4),f'{i}',(0,0,0), font=font)

textArr = ('ASdsd', 'svinka', 'pudel', 'kit', 'martishka')
step = [0, 0]

for i, tex in enumerate(textArr):
    c = start_pos[0] + step[0]
    size = len(tex) * sizeText
    draw.rectangle([c, start_pos[1], (c + size, start_pos[1]+sizeText)], outline='black')
    draw.text([(c + size/4), start_pos[1]], tex, (0,0,0), font=font)
    step[0] += size
    img.show()
    time.sleep(1)

