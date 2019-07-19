import  mysql.connector

connection = mysql.connector.connect(host="localhost", user="root", password="1234", database="practice")
studentCursor = connection.cursor()

print("Enter Student Information")
name = input("Enter Name: ")
email = input("Enter Email: ")


insertedRecord = studentCursor.callproc("insert_user", [name, email])
connection.commit()

print(insertedRecord);

studentCursor.execute("select * from users")

print("Student Information.")
print()

for student in studentCursor:
  print("Id: " + str(student[0]))
  print("Name: " + student[1])
  print("Email: " + student[2])
  print()

connection.close()