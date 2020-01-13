# 增

import pymysql


def connectDB():
    conn = pymysql.connect(
                host="localhost",
                port=3305, database="test",
                user="root",
                password="root",
                charset="utf8")
    return conn


def main():
    conn = connectDB()
    cursor = conn.cursor()
    cursor.execute("select * from tbt;")
    data = cursor.fetchone()
    print ("Database version : %s " %str(data))
    conn.close()

if __name__ == '__main__':
    main()
