import psycopg2

def create():
    conn = psycopg2.connect(dbname="postgres",user="postgres",password="7284559",host="localhost",port="5432")
    cur = conn.cursor()
    cur.execute(''' create table stud(id serial,name text,age text,address text);''')
    print("table created")
    conn.commit()
    conn.close()

def insert_data():
    conn = psycopg2.connect(dbname="postgres",user="postgres",password="7284559",host="localhost",port="5432")
    cur = conn.cursor()
    cur.execute('''insert into stud (name, age, address) values ('minal','19','US');''')
    print("table updated")
    conn.commit()
    conn.close()

insert_data()





