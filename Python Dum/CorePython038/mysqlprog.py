import mysql.connector
#1. Establishing the connection
conn = mysql.connector.connect(host="localhost",user='root',passwd='root')
# 2.Creating a cursor object using the cursor() method
cur = conn.cursor()
# create a database
# create database database_name;
#3. Execute the SQL command using curser object and execute() method
cur.execute("CREATE DATABASE IF NOT EXISTS mydatabase")

