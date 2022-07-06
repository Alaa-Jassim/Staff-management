

from tkinter import *
from tkinter import filedialog
from tkinter import ttk
import os , sys , shutil
import sqlite3
import csv
class SaveData(object):
	def __init__(self,save):
		self.save = save 

		self.menubar = Menu(self.save)
		self.file = Menu(self.menubar,tearoff=False)
		self.file.add_command(label='Save As')

		self.menubar.add_cascade(label='save the form',command=self.open_file)
		self.save.config(menu=self.menubar)


	def open_file(self):
		self.con = sqlite3.connect('EmployeesDataBase.db')
		self.curs = self.con.cursor()

		self.res = self.curs.execute('SELECT * FROM Employees')
		self.data = self.res.fetchall()

		self.columns = [
	'Email','Name','ID','Age',
	'marital_status','Gender','City',
	'Current_residence','Phone','Submission_date','Salary','Academic'
]


		self.path = filedialog.asksaveasfilename(initialdir = "C:\\",title = "Save As",filetypes = ("csv files",'csv files(*.*)'))

		with open(f'{self.path}.csv','w') as self.file :
			self.file = csv.writer(self.file)

			self.file.writerow(self.columns)
			self.file.writerows(self.data)
