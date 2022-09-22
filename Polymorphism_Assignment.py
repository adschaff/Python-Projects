
#Create two classes that inherit from another class.
    #each child should have at least two of their own attributes.
    #The parent class should have at least one method (function).
    #Both child classes should utilize polymorphism on the parent class method.
    #Add comments throughout your Python explaining your code.



#Parent class -- High School
class Main_HighSchool:
    Type = "Admin"
    ID_Number = 53351
    Login_Type = "admin"
    email = "admin@admin.com"

    def getLoginInfo(self):
        entry_email = input("Enter your email:")
        entry_type = input("Enter your role:")
        if (entry_email == self.email and entry_type == admin):
            print("Welcome into the admin portal!")
        else:
            print("You are not allowed entry.")


#Child Class Student - difference being that this for a student instead of admin and has two new attributes
class Student(Main_HighSchool):
    Type = "Student"
    grade = 12
    Student_Login = "student"
    
     
    def getLoginInfo(self):
        entry_email = input("Enter your email:")
        entry_type = input("Enter your role:")
        if (entry_email == self.email and entry_type == Student_Login):
            print("Welcome into the student portal!")
        else:
            print("You are not allowed entry.")


#Child Class Teacher  difference being that this for a student instead of admin and has two new attributes
class Teacher(Main_HighSchool):
    Type = "Teacher"
    Subject = 'English'
    Teacher_Login = "student"
    
     
    def getLoginInfo(self):
        entry_email = input("Enter your email:")
        entry_type = input("Enter your role:")
        if (entry_email == self.email and entry_type == Teacher_Login):
            print("Welcome into the Teacher portal!")
        else:
            print("You are not allowed entry.")


