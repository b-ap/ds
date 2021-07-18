#!/usr/bin/python3

import pymysql
from db import get_db, close_db
from faker import Faker
from flask import Flask, render_template

faker = Faker()

app = Flask(__name__)
app.teardown_appcontext(close_db)

@app.route('/')
def home():
    connection = get_db()
    cursor = connection.cursor(pymsql.cursors.DictCursor)
    try:
        cursor.execute('INSERT INTO users (name, email) VALUES (%s, %s)', (faker.name(), faker.email()))
    except pymysql.err.ProgrammingError as ex:
        cursor.execute('CREATE TABLE IF NOT EXISTS users (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(20), email VARCHAR(30))')

    cursor.execute('SELECT * FROM users')
    users = cursor.fetchall()
    return render_template('index.html', users = users)
