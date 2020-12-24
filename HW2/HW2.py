First_Name=input("Enter First Name:")
Last_Name=input("Enter Last Name:")
Date_Of_Birth=input("Enter Date Of Birth(Just Year):")
Age=2020-int(Date_Of_Birth)

users=[]
users.append([First_Name,Last_Name,Date_Of_Birth,Age])

for i in users:
	print(i)
	if i[3]<18:
		print("You can't go out because it's too dangerous")
	else:
		print("You can go to the street")
				