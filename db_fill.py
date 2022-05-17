import db_create_delete as db_cr
import db_class as dCls
import random as rn
import generator as gen

APUS_PLAN  = dCls.db_class('APUS_PLAN')
CONTRACT = dCls.db_class('CONTRACT')
DEPT = dCls.db_class('DEPT')
HOUSES = dCls.db_class('HOUSES')
OTHER_SVC = dCls.db_class('OTHER_SVC')
PAYMENTS = dCls.db_class('PAYMENTS')
SALDO = dCls.db_class('SALDO')
SERVICES = dCls.db_class('SERVICES')
STREETS_REF  = dCls.db_class('STREETS_REF')
SVC_REF = dCls.db_class('SVC_REF')
SVC_UNITS_REF = dCls.db_class('SVC_UNITS_REF')
TARIFED_SERVICES = dCls.db_class('TARIFED_SERVICES')
TAX_TARIF_REF = dCls.db_class('TAX_TARIF_REF')
TERRITORY_CONSTITUTE = dCls.db_class('TERRITORY_CONSTITUTE')
TERRITORY_TYPE = dCls.db_class('TERRITORY_TYPE')
TOWN = dCls.db_class('TOWN')
T_TOWN_TYPE = dCls.db_class('T_TOWN_TYPE')
USERS = dCls.db_class('USERS')
USER_TYPE_REF = dCls.db_class('USER_TYPE_REF')
tablesAll = {
    'APUS_PLAN': APUS_PLAN,
    'CONTRACT': CONTRACT,
    'DEPT': DEPT,
    'HOUSES': HOUSES,
    'OTHER_SVC': OTHER_SVC,
    'PAYMENTS': PAYMENTS,
    'SALDO': SALDO,
    'SERVICES': SERVICES,
    'STREETS_REF': STREETS_REF,
    'SVC_REF': SVC_REF,
    'SVC_UNITS_REF': SVC_UNITS_REF,
    'TARIFED_SERVICES': TARIFED_SERVICES,
    'TAX_TARIF_REF': TAX_TARIF_REF,
    'TERRITORY_CONSTITUTE': TERRITORY_CONSTITUTE,
    'TERRITORY_TYPE': TERRITORY_TYPE,
    'TOWN': TOWN,
    'T_TOWN_TYPE': T_TOWN_TYPE,
    'USERS': USERS,
    'USER_TYPE_REF': USER_TYPE_REF
}
language = False
if (not language):
    gen.alphRus = gen.alphEng
    gen.wordsRus = gen.wordsEng
cnt_row = 50

