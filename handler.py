# import modules
import csv
import pymysql

# function for insert data in Criminal.csv file 
def insertData(data):
    # heading of csv file
    field = ["Criminal-ID", "Address", "Phone", "Name", "Father's Name",
    "Gender", "DOB(yyyy-mm-dd)", "Crimes Done", "Date of Arrest(yyyy-mm-dd)",
    "Place of Arrest"]
    # data of criminal to be written in csv file
    x = [data['Name'], data["Father's Name"], data['Gender'], data['DOB(yyyy-mm-dd)'],
         data['Crimes Done'], data['Date of Arrest(yyyy-mm-dd)'], data["Place of Arrest"] ]
    filen = "Criminal.csv"
    with open(filen, 'w') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(field)
        csvwriter.writerow(x)
        
        
# function for insert data in mysql database
def insertData(data):
    print(data['Name'])
    print(data['Criminal-ID'])
    rowId = 0
    # connecting to the phpmyadmin localhost database
    db = pymysql.connect(host="localhost",user="root",password="",database="criminaldb")
    cursor = db.cursor()
    print("Opened Database")
    print("Database Connected successfully")
    
    # query for insert data into table criminaldata
    query = "INSERT INTO criminaldata VALUES('%s','%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s');" % \
            (data["Criminal-ID"], data["Address"], data["Phone"], data["Name"],
             data["Father's Name"], data["Gender"], data["DOB(yyyy-mm-dd)"],
             data["Crimes Done"], data["Date of Arrest(yyyy-mm-dd)"], data["Place of Arrest"])

    # executing the query 
    cursor.execute(query)
    db.commit()
    rowId = cursor.lastrowid
    
    #confirmation message in terminal
    print("data stored on new row in the database")
    print("Record Created")
    db.close()
    return rowId


