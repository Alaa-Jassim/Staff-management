
from ast import Str
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import os , sys , shutil
import sqlite3
import time
from tkcalendar import Calendar, DateEntry
from tkinter import messagebox
from PIL import Image , ImageTk
from datetime import datetime
from information_employees import InfoEmployees
from save_data_employees.save_data import SaveData 


class Main(object):
	""" Main Class """
	def __init__(self,root):
		self.root = root

		self.root.geometry('1700x900+100+20')
		self.root.resizable(width=False , height=False)
		self.root.configure(background='#dbf0f0')

		self.root.title('Employee Management System')

		self.object_class_save = SaveData(self.root)
		
		

		#-----------------Add frame title to show main app title ---------------------------



		self.title_frame = Frame(
			self.root , background='#87cefa' ,
			width=1660  , height=80 ,
			

			).place(x=20,y=4)

	


		self.title_app = Label(
			self.root , background='#87cefa' ,
			width=30 , height=1 , text='MANAGEMENT EMPLOYEE SYSTEM',font=('Bold Oblique',22) 

			).place(x=580,y=20)

	

		#------------------- Recall the class (InfoEmployees) to show the buttons and fields in this same interface until it is turned on ----------


		self.class_info_employees = InfoEmployees(self.root)
		"""  Recall the class (InfoEmployees) to show the buttons and fields in this same interface until it is turned on"""

		self.add_time()
		""" Calck Function Add Time Show In Main Class """



	#-----------------Add Time Function ---------------------------
		
	def add_time(self):

		self.date = datetime.now()
		self.date_now = self.date.strftime('%Y-%m-%d')
		self.label_date = Label(self.title_frame , text=f'{self.date_now}',
			font=('Impact, fantasy',20) ,background='#87cefa' 

			).place(x=70,y=20)


		self.clock_time = datetime.now()
		self.string_time = self.clock_time.strftime('%H:%M:%S %p')


		self.label_clock_time = Label(self.title_frame ,
										background='#87cefa'  ,
										font=('Impact, fantasy',20),
										text=f'{self.string_time}').place(x=1450,y=20)
		self.root.after(1000, self.add_time)



if __name__ == '__main__':
	window = Tk()
	object_class = Main(window)
	window.mainloop()
