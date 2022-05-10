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

language = 'ru'

for i in range(50):
    tables[0].addAll
    (   
    i+1,
    str(),
    int(),
    int(),
    str(),
    str()
    )
    tables[1].addAll
    (   
    i+1,
    int(),
    str(),
    str(), #date
    str(), #date
    int(),
    int(),
    int(),
    str()
    )
    tables[2].addAll
    (  
    i+1,
    str(),
    int(),
    int(),
    str(),
    str()
    )
    tables[3].addAll
    (   
    i+1,
    int(),
    str(),
    str(),
    str(),
    str(),
    str()
    )
    tables[4].addAll
    (   
    i+1,
    int(),
    int(),
    int(),
    int(),
    int(),
    str(),
    str(),
    int(),
    int(),
    int(),
    int(),
    str(), #date
    str()
    )
    tables[5].addAll
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
    str() #date
    )
    tables[6].addAll
    (  
    i+1,
    int(),
    int(),
    int(),
    int()
    )
    tables[7].addAll
    (   
    i+1,
    int(),
    int(),
    int(),
    int(),
    int(),
    str(),
    str(), #date
    str(), #date
    str(),
    str(), #date
    str(),
    int(),
    int()
    )
    tables[8].addAll
    (   
    i+1,
    int(),
    str(),
    int()
    )
    tables[9].addAll
    (   
    i+1,
    int(),
    str(),
    str(),
    str(),
    str(),
    str(),
    str(),
    int(),
    str(),
    str(),
    int()
    )
    tables[10].addAll
    ( 
    i+1,
    str(),
    str(),
    str()
    )
    tables[11].addAll
    (  
    i+1,
    int(),
    int(),
    int(),
    int(),
    int(),
    int(),
    int(),
    int(),
    int(),
    int()
    )
    tables[12].addAll
    ( 
    i+1,
    int(),
    str(), #date
    int(),
    str(),
    str() #date
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
