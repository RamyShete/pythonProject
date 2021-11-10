# import paramiko
import shutil
import MySQLdb
from datetime import datetime


def copy_file():
    print('Введите имя файла, которое хотите скопировать начиная со \\:')
    name = input()
    shutil.copyfile(sftp_remote_dir + name, local_dir + name)
    current_datetime = datetime.now()
    name1 = name[1:]
    in_sql(name1, current_datetime)


def in_sql(name_f, current_datetime_f):
    query = """ INSERT INTO sftp.num1 VALUES (%s,%s);"""
    in_table = (current_datetime_f, name_f)
    try:
        con = MySQLdb.connect(sftp_host, sql_user, sql_password, sql_database)
        cur = con.cursor()
        cur.execute(query,in_table)
        con.commit()
    finally:
        cur.close()
        con.close()


def print_sql():
    con = MySQLdb.connect(sftp_host, sql_user, sql_password, sql_database)
    cur = con.cursor()
    cur.execute("SELECT * FROM sftp.num1")
    for row in cur.fetchall():
        print(row)
    con.close()


if __name__ == '__main__':
    print("Введите путь к файлу настроек")
    path = input()
    file = open(path, 'r')
    data = file.read()
    mass = data.split('\n')

    sftp_host = mass[0]
    sftp_port = mass[1]
    sftp_user = mass[2]
    sftp_password = mass[3]
    sftp_remote_dir = mass[4]
    local_dir = mass[5]
    sql_user = mass[6]
    sql_password = mass[7]
    sql_database = mass[8]

    # a = (sftp_host, int(sftp_port))
    # print(type(a))
    # transport = paramiko.Transport(a)
    # transport.connect(sftp_user, sftp_password)
    # sftp = paramiko.SFTPClient.from_transport(transport)
    # sftp.get(sftp_remote_dir, local_dir)
    # #sftp.put(local_dir, sftp_remote_dir)
    # sftp.close()
    # transport.close()

    while True:
        print('\nВыберете пункт меню:\n 1.Скопировать файл и записать результат в БД\n 2.Вывести таблицу БД\n 3.Выход')
        num_variant = input()
        if num_variant == '1':
            copy_file()
        elif num_variant == '2':
            print_sql()
        else:
            print('Конец выполнения')
            break
