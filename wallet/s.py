import pymysql

"""Add Your Sql Credintial"""

host = 'localhost'
db_user = 'root'
db_password = 'password'
database = 'testing'
table_name = 'table_test'


def get_data():
    item = [
        {
            'Product_url': 'soni'
        },
        {
            'Product_url': 'prathmesh'
        },
        {
            'Product_url': 'soni'
        },
        {
            'Product_url': 'soni'
        },
        {
            'Product_url': 'mksoni'
        },

    ]
    for i in item:
        insert_to_DB(i['Product_url'])

def connection():
    con = pymysql.connect(host=host, user=db_user, passwd=db_password, database=database)
    return con


def create_table():
    con = pymysql.connect(host=host, user=db_user, passwd=db_password)
    cur = con.cursor()

    cur.execute(f'CREATE DATABASE IF NOT EXISTS {database}')

    con1 = pymysql.connect(host=host, user=db_user, passwd=db_password, database=database)
    cur1 = con1.cursor()

    f'''Create Table'''
    try:
        cur1.execute(f"""create table IF NOT EXISTS {table_name} (
                                            id int AUTO_INCREMENT NOT NULL,
                                            Product_url varchar(255) UNIQUE,
                                            primary key(id)
                                            );""")
    except Exception as e:

        pass


def insert_to_DB(table_dict):
    con = pymysql.connect(host=host, user=db_user, passwd=db_password, database=database)
    cur = con.cursor()
    # field_list = []
    # value_list = []
    # for field in table_dict:
    #     field_list.append(str(field).strip())
    #     value_list.append(str(table_dict[field]).replace("'", "’").strip())
    # fields = ','.join(field_list)
    # values = "','".join(value_list)
    insert_db = f"INSERT INTO {table_name} (id, Product_url) VALUES (%s, %s)"
    disable_auto_increment_query = f"ALTER TABLE {table_name} MODIFY id INT"

    try:
        cur.execute(disable_auto_increment_query)
        cur.execute(insert_db, (None, table_dict,))
        con.commit()
        print(f'Data Inserted in {table_name}')
    except Exception as e:
        print(e)
        pass



if __name__ == '__main__':
    create_table()
    get_data()
