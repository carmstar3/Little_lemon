# Importing MySQL Connector/Python
import mysql.connector as connector
from mysql. connector import Error

try: connection=connector.connect(user="root", passwords="")
except Error as er:
    print(er.msg)

#creating a cursor:
cursor= connection.cursor()
print("Cursor is created to communicate with the mysql using python.")

#creating the database and setting it for use:
cursor.execute("CREATE DATABASE little_lemon_db")
print("The database 'little_lemon-db' is created.\n")

#MenuItems table
create_menuitem_table = """CREATE TABLE MenuItems(
ItemID INT AUTO_INCREMENT,
Name VARCHAR(200),
Type VARCHAR(100),
Price INT,
PRIMARY KEY(ItemID)
);"""

# Create MenuItems table
cursor.execute(create_menuitem_table)
print("MenuItems table is created.")

create_menu_table = """CREATE TABLE Menus(
MenuID INT,
ItemID INT,
Cuisine VARCHAR(100),
PRIMARY KEY(MenuID,ItemID)
);"""

# Create Menu table
cursor.execute(create_menu_table)
print("Menu table is created.")

create_booking_table = """CREATE TABLE Bookings(
BookingID INT AUTO_INCREMENT,
TableNo INT,
GuestFirstName VARCHAR(100) NOT NULL,
GuestLastName VARCHAR(100) NOT NULL,
BookingSlot TIME NOT NULL,
EmployeeID INT,
PRIMARY KEY(BookingID)
);"""

# Create Bookings table
cursor.execute(create_booking_table)
print("Bookings table is created.")

create_orders_table = """CREATE TABLE Orders(
OrderID INT,
TableNo INT,
MenuID INT,
BookingID INT,
BillAmount INT,
Quantity INT,
PRIMARY KEY(OrderID,TableNo)
);"""

# Create Orders table
cursor.execute(create_orders_table)
print("Orders table is created.")

create_employees_table = """CREATE TABLE Employees(
EmployeeID INT AUTO_INCREMENT PRIMARY KEY,
Name VARCHAR(100),
Role VARCHAR(100),
Address VARCHAR(200),
Contact_Number INT,
Email VARCHAR(100),
Annual_Salary VARCHAR(100)
);"""

# Create Employees table
cursor.execute(create_employees_table)
print("Employees table is created.")

#*******************************************************#
# Insert query to populate "MenuItems" table:
#*******************************************************#
insert_menuitems="""
INSERT INTO MenuItems (ItemID, Name, Type, Price)
VALUES
(1, 'Olives','Starters',5),
(2, 'Flatbread','Starters', 5),
(3, 'Minestrone', 'Starters', 8),
(4, 'Tomato bread','Starters', 8),
(5, 'Falafel', 'Starters', 7),
(6, 'Hummus', 'Starters', 5),
(7, 'Greek salad', 'Main Courses', 15),
(8, 'Bean soup', 'Main Courses', 12),
(9, 'Pizza', 'Main Courses', 15),
(10, 'Greek yoghurt','Desserts', 7),
(11, 'Ice cream', 'Desserts', 6),
(12, 'Cheesecake', 'Desserts', 4),
(13, 'Athens White wine', 'Drinks', 25),
(14, 'Corfu Red Wine', 'Drinks', 30),
(15, 'Turkish Coffee', 'Drinks', 10),
(16, 'Turkish Coffee', 'Drinks', 10),
(17, 'Kabasa', 'Main Courses', 17);"""

#*******************************************************#
# Insert query to populate "Menu" table:
#*******************************************************#
insert_menu="""
INSERT INTO Menus (MenuID,ItemID,Cuisine)
VALUES
(1, 1, 'Greek'),
(1, 7, 'Greek'),
(1, 10, 'Greek'),
(1, 13, 'Greek'),
(2, 3, 'Italian'),
(2, 9, 'Italian'),
(2, 12, 'Italian'),
(2, 15, 'Italian'),
(3, 5, 'Turkish'),
(3, 17, 'Turkish'),
(3, 11, 'Turkish'),
(3, 16, 'Turkish');"""

#*******************************************************#
# Insert query to populate "Bookings" table:
#*******************************************************#
insert_bookings="""
INSERT INTO Bookings (BookingID, TableNo, GuestFirstName, 
GuestLastName, BookingSlot, EmployeeID)
VALUES
(1, 12, 'Anna','Iversen','19:00:00',1),
(2, 12, 'Joakim', 'Iversen', '19:00:00', 1),
(3, 19, 'Vanessa', 'McCarthy', '15:00:00', 3),
(4, 15, 'Marcos', 'Romero', '17:30:00', 4),
(5, 5, 'Hiroki', 'Yamane', '18:30:00', 2),
(6, 8, 'Diana', 'Pinto', '20:00:00', 5);"""

