

from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from tkcalendar import Calendar, DateEntry
from PIL import Image , ImageTk
import sqlite3
from database import DataBase
from show_database import TreeViewScroolBar


class InfoEmployees(object):
	def __init__(self,employee):
		self.employee = employee
		self.object_classSqlite3 = DataBase(self.employee)



		
		#------------------------------------------------- Frame Saecrh Aboute Employee -----------------------------------


		self.search_frame = Frame(
			self.employee, width=1660 , height=80 , background='#d9ddf7',
			relief=SUNKEN , bd=2

			).place(x=20,y=88)


	

		self.label_search = Label(
			self.search_frame , text='Please enter the employee"s personal identification number to search for it accurately',
			font=('Bold Oblique',16) , background='#d9ddf7'

			).place(x=90,y=110)



		self.entry_employee_search = Entry(
			self.search_frame , background='#b0c4de' , width=30 , relief=SUNKEN , bd=1 , justify='center',font=('Bold Oblique',18),
			textvariable=self.object_classSqlite3.variable_search_employee

			).place(x=940,y=110)


		


		self.button_search_employee = Button(
			self.search_frame , background='#7aa6bf' , width=12 , height=1 , text='Search Now',font=('Bold Oblique',14) ,
			command=self.object_classSqlite3.search_employee

			).place(x=1380,y=104)






		#==============================Add Frame Delete Employees ===============================



		self.frame_delete =  Frame(
			self.employee, width=1660 , height=80 , background='#ffddf4',padx=10,pady=3,
			relief=RIDGE , bd=2

			).place(x=20,y=170)


		self.lable_delete = Label(
			self.frame_delete , text='Please enter your personal identification number to be able to delete the employee',
			font=('Bold Oblique',16) , background='#ffddf4'

			).place(x=90,y=190)



		self.entry_employee_delete = Entry(
			self.frame_delete , background='#bc8f8f' , width=30 , relief=SUNKEN , bd=1 , justify='center',font=('Bold Oblique',18) , 
			textvariable=self.object_classSqlite3.variable_delete_employee


			).place(x=910,y=190)



		self.button_delete_employee = Button(
			self.frame_delete , background='#ffdab9' , width=12 , height=1 , text='Delete Now',font=('Bold Oblique',14) , pady=2 ,padx=1,command=self.object_classSqlite3.delete_employee
			).place(x=1360,y=187) 








		#=======================================================Frame Add Information Employees ===============================================



		self.frame_information =  Frame(
			self.employee, width=1660 , height=300 , background='#bcd4e6',padx=10,pady=3,
			relief=SUNKEN , bd=2

		
			).place(x=20,y=260)





		self.lable_email = Label(self.frame_information , text='Employee Email'
							 ,font=('Bold Oblique',16) ,background='#bcd4e6'

							 ).place(x=90,y=280)




		self.entry_email = Entry(
			self.employee , width=25 ,font=('Bold Oblique',16) , relief=RAISED , bd=1 ,
			background='#b7e3e0' ,textvariable=self.object_classSqlite3.data_email
			).place(x=270,y=280)




		# #------------------------------------------------------------------------------------------------------------
		self.lable_name = Label(self.employee , text='Employee name'
							 ,font=('Bold Oblique',16) ,background='#bcd4e6'

							 ).place(x=90,y=340)

		self.entry_name = Entry(
			self.employee , width=20 ,font=('Bold Oblique',16) , relief=RAISED , bd=1 ,
			background='#b7e3e0',textvariable=self.object_classSqlite3.data_name

			).place(x=270,y=340)




	#------------------------------------------------------------------------------------------------------------

		self.lable_id = Label(self.employee , text='Employee ID'
							 ,font=('Bold Oblique',16) ,background='#bcd4e6'

							 ).place(x=90,y=408)

		self.entry_id = Entry(
			self.employee , width=14 ,font=('Bold Oblique',16) , relief=RAISED , bd=1 ,
			background='#b7e3e0',justify='center',textvariable=self.object_classSqlite3.data_id 

			).place(x=270,y=408)



		#------------------------------------------------------------------------------------------------------------
		self.lable_age = Label(self.employee , text='Employee age'
							 ,font=('Bold Oblique',16) ,background='#bcd4e6'

							 ).place(x=90,y=480)



		self.entry_age = Entry(
			self.employee , width=10 ,font=('Bold Oblique',16) , relief=RAISED , bd=1 ,
			background='#b7e3e0',justify='center',textvariable=self.object_classSqlite3.data_age
			).place(x=270,y=480)



		#------------------------------------------------------------------------------------------------------------
		self.lable_marital_status = Label(self.employee , text='Marital status'
							 ,font=('Bold Oblique',16) ,background='#bcd4e6'

							 ).place(x=700,y=280)



		self.entry_marital_status = ttk.Combobox(self.employee , justify='center',width=18 ,font=('Bold Oblique',16) ,
			background='#c5eaed',textvariable=self.object_classSqlite3.data_marital_status )


		self.entry_marital_status['values'] = ('Unmarried','Married')
		self.entry_marital_status.place(x=850,y=280)





		#------------------------------------------------------------------------------------------------------------
		self.lable_male = Label(self.employee , text='Gender'
							 ,font=('Bold Oblique',16) ,background='#bcd4e6'

							 ).place(x=700,y=340)



		self.entry_male = ttk.Combobox(self.employee , justify='center',width=14 ,font=('Bold Oblique',16) ,
			background='#c5eaed',textvariable=self.object_classSqlite3.data_gender)
		self.entry_male['values'] = ('Male','Female')
		self.entry_male.place(x=785,y=340)




		
		



		#------------------------------------------------------------------------------------------------------------
		self.lable_city = Label(self.employee , text='Employee City'
							 ,font=('Bold Oblique',16) ,background='#bcd4e6'

							 ).place(x=700,y=408)

		self.entry_city = Entry(
			self.employee , width=14 ,font=('Bold Oblique',16) , relief=RAISED , bd=1 ,
			background='#b7e3e0',justify='center',textvariable=self.object_classSqlite3.data_city
			).place(x=850,y=408) # Current residence




		#------------------------------------------------------------------------------------------------------------
		self.lable_current = Label(self.employee , text='Current residence'
							 ,font=('Bold Oblique',16) ,background='#bcd4e6'

							 ).place(x=700,y=484)

		self.entry_current = Entry(
			self.employee , width=18 ,font=('Bold Oblique',16) , relief=RAISED , bd=1 ,
			background='#b7e3e0',justify='center',textvariable=self.object_classSqlite3.data_current_residence
			).place(x=890,y=484) # Current residence






		#------------------------------------------------------------------------------------------------------------






		self.lable_phone = Label(self.employee , text='Phone number'
							 ,font=('Bold Oblique',16) ,background='#bcd4e6'

							 ).place(x=1160,y=280)

		self.entry_phone = Entry(
			self.employee , width=22 ,font=('Bold Oblique',16) , relief=RAISED , bd=1 ,
			background='#b7e3e0',justify='center',textvariable=self.object_classSqlite3.data_phone
			).place(x=1320,y=280) # Submission date





		

		#------------------------------------------------------------------------------------------------------------
		self.lable_date = Label(self.employee , text='Submission date'
							 ,font=('Bold Oblique',16) ,background='#bcd4e6'

							 ).place(x=1160,y=340)

		self.entry_date = DateEntry(self.employee,selectmode='day',year=2022,month=4,day=15,font=('Bold Oblique',16),textvariable=self.object_classSqlite3.data_submission_date).place(x=1330,y=340)




		#------------------------------------------------------------------------------------------------------------
		self.lable_salary = Label(self.employee , text='Employee Salary'
							 ,font=('Bold Oblique',16) ,background='#bcd4e6'

							 ).place(x=1160,y=408)



		self.entry_salry = Entry(
			self.employee , width=18 ,font=('Bold Oblique',16) , relief=RAISED , bd=1 ,
			background='#b7e3e0',justify='center',textvariable=self.object_classSqlite3.data_salary
			).place(x=1330,y=408) #Academic achievement



		#------------------------------------------------------------------------------------------------------------
		self.lable_achievement = Label(self.employee , text='Academic achievement'
							 ,font=('Bold Oblique',16) ,background='#bcd4e6'

							 ).place(x=1160,y=485)

		self.entry_achievement = Entry(
			self.employee , width=18 ,font=('Bold Oblique',16) , relief=RAISED , bd=1 ,
			background='#b7e3e0',justify='center',textvariable=self.object_classSqlite3.data_academic_achievement
			).place(x=1390,y=485) #Academic achievement



		

		#=========================== Add Frame ScrollBar ===================================================




		#======================================= Frame Buttons ==============================================




		self.frame_buttons = Frame(
			self.employee, width=1660 , height=80 , background='#aed5ef',padx=10,pady=3,
			relief=RIDGE , bd=2

			).place(x=20,y=565)


		self.label_decs = Label(
			self.frame_buttons , text='Employee data control' ,font=('Bold Oblique',16) , fg='#da8a67',
			background='#aed5ef'

			).place(x=90,y=583)


		self.func_insert()
		self.func_update()
		self.func_delete()
		self.func_empty_fields()
		self.func_show_data()



	#======================================= functions Buttons ==========================================



	def func_insert(self):
		''' create button insert data to sqlite3 '''

		self.button_insert = Button(
			self.frame_buttons , background='#00b7eb' , width=12 , height=1 , text='Insert Data',font=('Bold Oblique',14), 
			relief=RIDGE , bd=1 ,command=self.object_classSqlite3.save_data


			).place(x=350,y=580)





	def func_update(self):
		''' create button update data from sqlite3 '''

		self.button_update = Button(
			self.frame_buttons , background='#b9f5b1' , width=12 , height=1 , text='Update Data',font=('Bold Oblique',14), 
			relief=RIDGE , bd=1,command=self.object_classSqlite3.update

			).place(x=650,y=580)


	def func_delete(self):

		''' create button delete data from sqlite3 '''

		self.button_delete = Button(
			self.frame_buttons , background='#ddadaf' , width=12 , height=1 , text='Delete Data',font=('Bold Oblique',14), 
			relief=RIDGE , bd=1,command=self.object_classSqlite3.deleteAlldata


			).place(x=950,y=580) # empty fields


	def func_empty_fields(self):
		''' create button empty fields from data  '''

		self.button_delete = Button(
			self.frame_buttons , background='#fadfad' , width=12 , height=1 , text='Empty fields',font=('Bold Oblique',14), 
			relief=RIDGE , bd=1,command=self.object_classSqlite3.clean_entry

			).place(x=1220,y=580) 


	def func_show_data(self):
		''' create button Shoa All Data from sqlite3   '''

		self.button_delete = Button(
			self.frame_buttons , background='#b2ec5d' , width=12 , height=1 , text='Show Data',font=('Bold Oblique',14), 
			relief=RIDGE , bd=1,command=self.object_classSqlite3.fetch_all_data

			).place(x=1500,y=580) 






