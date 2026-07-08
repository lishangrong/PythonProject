"""
目的：告诉大家，原生的pymysql很复杂，大家掌握pandas 读写mysql即可
了解即可
"""
# 导包
import pymysql

# 1. 获取链接对象(Python --> MySQL)
conn = pymysql.connect(
    host='127.0.0.1',
    port=3306,
    user='root',
    password='123456',
    database='day01',
    charset='utf8'
)

# 2. 获取游标对象(MySQL --> Python)
cursor = conn.cursor()

# 3 定义sql语句
sql = "select name, AKA from my_table limit 0, 2;"

# 4. 执行sql语句
cursor.execute(sql)

# 5. 获取结果
result = cursor.fetchall()

# 6. 遍历结果集
for row in result:
    print(row)

# 7. 释放资源
cursor.close()
conn.close()