#*******************************************************#
# Insert query to populate "Orders" table:
#*******************************************************#
insert_orders="""
INSERT INTO Orders (OrderID, TableNo, MenuID, BookingID, Quantity, BillAmount)
VALUES
(1, 12, 1, 1, 2, 86),
(2, 19, 2, 2, 1, 37),
(3, 15, 2, 3, 1, 37),
(4, 5, 3, 4, 1, 40),
(5, 8, 1, 5, 1, 43);"""

#*******************************************************#
# Insert query to populate "Employees" table:
#*******************************************************#
insert_employees = """
INSERT INTO employees (EmployeeID, Name, Role, Address, Contact_Number, Email, Annual_Salary)
VALUES
(01,'Mario Gollini','Manager','724, Parsley Lane, Old Town, Chicago, IL',351258074,'Mario.g@littlelemon.com','$70,000'),
(02,'Adrian Gollini','Assistant Manager','334, Dill Square, Lincoln Park, Chicago, IL',351474048,'Adrian.g@littlelemon.com','$65,000'),
(03,'Giorgos Dioudis','Head Chef','879 Sage Street, West Loop, Chicago, IL',351970582,'Giorgos.d@littlelemon.com','$50,000'),
(04,'Fatma Kaya','Assistant Chef','132  Bay Lane, Chicago, IL',351963569,'Fatma.k@littlelemon.com','$45,000'),
(05,'Elena Salvai','Head Waiter','989 Thyme Square, EdgeWater, Chicago, IL',351074198,'Elena.s@littlelemon.com','$40,000'),
(06,'John Millar','Receptionist','245 Dill Square, Lincoln Park, Chicago, IL',351584508,'John.m@littlelemon.com','$35,000');"""

# Populate MenuItems table
print("Inserting data in MenuItems table.")
cursor.execute(insert_menuitems)
print("Total number of rows in MenuItem table: {}\n".format(cursor.rowcount))
connection.commit()

# Populate Menu table
cursor.execute(insert_menu)
print("Inserting data in Menu table.")
print("Total number of rows in Menu table: {}\n".format(cursor.rowcount))
connection.commit()

# Populate Bookings table
print("Inserting data in Bookings table.")
cursor.execute(insert_bookings)
print("Total number of rows in Bookings table: {}\n".format(cursor.rowcount))
connection.commit()

# Populate Orders table
print("Inserting data in Orders table.")
cursor.execute(insert_orders)
print("Total number of rows in Orders table: {}\n".format(cursor.rowcount))
connection.commit()

# Populate Employees table
print("Inserting data in Employees table.")
cursor.execute(insert_employees)
print("Total number of rows in Employees table: {}\n".format(cursor.rowcount))
connection.commit()

# Import MySQLConnectionPool class
from mysql.connector.pooling import MySQLConnectionPool

# Import Error class
from mysql.connector import Error

dbconfig={"database":"little_lemon_db", "user":"root", "password":""}
try:
    pool = MySQLConnectionPool(pool_name="pool_a", pool_size=2, host='localhost', **dbconfig)
    print("The connection pool is created with name:", pool.pool_name)
    print("The pool size is:", pool.pool_size)
except Error as err:
    print("Error Code:", err.errno)
    print("Error Message:", err.msg)

print("Getting a connection from the pool.")

connection = pool.get_connection()
if connection.is_connected():
    cursor = connection.cursor()

print("'connection' object is created with a connection from the pool")

create_peakhours_proc = """
CREATE PROCEDURE PeakHours()
BEGIN
SELECT HOUR(BookingSlot) AS booking_hour, COUNT(BookingID) AS number_of_bookings
FROM Bookings
GROUP BY booking_hour
ORDER BY number_of_bookings DESC;
END
"""

cursor.execute(create_peakhours_proc)

cursor.callproc('PeakHours')

results = next(cursor.stored_results())

dataset = results.fetchall()

for column_id in cursor.stored_results():
    cols = [column[0] for column in column_id.description]

print(cols)
for data in dataset:
    print(data)

create_gueststatus_proc = """
CREATE PROCEDURE GuestStatus()
BEGIN
SELECT CONCAT(GuestFirstName, ' ', GuestLastName) AS GuestFullName,
CASE
WHEN Role in ('Manager','Assistant Manager') THEN 'Ready to pay'
WHEN Role in ('Head Chef') THEN 'Ready to serve'
WHEN Role in ('Assistant Chef') THEN 'Preparing Order'
WHEN Role in ('Head Waiter') THEN 'Order served'
ELSE "Pending"
END AS Status
FROM Bookings
LEFT JOIN Employees
ON Bookings.EmployeeID = Employees.EmployeeID;
END
"""

cursor.execute(create_gueststatus_proc)

cursor.callproc('GuestStatus')

results = next(cursor.stored_results())

dataset = results.fetchall()

for column_id in cursor.stored_results():
    cols = [column[0] for column in column_id.description]

print(cols)
for data in dataset:
    print(data)

connection.close()

# Import MySQLConnectionPool class
from mysql.connector.pooling import MySQLConnectionPool

