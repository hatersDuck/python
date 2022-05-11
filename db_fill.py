import db_create_delete as db_cr
import db_class as dCls
import random as rn
import generator as gen

tables = []
"""0 - APUS_PLAN \n
1 - CONTRACT \n
2 - DEPT \n
3 - HOUSES \n
4 - OTHER_SVC \n
5 - PAYMENTS \n
6 - SALDO \n
7 - SERVICES \n
8 - STREETS_REF \n
9 - SVC_REF \n
10 - SVC_UNITS_REF \n
11 - TARIFED_SERVICES \n
12 - TAX_TARIF_REF \n
13 - TERRITORY_CONSTITUTE \n
14 - TERRITORY_TYPE \n
15 - TOWN \n
16 - T_TOWN_TYPE \n
17 - USERS \n
18 - USER_TYPE_REF \n"""

for i,tab in enumerate(db_cr.create_tables):
    tables.append(tab[15:tab.find('"', 15)])
for i in range(len(tables)):
    tables[i] = dCls.db_class(tables[i])

language = True
if (not language):
    gen.alphRus = gen.alphEng
    gen.wordsRus = gen.wordsEng
cnt_row = 50

for i in range(cnt_row):
    tempRu = rn.randint(0, len(gen.wordsRus) - 1)
    tables[0].addAll
    (   
    i+1,
    gen.wordsRus[tempRu][1],
    rn.randint(1,cnt_row),
    rn.randint(1,cnt_row),
    str(rn.randint(0,1)),
    gen.wordsRus[tempRu][0]
    )
    tables[1].addAll
    (   
    i+1,
    rn.randint(1,cnt_row),
    gen.alphRus[rn.randint(0, len(gen.alphRus) - 1)] + str(rn.randint(10**8, 10**9-1)),
    gen.dateRN[rn.randint(0,int(len(gen.dateRN)/2)-1)],
    gen.dateRN[rn.randint(int(len(gen.dateRN)/2), len(gen.dateRN)-1)],
    rn.randint(1,cnt_row),
    rn.randint(10**16, 10**17-1),
    rn.randint(1,cnt_row),
    ('кв.' if (language) else 'r.') + str(rn.randint(1,300))
    )
    tempRu = rn.randint(0, len(gen.wordsRus) - 1)
    tables[2].addAll
    (  
    i+1,
    gen.wordsRus[tempRu][1],
    rn.randint(1,cnt_row),
    rn.randint(cnt_row,100 + cnt_row),
    gen.wordsRus[tempRu][0],
    f'#{rn.randint(10**4, 10**5-1)}'
    )
    note = ['Многокваритрный', 'Частный', "Общежитие"] if (language) else ['Skyscraper','Penthouse','Tower block','Palace']
    letters = 'aб' if (language) else 'ab'
    tables[3].addAll
    (   
    i+1,
    rn.randint(1,cnt_row),
    f'№{rn.randint(1,100)}',
    gen.alphRus[rn.randint(0, len(gen.alphRus) - 1)],
    note[rn.randint(0, len(note)-1)],
    letters[rn.randint(0,1)],
    str(rn.randint(1,10**5))
    )
    tempSum = rn.randint(300,1000)

    tables[4].addAll
    (   
    i+1,
    rn.randint(1,cnt_row),
    rn.randint(1,cnt_row),
    rn.randint(1,cnt_row),
    rn.randint(1,cnt_row),
    rn.randint(1,cnt_row),
    gen.alphRus[rn.randint(0,len(gen.alphRus) - 1)] + str(rn.randint(10**6, 10**7 - 1)),
    f'+7({rn.randint(900,999)})-{rn.randint(100,999)}-{rn.randint(10,99)}-{rn.randint(10,99)}',
    rn.randint(1,100),
    tempSum,
    int(tempSum*0.2),
    int(tempSum*1.2),
    gen.dateRN[rn.randint(0,len(gen.dateRN)-1)], #date
    gen.alphRus[rn.randint(0,10)] + str(rn.randint(10**4, 10**5-1))
    )
    tables[5].addAll
    (   
    i+1,
    rn.randint(1,cnt_row),
    rn.randint(1,cnt_row),
    rn.randint(1,cnt_row),
    rn.randint(500,1000),
    gen.alphRus[rn.randint(0,len(gen.alphRus) - 1)] + str(rn.randint(10**6, 10**7 - 1)),
    f'+7({rn.randint(900,999)})-{rn.randint(100,999)}-{rn.randint(10,99)}-{rn.randint(10,99)}',
    gen.alphRus[rn.randint(0,10)] + str(rn.randint(10**4, 10**5-1)),
    gen.dateRN[rn.randint(0,int(len(gen.dateRN)/2)-1)],
    gen.dateRN[rn.randint(int(len(gen.dateRN)/2), len(gen.dateRN)-1)]
    )
    tables[6].addAll
    (  
    i+1,
    rn.randint(1,cnt_row),
    rn.randint(0,10000),
    rn.randint(1,cnt_row),
    rn.randint(1,cnt_row)
    )
    tables[7].addAll
    (   
    i+1,
    rn.randint(1,cnt_row),
    rn.randint(10**5,10**6 - 1),
    rn.randint(1,cnt_row),
    rn.randint(1,cnt_row),
    rn.randint(1,100),
    f'+7({rn.randint(900,999)})-{rn.randint(100,999)}-{rn.randint(10,99)}-{rn.randint(10,99)}',
    gen.dateRN[rn.randint(0,int(len(gen.dateRN)/2)-1)],
    gen.dateRN[rn.randint(int(len(gen.dateRN)/2), len(gen.dateRN)-1)], #date
    ('кв.' if (language) else 'r.') + str(rn.randint(1,300)),
    gen.dateRN[-1], #date
    'YN'[rn.randint(0,1)],
    rn.randint(1,cnt_row),
    rn.randint(1,cnt_row)
    )
    tables[8].addAll
    (   
    i+1,
    rn.randint(1,cnt_row),
    gen.wordsRus[rn.randint(0, len(gen.wordsRus) - 1)][0],
    rn.randint(1,cnt_row)
    )

    tempRu = rn.randint(0, len(gen.wordsRus) - 1)
    tables[9].addAll
    (   
    i+1,
    rn.randint(1,cnt_row),
    rn.randint(1,cnt_row),
    gen.wordsRus[tempRu][1],
    'YN'[rn.randint(0,1)],
    str(rn.randint(0,1)),
    str(rn.randint(i+1*10000, 10**4-1)),
    gen.wordsRus[tempRu][0],
    rn.randint(1,cnt_row),
    ['PHONE','NGN', 'NGN_SVC', 'PHONE_CVC', 'FREE_CVC', 'OTHER_SVC', 'FREE_NGN'][rn.randint(0,6)],
    'KPSRTX'[rn.randint(0,5)],
    rn.randint(1,cnt_row)
    )
    tempRu = rn.randint(0, len(gen.wordsRus) - 1)
    tables[10].addAll
    ( 
    i+1,
    str(tempRu),
    gen.wordsRus[tempRu][0],
    gen.wordsRus[tempRu][1]
    )
    summ = rn.randint(500,1000)
    sumSt = rn.randint(500,1000)
    tables[11].addAll
    (  
    i+1,
    rn.randint(1,cnt_row),
    rn.randint(1,cnt_row),
    rn.randint(1,cnt_row),
    rn.randint(1,cnt_row),
    summ,
    int(summ*(rn.randint(0,20)/100)),
    rn.randint(1,100),
    sumSt,
    int(summ + summ*(rn.randint(0,20)/100) + sumSt*0.2),
    int(sumSt*0.2)
    )
    tables[12].addAll
    ( 
    i+1,
    rn.randint(1,cnt_row),
    gen.dateRN[rn.randint(0,int(len(gen.dateRN)/2)-1)], #date
    rn.randint(0,20),
    'YN'[rn.randint(0,1)],
    gen.dateRN[rn.randint(int(len(gen.dateRN)/2), len(gen.dateRN)-1)] #date
    )
    tables[13].addAll
    (  
    i+1,
    int(),
    str(),
    int()
    )
    tables[14].addAll
    (  
    i+1,
    str(),
    str()
    )
    tables[15].addAll
    ( 
    i+1,
    str(),
    int(),
    int(),
    int()
    )
    tables[16].addAll
    ( 
    i+1,
    str(),
    str(),
    int()
    )
    tables[17].addAll
    ( 
    i+1,
    int(),
    int(),
    int(),
    int(),
    str(),
    str(),
    str(),
    str(), #date
    str(), #date
    str(),
    str(),
    str(),
    str(),
    str(),
    str(),
    str(),
    str(),
    int(),
    int()
    )
    tables[18].addAll
    (  
    i+1,
    str(),
    str(),
    int()
    )
