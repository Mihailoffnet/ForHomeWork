import psycopg2 # сначала надо установить библиотеку командой pip install psycopg2-binary

# загружаю свой пароль
with open('token.txt', 'r') as file_object:
    psw = file_object.readline().strip()

# # для работы с БД нужно открыть и закрыть соединение connect и курсор cur
# connect = psycopg2.connect(database="netology_db", user="postgres", password=psw)
# cur = connect.cursor()
# cur.execute("CREATE TABLE IF NOT EXISTS test(id SERIAL PRIMARY KEY);")
# connect.commit() # применить измененения (завершить транзакцию)
# # или
# connect.rollback() # отменить все изменения
# # не забываем после закрыть курсор и коннект
# cur.close()
# connect.close()

# # чтобы не открывать и не закрывать каждый раз курсор, можно для них использовать контекстный менеджер with

# createdb -U postgress clients_db

with psycopg2.connect(database="clients_db", user="postgres", password=psw) as conn:
    with conn.cursor() as cur:
        # удаление таблиц
        cur.execute("""
        DROP TABLE phone;
        DROP TABLE name;
        """)

def create_db(conn):
    with conn.cursor() as cur:
        cur.execute("""
        CREATE TABLE IF NOT exists name (
    	name_id SERIAL PRIMARY KEY, first_name VARCHAR(50) NOT null, 
    	surname VARCHAR(50) NOT null, email VARCHAR(60) UNIQUE NOT null 
     	check (email ~* '^([a-zA-Z0-9_/.-]+)@([a-zA-Z0-9_/.-]+).([a-zA-Z0-9_/.-]+)$'));
        
        CREATE TABLE IF NOT exists phone (
        phone_id SERIAL PRIMARY KEY, phone_number VARCHAR(20) UNIQUE not null
        check (phone_number ~* '^([+][0-9]{10})$'),
        name_id INTEGER REFERENCES name(name_id) not null);
        """)
        # print(cur.fetchall())
        # return cur.fetchall()

def add_client(conn, first_name, surname, email, phones=None):
    with conn.cursor() as cur:
        if phones == None:
            cur.execute("""
            INSERT INTO name(first_name, surname, email) 
            VALUES 
                (%s, %s, %s) RETURNING *;
                """, (first_name, surname, email))
            print(f' Был добавлен клиент {cur.fetchall()}')
            return cur.fetchall()


def add_phone(conn, client_id, phone):
    with conn.cursor() as cur:
        cur.execute("""
        INSERT INTO phone(client_id, phone) 
            VALUES 
                (client_id, phone) RETURNING *;
        """)
        print(cur.fetchall())
        return cur.fetchall()

with psycopg2.connect(database="clients_db", user="postgres", password=psw) as conn:
    # вызов функции
    create_table = create_db(conn)
    print()
    add_client = add_client(conn, 'Михайлов', 'Виктор', 'mihailoff@inbox.ru')
    print()


conn.close()

# with psycopg2.connect(database="netology_db", user="postgres", password=psw) as conn:
#     with conn.cursor() as cur:
#         # удаление таблиц
#         cur.execute("""
#         DROP TABLE homework;
#         DROP TABLE course;
#         """)

#         # создание таблиц
#         cur.execute("""
#         CREATE TABLE IF NOT EXISTS course(
#             id SERIAL PRIMARY KEY,
#             name VARCHAR(40) UNIQUE
#         );
#         """)
#         cur.execute("""
#         CREATE TABLE IF NOT EXISTS homework(
#             id SERIAL PRIMARY KEY,
#             number INTEGER NOT NULL,
#             description TEXT NOT NULL,
#             course_id INTEGER NOT NULL REFERENCES course(id)
#         );
#         """)
#         conn.commit()  # фиксируем в БД

#         # наполнение таблиц (C из CRUD)
#         cur.execute("""
#         INSERT INTO course(name) VALUES('Python');
#         """)
#         conn.commit()  # фиксируем в БД

#         cur.execute("""
#         INSERT INTO course(name) VALUES('Java') RETURNING *;
#         """)
#         print(cur.fetchone())  # запрос данных 1 строка (fetchONE). 
#         # запрос данных автоматически зафиксирует изменения