# Import Error class
from mysql.connector import Error

dbconfig={"database":"little_lemon_db", "user":"root", "password":""}
try:
    pool = MySQLConnectionPool(pool_name="pool_b", pool_size=2, host='localhost', **dbconfig)
    print("The connection pool is created with name:", pool.pool_name)
    print("The pool size is:", pool.pool_size)
except Error as err:
    print("Error Code:", err.errno)
    print("Error Message:", err.msg)

# Connect the first guest.
connection1 = pool.get_connection()
cursor1=connection1.cursor()

booking1="""INSERT INTO Bookings 
(TableNo, GuestFirstName, GuestLastName, BookingSlot, EmployeeID)
VALUES
(8,'Anees','Java','18:00:00',6);"""

cursor1.execute(booking1)
connection1.commit()
print("""A new booking is added in the "Bookings" table.""")

# Connect the second guest.
connection2 = pool.get_connection()
cursor2=connection2.cursor()

booking2="""INSERT INTO Bookings 
(TableNo, GuestFirstName, GuestLastName, BookingSlot, EmployeeID)
VALUES
(5, 'Bald','Vin','19:00:00',6);"""

cursor2.execute(booking2)
connection2.commit()
print("""A new booking is added in the "Bookings" table.""")

# Adding a new connection to connect the third user.

import mysql.connector as connector
try:
    connection3 = pool.get_connection()
    print("The guest is connected")
except:
    print("Adding new connection in the pool.")
        
    # Create a connection
    connection=connector.connect(user="root",password="")
    
    # Add the connection into the pool
    pool.add_connection(cnx=connection)
    print("A new connection is added in the pool.\n")
        
    connection3 = pool.get_connection()
    print("'connection3' is added in the pool.")
    
# Connect the third guest 
cursor3=connection3.cursor()

booking3="""INSERT INTO Bookings 
(TableNo, GuestFirstName, GuestLastName, BookingSlot, EmployeeID)
VALUES
(12, 'Jay','Kon','19:30:00',6);"""

cursor3.execute(booking3)
connection3.commit()
print("""A new booking is added in the "Bookings" table.""")

# You can only return two connections back to the pool as the pool_size=2.
# Closing all connections and using try-except to print the pool error if the pool is already full.

from mysql.connector import Error
for connection in [connection1, connection2, connection3]:
    try:
        connection.close()
        print("Connection is returned to the pool")
    except Error as err:
        print("\nConnection can't be returned to the pool")
        print("Error Code:", err.errno)
        print("Error message:", err.msg)

# But First getting a connection from pool_a and creating a cursor object to communicate with the database. 
print("Getting a connection from the pool.")
connection = pool.get_connection()

print("""The object "connection" is created with a connection link from the pool_a""")
print("""Creating a cursor object to communicate with the database.""")

cursor=connection.cursor()
print("""The cursor object "cursor" is created.""")

report_stmt_1 = """
SELECT Name, EmployeeID 
FROM Employees
WHERE Role = 'Manager';
"""

cursor.execute(report_stmt_1)

results=cursor.fetchall()

columns=cursor.column_names

print(columns)
for result in results:
    print(result)

report_stmt_2 = """
SELECT Name, Role
FROM Employees
WHERE Annual_Salary = (SELECT MAX(Annual_Salary) FROM Employees);
"""

cursor.execute(report_stmt_2)

results=cursor.fetchall()

columns=cursor.column_names

print(columns)
for result in results:
    print(result)

report_stmt_3 = """
SELECT COUNT(BookingID) AS number_of_guests
FROM Bookings
WHERE BookingSlot BETWEEN '18:00:00' AND '20:00:00';
"""

cursor.execute(report_stmt_3)

results=cursor.fetchall()

columns=cursor.column_names

print(columns)
for result in results:
    print(result)

report_stmt_4 = """
SELECT CONCAT(Bookings.GuestFirstName, " ", Bookings.GuestLastName) AS GuestFullName, Bookings.BookingID
FROM Bookings
LEFT JOIN Employees 
ON Employees.EmployeeID = Bookings.EmployeeID
WHERE Employees.Role = "Receptionist"
ORDER BY Bookings.BookingSlot DESC;
"""

print("The following guests are waiting to be seated:")

cursor.execute(report_stmt_4)

results=cursor.fetchall()

columns=cursor.column_names

print(columns)
for result in results:
    print(result)

create_basicsalesreport_proc = """
CREATE PROCEDURE BasicSalesReport()
BEGIN
SELECT SUM(BillAmount) AS Total_sales,
AVG(BillAmount) AS Average_sale,
MIN(BillAmount) AS Min_bill_paid,
MAX(BillAmount) AS Max_bill_paid
FROM Orders;
END
"""

cursor.execute(create_basicsalesreport_proc)

cursor.callproc('BasicSalesReport')

results = next(cursor.stored_results())

dataset = results.fetchall()

for column_id in cursor.stored_results():
    cols = [column[0] for column in column_id.description]




