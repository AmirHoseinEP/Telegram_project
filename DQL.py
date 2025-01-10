import mysql.connector
import config

info_dict = dict()


def delete_fly(id):
    conn = mysql.connector.connect(**config.config)
    curs = conn.cursor(dictionary=True)
    SQL_Quary = "delete from vehicle where id = %s"
    curs.execute(SQL_Quary , (id,))
    SQL_Quary = """delete (Model_vehicle , Class_vehicle , company_name , plane_name , sarneshinan) from ticket """
    conn.commit()
    curs.close()
    conn.close()
    print('deleted')


def Edit_fly(am, col , Id ):
    my_Database = ['Model_vehicle' , 'class_vehicle' , 'company_name' , 'plane_name' , 'sarneshinan']
    conn = mysql.connector.connect(**config.config)
    curs = conn.cursor(dictionary=True)
    if col.startswith('M'):
        conn = mysql.connector.connect(**config.config)
        curs = conn.cursor(dictionary=True)
        SQL_Quary = """update vehicle set Model_vehicle = %s where id = %s"""
        curs.execute(SQL_Quary , (am , Id))
        conn.commit()
        curs.close()
        conn.close()
    if col.startswith('C'):
        conn = mysql.connector.connect(**config.config)
        curs = conn.cursor(dictionary=True)
        SQL_Quary = """update vehicle set class_vehicle = %s where id = %s"""
        curs.execute(SQL_Quary , (am , Id))
        conn.commit()
        curs.close()
        conn.close()
    if col.startswith('c'):
        conn = mysql.connector.connect(**config.config)
        curs = conn.cursor(dictionary=True)
        SQL_Quary = """update vehicle set company_name = %s where id = %s"""
        curs.execute(SQL_Quary , (am , Id))
        conn.commit()
        curs.close()
        conn.close()
    if col.startswith('p'):
        conn = mysql.connector.connect(**config.config)
        curs = conn.cursor(dictionary=True)
        SQL_Quary = """update vehicle set plane_name = %s where id = %s"""
        curs.execute(SQL_Quary , (am , Id))
        conn.commit()
        curs.close()
        conn.close()
    if col.startswith('s'):
        conn = mysql.connector.connect(**config.config)
        curs = conn.cursor(dictionary=True)
        SQL_Quary = """UPDATE vehicle SET sarneshinan = %s WHERE id = %s"""
        curs.execute(SQL_Quary , (int(am) , Id))
        conn.commit()
        print('edited')
        curs.close()
        conn.close()


def get_from_vehicle(x , y , z):
    lst_Id = [1 , 2 , 3]
    conn = mysql.connector.connect(**config.config)
    curs = conn.cursor(dictionary=True)
    if x == 'yes':
        SQL_Quary = """select * from vehicle"""
        curs.execute(SQL_Quary)
        dic1 = curs.fetchall()
        conn.commit()
        ID , M , C , CC , P , S = dic1[y].get('id') , dic1[y].get('Model_vehicle') , dic1[y].get('class_vehicle') , dic1[y].get('company_name') , dic1[y].get('plane_name') , dic1[y].get('sarneshinan')
        info_dict[ID] = {'model_vehicle' : M , 'class_vehicle' : C , 'company_name' : CC , 'plane_name' : P , 'sarneshinan' : S}
        return info_dict.get(z)

    elif x == 'no':
        SQL_Quary = """select id from vehicle"""
        curs.execute(SQL_Quary)
        lst = curs.fetchall()
        lst_2 = []
        for i in lst :
            lst_2.append(i.get('id'))
        conn.commit()
        return lst_2
    curs.close()
    conn.close()
    



def insert_into_customer(cid , name , lname , phone):
    conn = mysql.connector.connect(**config.config)
    curs = conn.cursor(dictionary=True)
    SQL_Quary = """insert into customer (cid , name , last_name , phone) values (%s , %s , %s , %s)"""
    curs.execute(SQL_Quary , (cid , name , lname , phone))
    conn.commit()
    curs.close()
    conn.close()
    print('inserted')



def get_id_from_vehicle():
    conn = mysql.connector.connect(**config.config)
    curs = conn.cursor(dictionary=True)
    SQL_Quary = """select * from customer"""
    curs.execute(SQL_Quary)
    conn.commit()
    curs.close()
    conn.close()
    return True



def get_from_customer(cid):
    conn = mysql.connector.connect(**config.config)
    curs = conn.cursor(dictionary=True)
    SQL_Quary = """select * from customer where cid = %s"""
    curs.execute(SQL_Quary , (cid,))
    lst_info = curs.fetchall()
    if not lst_info :
        return 'er'
    conn.commit()
    curs.close()
    conn.close()
    lst_final = lst_info[0]
    Cid = lst_final.get('cid')
    name = lst_final.get('name')
    last_name = lst_final.get('last_name')
    phone = lst_final.get('phone')
    return f"cid : {cid} \nname : {name} \nlast name : {last_name} \nphone : {phone} \nbuy a ticket : /buy"



def delete_from_customer(cid):
    conn = mysql.connector.connect(**config.config)
    curs = conn.cursor(dictionary=True)
    SQL_Quary = """delete from customer where cid = %s"""
    curs.execute(SQL_Quary , (cid,))
    conn.commit()
    curs.close()
    conn.close()


def get_cid_from_customer(cid):
    conn = mysql.connector.connect(**config.config)
    curs = conn.cursor(dictionary=True)
    SQL_Quary = """select * from customer where cid = %s"""
    curs.execute(SQL_Quary , (cid,))
    conn.commit()
    lst_info = curs.fetchall()
    if not lst_info:
        return 'er'
    curs.close()
    conn.close()


if __name__ == "__main__":
    # print(get_from_customer(6728418988))
    # print(get_from_vehicle('yes' , y= 2))
    # print(get_id_from_vehicle())
    # print(Edit_fly())
    pass