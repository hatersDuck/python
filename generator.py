import datetime
import random as rn

today = datetime.date.today()
date = datetime.date(2020, 1, 1)
alphRus = ['БВГДЖЗКЛМНПРСТФХЦЧШЩ', 'АИОУЫЭ']
alphEng = ['BCDFGHJKLMNPQRSTVWXYZ', 'AEIOU']
dateRN = []
wordL2rus = []
wordL3rus = []
wordL2eng = []
wordL3eng = []
wordsRus = []
wordsEng = []
countWords = 100

#Не убирал всё в функции думаю, что буду менять алгоритмы для разных языков
while date < today:
    dateRN.append(str(date))
    date += datetime.timedelta(days=1)
    
for i in range(len(alphRus[0])):
    for j in range(len(alphRus[1])):
        wordL2rus.append(alphRus[0][i] + alphRus[1][j])
for i in range(len(wordL2rus)):
    for j in range(len(alphRus[1]) + len(alphRus[0]) - 2):
        if (j >= len(alphRus[1])):
            wordL3rus.append(wordL2rus[i] + alphRus[0][j-len(alphRus[1])])
        else:
            wordL3rus.append(wordL2rus[i] + alphRus[1][j])
for i in range(len(alphEng[0])):
    for j in range(len(alphEng[1])):
        wordL2eng.append(alphEng[0][i] + alphEng[1][j])
for i in range(len(wordL2eng)):
    for j in range(len(alphEng[1]) + len(alphEng[0]) - 2):
        if (j >= len(alphEng[1])):
            wordL3eng.append(wordL2eng[i] + alphEng[0][j-len(alphEng[1])])
        else:
            wordL3eng.append(wordL2eng[i] + alphEng[1][j])
for i in range(countWords):
    wordsRus.append([0]*2)
    wordsEng.append([0]*2)
    if (i%3 == 0):
        wordsRus[i][0] = wordL2rus[rn.randint(0, len(wordL2rus)-1)] + wordL3rus[rn.randint(0, len(wordL3rus)-1)]
        wordsEng[i][0] = wordL2eng[rn.randint(0, len(wordL2eng)-1)] + wordL3eng[rn.randint(0, len(wordL3eng)-1)]
    elif (i%3 == 1):
        wordsRus[i][0] = wordL3rus[rn.randint(0, len(wordL3rus)-1)] + wordL3rus[rn.randint(0, len(wordL3rus)-1)]
        wordsEng[i][0] = wordL3eng[rn.randint(0, len(wordL3eng)-1)] + wordL3eng[rn.randint(0, len(wordL3eng)-1)]
    elif (i%3 == 2):
        wordsRus[i][0] = wordL3rus[rn.randint(0, len(wordL3rus)-1)] + wordL2rus[rn.randint(0, len(wordL2rus)-1)] + wordL2rus[rn.randint(0, len(wordL2rus)-1)]
        wordsEng[i][0] = wordL3eng[rn.randint(0, len(wordL3eng)-1)] + wordL2eng[rn.randint(0, len(wordL2eng)-1)] + wordL2eng[rn.randint(0, len(wordL2eng)-1)]
    wordsRus[i][1] = wordsRus[i][0][0] + wordsRus[i][0][rn.randint(1, len(wordsRus[i][0]) - 1)]
    wordsEng[i][1] = wordsEng[i][0][0] + wordsEng[i][0][rn.randint(1, len(wordsEng[i][0]) - 1)]
    wordsRus[i][0] = wordsRus[i][0].title()
    wordsRus[i][0] = wordsRus[i][0].title()

alphRus = alphRus[0] + alphRus[1]
alphEng = alphEng[0] + alphEng[1]