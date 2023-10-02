import sqlite3

connect = sqlite3.connect('database.db', check_same_thread=False)
cursor = connect.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS "user"
("id" INTEGER NOT NULL,
"tg_id" TEXT NOT NULL,
primary key ("id" AUTOINCREMENT)
);''')
connect.commit()

cursor.execute('''CREATE TABLE IF NOT EXISTS "categories"
("id" INTEGER NOT NULL,
"name_eng" TEXT NOT NULL,
"name_ru" TEXT NOT NULL,
primary key ("id" AUTOINCREMENT)
);''')
connect.commit()

cursor.execute('''CREATE TABLE IF NOT EXISTS "subscribes"
("id" INTEGER NOT NULL,
"user_id" INTEGER NOT NULL,
"category_id" INTEGER NOT NULL,
primary key ("id" AUTOINCREMENT)
);''')
connect.commit()

#регистрация
def reg(tg_id):
    cursor.execute('''INSERT INTO
        user (tg_id)
        VALUES (?) 
        ''', (tg_id,))
    connect.commit()
    return "Регистрация прощла успешно"

#поиск пользователя в базе
def searchUser(tg_id):
    return cursor.execute('''SELECT tg_id
    FROM user
    WHERE tg_id = ?
    ''',(tg_id,)).fetchone()

def searchUserId(tg_id):
    return cursor.execute('''SELECT id
    FROM user
    WHERE tg_id = ?
    ''',(tg_id,)).fetchone()

#добавление новой категории
def addCategory(name_eng,name_ru):
    cursor.execute('''INSERT INTO
        categories (name_eng,name_ru)
        VALUES (?,?)
        ''', (name_eng,name_ru))
    connect.commit()
    return "Добавление категории прошло успешно"

#вывод категорий новостей
def category():
    return cursor.execute('''SELECT name_ru
    FROM categories''').fetchall()

#получаем id из бд
def getUserId(tg_id):
    return cursor.execute('''SELECT id FROM user WHERE tg_id = ?''', (tg_id,)).fetchone()

#подписаться на категорию
def subCategory(user_id,category_id):
    cursor.execute('''INSERT INTO
        subscribes (user_id,category_id)
        VALUES (?,?)
        ''',(user_id,category_id))
    connect.commit()
    return "Вы подписались"

#поиск категории у пользователя
def searchUserCategory(user_id):
    return cursor.execute('''SELECT categories.name_ru
        FROM subscribes 
        INNER JOIN categories ON subscribes.category_id = categories.id
        WHERE subscribes.user_id = ?
        ''',(user_id,)).fetchall()

#Поиск категории в бд
def searchCategory(name):
    return cursor.execute('''SELECT id
        FROM categories 
        WHERE name_ru = ?
        ''',(name,)).fetchone()

def searchEngCategory(category_id):
    return cursor.execute('''SELECT name_eng
    FROM categories
    WHERE id = ?
    ''',(category_id,)).fetchone()

#отписаться от категории
def unsubCategory(tg_id,category_id):
    cursor.execute('''DELETE FROM subscribes 
        WHERE user_id = ?
        AND category_id = ?
        ''', (tg_id, category_id))
    connect.commit()
    return "Вы отписались"

def searchSubUser(user_id):
    return cursor.execute('''SELECT categories.name_ru FROM subscribes
    INNER JOIN categories ON categories.id = subscribes.category_id
    WHERE subscribes.user_id = ?
    ''',(user_id,)).fetchall()

def seacrCategory():
    return cursor.execute('''SELECT * FROM categories
    ''',()).fetchall()

def addCategories():
    addCategory("general", "В мире🌍")
    addCategory("technology", "Технологии💻")
    addCategory("science", "Наука🔭")
    addCategory("sports", "Спорт⚽")
    addCategory("business", "Бизнес💰")
    addCategory("entertainment", "Развлечения🌷")
    addCategory("health", "Здоровье💌")