
import time
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw 
import db_class as dd

# Поиск максимального размера строки в колонке
def maxSizeColumn(table:dd.db_class):
    listText = table.selectAll()
    sizeCol = []
    for i in range(table.countCol):
        sizeCol.append([0]*table.countRows)
    for i,txt in enumerate(listText):
        for j in range(table.countCol):
            sizeCol[j][i] = len(str(txt[j])) 
    for i in range(table.countCol):
        sizeCol[i] = max(sizeCol[i])
    for i, nameCol in enumerate(table.atribute):
        if (len(nameCol[0]) > sizeCol[i]):
            sizeCol[i] = len(nameCol[0])

    return sizeCol

def sizeIMG(sizeCol, sizeTxt, rows):
    w = sizeTxt*4
    for i in sizeCol:
        w += i*sizeTxt 
    h = sizeTxt*(rows+3) * 2
    return (w,h)


def fail():
    img = Image.new("RGB", (1000, 50), 'white')
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype('/home/danila/codes/python/fonts/UbuntuMono-R.ttf', 32)
    draw.text([0, 0], 'Это ошибка я точно её исправлю, но не сегодня!', (255,0,0), font=font)
    return img

def createIMG(table:dd.db_class, where = None, startIndex = 0) -> Image:
    #Создание картинки
    listText = table.selectAll(where=where)
    if (listText is not None and len(listText) > 0):
        sizeColumn = maxSizeColumn(table)
        sizeText = 16
        w, h = sizeIMG(sizeColumn, sizeText, len(listText))
        if (w > 2000):
            sizeText += 16
            w, h = sizeIMG(sizeColumn, sizeText, len(listText))
        start_pos = [sizeText*2, sizeText*2]
        img = Image.new("P", (w, h), 'white')
        draw = ImageDraw.Draw(img)
        font = ImageFont.truetype('/home/danila/codes/python/fonts/UbuntuMono-R.ttf', sizeText)
        step = [0, 0]
        for i, nameCol in enumerate(table.atribute):
            c = start_pos[0] + step[0]
            size = sizeColumn[i] * sizeText
            draw.rectangle([c, start_pos[1], (c + size, start_pos[1] + sizeText*2)], outline='black')
            draw.text([(c + size/4), start_pos[1] + sizeText/2], nameCol[0], (255,0,0), font=font)
            step[0] += size
        
        start_pos[1] += sizeText*2
        step[0] = 0
        for i, txt in enumerate(listText[startIndex:]):
            for j in range(table.countCol):
                c = start_pos[0] + step[0]
                size = sizeColumn[j] * sizeText
                draw.rectangle([c, start_pos[1], (c + size, start_pos[1] + sizeText*2)], outline='black')
                draw.text([(c + size/4), start_pos[1] + sizeText/2], str(txt[j]), (0,0,0), font=font)
                step[0] += size
            start_pos[1] += sizeText*2
            step[0] = 0
            if (start_pos[1] >= h):
                break
        if (w > 7000 and h > 3000):
            return fail()
    else:
        if (len(listText) == 0):
            None
        else:
            return fail()
        
    return img
