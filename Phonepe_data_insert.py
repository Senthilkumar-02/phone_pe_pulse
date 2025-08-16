import pandas as pd
import mysql.connector
import json
import os


# MySQL connection
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="123456",  # replace with your password
    database="phonepe_data"
)


cursor = conn.cursor()


#Aggregated Transaction Table Insert


path="C:/Users/WELCOME/Documents/Phone_pe/pulse/data/aggregated/transaction/country/india/state/"
Agg_state_list=os.listdir(path)
    #Agg_state_list

clm={'State':[], 'Year':[],'Quarter':[],'Transaction_type':[], 'Transaction_count':[], 'Transaction_amount':[]}

for i in Agg_state_list:
    p_i=path+i+"/"
    Agg_yr=os.listdir(p_i)
    for j in Agg_yr:
        p_j=p_i+j+"/"
        Agg_yr_list=os.listdir(p_j)
        for k in Agg_yr_list:
            p_k=p_j+k
            Data=open(p_k,'r')
            D=json.load(Data)
            for z in D['data']['transactionData']:
                Name=z['name']
                count=z['paymentInstruments'][0]['count']
                amount=z['paymentInstruments'][0]['amount']
                clm['Transaction_type'].append(Name)
                clm['Transaction_count'].append(count)
                clm['Transaction_amount'].append(amount)
                clm['State'].append(i)
                clm['Year'].append(j)
                clm['Quarter'].append(int(k.strip('.json')))

Agg_Trans=pd.DataFrame(clm)


Agg_Trans["State"] = Agg_Trans["State"].str.replace("andaman-&-nicobar-islands","Andaman & Nicobar")
Agg_Trans["State"] = Agg_Trans["State"].str.replace("-"," ")
Agg_Trans["State"] = Agg_Trans["State"].str.title()
Agg_Trans['State'] = Agg_Trans['State'].str.replace("Dadra & Nagar Haveli & Daman & Diu", "Dadra and Nagar Haveli and Daman and Diu")
    
insert_query = """
                INSERT INTO Agg_Trans_Table 
    (State, Year, Quarter, Transaction_type, Transaction_count, Transaction_amount) 
    VALUES (%s, %s, %s, %s, %s, %s)
                """
    #data=tuple(Agg_User)
data = [
    tuple(row)
    for row in Agg_Trans[["State", "Year", "Quarter", "Transaction_type", "Transaction_count", "Transaction_amount"]].values
    ]

cursor.executemany(insert_query, data)


#Aggregated Insurance Table Insert



path1="C:/Users/WELCOME/Documents/Phone_pe/pulse/data/aggregated/insurance/country/india/state/"
Agg_state_list1=os.listdir(path1)
    #Agg_state_list

clm1={'State':[], 'Year':[],'Quarter':[],'Transaction_type':[], 'Transaction_count':[], 'Transaction_amount':[]}

for i in Agg_state_list1:
    p_i1=path1+i+"/"
    Agg_yr1=os.listdir(p_i1)
    for j in Agg_yr1:
        p_j1=p_i1+j+"/"
        Agg_yr_list1=os.listdir(p_j1)
        for k in Agg_yr_list1:
            p_k1=p_j1+k
            Data1=open(p_k1,'r')
            D1=json.load(Data1)
            for z in D1['data']['transactionData']:
                Name=z['name']
                count=z['paymentInstruments'][0]['count']
                amount=z['paymentInstruments'][0]['amount']
                clm1['Transaction_type'].append(Name)
                clm1['Transaction_count'].append(count)
                clm1['Transaction_amount'].append(amount)
                clm1['State'].append(i)
                clm1['Year'].append(j)
                clm1['Quarter'].append(int(k.strip('.json')))

Agg_Ins=pd.DataFrame(clm1)

Agg_Ins["State"] = Agg_Ins["State"].str.replace("andaman-&-nicobar-islands","Andaman & Nicobar")
Agg_Ins["State"] = Agg_Ins["State"].str.replace("-"," ")
Agg_Ins["State"] = Agg_Ins["State"].str.title()
Agg_Ins['State'] = Agg_Ins['State'].str.replace("Dadra & Nagar Haveli & Daman & Diu", "Dadra and Nagar Haveli and Daman and Diu")

insert_query1 = """
                INSERT INTO Agg_Ins_Table 
    (State, Year, Quarter, Transaction_type, Transaction_count, Transaction_amount) 
    VALUES (%s, %s, %s, %s, %s, %s)
                """
    #data=tuple(Agg_User)
