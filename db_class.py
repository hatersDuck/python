
from curses.ascii import isdigit
import sqlite3

db_connect = sqlite3.connect('bdRS.db', check_same_thread = False)
cursor = db_connect.cursor()

class db_class(object):
    def __init__(self, nameTable:str):
        self.nameTable = nameTable
        self.atribute = []
        for atr in cursor.execute(f"PRAGMA table_info({self.nameTable});").fetchall():
            self.atribute.append([0]*2)
            self.atribute[atr[0]][0] = atr[1]
            self.atribute[atr[0]][1] = self.__checkType(atr=atr[2])
            self.countCol = atr[0] + 1
        self.countRows = 0

    def __checkType (self, atr):
        if (atr == 'INTEGER'):
            return 1
        elif (atr == 'VARCHAR'):
            return 'str'
        elif (atr == 'DATE'):
            return 'date'

    def addAll(self, *atr):
        if (len(atr) > len(self.atribute)):
            print(f'Слишком много аргументов ({self.nameTable}) ({len(atr) = } - {len(self.atribute)})')
        else:
            exec = f'INSERT INTO {self.nameTable} VALUES('
            for i,a in enumerate(atr):
                if (isinstance(a, type(self.atribute[i][1]))):
                    if (isinstance(a, str)):
                        exec += f"'{a}',"
                    else:
                        exec += str(a) + ','
                else:
                    print(f'Failed type -> {a =} {i =}, need {self.atribute[i][1]}, \ttable {self.nameTable}')
            exec = exec[:len(exec) - 1] + ');'

            cursor.execute(exec)
            self.countRows += 1
            db_connect.commit()

    def insertIntoText(self, txt:str):
        exec = f'INSERT INTO {self.nameTable} VALUES('
        temp = self.selectAll()[-1][0] + 1
        exec += str(temp) + ','
        atr = txt.split(',')
        for i,a in enumerate(atr):
            if (isinstance(a, str)):
                exec += f"'{a}',"
            else:
                exec += str(a) + ','
        exec = exec[:len(exec) - 1] + ');'

        cursor.execute(exec)
        self.countRows += 1
        db_connect.commit()

    def selectAll(self, where = None) -> list:
        try:
            exec = F'SELECT * FROM {self.nameTable}'
            if (where is not None):
                exec += ' WHERE ' + where + ';'
            cursor.execute(exec)
            return cursor.fetchall()
        except:
            return None

    def updateValues(self, column:list, where):
        exec = F'UPDATE {self.nameTable} SET '
        check = False
        for i in column:
            if (check):
                exec += ', '
            exec += f'{i[0]} = '
            if (isinstance(i[1], int)):
                exec += str(i[1])
            else:
                exec += f"'{i[1]}'"
            check = True
        exec += 'WHERE ' + where + ';'
        cursor.execute(exec)
        db_connect.commit()

    def deleteRow(self, where):
        exec = F'DELETE FROM {self.nameTable} WHERE {where};'
        cursor.execute(exec)
        db_connect.commit()