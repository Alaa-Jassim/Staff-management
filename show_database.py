

from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import sqlite3


class TreeViewScroolBar(object):
	""" The Class show Data from SQlite3 In Table Treeview And Add Frame ScrollBar """
	def __init__(self,data_treeview):
		self.data_treeview = data_treeview

		self.frame_scroll = Frame(
            self.data_treeview, width=1660 , height=240 , relief=GROOVE , bd=1,
            background='#ecf7e0'
            ).place(x=10,y=650)



		self.scroll_x = Scrollbar(self.frame_scroll , orient=HORIZONTAL)
		self.scroll_y = Scrollbar(self.frame_scroll , orient=VERTICAL)


		self.table_data = ttk.Treeview(self.frame_scroll,
                columns=('Email','Name','ID','Age','Marital status','Gender','City','Current residence','Phone','Submission date','Salary','Academic achievement'),
                xscrollcommand=self.scroll_x.set ,
                yscrollcommand=self.scroll_y.set
                )

		self.table_data.place(x=20,y=650,width=1660,height=230)

		self.scroll_x.pack(side=BOTTOM,fill=X)
		self.scroll_y.pack(side=LEFT,fill=Y)


		self.table_data['show'] = 'headings'
		self.table_data.heading('Email',text='Email')
		self.table_data.heading('Name',text='Name')
		self.table_data.heading('ID',text='ID')
		self.table_data.heading('Age',text='Age')



		self.table_data.heading('Marital status',text='Marital status')
		self.table_data.heading('Gender',text='Gender')
		self.table_data.heading('City',text='City')
		self.table_data.heading('Current residence',text='Current residence')


		self.table_data.heading('Phone',text='Phone')
		self.table_data.heading('Submission date',text='Submission date')
		self.table_data.heading('Salary',text='Salary')
		self.table_data.heading('Academic achievement',text='Academic achievement')



		#========================================================================================


		self.table_data.column('Email',width=20,anchor=CENTER)
		self.table_data.column('Name',width=20,anchor=CENTER)
		self.table_data.column('ID',width=3,anchor=CENTER)
		self.table_data.column('Age',width=2,anchor=CENTER)


		self.table_data.column('Marital status',width=5,anchor=CENTER)
		self.table_data.column('Gender',width=4,anchor=CENTER)
		self.table_data.column('City',width=6,anchor=CENTER)
		self.table_data.column('Current residence',width=8,anchor=CENTER)


		self.table_data.column('Phone',width=10,anchor=CENTER)
		self.table_data.column('Submission date',width=8,anchor=CENTER)
		self.table_data.column('Current residence',width=8,anchor=CENTER)
		self.table_data.column('Salary',width=6,anchor=CENTER)
		self.table_data.column('Academic achievement',width=4,anchor=CENTER)
		
	

	def add_dataToTreeveiw(self):
		""" The Function Add data To Treeview table """
		self.connection_veiw_data = sqlite3.connect('EmployeesDataBase.db')
		self.cursor_veiw_data = self.connection_veiw_data.cursor()


		self.cursor_veiw_data.execute(''' SELECT * FROM Employees''')
		self.rows = self.cursor_veiw_data.fetchall()

		if len(self.rows) != 0 :
			self.table_data.delete(*self.table_data.get_children())

			for self.row in self.rows :
				self.table_data.insert('',END,value=self.row)

		self.connection_veiw_data.commit()
		self.connection_veiw_data.close()





        





