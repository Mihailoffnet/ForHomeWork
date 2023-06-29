import psycopg2 

# база данных создана
# createdb -U postgres clients_db

# пропишите пароль в переменную psw
# psw = ''

# Или поместите в корень файл psw.txt с паролем к пользователю postgres вашей БД
# и разкоментируйте код ниже
with open('psw.txt', 'r') as file_object:
    psw = file_object.readline().strip()

# удаление таблиц. Не нужно для первого запуска
with psycopg2.connect(database="clients_db", 
                      user="postgres", password=psw) as conn:
    with conn.cursor() as cur:
        # удаление таблиц
        cur.execute("""
        DROP TABLE phone;
        DROP TABLE name;
        """)
    conn.commit()

def create_db(conn):
    with conn.cursor() as cur:
        cur.execute("""
        CREATE TABLE IF NOT exists name (
    	name_id SERIAL PRIMARY KEY, first_name VARCHAR(50) NOT null, 
    	surname VARCHAR(50) NOT null, email VARCHAR(60) UNIQUE NOT null 
     	check (email ~* 
        '^([a-zA-Z0-9_/.-]+)@([a-zA-Z0-9_/.-]+).([a-zA-Z0-9_/.-]+)$'));
        
        CREATE TABLE IF NOT exists phone (
        phone_id SERIAL PRIMARY KEY, phone_number VARCHAR(20) UNIQUE not null
        check (phone_number ~* '^([+][0-9]{11})$'),
        name_id INTEGER REFERENCES name(name_id) not null);
        """)
        conn.commit()
        # print(cur.fetchall())
        # return cur.fetchall()

def add_client(conn, first_name, surname, email, phones=None):
    with conn.cursor() as cur:
        cur.execute("""
        INSERT INTO name(first_name, surname, email) 
            VALUES 
                (%s, %s, %s) RETURNING *;
            """, (first_name, surname, email))
        name_id = cur.fetchone()[0]
        print(f'Добавлен клиент {name_id} - {first_name} {surname}, {email}')
        if phones != None:
            add_phone(conn, name_id, phones)
        conn.commit()
        return cur.fetchone()

def add_phone(conn, name_id, phones):
    with conn.cursor() as cur:
        cur.execute("""
        INSERT INTO phone(name_id, phone_number) 
            VALUES 
                (%s, %s) RETURNING *;
        """, (name_id, phones))
        print(f'Добавлен телефон {phones} клиенту {name_id}')
        conn.commit()

def change_client(conn, name_id, first_name=None, surname=None, email=None):
    with conn.cursor() as cur:
        if first_name != None:
            cur.execute("""
            UPDATE name SET first_name = %s WHERE name_id = %s RETURNING *;
            """, (first_name, name_id))
            print(f'Изменено имя клиента {name_id} на {first_name}') 
        if surname != None:
            cur.execute("""
            UPDATE name SET surname = %s WHERE name_id = %s RETURNING *;
            """, (surname, name_id))
            print(f'Изменена фамилия клиента {name_id} на {surname}') 
        if email != None:
            cur.execute("""
            UPDATE name SET email = %s WHERE name_id = %s RETURNING *;
            """, (email, name_id))
            print(f'Изменен email клиента {name_id} на {email}') 
        conn.commit()

def delete_phone(conn, phones):
    with conn.cursor() as cur:
        cur.execute("""
        SELECT name_id FROM phone WHERE phone_number = %s;
        """, (phones,))
        name_id = cur.fetchone()[0]

        cur.execute("""
        DELETE FROM phone WHERE phone_number = %s;
        """, (phones,))
        print(f'Удален номер телефона {phones} клиента {name_id}') 
    conn.commit()

def delete_client(conn, name_id):
    with conn.cursor() as cur:
        cur.execute("""
        SELECT * FROM phone WHERE name_id = %s;
        """, (name_id,));
        res = cur.fetchone()
        while res != None:
            delete_phone(conn, res[1])
            cur.execute("""
            SELECT * FROM phone WHERE name_id = %s;
            """, (name_id,));
            res = cur.fetchone()
        cur.execute("""
        DELETE FROM name WHERE name_id = %s;
        """, (name_id,));
        print(f'Данные клиента {name_id} полностью удалены')
    conn.commit()

def find_client(conn, first_name=None, surname=None, email=None, phones=None):
    with conn.cursor() as cur:
        if first_name != None:
            cur.execute("""
            SELECT * FROM name WHERE first_name = %s;
           """, (first_name,));
            res = cur.fetchall()
            if res == []:
                print(f'По имени {first_name} клиентов не найдено')
            for client in res:
                print(f'По имени {first_name} найден клиент {client}')
        if surname != None:
            cur.execute("""
            SELECT * FROM name WHERE surname = %s;
           """, (surname,));
            res = cur.fetchall()
            if res == []:
                print(f'По фамилии {surname} клиентов не найдено')
            for client in res:
                print(f'По фамилии {surname} найден клиент {client}')
        if email != None:
            cur.execute("""
            SELECT * FROM name WHERE email = %s;
           """, (email,));
            res = cur.fetchall()
            if res == []:
                print(f'По электронной почте {email} клиентов не найдено')
            for client in res:
                print(f'По электронной почте {email} найден клиент {client}')
        if phones != None:
            cur.execute("""
            SELECT name_id FROM phone WHERE phone_number = %s;
           """, (phones,));
            res = cur.fetchone()
            if res == None:
                print(f'По телефону {phones} клиентов не найдено')
            else:
                name_id = res[0]
                cur.execute("""
                SELECT * FROM name WHERE name_id = %s;
                """, (name_id ,));
                res = cur.fetchone()
                print(f'По телефону {phones} найден клиент {res}')
    conn.commit()
    return res


# вызов функции
with psycopg2.connect(database="clients_db", 
                      user="postgres", password=psw) as conn:
    create_table = create_db(conn)
    add_client(conn, 'Виктор', 'Михайлов', 'mihailoff@inbox.ru', 
               '+79170000001')
    add_client(conn, 'Второй', 'Студент', 'second_studen@mail.com')
    add_client(conn, 'Третий', 'Лишний','third.1@gmail.com', '+79170000003')
    add_client(conn, 'Четвертый', 'Запасной','fourth@yandex.ru', 
               '+79170000004')
    add_client(conn, 'Пятый', 'Элемент', 'fifth@mail.ru')
    add_client(conn, 'Виктор', 'Студент', 'viktor@mail.ru', '+79170000005')
    print()
    add_phone(conn, 1, '+79170000002')
    add_phone(conn, 5, '+79170000010')
    add_phone(conn, 1, '+79170000011')
    print()
    change_client(conn, 2, first_name='Второй2', surname='Студент2')
    change_client(conn, 3, surname='Лишний2', email='third.2@gmail.com')
    change_client(conn, 5, first_name='Пятый2')
    print()
    delete_phone(conn, '+79170000010')   
    delete_phone(conn, '+79170000004')
    print()
    find_client(conn, first_name='Виктор')
    find_client(conn, first_name='Второй2')
    find_client(conn, first_name='Второй')
    print()
    find_client(conn, surname='Лишний2')
    find_client(conn, surname='Чужой')
    print()
    find_client(conn, email='mihailoff@inbox.ru')
    find_client(conn, email='mmm@inbox.ru')
    print()
    find_client(conn, phones='+79170000005')
    find_client(conn, phones='+79170000020')
    print()
    delete_client(conn, 1)
    delete_client(conn, 2)

conn.close
