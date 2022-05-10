
import sqlite3

db_connect = sqlite3.connect('bdRS.db')
cursor = db_connect.cursor()


class db_class(object):
    def __init__(self, nameTable:str):
        self.__nameTable = nameTable
        self.__atribute = []
        for atr in cursor.execute(f"PRAGMA table_info({self.__nameTable});").fetchall():
            self.__atribute.append([0]*2)
            self.__atribute[atr[0]][0] = atr[1]
            self.__atribute[atr[0]][1] = self.__checkType(atr=atr[2])

    def __checkType (self, atr):
        if (atr == 'INTEGER'):
            return 1
        elif (atr == 'VARCHAR'):
            return 'str'
        elif (atr == 'DATE'):
            return 'date'

    def addAll(self, *atr):
        if (len(atr) > len(self.__atribute)):
            print(f'Слишком много аргументов ({self.__nameTable})')
        else:
            exec = f'INSERT INTO {self.__nameTable} VALUES('
            for i,a in enumerate(atr):
                if (isinstance(a, type(self.__atribute[i][1]))):
                    if (isinstance(a, str)):
                        exec += f"'{a}',"
                    else:
                        exec += str(a) + ','
                else:
                    print(f'Failed type -> {a = }, need {self.__atribute[i][1]}, \ttable {self.__nameTable}')
            exec = exec[:len(exec)-1] + ');'
            cursor.execute(exec)
            db_connect.commit()
