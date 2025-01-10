import mysql.connector as msc
from config import *


"------------------------------------------------------------------------------------------------------------------------------------"
"customer"

def Insert_in_customer(Name , Phone):
    conn = msc.connect(**config)
    curs = conn.cursor()
    SQL_Quary = """insert ignore into customer (name , phone) values (%s , %s)"""
    curs.execute(SQL_Quary , (Name , Phone))
    conn.commit()
    curs.close()
    conn.close()    
    print(f'Inserted!(customer)')


"------------------------------------------------------------------------------------------------------------------------------------"
"vehicle"

def Insert_to_vehicle(Model_vehicle , class_vehicle , company_name , plane_name , sarneshinan):
    conn = msc.connect(**config)
    curs = conn.cursor()
    SQL_Quary = """insert ignore into vehicle (Model_vehicle , class_vehicle , company_name , plane_name , sarneshinan) values (%s , %s , %s , %s , %s)"""
    curs.execute(SQL_Quary , (Model_vehicle , class_vehicle , company_name , plane_name , sarneshinan))
    conn.commit()
    curs.close()
    conn.close()    
    print(f'Inserted!(vehicle)')


"------------------------------------------------------------------------------------------------------------------------------------"
"station"

def Insert_to_station(bg_STATION , des_station):
    conn = msc.connect(**config)
    curs = conn.cursor()
    SQL_Quary = """insert into station (bg_STATION , des_station , tavaghof) values (%s , %s)"""
    curs.execute(SQL_Quary , (bg_STATION , des_station))
    conn.commit()
    curs.close()
    conn.close()    
    print(f'Inserted!(station)')


"------------------------------------------------------------------------------------------------------------------------------------"
"ticket"


def Insert_to_ticket(Name , model_vehicle):
    conn = msc.connect(**config)
    curs = conn.cursor()
    SQL_Quary = """insert into ticket (Name , model_vehicle , Tavaghof) values (%s , %s)"""
    curs.execute(SQL_Quary , (Name , model_vehicle))
    conn.commit()
    curs.close()
    conn.close()    
    print(f'Inserted!(ticket)')


"------------------------------------------------------------------------------------------------------------------------------------"
"At the END..."

if __name__ == '__main__':
    pass
#     Insert_in_customer('Amir' , '0912345678' )
#     Get_from_customer()
#     Insert_to_vehicle('bus' , 'A1' , 'A2' , 12.5 , 'vip')
#     Get_from_vehicle()
#     Insert_to_ticket('AliIsEPIC1' , 'bus' , 'cash')
#     Get_from_ticket()
#     print('End')