data1 = [
    tuple(row)
    for row in Agg_Ins[["State", "Year", "Quarter", "Transaction_type", "Transaction_count", "Transaction_amount"]].values
    ]

cursor.executemany(insert_query1, data1)


#Aggregated User Table Insert


path2="C:/Users/WELCOME/Documents/Phone_pe/pulse/data/aggregated/user/country/india/state/"
Agg_state_list2=os.listdir(path2)
    #Agg_state_list

clm2={'State':[], 'Year':[],'Quarter':[],'User_brand_type':[], 'Users_count':[], 'Users_Percentage':[]}

for i in Agg_state_list2:
    p_i2=path2+i+"/"
    Agg_yr2=os.listdir(p_i2)
    for j in Agg_yr2:
        p_j2=p_i2+j+"/"
        Agg_yr_list2=os.listdir(p_j2)
        for k in Agg_yr_list2:
            p_k2=p_j2+k
            Data2=open(p_k2,'r')
            D2=json.load(Data2)
            for z in (D2.get('data', {}).get('usersByDevice') or []):
                        Name=z['brand']
                        count=z['count']
                        percentage=z['percentage']
                        clm2['User_brand_type'].append(Name)
                        clm2['Users_count'].append(count)
                        clm2['Users_Percentage'].append(percentage)
                        clm2['State'].append(i)
                        clm2['Year'].append(j)
                        clm2['Quarter'].append(int(k.strip('.json')))

Agg_User=pd.DataFrame(clm2)

Agg_User["State"] = Agg_User["State"].str.replace("andaman-&-nicobar-islands","Andaman & Nicobar")
Agg_User["State"] = Agg_User["State"].str.replace("-"," ")
Agg_User["State"] = Agg_User["State"].str.title()
Agg_User['State'] = Agg_User['State'].str.replace("Dadra & Nagar Haveli & Daman & Diu", "Dadra and Nagar Haveli and Daman and Diu")


insert_query2 = """
                INSERT INTO Agg_User_Table 
    (State, Year, Quarter, User_brand_type, Users_count, Users_Percentage) 
    VALUES (%s, %s, %s, %s, %s, %s)
                """
    #data=tuple(Agg_User)
data2 = [
    tuple(row)
    for row in Agg_User[["State", "Year", "Quarter", "User_brand_type", "Users_count", "Users_Percentage"]].values
    ]

cursor.executemany(insert_query2, data2) 


#Map Insurance Table Insert
   

path3="C:/Users/WELCOME/Documents/Phone_pe/pulse/data/map/insurance/hover/country/india/state/"
Map_state_list=os.listdir(path3)
    #Agg_state_list

clm3={'State':[], 'Year':[],'Quarter':[],'Dist_Name':[], 'Transaction_count':[], 'Transaction_amount':[]}

for i in Map_state_list:
    p_i3 = os.path.join(path3, i)
    Map_yr = os.listdir(p_i3)
    
    for j in Map_yr:
        p_j3 = os.path.join(p_i3, j)
        Map_yr_list = os.listdir(p_j3)
        
        for k in Map_yr_list:
            p_k3 = os.path.join(p_j3, k)
            with open(p_k3, 'r') as Data3:
                D3 = json.load(Data3)
                for z in D3["data"]["hoverDataList"]:
                    name = z['name']
                    count = z['metric'][0]['count']
                    amount = z['metric'][0]['amount']

                    clm3['Dist_Name'].append(name)
                    clm3['Transaction_count'].append(count)
                    clm3['Transaction_amount'].append(amount)
                    clm3['State'].append(i)
                    clm3['Year'].append(j)
                    clm3['Quarter'].append(int(k.strip('.json')))

# Create DataFrame
Map_ins = pd.DataFrame(clm3)

Map_ins["State"] = Map_ins["State"].str.replace("andaman-&-nicobar-islands","Andaman & Nicobar")
Map_ins["State"] = Map_ins["State"].str.replace("-"," ")
Map_ins["State"] = Map_ins["State"].str.title()
Map_ins['State'] = Map_ins['State'].str.replace("Dadra & Nagar Haveli & Daman & Diu", "Dadra and Nagar Haveli and Daman and Diu")

Map_ins["Dist_Name"] = (
    Map_ins["Dist_Name"]
    .str.replace("district", "", case=False, regex=False)  # Remove "district" (case insensitive)
    .str.strip()                                            # Remove leading/trailing spaces
    .str.title()                                            # Convert to Title Case
)


