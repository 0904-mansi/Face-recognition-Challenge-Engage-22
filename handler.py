# import modules
import pymysql
        
# function for insert data in mysql database
def insertData(data):
    print(data['Name'])
    print(data['Criminal-ID'])
    rowId = 0
    # connecting to the phpmyadmin localhost database
    db = pymysql.connect(host="localhost",user="root",password="",database="criminaldb")
# db.cursor() Allows Python code to execute sql command in a database session
    cursor = db.cursor()
    print("Opened Database")
    print("Database Connected successfully")
    
    # query for insert data into table criminaldata
    # As the whole query needs to be in a string format while execution of query so %s is used for formatting
    query = "INSERT INTO criminaldata VALUES('%s','%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s');" % \
            (data["Criminal-ID"], data["Address"], data["Phone"], data["Name"],
             data["Father's Name"], data["Gender"], data["DOB(yyyy-mm-dd)"],
             data["Crimes Done"], data["Date of Arrest(yyyy-mm-dd)"], data["Place of Arrest"])

    # executing the query 
    cursor.execute(query)
    # to save changes into database
    db.commit()
    rowId = cursor.lastrowid
    
    #c onfirmation message in terminal
    print("Record Created")
    # close the database
    db.close()
    return rowId


