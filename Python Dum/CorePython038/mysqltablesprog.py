import mysql.connector

#1. Establishing the connection
conn = mysql.connector.connect(host="localhost",user='root',passwd='root',database='mydatabase')
# 2.Creating a cursor object using the cursor() method
cur = conn.cursor()
# create a tables
# create table table_name(column1 datatype, column2 datatype, column3 datatype, ...);
#3. Execute the SQL command using curser object and execute() method
#sql = "CREATE TABLE students (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255) not null, age INT)"
# insert into table_name(column1, column2, column3, ...) values(value1, value2, value3, ...);
#sql = "INSERT INTO students (name, age) VALUES ('John', 20)"
# update table_name set column1 = value1, column2 = value2, ... where condition;
#sql = "UPDATE students SET id= 2 WHERE name = 'John'"

#delete from table_name where condition;
#sql = "DELETE FROM students WHERE id = 4"
# Fetch all the records from the table
#sql = "select * from table_name"
sql = "select * from students"
cur.execute(sql)
data = cur.fetchall()
print(data,type(data))
for i in data:
    print(i)
#4. Commit your changes
conn.commit()
#5. Close the connection
conn.close()