insert_query3 = """
                INSERT INTO Map_ins_Table 
    (State, Year, Quarter, Dist_Name, Transaction_count, Transaction_amount) 
    VALUES (%s, %s, %s, %s, %s, %s)
                """
    #data=tuple(Map_ins)
data3 = [
    tuple(row)
    for row in Map_ins[["State", "Year", "Quarter", "Dist_Name", "Transaction_count", "Transaction_amount"]].values
    ]

cursor.executemany(insert_query3, data3)


#Map Transaction Table Insert


path4="C:/Users/WELCOME/Documents/Phone_pe/pulse/data/map/transaction/hover/country/india/state/"
Map_state_list1=os.listdir(path4)

clm4={'State':[], 'Year':[],'Quarter':[],'Dist_Name':[], 'Transaction_count':[], 'Transaction_amount':[]}

for i in Map_state_list1:
    p_i4 = os.path.join(path4, i)
    Map_yr1 = os.listdir(p_i4)
    
    for j in Map_yr1:
        p_j4 = os.path.join(p_i4, j)
        Map_yr_list1 = os.listdir(p_j4)
        
        for k in Map_yr_list1:
            p_k4 = os.path.join(p_j4, k)
            with open(p_k4, 'r') as Data4:
                D4 = json.load(Data4)
                for z in D4["data"]["hoverDataList"]:
                    name = z['name']
                    count = z['metric'][0]['count']
                    amount = z['metric'][0]['amount']

                    clm4['Dist_Name'].append(name)
                    clm4['Transaction_count'].append(count)
                    clm4['Transaction_amount'].append(amount)
                    clm4['State'].append(i)
                    clm4['Year'].append(j)
                    clm4['Quarter'].append(int(k.strip('.json')))

# Create DataFrame
Map_Trans = pd.DataFrame(clm4)

Map_Trans["State"] = Map_Trans["State"].str.replace("andaman-&-nicobar-islands","Andaman & Nicobar")
Map_Trans["State"] = Map_Trans["State"].str.replace("-"," ")
Map_Trans["State"] = Map_Trans["State"].str.title()
Map_Trans['State'] = Map_Trans['State'].str.replace("Dadra & Nagar Haveli & Daman & Diu", "Dadra and Nagar Haveli and Daman and Diu")

Map_Trans["Dist_Name"] = (
    Map_Trans["Dist_Name"]
    .str.replace("district", "", case=False, regex=False)  # Remove "district" (case insensitive)
    .str.strip()                                            # Remove leading/trailing spaces
    .str.title()                                            # Convert to Title Case
)



insert_query4 = """
                INSERT INTO Map_trans_Table 
    (State, Year, Quarter, Dist_Name, Transaction_count, Transaction_amount) 
    VALUES (%s, %s, %s, %s, %s, %s)
                """
    #data=tuple(Map_Trans)
data4 = [
    tuple(row)
    for row in Map_Trans[["State", "Year", "Quarter", "Dist_Name", "Transaction_count", "Transaction_amount"]].values
    ]

cursor.executemany(insert_query4, data4)


#Map User Table Insert


path5="C:/Users/WELCOME/Documents/Phone_pe/pulse/data/map/user/hover/country/india/state/"
Map_state_list2=os.listdir(path5)

clm5={'State':[], 'Year':[],'Quarter':[],'Dist_Name':[], 'RegisteredUser':[], 'AppOpens':[]}

for i in Map_state_list2:
    p_i5 = os.path.join(path5, i)
    Map_yr2 = os.listdir(p_i5)
    
    for j in Map_yr2:
        p_j5 = os.path.join(p_i5, j)
        Map_yr_list2 = os.listdir(p_j5)
        
        for k in Map_yr_list2:
            p_k5 = os.path.join(p_j5, k)
            with open(p_k5, 'r') as Data5:
                D5 = json.load(Data5)
                for z in D5["data"]["hoverData"].items():
                    name = z[0]
                    count = z[1]["registeredUsers"]
                    amount = z[1]["appOpens"]

                    clm5['Dist_Name'].append(name)
                    clm5['RegisteredUser'].append(count)
                    clm5['AppOpens'].append(amount)
                    clm5['State'].append(i)
                    clm5['Year'].append(j)
                    clm5['Quarter'].append(int(k.strip('.json')))