for i in range(cnt_row):
    PAYMENTS.addAll(   
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

    tempRu = rn.randint(0, len(gen.wordsRus) - 1)
    SVC_UNITS_REF.addAll( 
    i+1,
    str(tempRu),
    gen.wordsRus[tempRu][0],
    gen.wordsRus[tempRu][1]
    )

    tempRu = rn.randint(0, len(gen.wordsRus) - 1)
    TERRITORY_TYPE.addAll(  
    i+1,
    gen.wordsRus[tempRu][0],
    gen.wordsRus[tempRu][1]
    )

    tempRu = rn.randint(0, len(gen.wordsRus) - 1)
    T_TOWN_TYPE.addAll( 
    i+1,
    gen.wordsRus[tempRu][0],
    gen.wordsRus[tempRu][1],
    rn.randint(0, 1)
    )
    
    USER_TYPE_REF.addAll(  
    i+1,
    gen.wordsRus[rn.randint(0,len(gen.wordsRus) - 1)][0],
    'YN'[rn.randint(0,1)],
    rn.randint(0,1)
    )
    
for i in range(cnt_row):
    tempRu = rn.randint(0, len(gen.wordsRus) - 1)
    APUS_PLAN.addAll(   
    i+1,
    gen.wordsRus[tempRu][1],
    rn.randint(1,cnt_row),
    rn.randint(1,cnt_row),
    str(rn.randint(0,1)),
    gen.wordsRus[tempRu][0]
    )
    CONTRACT.addAll(   
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
    DEPT.addAll(  
    i+1,
    gen.wordsRus[tempRu][1],
    rn.randint(1,cnt_row),
    rn.randint(cnt_row,100 + cnt_row),
    gen.wordsRus[tempRu][0],
    f'#{rn.randint(10**4, 10**5-1)}'
    )
    note = ['Многокваритрный', 'Частный', "Общежитие"] if (language) else ['Skyscraper','Penthouse','Tower block','Palace']
    letters = 'aб' if (language) else 'ab'
    HOUSES.addAll(   
    i+1,
    rn.randint(1,cnt_row),
    f'№{rn.randint(1,100)}',
    gen.alphRus[rn.randint(0, len(gen.alphRus) - 1)],
    note[rn.randint(0, len(note)-1)],
    letters[rn.randint(0,1)],
    str(rn.randint(1,10**5))
    )
    tempSum = rn.randint(300,1000)

    OTHER_SVC.addAll(   
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
    SALDO.addAll(  
    i+1,
    rn.randint(1,cnt_row),
    rn.randint(0,10000),
    rn.randint(1,cnt_row),
    rn.randint(1,cnt_row)
    )
    SERVICES.addAll(   
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
    STREETS_REF.addAll(   
    i+1,
    rn.randint(1,cnt_row),
    gen.wordsRus[rn.randint(0, len(gen.wordsRus) - 1)][0],
    rn.randint(1,cnt_row)
    )

    tempRu = rn.randint(0, len(gen.wordsRus) - 1)
    SVC_REF.addAll(   
    i+1,
    rn.randint(1,cnt_row),
    str(rn.randint(1,cnt_row)),
    gen.wordsRus[tempRu][1],
    'YN'[rn.randint(0,1)],
    str(rn.randint(0,1)),
    str(rn.randint(10**3, 10**4-1)),
    gen.wordsRus[tempRu][0],
    rn.randint(1,cnt_row),
    ['PHONE','NGN', 'NGN_SVC', 'PHONE_CVC', 'FREE_CVC', 'OTHER_SVC', 'FREE_NGN'][rn.randint(0,6)],
    'KPSRTX'[rn.randint(0,5)],
    rn.randint(1,cnt_row)
    )
    summ = rn.randint(500,1000)
    sumSt = rn.randint(500,1000)
    TARIFED_SERVICES.addAll(  
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
    TAX_TARIF_REF.addAll( 
    i+1,
    rn.randint(1,cnt_row),
    gen.dateRN[rn.randint(0,int(len(gen.dateRN)/2)-1)], #date
    rn.randint(0,20),
    'YN'[rn.randint(0,1)],
    gen.dateRN[rn.randint(int(len(gen.dateRN)/2), len(gen.dateRN)-1)] #date
    )
    TERRITORY_CONSTITUTE.addAll(  
    i+1,
    rn.randint(1,cnt_row),
    gen.wordsRus[rn.randint(0, len(gen.wordsRus) - 1)][0],
    rn.randint(1,cnt_row)
    )
    tempRu = rn.randint(0, len(gen.wordsRus) - 1)
    TOWN.addAll( 
    i+1,
    gen.wordsRus[tempRu][0],
    rn.randint(1,cnt_row),
    rn.randint(1,cnt_row),
    rn.randint(1,cnt_row)
    )
    tempRu = rn.randint(0, len(gen.wordsRus) - 1)
    USERS.addAll( 
    i+1,
    rn.randint(1,cnt_row),
    rn.randint(1,cnt_row),
    rn.randint(1,cnt_row),
    rn.randint(1,cnt_row),
    str(gen.alphRus[rn.randint(0,len(gen.alphRus) - 1)] + str(rn.randint(10**6, 10**7 - 1)),),
    str(gen.wordsRus[tempRu][0]),
    str(rn.randint(10**12, 10**13 - 1)),
    gen.dateRN[rn.randint(0,int(len(gen.dateRN)/2)-1)],
    gen.dateRN[rn.randint(int(len(gen.dateRN)/2), len(gen.dateRN)-1)],
    ('кв.' if (language) else 'r.') + str(rn.randint(1,300)),
    'YN'[rn.randint(0,1)],
    gen.wordsRus[rn.randint(0, len(gen.wordsRus) - 1)][0] + gen.wordsRus[rn.randint(0, len(gen.wordsRus) - 1)][0] ,
    f'{rn.randint(10**4, 10**5-1)}-{rn.randint(10**4, 10**5-1)}-{rn.randint(10**4, 10**5-1)}-{rn.randint(10**4, 10**5-1)}',
    str(rn.randint(10**8, 10**9-1)),
    f'+7({rn.randint(900,999)})-{rn.randint(100,999)}-{rn.randint(10,99)}-{rn.randint(10,99)}',
    f'+7({rn.randint(900,999)})-{rn.randint(100,999)}-{rn.randint(10,99)}-{rn.randint(10,99)}',
    f'{rn.randint(10,99)} {rn.randint(10,99)} {rn.randint(10**6, 10**7-1)}',
    rn.randint(1,cnt_row),
    rn.randint(1,cnt_row)
    )
    
