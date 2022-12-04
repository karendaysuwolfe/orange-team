

import mysql.connector

mydb= mysql.connector.connect()
config = {
    "user": "bacchus_user",
    "password": "mysqltest",
    "host": "localhost",
    "database": "bacchus_wine",
    "raise_on_warnings": True
}

db = mysql.connector.connect(**config)

mycursor = db.cursor()

# create employee table
# cursor.execute("CREATE TABLE employee (Employee_ID INT NOT NULL, First_Name VARCHAR(25) NOT NULL, Last_Name VARCHAR(25) NOT NULL, Hire_Date DATE NOT NULL, Start_Date DATE, Active BIT(1) NOT NULL, Department_ID INT NOT NULL, Position_ID INT NOT NULL, PRIMARY KEY(Employee_ID));")

def fill_tables():
    # fill employee table
    employee = ("INSERT INTO employee (Employee_ID, First_Name VARCHAR(25), Last_Name VARCHAR(25), Hire_Date DATE, Start_Date DATE, Active BIT(1), Department_ID INT, Position_ID INT)" 
                "VALUES (%s,%s, %s,%s,%s,%s,%s)")

    values = [
        (6930090, 'Stan', 'Bacchus',	'2019-12-04',	'2019-12-04',	'Y', 1000, 100,),
        (1380275, 'Davis', 'Bacchus', '2019-12-04', '2019-12-04', 'Y', 1000, 100),
        (8613677, 'Elyse', 'Bailey', '1983-08-04', '1983-08-05', 'Y', 4000, 120),
        (4059962, 'Emmanuel', 'Ramsey', '2016-10-07', '2016-10-15', 'Y', 3000, 120),
        (1842386, 'Keira', 'Peck', '1992-08-25', '1992-08-26', 'Y', 6000, 200),
        (5937994, 'Mia', 'Frost', '1999-09-15', '1999-09-16', 'Y', 5000, 200),
        (9685338, 'Amaya', 'Hebert', '2014-01-14', '2014-01-15', 'Y', 2000, 200),
        (7480510, 'Roz', 'Murphy', '2010-03-10', '2010-03-15', 'Y', 3000, 220),
        (8995741, 'Bob', 'Ulrich', '2011-04-25', '2011-04-26', 'Y', 3000, 220),
        (5687918, 'Antwan', 'Cline', '1985-04-16', '1985-04-17', 'Y', 3000, 220),
        (3695025, 'Anyiah', 'Vincent', '1997-11-14', '1997-11-15', 'Y', 3000, 220),
        (5667699, 'Davian', 'Clark', '2003-04-28', '2003-04-29', 'Y', 3000, 220),
        (4180563, 'Deborah', 'Harrell', '2007-08-13', '2007-08-17', 'Y', 3000, 220),
        (9855487, 'Leon', 'Gibbins', '2022-05-19', '2022-05-26', 'Y', 3000, 220),
        (7767463, 'Henry', 'Doyle', '1982-04-02', '1982-04-03', 'Y', 5000, 300),
        (5939049, 'Sara', 'Esparza', '2020-01-22', '2020-01-26', 'Y', 2000, 320),
        (5823178, 'Jordyn', 'Aguilar', '2007-03-05', '2007-03-06', 'Y', 4000, 400),
        (7863543, 'Santiago', 'Branch', '2020-01-29', '2020-02-05', 'Y', 5000, 400),
        (4916879, 'Marley', 'Herring', '2007-09-27', '2007-09-28', 'Y', 5000, 420),
        (5307392, 'Vivian', 'Caldwell', '2011-07-27', '2011-07-28', 'Y', 4000, 420),
        (6383017, 'Janet', 'Collins', '2017-05-15', '2017-05-17', 'Y', 2000, 500),
        (2795091, 'Alisa', 'Franklin', '1988-06-16', '1988-06-17', 'Y', 2000, 500),
        (2799911, 'Trenton', 'Bird', '1990-12-14', '1990-12-15', 'Y', 2000, 500),
        (3021812, 'Adriana', 'Randolph', '2002-02-08', '2002-02-09', 'Y', 2000, 500),
        (7579383, 'Alexus', 'Calhoun', '2006-08-30', '2006-09-05', 'Y', 2000, 500),
        (1944186, 'Maria', 'Costanza', '1983-06-17', '1983-06-18', 'Y', 6000, 600),
        (1314667, 'Carlos', 'Horne', '1995-02-17', '1995-02-18', 'Y', 5000, 600),
        (4145223, 'Parker', 'Hart', '2006-11-02', '2006-11-03', 'Y', 5000, 600)
    ]
    mycursor.executemany(employee, values)
    mydb.commit()
    print(mycursor.rowcount, "rows were insert into employees table")

    # fill employee time worked table

    employee_time_worked = ("INSERT INTO employee_time_worked (Date_Worked DATE, Clock_In_Shift TIME, Clock_Out_Shift TIME, Clock_Out_Break TIME, Clock_In_Break TIME, Clock_Out_Lunch TIME, Clock_In_Lunch TIME, Employee_ID INT)"
                            "VALUES(%s,%s, %s,%s,%s,%s,%s)")

    values = [
    ('2022-11-01',  '07:00:00',  '11:00:00',    'NULL',       'NULL',      'NULL',      'NULL',        '4916879'),
    ('2022-11-02',  '07:00:00',	 '12:00:00',	'10:00:00',	  '10:15:00',  'NULL',	    'NULL',	      '5307392'),
    ('2022-11-03',  '08:00:00',  '16:00:00',    '11:00:00'    '11:15:00',  '13:00:00',  '13:30:00',    '6383017'),
    ('2022-11-04',  '10:00:00',  '15:00:00',    '13:00:00',   '13:15:00',  'NULL',      'NULL',        '2795091'),
    ('2022-11-05',  '10:00:00',  '18:00:00',    '13:00:00',   '13:15:00',  '15:00:00',  '15:30:00',    '2799911'),
    ('2022-11-06',  '11:00:00',  '19:00:00',    '14:00:00',   '14:15:00',  '16:00:00',  '16:30:00',    '3021812'),
    ('2022-11-07',  '13:00:00',  '17:00:00',    'NULL',       'NULL',      'NULL',      'NULL',        '7579383'),
    ('2022-11-08',  '13:00:00',  '21:00:00',    '16:00:00',   '16:15:00',  '18:00:00'   '18:30:00',    '1944186'),
    ('2022-11-09',  '15:00:00',  '20:00:00',    '18:00:00',   '18:15:00',  'NULL',      'NULL',         '1314667'),
    ('2022-11-10',  '17:00:00',  '21:00:00',    'NULL',       'NULL',      'NULL',      'NULL',         '4145223'),

    ]
    mycursor.executemany(employee_time_worked, values)
    mydb.commit()
    print(mycursor.rowcount, "rows were inserted into Employee Time Worked Table")

    # fill position table

    position = ("INSERT INTO position (Position_ID, Position_Title VARCHAR(25), Pay_Grade INT, Hourly BIT(1), Supervisory BIT(1))" 
                "VALUES (%s,%s, %s,%s,%s)")

    values = [
        (100, 'Owner', 'Null', 'N','Y'),
        (120, 'Administrative Assistant', 20, 'Y', 'N'),
        (200, 'Sales', 30, 'N', 'N'),
        (220, 'Marketing', 25, 'N', 'N'),
        (300, 'Production Manager', 23, 'Y', 'Y'),
        (320, 'Production Laborer', 20, 'Y', 'N'),
        (400, 'Maintenance', 20, 'Y', 'N'),
        (420, 'Environmental', 15, 'Y', 'N'),
        (500, 'Accounting / Payroll', 30, 'Y', 'N'),
        (600, 'Logistics', 25, 'Y', 'N'),
    ]
    mycursor.executemany(position, values)
    mydb.commit()
    print(mycursor.rowcount, "row were inserted into position table")