# Create DataFrame
Map_User = pd.DataFrame(clm5)

Map_User["State"] = Map_User["State"].str.replace("andaman-&-nicobar-islands","Andaman & Nicobar")
Map_User["State"] = Map_User["State"].str.replace("-"," ")
Map_User["State"] = Map_User["State"].str.title()
Map_User['State'] = Map_User['State'].str.replace("Dadra & Nagar Haveli & Daman & Diu", "Dadra and Nagar Haveli and Daman and Diu")
Map_User["Dist_Name"] = (
    Map_User["Dist_Name"]
    .str.replace("district", "", case=False, regex=False)  # Remove "district" (case insensitive)
    .str.strip()                                            # Remove leading/trailing spaces
    .str.title()                                            # Convert to Title Case
)



insert_query5 = """
                INSERT INTO Map_user_Table 
    (State, Year, Quarter, Dist_Name, RegisteredUser, AppOpens) 
    VALUES (%s, %s, %s, %s, %s, %s)
                """
    #data=tuple(Map_User)
data5 = [
    tuple(row)
    for row in Map_User[["State", "Year", "Quarter", "Dist_Name", "RegisteredUser", "AppOpens"]].values
    ]

cursor.executemany(insert_query5, data5)


#Top Transaction Table Insert



path6="C:/Users/WELCOME/Documents/Phone_pe/pulse/data/top/transaction/country/india/state/"
Top_state_list=os.listdir(path6)

clm6={'State':[], 'Year':[],'Quarter':[],'Pincodes':[], 'Transaction_count':[], 'Transaction_amount':[]}
clm9={'State':[], 'Year':[],'Quarter':[],'Dist_Name':[], 'Transaction_count':[], 'Transaction_amount':[]}
for i in Top_state_list:
    p_i6 = os.path.join(path6, i)
    Top_yr = os.listdir(p_i6)
    
    for j in Top_yr:
        p_j6 = os.path.join(p_i6, j)
        Top_yr_list = os.listdir(p_j6)
        
        for k in Top_yr_list:
            p_k6 = os.path.join(p_j6, k)
            with open(p_k6, 'r') as Data6:
                D6 = json.load(Data6)
                districts_list = [d["entityName"] for d in D6["data"]["districts"]]
                pincodes_list = D6["data"]["pincodes"]
                for z,district in zip(pincodes_list, districts_list):
                    name = z["entityName"]
                    count = z["metric"]["count"]
                    amount = z["metric"]["amount"]

                    clm6['Pincodes'].append(name)
                    clm6['Transaction_count'].append(count)
                    clm6['Transaction_amount'].append(amount)
                    clm6['State'].append(i)
                    clm6['Year'].append(j)
                    clm6['Quarter'].append(int(k.strip('.json')))
                    clm9['Dist_Name'].append(district)
                    clm9['Transaction_count'].append(count)
                    clm9['Transaction_amount'].append(amount)
                    clm9['State'].append(i)
                    clm9['Year'].append(j)
                    clm9['Quarter'].append(int(k.strip('.json')))

# Create DataFrame
Top_trans = pd.DataFrame(clm6)
Top_trans_dist= pd.DataFrame(clm9)

Top_trans["State"] = Top_trans["State"].str.replace("andaman-&-nicobar-islands","Andaman & Nicobar")
Top_trans["State"] = Top_trans["State"].str.replace("-"," ")
Top_trans["State"] = Top_trans["State"].str.title()
Top_trans['State'] = Top_trans['State'].str.replace("Dadra & Nagar Haveli & Daman & Diu", "Dadra and Nagar Haveli and Daman and Diu")


Top_trans_dist["State"] = Top_trans_dist["State"].str.replace("andaman-&-nicobar-islands","Andaman & Nicobar")
Top_trans_dist["State"] = Top_trans_dist["State"].str.replace("-"," ")
Top_trans_dist["State"] = Top_trans_dist["State"].str.title()
Top_trans_dist['State'] = Top_trans_dist['State'].str.replace("Dadra & Nagar Haveli & Daman & Diu", "Dadra and Nagar Haveli and Daman and Diu")
Top_trans_dist["Dist_Name"] = (
    Top_trans_dist["Dist_Name"]
    .str.replace("district", "", case=False, regex=False)  # Remove "district" (case insensitive)
    .str.strip()                                            # Remove leading/trailing spaces
    .str.title()                                            # Convert to Title Case
)


