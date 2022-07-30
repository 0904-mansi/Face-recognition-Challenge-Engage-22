# import modules
import pymysql
        
# function for insert data in mysql database        
def insertData(data):
    print(data['Name'])
    print(data['Report-ID'])
    rowId = 0
    # connecting to the phpmyadmin localhost database
    db = pymysql.connect(host="localhost",user="root",password="",database="criminaldb")
    cursor = db.cursor()
    print("Opened Database")
    print("Database Connected successfully")
    # query for insert data into table missingdata 
    # As the whole query needs to be in a string format while execution of query so %s is used for formatting
    query = "INSERT INTO missingdata VALUES('%s','%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s');" % \
            (data["Report-ID"], data["Name"], data["Father's Name"], data["Address"],
             data["Phone"], data["Gender"], data["DOB(yyyy-mm-dd)"],
             data["Identification"], data["Date of Missing(yyyy-mm-dd)"], data["Place of Missing"])

    
    # executing the query
    cursor.execute(query)
     # saving the changes into database
    db.commit()
    rowId = cursor.lastrowid
    #confirmation message in terminal
    print("Record Created")
     # closing the database
    db.close()
    return rowId


