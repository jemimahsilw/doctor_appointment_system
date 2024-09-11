import mysql.connector as mysql
db = mysql.connect(
    host = "localhost",
#or "127.0.0.1
    user = "root",
    passwd = "",
    database ="doctor_appointment"
)
print(db)
cursor = db.cursor()
#cursor.execute("CREATE DATABASE Doctor_appointment")
#cursor.execute("CREATE TABLE Hospital(ID int(10) NOT NULL AUTO_INCREMENT PRIMARY KEY ,name varchar(255),email char(255),residence varchar(255),postal_address varchar(255),special_quote varchar(255))")

class Hospital:
        print("REGISTER HOSPITAL INTO SYSTEM")
        #public variables :encapsulation
        ID =""
        name = "ZOYA"
        email = "zoya@malawi.ac.mw"
        residence = "machinga in ntaja"
        postal_address = "Zoya hospital,P.O.BOX 31,Machinga,Ntaja"
        special_quote = "we fight wars and we overcome"

obj = Hospital()
#qry1 = "INSERT INTO Hospital (ID,name,email,residence,postal_address,special_quote) VALUES(%s,%s,%s,%s,%s,%s)"
#values = (obj.ID,obj.name,obj.email,obj.residence,obj.postal_address,obj.special_quote)
#cursor.execute(qry1,values)
#db.commit()

class Personnel: #inheritance : hierarchical
    def __init__(self):
     pass
    #public variables: encapsulation
    fullname = "name"
    age = 23
    gender = "gender"
    contact = "phonenumber"
    email = "email"

class Doctor(Personnel): #inheritance : subclass
  def __init__(self,doccode,workhours):
    Personnel.__init__(self)
    #private variables
    self.fullname = Personnel.fullname #variable overriding : polymorphism
    self.age = Personnel.age
    self.gender = Personnel.gender
    self.contact = Personnel.contact
    self.email = Personnel.email
    self.specialization = ""
    self.workhours = workhours
    self.doccode = doccode
  def password(self):
      from random import randint
      letter = ["az","by","cx","dv","et","fs","gq"]
      num = ['132','56','67','7645','68','534']
      char = ['#','$','@','&','*','%']
      return (letter[randint(0,len(letter)-1)]+""+num[randint(0,len(num)-1)]+""+char[randint(0,len(char)-1)])

#cursor.execute("CREATE TABLE Doctor(fullname varchar(255),age int(115),gender varchar(255),email varchar(255),contact varchar(255),workhours int(100),doc_code VARCHAR(255) PRIMARY KEY NOT NULL,specialization varchar(255),password varchar(255))")
doctor1 = Doctor("zoya-100",8)
doctor1.fullname = "Jennifer Miller"
doctor1.age = 24
doctor1.gender = "female"
doctor1.contact = "0999943262"
doctor1.email = "jmiller@yawo.ac"
doctor1.specialization = "cardiology"
doctor1.encrypt = doctor1.password()

#qry2 = "INSERT INTO doctor (fullname,age,gender,email,contact,workhours,doc_code,specialization,password) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
#values = (doctor1.fullname,doctor1.age,doctor1.gender,doctor1.email,doctor1.contact,doctor1.workhours,doctor1.doccode,doctor1.specialization,doctor1.encrypt)
#cursor.execute(qry2,values)
#db.commit()

doctor2 = Doctor("zoya-101",8)
doctor2.fullname = "Isaac Thomson"
doctor2.age = 43
doctor2.gender = "male"
doctor2.contact = "088832453"
doctor2.email = "ithomson@muliko.ac"
doctor2.specialization = "bones"
doctor2.encrypt = doctor2.password()

#qry3 = "INSERT INTO Doctor(fullname,age,gender,email,contact,workhours,doc_code,specialization,password) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
#values = (doctor2.fullname,doctor2.age,doctor2.gender,doctor2.email,doctor2.contact,doctor2.workhours,doctor2.doccode,doctor2.specialization,doctor2.encrypt)
#cursor.execute(qry3,values)
#db.commit()

doctor3 = Doctor("zoya-102",8)
doctor3.fullname = "Thaila lyson"
doctor3.age = 35
doctor3.gender = "female"
doctor3.contact = "0888664532"
doctor3.email = "tlyson@tikule.ac"
doctor3.specialization = "neurosurgeon"
doctor3.encrypt = doctor3.password()

#qry4 = "INSERT INTO Doctor(fullname,age,gender,email,contact,workhours,doc_code,specialization,password) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
#values = (doctor3.fullname,doctor3.age,doctor3.gender,doctor3.email,doctor3.contact,doctor3.workhours,doctor3.doccode,doctor3.specialization,doctor3.encrypt)
#cursor.execute(qry4,values)
#db.commit()

class Patient(Personnel): #inheritance : subclass
    def __init__(self):
        Personnel.__init__(self)
        self.fullname = Personnel.fullname # polymorphism : variable overriding
        self.age = Personnel.age
        self.gender = Personnel.gender
        self.contact = Personnel.contact
        self.email = Personnel.email
        self.sicknessdesc = ""
        self.app_time = ""
    def ticket(self):
     from random import randint
     d = ["su", "mo", "tu", "we", "th", "fr", "sa"]
     t = ['1', '2', '3', '4', '5', '6','7']
     c = ['||', '>', '<', '?', '~', '^','`']
     return (d[randint(0, len(d) - 1)] + "" + c[randint(0, len(c) - 1)] + "" + t[randint(0, len(t) - 1)])

