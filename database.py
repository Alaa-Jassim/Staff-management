


from tkinter import *
from tkinter import messagebox
import sqlite3
from show_database import TreeViewScroolBar
from show_database import *


class DataBase(object):
    def __init__(self,data):
    	self.data = data 
    	self.create_database()

    	self.object_classTreeview = TreeViewScroolBar(self.data)
    	self.object_classTreeview.add_dataToTreeveiw()

    
    	self.object_classTreeview.table_data.bind('<ButtonRelease-1>',self.get_cursor)
    	


    	self.data_email = StringVar()
    	self.data_name = StringVar()
    	self.data_id = StringVar()
    	self.data_age = StringVar()


    	self.data_marital_status = StringVar()
    	self.data_gender = StringVar()
    	self.data_city = StringVar()
    	self.data_current_residence = StringVar()


    	self.data_phone = StringVar()
    	self.data_submission_date = StringVar()
    	self.data_salary = StringVar()
    	self.data_academic_achievement = StringVar()


    	self.variable_delete_employee = StringVar()
    	self.variable_search_employee = StringVar()








    def create_database(self):
    	self.connection = sqlite3.connect('EmployeesDataBase.db')
    	self.cursor = self.connection.cursor()


    	self.cursor.execute(
			''' CREATE TABLE IF NOT EXISTS Employees
			(Email TEXT NOT NULL ,
			Name TEXT NOT NULL ,
			ID TEXT NOT NULL ,
			Age TEXT NOT NULL ,
			marital_status TEXT NOT NULL ,
			Gender TEXT NOT NULL ,
			City TEXT NOT NULL ,
			Current_residence TEXT NOT NULL ,
			Phone TEXT NOT NULL ,
			Submission_date TEXT NOT NULL ,
			Salary TEXT NOT NULL ,
			Academic_achievement TEXT NOT NULL 
			)''')

    	self.connection.commit()
    	self.connection.close()



    def save_data(self):
    	""" Get data from class information_employess and Save The Data in SQlite3 """

    	if self.data_email.get() == '':
    		messagebox.showerror('Error','Error The field cannot be left Email blank')
    	elif self.data_name.get() == '':
    		messagebox.showerror('Error','Error The field cannot be left Name blank')
    	elif self.data_id.get() == '':
    		messagebox.showerror('Error','Error The field cannot be left ID blank')
    	elif self.data_age.get() == '':
    		messagebox.showerror('Error','Error The field cannot be left Age blank')



    	elif self.data_marital_status.get() == '':
    		messagebox.showerror('Error','Error The field cannot be left marital status blank')
    	elif self.data_gender.get() == '':
    		messagebox.showerror('Error','Error The field cannot be left Gender blank')
    	elif self.data_city.get() == '':
    		messagebox.showerror('Error','Error The field cannot be left City blank')
    	elif self.data_current_residence.get() == '':
    		messagebox.showerror('Error','Error The field cannot be left Current Residence blank')



    	elif self.data_phone.get() == '':
    		messagebox.showerror('Error','Error The field cannot be left Number Phone blank')
    	elif self.data_submission_date.get() == '':
    		messagebox.showerror('Error','Error The field cannot be left Submission Date blank')
    	elif self.data_salary.get() == '':
    		messagebox.showerror('Error','Error The field cannot be left Salary blank')
    	elif self.data_academic_achievement.get() == '':
    		messagebox.showerror('Error','Error The field cannot be left Academic achievement blank')

    	else :
    		self.con_checkID = sqlite3.connect('EmployeesDataBase.db')
    		self.curs_checkID = self.con_checkID.cursor()

    		self.curs_checkID.execute('SELECT * FROM Employees WHERE ID =?',(self.data_id.get(),))
    		if self.curs_checkID.fetchall() :
    			messagebox.showerror('Invalid ID','The personal identification number is already in use Please enter a valid number ')
    		else :
    			self.messageTrue = messagebox.askquestion('The data is correct','Do you want to save your data in the database?')
    			if self.messageTrue == 'yes':
    				self.insert_data() 



    
    	

    def insert_data(self):
	    self.connection_save = sqlite3.connect('EmployeesDataBase.db')
	    self.cursor_save = self.connection_save.cursor()

	    self.cursor_save.execute(
	    			''' INSERT INTO Employees 

	    	(Email , Name , ID , Age ,
	    	marital_status ,Gender ,City,
	    	Current_residence ,Phone,Submission_date,
	    	Salary ,Academic_achievement
	    	)VALUES (?,?,?,?,?,?,?,?,?,?,?,?)''',

	    	(self.data_email.get() , self.data_name.get() , self.data_id.get() , self.data_age.get(),
	    	self.data_marital_status.get() ,self.data_gender.get() , self.data_city.get() , self.data_current_residence.get(),
	    	self.data_phone.get(),self.data_submission_date.get() , self.data_salary.get() , self.data_academic_achievement.get())

			)

	    self.connection_save.commit()

	    self.data_email.set('') ; self.data_name.set('') ; self.data_id.set('') ; self.data_age.set('') ;
	    self.data_marital_status.set('') ; self.data_gender.set('') ; self.data_city.set('') ; self.data_current_residence.set('')

	    self.data_phone.set('') ; self.data_submission_date.set('') ; self.data_salary.set('') ; self.data_academic_achievement.set('')


	    #================ Call Class TreeViewScroolBar ==============

	    self.object_classTreeview.add_dataToTreeveiw()
	    self.connection_save.close()



    def delete_employee(self):
    	""" The Function Is Delete One  Employee data from database And from table Treeview"""

    	self.con_delete = sqlite3.connect('EmployeesDataBase.db')
    	self.curs_delete = self.con_delete.cursor()
    	self.curs_delete.execute('SELECT * FROM Employees WHERE ID =?',(self.variable_delete_employee.get(),))

    	if not self.curs_delete.fetchall():
    		messagebox.showerror('There are no search results','Please check the employee"s ID correctly')
    	else:
    		self.message_employee_delete = messagebox.askquestion('Do you agree','Do you agree to this action? The selected employee will be deleted?')

    		if self.message_employee_delete == 'yes':
    			self.curs_delete.execute('DELETE  FROM Employees WHERE ID =?',(self.variable_delete_employee.get(),))

    	self.con_delete.commit()
    	self.object_classTreeview.add_dataToTreeveiw()
    	self.con_delete.close()


    #=================================================================================================================================


    def search_employee(self):
    	""" The Function Search Data Employees from DataBase """
    	self.conn_search = sqlite3.connect('EmployeesDataBase.db')
    	self.curs_search = self.conn_search.cursor()

    	self.curs_search.execute('SELECT * FROM Employees WHERE ID =?',(self.variable_search_employee.get(),))
    	self.result_search = self.curs_search.fetchall()

    	if not self.result_search:
    		messagebox.showerror('There are no search results','Please use ID Correct And try Again') 
    	else :
    		self.curs_search.execute('SELECT * FROM Employees WHERE ID =?',(self.variable_search_employee.get(),))

    		self.object_classTreeview.table_data.delete(*self.object_classTreeview.table_data.get_children())

    		for self.row in self.result_search :
    			self.object_classTreeview.table_data.insert('',END,value=self.row)

    	self.conn_search.commit()
    	self.conn_search.close()