# fill zip code table

    zip_lookup = ("INSERT INTO zip_lookup(Zip INT, City VARCHAR(25), State VARCHAR(10), Country VARCHAR(20))"
                  "VALUES (%s, %s,%s,%s)")

    values = [
        (68111, 'Omaha', 'NE', 'USA'),
        (50310, 'Des Moines', 'IA', 'USA'),
        (53188, 'Waukesha', 'WI', 'USA'),
        (27513, 'Cary', 'NC', 'USA'),
        (52501, 'Ottumwa', 'IA', 'USA'),
        (51537, 'Harland', 'IA', 'USA'),
    ]

    mycursor.executemany(zip_lookup, values)
    mydb.commit()
    print(mycursor.rowcount, "row were inserted into zip table")

# fill department table
    deparment = ("INSERT INTO department(Department_ID INT, Department_Name VARCHAR(15), Department_Head INT (Employee_ID))"
                  "VALUES (%s, %s,%s)")

    values = [
        (1000, 'owners', 6930090),
        (2000, 'Finance', 6383017),
        (3000, 'Marketing', 748051),
        (4000, 'Facilites', 5307392),
        (5000, 'Production', 7767463),
        (6000, 'Distribution', 1944186),
    ]

    mycursor.executemany(deparment, values)
    mydb.commit()
    print(mycursor.rowcount, "row were inserted into department table")

    # employee_alternate

    employee_alternate = ( "INSERT INTO employee_alternate( Stree_Address_1 VARCHAR(35), Stree_Address_1 VARCHAR(35) , Zip INT, Phone_Number VARCHAR(15), Email_Address VARCHAR(45), Term_Date DATE, Term_Reason VARCHAR(25), Rehireable BIT(1), SSN INT UNIQUE, DOB DATE, Employee_ID INT )"
        "VALUES (%s, %s,%s,%s,%s, %s,%s,%s,%s, %s,%s)")

    values = [
    ('3924 Rose Stree',	'NULL', 68111, '402-966-8247',	'Stantheman@gmail.com',	'NULL',	'NULL',	'NULL',	748149274,	'1984-11-11', 6930090),
    ('3205 Pearcy Avenue',	'Apt 10', 68111, '402-826-5015', 'Dbaccu80@yahoo.com',	'NULL',	'NULL',	'NULL',	251345289,	'1965-04-12', 1380275),
    ('826 Westport Avenue',	'NULL',	68111,	'402-372-6785',	'Jcollinshi@yahoo.com',	'NULL',	'NULL',	'NULL',	634587654,	'1996-09-23', 6383017),
    ('70 East Marlborough Avenue',	'NULL',	50310,	'515-392-9069',	'Rozzu4@gmail.com',	'NULL',	'NULL',	'NULL',	214375683,	'1990-10-03', 7480510),
    ('7123 S. Glenwood St',	'NULL',	53188,	'262-601-9735',	'BobbyUl@gmail.com', 'NULL', 'NULL', 'NULL', 963620155,	'1994-04-20', 8995741),
    ('446 North Ave', 'Apt 2',	27513,	'919-195-2072',	'Doyleman@hotmail.com',	'NULL',	'NULL',	'NULL',	135249771,	'1983-07-20', 7767463),
    ('7603 Third Dr', 'Apt 3',	52501, '641-209-9539',	'Dogloverxooxxo@aol.com', 'NULL', 'NULL', 'NULL', 912662242, '1986-07-09', 1944186),
    ('9423 Belmont Street',	'NULL',	51537,	'712-712-7573',	'Catlady44Elyse@gmail.com',	'NULL',	'NULL',	'NULL',	289979667,	'1974-05-23',	8613677),
    ('12 Pineknoll St',	'NULL',	68111,	'402-817-7588',	'Clineantwan@gmail.com',	'NULL',	'NULL',	'NULL',	645881321,	'1997-06-23',	5687918),
    ('3 West Street', 'NULL',	50310,	'515-738-5018',	'AFrankhappy111@icloud.com',	'NULL',	'NULL',	'NULL',91220286,	'2001-12-26',	2795091),
    ('27 Old Colonial Ave',	'NULL',	53188,	'262-523-9023',	'TBird@icloud.com',	'NULL',	'NULL',	'NULL',	338355472,	'1976-10-02',	2799911),
    ('167 Pine St',	'Suite 100',	27513,	'919-577-9325',	'Keirasmail@gmail.com',	'NULL',	'NULL',	'NULL',	817261829,	'1979-08-29',	1842386),
    ('7172 NW. Saxon Ave',	'NULL',	52501,	'641-538-0399',	'C4Horne@yahoo.com',	'NULL',	'NULL',	'NULL',	373644533,	'1977-06-15',	1314667),
    ('69 Sutor Ave',	'NULL',	51537,	'712-575-5087',	'Vinanyiah@aol.com',	'NULL',	'NULL',	'NULL',	844236731,	'1986-02-13',	3695025),
    ('700 Valley Farms Ave',	'NULL',	68111,	'402-335-8005',	'Frosty0mia@icloud.com',	'NULL',	'NULL',	'NULL',	635478765,	'1992-04-16',	5937994),
    ('80 SE. Hillside Road',	'NULL',	50310,	'515-253-1609',	'Adrianadolph@hotmail.com',	'NULL',	'NULL',	'NULL',	475645765,	'1983-01-04',	3021812),
    ('7272C Linden Rd',	'NULL',	53188,	'262-858-7453',	'daviclark4312@aol.com',	'NULL',	'NULL',	'NULL',	870978909,	'2000-09-17',	5667699),
    ('9684 Lees Creek Ave',	'NULL',	27513,	'919-304-6304',	'lexicalhoun99@gmail.com',	'NULL',	'NULL',	'NULL',	125432454,	'1999-01-30',	7579383),
    ('796 Plymouth Street',	'NULL',	52501,	'641-712-6123',	'Parker7Hart@icloud.com',	'NULL',	'NULL',	'NULL',	745667546,	'1992-03-15',	4145223),
    ('82 Roosevelt St',	'NULL',	51537,	'712-433-1562',	'Jord10A@aol.com',	'NULL',	'NULL',	'NULL',	987689879,	'1996-10-24',	5823178),
    ('415 West Henry Smith St',	'NULL',	68111,	'402-674-8021',	'DH4632@gmail.com',	'NULL',	'NULL',	'NULL',	346554634,	'1991-05-23',	4180563),
    ('9774 Birch Hill Rd',	'NULL',	50310,	'515-452-2415',	'herringml76@yahoo.com',	'NULL',	'NULL',	'NULL',	323243324,	'1993-07-09',	4916879),
    ('215 Brookside Avenue',	'NULL',	53188,	'262-848-0672',	'mscaldwel@gmail.com',	'NULL',	'NULL',	'NULL',	524323453,	'1995-10-02',	5307392),
    ('7874 Sunbeam Avenue',	'NULL',	27513,	'919-845-9528',	'alherb2060@icloud.com',	'NULL',	'NULL',	'NULL',	634536455,	'1998-01-21',	9685338),
    ('7848 S. Clark St',	'NULL',	52501,	'641-525-3606',	'Ramseyem49@hotmail.com',	'NULL',	'NULL',	'NULL',	689575689,	'1989-05-04',	4059962),
    ('827 NE. Vine St',	'NULL',	51537,	'712-657-6502',	'Sparzasar0u@icloud.com',	'NULL',	'NULL',	'NULL',	678586756,	'1988-12-13',	5939049),
    ('7 North Bear Hill Ave',	'NULL',	68111,	'402-177-4774',	'branchbrantiago@gmail.com',	'NULL',	'NULL',	'NULL',	520296509,	'1987-03-26',	7863543),
    ('70 North Summerhouse Street',	'NULL',	50310,	'515-974-2114',	'leonbig7474@aol.com',	'NULL',	'NULL',	'NULL',	980123098,	'1985-09-13',	9855487),
]

    mycursor.executemany(employee_alternate, values)
    mydb.commit()
    print(mycursor.rowcount, "row were inserted into employee alternate table")

    supply_order = ("INSERT INTO supply_order(Supply_Order_Id INT, Total_Cost DECIMAL (10,2), Order_Date DATETIME, Order_Method ENUM, Order_Tracking_Number VARCHAR (30), Order_Delivery_Carrier, Order_Estimated_Delivery_Date, Order_Actual_Delivery_Date, Supplier_ID)"
                "VALUES (%s,%s, %s, %s,%s, %s, %s, %s, %s)")

    values = [
    (1111,	'2500.00',	'2022-04-21',	'online',	33783220542444073463,	'USPS',	'2022-04-26',	'2022-04-26', '14:00',	1),
    (2222,	'12,000.00',	'2022-05-21',	'online',	33668316260356970224,	'USPS',	'2022-05-26',	'2022-05-25', '14:30',	1),
    (3333,	'500.00',	'2022-06-21',	'phone',	81102417195194130687,	'UPS',	'2022-06-26',	'2022-06-28', '16:00',	4),
    (4444,	'2,500.00',	'2022-08-21',	'phone',	58613729517346820701,	'FEDEX',	'2022-08-26',	'2022-08-27', '09:00',	3),
    (5555,	'25,000.00',	'2022-10-21',	'phone',	71763449314037379282,	'FEDEX',	'2022-10-26',	'2022-10-24', '11:00',	3),
    (6666,	'20,000.00',	'2022-11-21',	'phone',	84904082002849849284,	'UPS',	'2022-11-26',	'2022-11-30', '16:4',	4),

]
    mycursor.executemany(supply_order, values)
    mydb.commit()
    print(mycursor.rowcount, "row were inserted into suppy_order table")

    wine_order = ("INSERT INTO wine_order_ID(Wine_Order_ID, Wine_ID, Quantity_Ordered)" "VALUES(%s,%s,%s)")

    values = [
        (1154, 1, 100),
        (1155, 2, 100),
        (1156, 3, 100),
        (1157, 4, 100),
        (1158, 5, 10),
        (1159, 6, 40),

    ]
    mycursor.executemany(wine_order, values)
    mydb.commit()
    print(mycursor.rowcount, "row were inserted into wine_order table")

    distributor = ("INSERT INTO distributor(Distributor_ID, Name, Street_Address, Street_Address_2, Zip, Contact_First_Name, Contact_Last_Name, Phone_Number, Email_Address, Active Bit)"
                   "VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)")

    values = [
        (441, 'Hy - vee Wine and Spirits', '14195 Corkey Road', 'NULL', 68111, 'Sally', 'Sanders', 7012329585, 'salsan@hyveeus.com', 'Y'),
        (342, 'A1 Beer and Liquor','693343 Main Street' , 'NULL', 50310, 'John', 'Coleman', 6239256644, 'JColeman@a1liquors.com', 'Y'),
        (775, 'Bakers Grocery', '4298 Merlot Place', 'NULL', 53188, 'Candace', 'Bidson', 5159544232, 'Bidson@bakersdillons.com', 'Y'),
        (889, 'Wine Club Platinum', '9899 Rocket Road', 'NULL', 27513, 'Asher', 'Jones', 7128453980, 'AJones@wineclub.com', 'Y'),
        (442, 'Wine Styles Club', '22 Canary Road', 'NULL', 52501, 'Katie', 'Brown', 3764548878, 'Brown@winestyles.com', 'Y'),
        (332, 'Cheesecake Factory', '555 Cake Drive', 'NULL', 51537, 'Spencer', 'Hilgen', 5315585933, 'hilgen@cheesecake.com', 'Y'),
 
    ]
    mycursor.executemany(distributor, values)
    mydb.commit()
    print(mycursor.rowcount, "row were inserted into distributor table")