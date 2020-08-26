#/usr/bin/python
# -*- coding: UTF-8 -*-
import pymysql
# 创建连接
conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='root', db='db', charset='utf8')
#创建游标
cursor = conn.cursor()
cursor.execute("select * from ww_link")

# 获取剩余结果的第一行数据
# row_1 = cursor.fetchone()
# print row_1
# 获取剩余结果前n行数据
# row_2 = cursor.fetchmany(3)

# 获取剩余结果所有数据
row_3 = cursor.fetchall()
print row_3
conn.commit()
cursor.close()
conn.close()



