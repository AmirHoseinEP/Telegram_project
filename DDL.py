import mysql.connector as msc
import config
from DML import *


try :
    def Create_Database_amirhosein_ticket():
        conn = msc.connect(user = 'root' , password = 'password' , host = 'localhost')
        curs = conn.cursor()
        curs.execute(f"drop database if exists amirhosein_ticket")
        SQL_Quary = f"CREATE DATABASE if not exists amirhosein_ticket"
        curs.execute(SQL_Quary)
        conn.commit()
        curs.close()
        conn.close()
        print(f'Data base amirhosein_ticket created')


    def Create_Table_Customer():
        conn = msc.connect(user = 'root' , password = 'password' , host = 'localhost' , database = 'amirhosein_ticket')
        curs = conn.cursor()
        SQL_Quary = """Create table customer (
            cid              bigint not null primary key,
            name             varchar(50) not null,
            last_name        varchar(50) not null ,
            phone            varchar(11) not null unique,
            Register_date    datetime default current_timestamp,
            Last_update      datetime default current_timestamp on update current_timestamp
        )"""
        curs.execute(SQL_Quary)
        conn.commit()
        curs.close()
        conn.close()    
        print(f'Table customer created')




    def Create_Table_vehicle():
        conn = msc.connect(user = 'root' , password = 'password' , host = 'localhost' , database = 'amirhosein_ticket')
        curs = conn.cursor()
        SQL_Quary = """create table vehicle (
            id                      bigint not null auto_increment primary key,
            Model_vehicle           varchar(10),
            class_vehicle           varchar(20),
            company_name            varchar(20),
            plane_name              varchar(50),
            sarneshinan             smallint,
            last_update             datetime default current_timestamp on update current_timestamp
        );"""
        curs.execute(SQL_Quary)
        conn.commit()
        curs.close()
        conn.close()
        print(f'table vehicle created')


    def Create_Table_ticket():
        conn = msc.connect(user = 'root' , password = 'password' , host = 'localhost' , database = 'amirhosein_ticket')
        curs = conn.cursor()
        SQL_Quary = """create table ticket (
            cid                   bigint not null primary key,
            date                 datetime default current_timestamp,
            foreign key (cid) references vehicle (id),
            foreign key (cid) references customer (cid)
        )"""
        curs.execute(SQL_Quary)
        conn.commit()
        curs.close()
        conn.close()
        print(f'table ticket created')


    if __name__=='__main__':
        Create_Database_amirhosein_ticket()
        Create_Table_Customer()
        Create_Table_vehicle()
        Create_Table_ticket()
        print('End')
    
    Insert_to_vehicle('plane' , 'vip' , 'mahan' , 'Boeing 747' , 250)
    Insert_to_vehicle('plane' , 'economy' , 'Iran air' , 'Boeing 747' , 450)
    
except Exception as e:
    print(f'Error{e}')