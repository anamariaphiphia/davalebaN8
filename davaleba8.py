import sqlite3
conn = sqlite3.connect("books_db.sqlite")
cursor = conn.cursor()
cursor.execute("""CREATE TABLE books
( id INTEGER PRIMARY KEY AUTOINCREMENT,
title VARCHAR (50),
author VARCHAR (60),
release_year INT;
         
""")
cursor.execute(""" INSERT INTO books(title,author,relace_year)VALUES("ნუ მოკლავ ჯაფარას", "ჰარპერ ლი","1960")""")
books_list = [
    ("ალქიმიკოსი", "პაულო კოელიო",1988)
    ("დანაშაულის თანამონაწილენი","აგათა კრისტი",1890)
    ("ჯეინ ეარი", "შარლოტ ბრონტე",1847)
    ("მე,ბებია,ილიკო და ილარიონი","ნოდარ დუმბაძე",1960)
]
cursor.executemanty("""INSERT INTO books(title,uathor,relace_year)VALUE(*,*,*)""",books_list)
conn.commit()

#2davaleba
import sqlite3
conn = sqlite3.connect("titanic")
cursor = conn.cursor()
cursor.execute(""""CREATE TABLE titanic 
( id INTEGER PRIMARY KEY AUTOINCREMENT,
passenger_name VARCHAR (40),
age INT,
sex VARCHAR (50),
ticket INT,
cabin INT;
""")
name = input("passengers name")
age = input("passenger age")
sex = input("passengers gender")
ticket = input("ticket price")
cabin = input("passengers cabin")
cursor.execute("""INSERT INTO titanic (passenger_name,age,sex, ticket,cabin)VALUES(passenger_name,age,sex,ticket,cabin)""",)
conn.commit()
print(" entered succesfully ")
conn.close()
if (conn):
    conn.close()
print("sqlite connection is closed")
#davaleba3

class Movie:
    def __init__(self, title, genre, year, imdb):
        self.title = title
        self.genre = genre
        self.year = year
        self.imdb = imdb

    def __str__(self):
        return f"title: {self.title}, genre: {self.genre}, year: {self.year}, imdb: {self.imdb}"

    import sqlite3
    conn = sqlite3.connect("movies")
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE movies,
    movie_id INTEGER PRIMARY KEY AUTOINCREMENT,
    title VARCHAR(50),
    genre VARCHAR(50),
    year int,
    imdb int;

    """)
    cursor.execute("""INSERT INTO movies.Movie(title,genre,year,imdb)VALUES("escape","mystery",1999,10/10))
    conn.commit()
     movie_list[("home","adventure",200,10/8)
        ("dark sky","mystery",2016,10/10)
        ("lucky","action adventure",2019,10/10)
        ("mr x","romance",2001,10/10)""")
    ]
    cursor.executemanty("""INSERT INTO movies(title,genre,year,imdb)VALUE(*,*,*)""", movie_list)
    conn.commit()


