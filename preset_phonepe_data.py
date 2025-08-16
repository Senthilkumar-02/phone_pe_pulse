import mysql.connector

print("PhonePe Preset Data Store")

# MySQL connection
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="123456",  # replace with your password
    database="phonepe_data"
)

cursor = conn.cursor()

#Aggregated user table Creation
Agg_User_Table = """
        CREATE TABLE IF NOT EXISTS Agg_User_Table (
    State VARCHAR(100),
    Year int,
    Quarter int,
    User_brand_type VARCHAR(100),
    Users_count bigint,
    Users_Percentage DECIMAL(5,2)
)
        """
		
		
		
Agg_Trans_Table = """
        CREATE TABLE IF NOT EXISTS Agg_Trans_Table (
    State VARCHAR(100),
    Year int,
    Quarter int,
    Transaction_type VARCHAR(100),
    Transaction_count bigint,
    Transaction_amount bigint
)
        """
		
		
Agg_Ins_Table = """
        CREATE TABLE IF NOT EXISTS Agg_Ins_Table (
    State VARCHAR(100),
    Year int,
    Quarter int,
    Transaction_type VARCHAR(100),
    Transaction_count bigint,
    Transaction_amount bigint
)
        """
		
Map_Ins_Table = """
        CREATE TABLE IF NOT EXISTS Map_Ins_Table (
    State VARCHAR(100),
	Year int,
    Quarter int,
    Dist_Name VARCHAR(100),
    Transaction_count bigint,
    Transaction_amount bigint
)
        """
		

Map_User_Table = """
        CREATE TABLE IF NOT EXISTS Map_User_Table (
    State VARCHAR(100),
    Year int,
    Quarter int,
    Dist_Name VARCHAR(100),
    RegisteredUser bigint,
    AppOpens bigint
)
        """
		
		
		
Map_Trans_Table = """
        CREATE TABLE IF NOT EXISTS Map_Trans_Table (
	State VARCHAR(100),
    Year int,
    Quarter int,
    Dist_Name VARCHAR(100),
    Transaction_count bigint,
    Transaction_amount bigint
)
        """
		
		
		


Top_Ins_Table = """
        CREATE TABLE IF NOT EXISTS Top_Ins_Table (
    State VARCHAR(100),
	Year int,
    Quarter int,
    Pincodes VARCHAR(100),
    Transaction_count bigint,
    Transaction_amount bigint
)
        """
		

Top_User_Table = """
        CREATE TABLE IF NOT EXISTS Top_User_Table (
    State VARCHAR(100),
    Year int,
    Quarter int,
    Pincodes VARCHAR(100),
    RegisteredUser bigint
)
        """
		
		
		
Top_Trans_Table = """
        CREATE TABLE IF NOT EXISTS Top_Trans_Table (
	State VARCHAR(100),
    Year int,
    Quarter int,
    Pincodes VARCHAR(100),
    Transaction_count bigint,
    Transaction_amount bigint
)
        """



Top_Ins_Dist_Table = """
        CREATE TABLE IF NOT EXISTS Top_Ins_Dist_Table (
    State VARCHAR(100),
	Year int,
    Quarter int,
    Dist_Name VARCHAR(100),
    Transaction_count bigint,
    Transaction_amount bigint
)
        """
		

Top_User_Dist_Table = """
        CREATE TABLE IF NOT EXISTS Top_User_Dist_Table (
    State VARCHAR(100),
    Year int,
    Quarter int,
    Dist_Name VARCHAR(100),
    RegisteredUser bigint
)
        """
		
		
		
Top_Trans_Dist_Table = """
        CREATE TABLE IF NOT EXISTS Top_Trans_Dist_Table (
	State VARCHAR(100),
    Year int,
    Quarter int,
    Dist_Name VARCHAR(100),
    Transaction_count bigint,
    Transaction_amount bigint
)
        """
		
		

cursor.execute(Agg_User_Table)
cursor.execute(Agg_Trans_Table)
cursor.execute(Agg_Ins_Table)
cursor.execute(Map_User_Table)
cursor.execute(Map_Trans_Table)
cursor.execute(Map_Ins_Table)
cursor.execute(Top_User_Table)
cursor.execute(Top_Trans_Table)
cursor.execute(Top_Ins_Table)
cursor.execute(Top_User_Dist_Table)
cursor.execute(Top_Trans_Dist_Table)
cursor.execute(Top_Ins_Dist_Table)

conn.commit()