#         cur.execute("""
#         INSERT INTO homework(number, description, course_id) VALUES(1, 'простое дз', 1)
#         RETURNING *;
#         """)
#         print(cur.fetchone())
#         conn.commit()  # фиксируем в БД

#         # извлечение данных (R из CRUD)
#         cur.execute("""
#         SELECT * FROM course;
#         """)
#         print('fetchall', cur.fetchall())  # извлечь все строки (fetchALL)

#         cur.execute("""
#         SELECT * FROM course;
#         """)
#         print('fetchone', cur.fetchone())  # извлечь первую строку (аналог LIMIT 1)

#         cur.execute("""
#         SELECT * FROM course;
#         """)
#         print('fetchmany', cur.fetchmany(3))  # извлечь первые N строк (аналог LIMIT N)

#         cur.execute("""
#         SELECT name FROM course;
#         """)
#         print(cur.fetchall())

#         cur.execute("""
#         SELECT id FROM course WHERE name='Python';
#         """)
#         print(cur.fetchone())

# #         cur.execute("""
# #         SELECT id FROM course WHERE name='{}';
# #         """.format("Python"))  # плохо - возможна SQL инъекция
# #         print(cur.fetchone())

#         cur.execute("""
#         SELECT id FROM course WHERE name=%s;
#         """, ("Python",))  # хорошо, обратите внимание на кортеж
#         print(cur.fetchone())

#         def get_course_id(cursor, name: str) -> int:
#             cursor.execute("""
#             SELECT id FROM course WHERE name=%s;
#             """, (name,))
#             return cur.fetchone()[0]
        
#         # вызов функции
#         python_id = get_course_id(cur, 'Python')
#         print('python_id', python_id)

#         cur.execute("""
#         INSERT INTO homework(number, description, course_id) VALUES(%s, %s, %s);
#         """, (2, "задание посложнее", python_id))
#         conn.commit()  # фиксируем в БД

#         cur.execute("""
#         SELECT * FROM homework;
#         """)
#         print(cur.fetchall())

#         # обновление данных (U из CRUD)
#         cur.execute("""
#         UPDATE course SET name=%s WHERE id=%s;
#         """, ('Python Advanced', python_id))
#         cur.execute("""
#         SELECT * FROM course;
#         """)
#         print(cur.fetchall())  # запрос данных автоматически зафиксирует изменения

#         # удаление данных (D из CRUD)
#         cur.execute("""
#         DELETE FROM homework WHERE id=%s;
#         """, (1,))
#         cur.execute("""
#         SELECT * FROM homework;
#         """)
#         print(cur.fetchall())  # запрос данных автоматически зафиксирует изменения

# conn.close()



# # CREATE TABLE IF NOT exists name (
# # 	name_id SERIAL PRIMARY KEY, first_name VARCHAR(50) NOT null, 
# # 	surname VARCHAR(50) NOT null, email VARCHAR(60) UNIQUE NOT null 
# # 	check (email ~* '^([a-zA-Z0-9_/.-]+)@([a-zA-Z0-9_/.-]+).([a-zA-Z0-9_/.-]+)$'));


# # CREATE TABLE IF NOT exists phone (
# # 	phone_id SERIAL PRIMARY KEY, phone_number VARCHAR(20) UNIQUE not null
# # 	check (phone_number ~* '^([+][0-9]{10})$'),
# # 	name_id INTEGER REFERENCES name(name_id) not null);

# # INSERT INTO name(first_name, surname, email) 
# # VALUES 
# # 	('Виктор', 'Михайлов', 'mihailoff@inbox.ru'),
# # 	('Второй', 'Студент', 'second_studen@mail.com'),
# # 	('Третий', 'Лишний','third.1@gmail.com'),
# # 	('Четвертый', 'Запасной','fourth@yandex.ru'),
# # 	('Пятый', 'Элемент', 'fifth@mail.ru'),
# # 	('Виктор', 'Студент', 'viktor@mail.ru');

# # INSERT INTO phone(name_id, phone_number) 
# # VALUES 
# # 	(1, '+7917000000'),
# # 	(1, '+7917000001'),
# # 	(2, '+7917000002'),
# # 	(3, '+7917000003'),
# # 	(4, '+7917000004'),
# # 	(4, '+7917000005');