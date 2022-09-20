
import sqlite3

conn = sqlite3.connect('test2.db') #Import SQLLITE3 & connect to the database I created 

with conn: #With connection established, create (if not already created) a table with Integer Primary key and a column for File_Name
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_strings(\
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        File_Name TEXT \
        )")

fileList = ('information.docx', 'Hello.txt', 'myImage.png', 'myMovie.mpg', 'World.txt', 'data.pdf', 'myPhoto.jpg')
#Set the variable filelist with its values


#Run the for loop that identifies which values end in txt and only print those values 
with conn:
    cur = conn.cursor()
    for File_Name in fileList:
        if File_Name.endswith("txt"):
            cur.execute("INSERT INTO tbl_strings(File_Name) VALUES (?)",(File_Name,))
            print(File_Name)

 #This not only identifies the txt files but also adds them to our test database


            
  
