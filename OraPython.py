#Code Reference --> https://www.oracle.com/database/technologies/appdev/python/quickstartpythononprem.html 
import getpass
import oracledb
# python -m pip install oracledb

connection = oracledb.connect(
    user="SCOTT",
    password="TIGER",
    dsn="localhost/ORCL")

print("Oracle Database Connection Sucessfull")

cursor = connection.cursor()



# drop the table customtask
cursor.execute("""
    begin
        execute immediate 'drop table customtask';
        exception when others then if sqlcode <> -942 then raise; end if;
    end;""")

# Create the table customtask

cursor.execute("""
    create table customtask (
        task_id number generated always as identity,
        task_description varchar2(256),
        task_timestamp timestamp with time zone default current_timestamp,
        task_status number(1,0),
        primary key (task_id))""")

# Insert some data

rows = [ ("Task 10001", 1 ),
         ("Task 10035", 0 ),
         ("Task 10093", 0 ),
         ("Task 10104", 0 ),
         ("Task 11001", 0 ),
         ("Task 11025", 0 ),
         ("Task 11027", 1 ),
         ("Task 11139", 0 ),
         ("Task 12101", 0 ),
         ("Task 13601", 0 ),		 
         ("Task 14801", 1 ) ]

cursor.executemany("insert into customtask (task_description, task_status) values(:1, :2)", rows)
print(cursor.rowcount, "Rows Inserted")

connection.commit()

# Query the Tasks 
for row in cursor.execute('select task_description, task_status from customtask'):
    if (row[1]):
        print(row[0], "has completed ")
    else:
        print(row[0], "has not completed")

#Fetch the Data in Python 
cursor.execute(""" select * from customtask """)
#print(cursor.rowcount, "Rows Inserted for SELECT")       
results = cursor.fetchall()
print(cursor.rowcount, "Rows Returned for SELECT after call to FetchAll") 
for row in results:
    print(row)

# Close the cursor and the database connection
cursor.close()
connection.close()