insert_query6 = """
                INSERT INTO top_trans_Table 
    (State, Year, Quarter, Pincodes, Transaction_count, Transaction_amount) 
    VALUES (%s, %s, %s, %s, %s, %s)
                """

insert_query9 = """
                INSERT INTO top_trans_dist_Table 
    (State, Year, Quarter, Dist_Name, Transaction_count, Transaction_amount) 
    VALUES (%s, %s, %s, %s, %s, %s)
                """
    #data=tuple(Top_trans)
data6 = [
    tuple(row)
    for row in Top_trans[["State", "Year", "Quarter", "Pincodes", "Transaction_count", "Transaction_amount"]].values
    ]

data9 = [
    tuple(row)
    for row in Top_trans_dist[["State", "Year", "Quarter", "Dist_Name", "Transaction_count", "Transaction_amount"]].values
    ]

cursor.executemany(insert_query6, data6)
cursor.executemany(insert_query9, data9)

#Top Insurance Table Insert




path7="C:/Users/WELCOME/Documents/Phone_pe/pulse/data/top/insurance/country/india/state/"
Top_state_list1=os.listdir(path7)

clm7={'State':[], 'Year':[],'Quarter':[],'Pincodes':[], 'Transaction_count':[], 'Transaction_amount':[]}
clm10={'State':[], 'Year':[],'Quarter':[],'Dist_Name':[], 'Transaction_count':[], 'Transaction_amount':[]}
for i in Top_state_list1:
    p_i7 = os.path.join(path7, i)
    Top_yr1 = os.listdir(p_i7)
    
    for j in Top_yr1:
        p_j7 = os.path.join(p_i7, j)
        Top_yr_list1 = os.listdir(p_j7)
        
        for k in Top_yr_list1:
            p_k7 = os.path.join(p_j7, k)
            with open(p_k7, 'r') as Data7:
                D7 = json.load(Data7)
                districts_list = [d["entityName"] for d in D7["data"]["districts"]]
                pincodes_list = D7["data"]["pincodes"]
                for z,district in zip(pincodes_list, districts_list):
                    name = z["entityName"]
                    count = z["metric"]["count"]
                    amount = z["metric"]["amount"]

                    clm7['Pincodes'].append(name)
                    clm7['Transaction_count'].append(count)
                    clm7['Transaction_amount'].append(amount)
                    clm7['State'].append(i)
                    clm7['Year'].append(j)
                    clm7['Quarter'].append(int(k.strip('.json')))
                    clm10['Dist_Name'].append(district)
                    clm10['Transaction_count'].append(count)
                    clm10['Transaction_amount'].append(amount)
                    clm10['State'].append(i)
                    clm10['Year'].append(j)
                    clm10['Quarter'].append(int(k.strip('.json')))
                    #print(district)

# Create DataFrame
Top_ins = pd.DataFrame(clm7)
Top_ins_dist= pd.DataFrame(clm10)

Top_ins["State"] = Top_ins["State"].str.replace("andaman-&-nicobar-islands","Andaman & Nicobar")
Top_ins["State"] = Top_ins["State"].str.replace("-"," ")
Top_ins["State"] = Top_ins["State"].str.title()
Top_ins['State'] = Top_ins['State'].str.replace("Dadra & Nagar Haveli & Daman & Diu", "Dadra and Nagar Haveli and Daman and Diu")



Top_ins_dist["State"] = Top_ins_dist["State"].str.replace("andaman-&-nicobar-islands","Andaman & Nicobar")
Top_ins_dist["State"] = Top_ins_dist["State"].str.replace("-"," ")
Top_ins_dist["State"] = Top_ins_dist["State"].str.title()
Top_ins_dist['State'] = Top_ins_dist['State'].str.replace("Dadra & Nagar Haveli & Daman & Diu", "Dadra and Nagar Haveli and Daman and Diu")

Top_ins_dist["Dist_Name"] = (
    Top_ins_dist["Dist_Name"]
    .str.replace("district", "", case=False, regex=False)  # Remove "district" (case insensitive)
    .str.strip()                                            # Remove leading/trailing spaces
    .str.title()                                            # Convert to Title Case
)


insert_query7 = """
                INSERT INTO top_ins_Table 
    (State, Year, Quarter, Pincodes, Transaction_count, Transaction_amount) 
    VALUES (%s, %s, %s, %s, %s, %s)
                """

