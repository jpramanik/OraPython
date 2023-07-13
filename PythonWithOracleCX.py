import cx_Oracle

# Establish a connection to the Oracle database
dsn = cx_Oracle.makedsn('localhost', '1521', service_name='<ORCL>')
conn = cx_Oracle.connect(user=r'SCOTT', password='TIGER', dsn=dsn)

# Create a cursor to execute SQL queries
cursor = conn.cursor()

print("success")

# Execute the query to retrieve the top 10 values from the customer table
cursor.execute("SELECT * FROM CUSTOMER_TABLE ORDER BY CUST_ID ASC FETCH FIRST 5 ROWS ONLY")
results = cursor.fetchall()

# Print the retrieved data
for row in results:
    print(row)

# Close the cursor and the database connection
cursor.close()
conn.close()
