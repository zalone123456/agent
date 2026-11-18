import os

import pymysql
from datetime import date

def main():
    DB_USER = os.environ.get("DB_USER")
    DB_PASSWORD = os.environ.get("DB_PASSWORD")
    if not DB_USER or not DB_PASSWORD:
        print("环境变量为空")
        return
    connecton=get_connection(DB_USER,DB_PASSWORD)
    if connecton is None:
        return
    else:
        try:
            while True:
                if Interface(connecton) == -1:
                    break
        finally:
            connecton.close()
def get_connection(DB_USER,DB_PASSWORD):
    try:
        connection = pymysql.connect(
            host='127.0.0.1',
            port=3306,
            user=DB_USER,
            password= DB_PASSWORD,
            database='learning_db',
            charset='utf8mb4'
        )
        return connection
    except pymysql.MySQLError as e:
        print(e)
    except OSError as e:
        print(e)
def select_data(connection,topic):
    my_cursor = connection.cursor()
    try:
        sql = "SELECT * FROM study_records WHERE topic = %s"
        my_cursor.execute(sql, (topic,))
        results = my_cursor.fetchall()
        return results
    except pymysql.MySQLError as e:
        print(e)
    except OSError as e:
        print(e)
    finally:
        my_cursor.close()
def list_records(connection):
    my_cursor = connection.cursor()
    try:
        sql = "SELECT * FROM study_records ORDER BY id"
        my_cursor.execute(sql)
        results = my_cursor.fetchall()
        return  results
    except pymysql.MySQLError as e:
        print(e)
    except OSError as e:
        print(e)
    finally:
        my_cursor.close()
def get_statistics(connection):
    my_cursor = connection.cursor()
    try:
        sql = "SELECT count(*),COALESCE(SUM(study_minutes), 0) FROM study_records"
        my_cursor.execute(sql)
        result_first=my_cursor.fetchone()
        sql = "SELECT topic,count(*),COALESCE(SUM(study_minutes), 0) FROM study_records group by topic"
        my_cursor.execute(sql)
        results = my_cursor.fetchall()
        return result_first, results
    except pymysql.MySQLError as e:
        print(e)
    except OSError as e:
        print(e)
    finally:
        my_cursor.close()
def add_record(connection,topic,study_minutes,study_date,notes):
    my_cursor = connection.cursor()
    try:
        sql = "INSERT INTO study_records(topic,study_minutes,study_date,notes) VALUES (%s,%s,%s,%s)"
        my_cursor.execute(sql, (topic,study_minutes,study_date,notes))
        record_id = my_cursor.lastrowid
        connection.commit()
        return record_id
    except pymysql.MySQLError as e:
        connection.rollback()
        print(e)
    except OSError as e:
        connection.rollback()
        print(e)
    finally:
        my_cursor.close()
def Interface(connecton):
    print("\n===== 学习记录管理系统 =====")
    print("1. 添加学习记录")
    print("2. 查看全部记录")
    print("3. 按主题查询")
    print("4. 查看统计结果")
    print("0. 退出程序")
    choice=input("请选择功能").strip()
    try:
        choice=int(choice)
    except ValueError as e:
        print(e)
        return
    except OSError as e:
        print(e)
        return
    match choice:
        case 1:
            try:
                # 输入并检查主题
                topic = input("请输入学习主题：").strip()
                if not topic:
                    print("学习主题不能为空")
                    return
                try:
                    study_minutes = int(input("请输入学习分钟数：").strip())
                    if study_minutes <= 0:
                        print("学习分钟数必须是正整数")
                        return
                except ValueError:
                    print("输入错误，请输入数字！")
                    return
                study_date_text = input("请输入学习日期（例如 2026-11-16）：").strip()

                try:
                    study_date = date.fromisoformat(study_date_text)
                    if study_date.isoformat() != study_date_text:
                        print("日期格式错误，请使用 YYYY-MM-DD")
                        return
                except ValueError:
                    print("日期无效，请使用 YYYY-MM-DD 格式")
                    return
                notes = input("请输入备注（可直接回车跳过）：").strip()
                if not notes:
                    notes = None
                id= add_record(connecton, topic, study_minutes, study_date, notes)
                if not id:
                    print("s失败")
                    return
                else:
                    print(f"添加成功，编号{id}")
            except OSError as e:
                print(e)
        case 2:
            a=list_records(connecton)
            if a is None:
                print("查询失败")
                return
            if not a:
                print('查询成功，但没有记录')
                return
            for i in a:
                print(i)
        case 3:
            topic = input("请输入学习主题：").strip()
            if not topic:
                print("学习主题不能为空")
                return
            a=select_data(connecton, topic)
            if a is None:
                print("查询失败")
                return
            if not a:
                print('查询成功，但没有记录')
                return
            for row in a:
                print(row)
        case 4:
            b=get_statistics(connecton)
            if b is None:
                print("查询失败")
                return
            a_first,a=b
            print(a_first)
            if not a:
                print('查询成功，但没有记录')
                return
            for row in a:
                print(row)

        case 0:
            return -1
        case _:
            print("选项错误，请重新输入选项")
            return
if __name__ == '__main__':
    main()
