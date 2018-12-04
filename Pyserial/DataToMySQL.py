#!/usr/bin/python3
# -*- coding: utf-8 -*-

import pymysql


def save_data(data_, type_, count):
    # MySQL数据库连接
    db = pymysql.connect('localhost', 'root', '123456', 'temp_col_sys', charset='utf8')

    # 获取游标
    cursor = db.cursor()

    # 事务处理
    try:
        print(123)
        print(type(count))
        if type_ == "save":
            cursor.execute("insert into save_data (data) value(%s);", data_)
        elif type_ == "insert_set":
            cursor.execute("insert into set_data (data) value(%s);", data_)
        elif type_ == "set":
            cursor.execute("select data from set_data where id = %s;", count)
            data_ = cursor.fetchone()
            print(data_)
            print(type(data_))

            return data_[0]

    except Exception as e:
        db.rollback()               # 事务回滚
        print('事务处理失败', e)

    else:
        print(456)
        db.commit()                 # 事务提交

    # cursor.execute(sql.create_employee_sql)

    cursor.close()                  # 游标关闭
    db.close()                      # 连接关闭


if __name__ == "__main__":
    data = save_data("sa", "set", 1)
    print(data)


