import sqlite3

connection = sqlite3.connect('database.db')


with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO posts (title, content) VALUES (?, ?)",
            ('First Post', 'Content for the first post')
            )

cur.execute("INSERT INTO posts (title, content) VALUES (?, ?)",
            ('Second Post, this one with a picture', 'Content for the second post : <img src="/home/roman.rutka@Digital-Grenoble.local/Documents/Module Projet Orienté Objet/CasEtude_3/helloFlask/helloflask/static/images.image.jpg"/>')
            )

connection.commit()
connection.close()