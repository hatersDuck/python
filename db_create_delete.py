from colorama import Cursor
import db_class

create_tables = ["""
CREATE TABLE "APUS_PLAN"
(   ID_PLAN INTEGER PRIMARY KEY AUTOINCREMENT,
    NAME VARCHAR,
    SVC_ID INTEGER,
    C_SVC_ID INTEGER,
    IS_FIX_SUMM VARCHAR,
    FULLNAME VARCHAR
);
""","""
CREATE TABLE "CONTRACT"
( 
    CONTRACT_ID INTEGER PRIMARY KEY AUTOINCREMENT,
    USER_ID INTEGER,
    NMB VARCHAR,
    DATEBEGIN DATE,
    DATEEND DATE,
    DEPT_ID INTEGER,
    REQ_ID INTEGER,
    HOUSE_ID INTEGER,
    FLAT VARCHAR
);
""","""
CREATE TABLE "DEPT"
( 
    DEPT_ID INTEGER PRIMARY KEY AUTOINCREMENT,
    NAME VARCHAR,
    DEPT_MANAGES INTEGER,
    MAIN_DEPT INTEGER,
    FULL_NAME VARCHAR,
    FILIAL_GOD VARCHAR
);
""","""
CREATE TABLE "HOUSES"
( 
    HOUSE_ID INTEGER PRIMARY KEY AUTOINCREMENT,
    STREET_ID INTEGER,
    HOUSE VARCHAR,
    CORPUS VARCHAR,
    NOTE VARCHAR,
    LETTER VARCHAR,
    BUILDING VARCHAR 
);
""","""
CREATE TABLE "OTHER_SVC"
( 
    OTH_SVC_ID INTEGER PRIMARY KEY AUTOINCREMENT,
    PAYMENT_ID INTEGER,
    BILLING_ID INTEGER,
    DEPT_ID INTEGER,
    SVC_ID INTEGER,
    USER_ID INTEGER,
    ACCOUNT VARCHAR,
    PHONE VARCHAR,
    SVC_NMB INTEGER,
    SUMM INTEGER,
    TAX INTEGER,
    OPERSUMM INTEGER,
    SVC_DATE DATE,
    DOC_NUM VARCHAR
);
""","""
CREATE TABLE "PAYMENTS"
( 
    PAYMENT_ID INTEGER PRIMARY KEY AUTOINCREMENT,
    USER_ID INTEGER,
    PAY_DOC_ID INTEGER,
    BILLING_ID INTEGER,
    SUMM INTEGER,
    ACCOUNT VARCHAR,
    PHONE VARCHAR,
    DOC_NUM VARCHAR,
    PAY_DATE DATE,
    DATE_REC DATE
);
""","""
CREATE TABLE "SALDO"
( 
    BILLING_ID INTEGER PRIMARY KEY AUTOINCREMENT,
    USER_ID INTEGER,
    SALDO INTEGER,
    USER_TYPE_ID INTEGER,
    DEPT_ID INTEGER
);
""","""
CREATE TABLE "SERVICES"
( 
    SERVICE_ID INTEGER PRIMARY KEY AUTOINCREMENT,
    DEPT_ID INTEGER,
    CONTRACT_TARIF INTEGER,
    SVC_ID INTEGER,
    USER_ID INTEGER,
    SVC_NMB INTEGER,
    PHONE VARCHAR,
    DATE_BEGIN DATE,
    DATE_END DATE,
    FLAT VARCHAR
    INSERT_DATE DATE,
    ISFREE VARCHAR,
    HOUSE_ID INTEGER,
    ID_PLAN INTEGER
);
""","""
CREATE TABLE "STREETS_REF"
( 
    STREET_ID INTEGER PRIMARY KEY AUTOINCREMENT,
    TOWN_ID INTEGER,
    NAME    VARCHAR,
    TYPE_STREET_ID INTEGER
);
""","""
CREATE TABLE "SVC_REF"
( 
    SVC_ID INTEGER PRIMARY KEY AUTOINCREMENT,
    DEPT_ID INTEGER,
    COD VARCHAR,
    NAME VARCHAR,
    ISCONST VARCHAR,
    SVCTYPE VARCHAR,
    FULL_COD VARCHAR,
    FULL_NAME VARCHAR,
    SELDOM_USED INTEGER,
    SERVICE_TYPE_ID VARCHAR,
    EQUIP_TYPE_ID VARCHAR,
    SVCUNITS_ID INTEGER
);
""","""
CREATE TABLE "SVC_UNITS_REF"
( 
    SVCUNITS_ID INTEGER PRIMARY KEY AUTOINCREMENT,
    CODE VARCHAR,
    NAME VARCHAR,
    SHORT_NAME VARCHAR
);
""","""
CREATE TABLE "TARIFED_SERVICES"
( 
    PRIVILEGE_MAKER_ID INTEGER,
    USER_ID INTEGER,
    SVC_ID INTEGER,
    BILLING_ID INTEGER,
    SERVICE_ID INTEGER,
    SUMM INTEGER,
    TAX INTEGER,
    SVC_NMB INTEGER,
    PRICE INTEGER,
    EXACT_SUMM INTEGER
)
""","""
CREATE TABLE "TAX_TARIF_REF"
( 
    TAX_ID INTEGER PRIMARY KEY AUTOINCREMENT,
    USER_TYPE_ID INTEGER,
    DATE_BEGIN DATE,
    VALUE INTEGER,
    LTAXIN VARCHAR,
    DATE_END DATE
);
""","""
CREATE TABLE "TERRITORY_CONSTITUTE"
( 
    ID_TERRITORY INTEGER PRIMARY KEY AUTOINCREMENT,
    ID_TERRITORY_TYPE INTEGER,
    NAME_TERR VARCHAR,
    ID_PARENT_TERRITORY INTEGER
);
""","""
CREATE TABLE "TERRITORY_TYPE"
( 
    ID_TERRITORY_TYPE INTEGER PRIMARY KEY AUTOINCREMENT,
    NAME VARCHAR,
    SHORTNAME VARCHAR
);
""","""
CREATE TABLE "TOWN"
( 
    TOWN_ID INTEGER PRIMARY KEY AUTOINCREMENT,
    NAME VARCHAR,
    TYPE_TOWN_ID INTEGER,
    ID_TERRITORY INTEGER,
    TARIF_ZONE_ID INTEGER
);
""","""
CREATE TABLE "T_TOWN_TYPE"
( 
    TYPE_TOWN_ID INTEGER PRIMARY KEY AUTOINCREMENT,
    NAME VARCHAR,
    SHORTNAME VARCHAR,
    IS_CITY INTEGER
);
""","""
CREATE TABLE "USERS"
( 
    USER_ID INTEGER PRIMARY KEY AUTOINCREMENT,
    BANK_DEPT_ID INTEGER,
    DEPT_ID INTEGER,
    OKONX_ID INTEGER,
    USER_TYPE_ID INTEGER,
    ACCOUNT VARCHAR,
    NAME VARCHAR,
    INN VARCHAR,
    DATE_BEGIN DATE,
    DATE_END DATE,
    FLAT VARCHAR,
    ISCORP VARCHAR,
    COMMENTARY VARCHAR,
    BANK_ACCOUNT VARCHAR,
    OKPO VARCHAR,
    J_PHONE VARCHAR,
    F_PHONE VARCHAR,
    DOCUMENT_TEXT VARCHAR,
    HOUSE_ID INTEGER,
    CHIEF_USER_ID INTEGER
);
""","""
CREATE TABLE "USER_TYPE_REF"
( 
    USER_TYPE_ID INTEGER PRIMARY KEY AUTOINCREMENT,
    NAME VARCHAR,
    ISCORP VARCHAR,
    COEF INTEGER
);
"""
]
def create():
    for exec in create_tables:
        db_class.cursor.execute(exec)
        db_class.db_connect.commit()

def delete():
    for table in db_class.cursor.execute("PRAGMA table_list;").fetchall():
        try:
            db_class.cursor.execute(f"DROP TABLE {table[1]};")
            db_class.db_connect.commit()
        except:
            pass

delete()
create()