import pandas as pd
import mysql.connector

# Connect to MySQL database
db = mysql.connector.connect(
    host="barcodepipeline-staging-barcodepipelinedbcluster-kang6zjkf533.cluster-cnxxecorhlum.us-east-1.rds.amazonaws.com",
    user="masteruser",
    password="pass",
    database="barcodepipelinedb"
)

# Excel file path
excel_file = "Prime_Pantry_catalog_trimmed.xlsx"

# Sheet name in the Excel file
sheet_name = "in"

# Read the Excel file into a pandas DataFrame
df = pd.read_excel(excel_file, sheet_name=sheet_name)

# Iterate over the rows in the DataFrame
for _, row in df.iterrows():
    # Get the values from the row
    col1 = row['barcode']
    col2 = row['name']
    col3 = row['url']
    col4 = row['price']
    col5 = row['salestitan_medicine_name']


    # Create a cursor object to execute SQL queries
    cursor = db.cursor()

    # Define the SQL query to insert a row into the MySQL table
    sql = "INSERT INTO warehouse_medicine (uuid, warehouse_uuid, barcode, name, image_url, price, flag_p, flag_d, flag_rm, flag_rc, salestitan_medicine_name) VALUES (UUID(),'b69c0b9b-14f8-11ee-9b71-0adfaed9a19d', %s, %s, %s, '$%s',0,0,0,0, %s)"

    # Execute the SQL query with the row values
    cursor.execute(sql, (col1, col2, col3, col4, col5))


    # Commit the changes to the database
    db.commit()

# Close the database connection
db.close()