insert_query10 = """
                INSERT INTO top_ins_dist_Table 
    (State, Year, Quarter, Dist_Name, Transaction_count, Transaction_amount) 
    VALUES (%s, %s, %s, %s, %s, %s)
    """
    #data=tuple(Top_ins)
data7 = [
    tuple(row)
    for row in Top_ins[["State", "Year", "Quarter", "Pincodes", "Transaction_count", "Transaction_amount"]].values
    ]


data10 = [
    tuple(row)
    for row in Top_ins_dist[["State", "Year", "Quarter", "Dist_Name", "Transaction_count", "Transaction_amount"]].values
    ]

cursor.executemany(insert_query7, data7)
cursor.executemany(insert_query10, data10)



#Top User Table Insert



path8="C:/Users/WELCOME/Documents/Phone_pe/pulse/data/top/user/country/india/state/"
Top_state_list2=os.listdir(path8)

clm8={'State':[], 'Year':[],'Quarter':[],'Pincodes':[], 'RegisteredUser':[]}
clm11={'State':[], 'Year':[],'Quarter':[],'Dist_Name':[], 'RegisteredUser':[]}


for i in Top_state_list2:
    p_i8 = os.path.join(path8, i)
    Top_yr2 = os.listdir(p_i8)
    
    for j in Top_yr2:
        p_j8 = os.path.join(p_i8, j)
        Top_yr_list2 = os.listdir(p_j8)
        
        for k in Top_yr_list2:
            p_k8 = os.path.join(p_j8, k)
            with open(p_k8, 'r') as Data8:
                D8 = json.load(Data8)
                districts_list = [d["name"] for d in D8["data"]["districts"]]
                pincodes_list = D8["data"]["pincodes"]
                for z,district in zip(pincodes_list, districts_list):
                    name = z["name"]
                    user_count = z["registeredUsers"]

                    clm8['Pincodes'].append(name)
                    clm8['RegisteredUser'].append(user_count)
                    clm8['State'].append(i)
                    clm8['Year'].append(j)
                    clm8['Quarter'].append(int(k.strip('.json')))
                    clm11['Dist_Name'].append(district)
                    clm11['RegisteredUser'].append(user_count)
                    clm11['State'].append(i)
                    clm11['Year'].append(j)
                    clm11['Quarter'].append(int(k.strip('.json')))

# Create DataFrame
Top_user = pd.DataFrame(clm8)
Top_user_dist = pd.DataFrame(clm11)

Top_user["State"] = Top_user["State"].str.replace("andaman-&-nicobar-islands","Andaman & Nicobar")
Top_user["State"] = Top_user["State"].str.replace("-"," ")
Top_user["State"] = Top_user["State"].str.title()
Top_user['State'] = Top_user['State'].str.replace("Dadra & Nagar Haveli & Daman & Diu", "Dadra and Nagar Haveli and Daman and Diu")


Top_user_dist["State"] = Top_user_dist["State"].str.replace("andaman-&-nicobar-islands","Andaman & Nicobar")
Top_user_dist["State"] = Top_user_dist["State"].str.replace("-"," ")
Top_user_dist["State"] = Top_user_dist["State"].str.title()
Top_user_dist['State'] = Top_user_dist['State'].str.replace("Dadra & Nagar Haveli & Daman & Diu", "Dadra and Nagar Haveli and Daman and Diu")

Top_user_dist["Dist_Name"] = (
    Top_user_dist["Dist_Name"]
    .str.replace("district", "", case=False, regex=False)  # Remove "district" (case insensitive)
    .str.strip()                                            # Remove leading/trailing spaces
    .str.title()                                            # Convert to Title Case
)



insert_query8 = """
                INSERT INTO top_user_Table 
    (State, Year, Quarter, Pincodes, RegisteredUser) 
    VALUES (%s, %s, %s, %s, %s)
                """


insert_query11 = """
                INSERT INTO top_user_dist_Table 
    (State, Year, Quarter, Dist_Name, RegisteredUser) 
    VALUES (%s, %s, %s, %s, %s)
                """
    #data=tuple(Top_user)
data8 = [
    tuple(row)
    for row in Top_user[["State", "Year", "Quarter", "Pincodes", "RegisteredUser"]].values
    ]


data11 = [
    tuple(row)
    for row in Top_user_dist[["State", "Year", "Quarter", "Dist_Name", "RegisteredUser"]].values
    ]

cursor.executemany(insert_query8, data8)
cursor.executemany(insert_query11, data11)

print("Executed All")    

conn.commit()