#cursor.execute("CREATE TABLE Patient(fullname varchar(255),age int(115),gender varchar(255),email varchar(255),contact varchar(255),sickness_description varchar(255),ticket_number VARCHAR(255) PRIMARY KEY NOT NULL,best_appointment_time varchar(255))")
patient1 = Patient()
patient1.fullname = "natasha mikelson"
patient1.age = 15
patient1.gender = "female"
patient1.contact = "08452834655"
patient1.email = "nmikelson@mui.ac"
patient1.sicknessdesc = "constant nose bleeding and severe chronical headache as well as dizziness"
patient1.app_time = "1pm"
patient1.num = patient1.ticket()

#qry6 = "INSERT INTO Patient(fullname,age,gender,email,contact,sickness_description,ticket_number,best_appointment_time) VALUES(%s,%s,%s,%s,%s,%s,%s,%s)"
#values = (patient1.fullname,patient1.age,patient1.gender,patient1.email,patient1.contact,patient1.sicknessdesc,patient1.num,patient1.app_time)
#cursor.execute(qry6,values)
#db.commit()


query1 = "SELECT * FROM Hospital"
cursor.execute(query1)
name = cursor.fetchone()[1]
print("=============================================================================================================")
print("                                     WELCOME TO",name,"HOSPITAL                                              ")
print("=============================================================================================================")
n=0
while n<3:
 x = input("WELCOME :\n"
          "1.doctor\n"
          "2.patient\n")
 option = int(x)
 if option == 1:
    p = input("HELLO DOCTOR WOULD YOU LIKE TO :\n"
          "1.register\n"
          "2.view hospital details\n"
          "3.view patients appointments\n")
    choice = int(p)
    if choice == 1:
        doctor4 = Doctor("Zoya-105",8)
        doctor4.fullname = input("enter full name ")
        doctor4.age = input("enter age ")
        doctor4.gender = input("enter your gender ")
        doctor4.contact = input("enter phonenumber ")
        doctor4.email = input("enter your email ")
        doctor4.specialization = input("area of specialization ")
        doctor4.encrypt = doctor4.password()
        qry5 = "INSERT INTO Doctor(fullname,age,gender,email,contact,workhours,doc_code,specialization,password) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        values = (doctor4.fullname,doctor4.age,doctor4.gender,doctor4.email,doctor4.contact,doctor4.workhours,doctor4.doccode,doctor4.specialization,doctor4.encrypt)
        cursor.execute(qry5,values)
        db.commit()

    elif choice == 2:
        print("HOSPITAL DETAILS\n")
        query2 = "SELECT * FROM Hospital"
        cursor.execute(query2)
        list = cursor.fetchone()
        print("NAME :",list[1],"\n")
        print("EMAIL :",list[2],"\n")
        print("RESIDENCE :",list[3],"\n")
        print("POSTAL ADDRESS :",list[4],"\n")
        print("SPECIAL QUOTE :",list[5],"\n")

    elif choice == 3:
        print("PATIENT DETAILS\n")
        query4 = "SELECT * FROM Patient"
        cursor.execute(query4)
        list = cursor.fetchall()
        print(list)

    else:
        print("invalid input")

 elif option == 2:
    m = input("HELLO WOULD YOU LIKE TO :\n"
              "1.register for an appointment\n"
              "2.view hospital details\n"
              "3.view doctor details\n")
    alternative = int(m)
    if alternative == 1:
        patient2 = Patient()
        patient2.fullname = input("enter fullname ")
        patient2.age = input("enter your age ")
        patient2.gender = input("enter gender ")
        patient2.contact = input("enter phonenumber ")
        patient2.email = input("enter email ")
        patient2.sicknessdesc = input("describe the symptoms ")
        patient2.app_time = input("what's the best time to make an appointment ")
        patient2.num = patient2.ticket()
        qry7 = "INSERT INTO Patient(fullname,age,gender,email,contact,sickness_description,ticket_number,best_appointment_time) VALUES(%s,%s,%s,%s,%s,%s,%s,%s)"
        values = (patient2.fullname,patient2.age,patient2.gender,patient2.email,patient2.contact,patient2.sicknessdesc,patient2.num,patient2.app_time)
        cursor.execute(qry7,values)
        db.commit()
        print(" from the ticket your day of appointment: su-sunday; mo-monday; tu-tuesday; we-wednesday; th-thursday; fr-friday; sa-saturday\ntime: the one you have choosen\n "
              "remember to never forget the ticket number cause we require you to showit to us\nticket number:",patient2.num)

    elif alternative == 2:
        print("HOSPITAL DETAILS\n")
        query5 = "SELECT * FROM Hospital"
        cursor.execute(query5)
        list = cursor.fetchone()
        print("NAME :",list[1],"\n")
        print("EMAIL :",list[2],"\n")
        print("RESIDENCE :",list[3],"\n")
        print("POSTAL ADDRESS :",list[4],"\n")
        print("SPECIAL QUOTE :",list[5],"\n")

    elif alternative == 3:
        print("DOCTOR DETAILS\n")
        query6 = "SELECT * FROM Doctor"
        cursor.execute(query6)
        list = cursor.fetchall()
        print(list)

    else:
        print("invalid input")

 print("<=============================================================================================================================>")
 print("THANK YOU FOR YOUR SERVICE")
 print("<=============================================================================================================================>")
 n += 1