# here =================================================================


    def fetch_all_data(self):
    	""" The Function Show All Data """
    	self.con_all_data = sqlite3.connect('EmployeesDataBase.db')
    	self.curs_all_data = self.con_all_data.cursor()

    	self.curs_all_data.execute('SELECT * FROM Employees')
    	if self.curs_all_data.fetchall():
    		self.object_classTreeview.add_dataToTreeveiw()
    	
    	self.con_all_data.commit()
    	self.con_all_data.close()


    def get_cursor(self,ev):
        """ Get Cursor Data From Table  """

        try :

	        self.cursor_row = self.object_classTreeview.table_data.focus()
	        self.contents = self.object_classTreeview.table_data.item(self.cursor_row)
	        self.row = self.contents['values']


	        self.data_email.set(self.row[0]) ; self.data_name.set(self.row[1]) ;
	        self.data_id.set(self.row[2]) ; self.data_age.set(self.row[3]) ;
	        self.data_marital_status.set(self.row[4]) ; self.data_gender.set(self.row[5]) ;

	        self.data_city.set(self.row[6]);self.data_current_residence.set(self.row[7]);
	        self.data_phone.set(self.row[8]) ; self.data_submission_date.set(self.row[9]);
	        self.data_salary.set(self.row[10]) ; self.data_academic_achievement.set(self.row[11])

        except Exception as error :
            pass



    def update(self):
    	""" The Function Update All Data """
    	self.con_update = sqlite3.connect('EmployeesDataBase.db')
    	self.curs_update = self.con_update.cursor()

    	self.curs_update.execute(
    		'''UPDATE Employees SET Email=? , Name=? ,Age=? ,marital_status=?,
    		Gender=? ,City=?,Current_residence=?,Phone=?,Submission_date=?,Salary=?,Academic_achievement=? WHERE ID=?


    		''',(self.data_email.get(),self.data_name.get() , self.data_age.get(),
    			self.data_marital_status.get(),self.data_gender.get(),self.data_city.get(),
    			self.data_current_residence.get(),self.data_phone.get(),self.data_submission_date.get(),
    			self.data_salary.get(),self.data_academic_achievement.get(),self.data_id.get())

    		)

    	if self.curs_update :
    		self.curs_update.execute('SELECT * FROM Employees')
    		self.object_classTreeview.table_data.delete(*self.object_classTreeview.table_data.get_children())

    		for self.row in self.curs_update.fetchall() :
    			self.object_classTreeview.table_data.insert('',END,value=self.row)
    	else :
    		messagebox.showerror('Error!','Wrong Please do not change the employee ID number')

    	self.con_update.commit()
    	self.con_update.close()



    def clean_entry(self):
    	""" Clean Entry from data"""
    	self.data_email.set('') ; self.data_name.set('') ;
    	self.data_id.set('') ; self.data_age.set('') ;
    	self.data_marital_status.set('') ; self.data_gender.set('') ;

    	self.data_city.set('');self.data_current_residence.set('');
    	self.data_phone.set('') ; self.data_submission_date.set('');
    	self.data_salary.set('') ; self.data_academic_achievement.set('')



    def deleteAlldata(self):
    	""" Function Delete Al Data from SQlite3"""
    	self.conn_delete_all = sqlite3.connect('EmployeesDataBase.db')
    	self.curs_delete_all = self.conn_delete_all.cursor()

    	
    	self.messageDeleteAll = messagebox.askquestion('Are you sure','Are you sure to perform this operation, all employees will be deleted?')
    	if self.messageDeleteAll == 'yes':
    		self.curs_delete_all.execute('DELETE FROM Employees')
    		self.object_classTreeview.table_data.delete(*self.object_classTreeview.table_data.get_children())

    		for self.row in self.curs_delete_all.fetchall() :
    			self.object_classTreeview.table_data.insert('',END,value=self.row)

    	self.conn_delete_all.commit()
    	# self.object_classTreeview.add_dataToTreeveiw()
    	self.conn_delete_all.close()




