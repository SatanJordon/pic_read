import psycopg2

conn = psycopg2.connect(database="my_site", user="postgres", password="postgres", host="localhost", port="5432")

cur = conn.cursor()


def read_users_account():
    cur.execute("SELECT * FROM public.users_account")
    rows = cur.fetchall()
    conn.commit()
    return rows


def read_users_account_by_carNumber(car_number):
    query_to_execute = """SELECT * FROM public.users_account where car_number = %s"""
    where_query = (car_number,)
    cur.execute(query_to_execute, where_query)
    rows = cur.fetchall()
    conn.commit()
    return rows


def read_auth_user():
    cur.execute("SELECT * FROM public.auth_user")
    rows = cur.fetchall()
    conn.commit()
    return rows


def read_users_tax():
    cur.execute("SELECT * FROM public.users_tax")
    rows = cur.fetchall()
    conn.commit()
    return rows


def read_users_tax_by_carNumber(car_number):
    query_to_execute = """SELECT * FROM public.users_tax where t_car_number = %s"""
    where_query = (car_number,)
    cur.execute(query_to_execute, where_query)
    rows = cur.fetchall()
    conn.commit()
    return rows


def insert_users_tax(car_number, time, is_registered, amount):
    postgres_insert_query = """INSERT INTO public.users_tax (t_car_number, time, is_registered, amount) VALUES (%s,
    %s,%s,%s); """
    record_to_insert = (car_number, time, is_registered, amount)
    cur.execute(postgres_insert_query, record_to_insert)

    conn.commit()
    count = cur.rowcount
    print(count, "Record inserted successfully.")


def update_users_tax_by_carNumber(car_number, time, amount):
    postgres_insert_query = """Update public.users_tax set time = %s, amount = %s where t_car_number = %s"""
    record_to_insert = (time, amount, car_number)
    cur.execute(postgres_insert_query, record_to_insert)

    conn.commit()
    count = cur.rowcount
    print(count, "Record inserted successfully.")


