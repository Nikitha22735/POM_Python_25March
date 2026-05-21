import sqlite3

def sqLite(quer):
    dataTable = sqlite3.connect("C:\\Users\\Nikitha\\AppData\\Roaming\\DBeaverData\\workspace6\\.metadata\\sample-database-sqlite-1\\Chinook.db")
    curs = dataTable.cursor()
    curs.execute(quer)
    data = curs.fetchall()
    # print(curs.description)
    # print(curs.fetchall())
    # print(curs.fetchone())
    # print(curs.fetchmany(5))
    # print(data.rowcount())

    ###headers
    l1 = []
    headers = curs.description
    for i in curs.description:
        l1.append(i[0])
    # print(len(data))
    # # print(data)
    # curs.close()
    # dataTable.close()
    return data


# ===========================================================================================


# qe = "selct amount from db"
def test_ba():
    bala = sqLite("SELECT * from Artist where Artist.ArtistId is 8")
    usrname = bala[0][0]
    pw = bala[0][1]



# ===========================================================================================
##MYSQL
### pip install mysql-connector-python

# import mysql.connector

# def mysqLite(quer):
#     dataTable = mysql.connector.connect(host="hostdata",database="data",username="us",password="pw")
#     curs = dataTable.cursor()
#     curs.execute(quer)
#     data = curs.fetchall()





# ===========================================================================================
##postgress
## pip install psycopg2-binary

# import psycopg2

# def mysqLite(quer):
#     dataTable = psycopg2.connect(host="hostdata",database="data",username="us",password="pw",port="5432")
#     curs = dataTable.cursor()
#     curs.execute(quer)
#     data = curs.fetchall()




# ===========================================================================================
##snowflake
## pip install snowflake-connector-python
# import snowflake.connector


# def snowflake(quer):
#     dataTable = snowflake.connector.connect(host="hostdata",warehouwe="",schema="",database="data",username="us",password="pw",port="5432")
#     curs = dataTable.cursor()
#     curs.execute(quer)
#     data = curs.fetchall()






    
