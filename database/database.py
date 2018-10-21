#!/usr/bin/python

# =================================================================================
"""

"""
# =================================================================================
from __future__ import print_function
from copy import deepcopy as dcp
#from attribute import Attibute
import db_methods as dbm
from matplotlib import pyplot as plt

class database:
	__Class__=None

	def __init__(self):
		self.name = "omari"
		self.createtime=0
		self.attributes=[]
		self.__selected__att__=[]
		#self.__meta__={}
		self.__export_to_globels__=False
		#
		self.__functions__={}
		self.__method_att__=[]
		#self.n=0

		self.__call__();self.Attribute();self.Attribute().myclass=self
	def __call__(self):
		database.__Class__=self;print(self.attributes)
		#print(__main__.globals())
		#return self
		pass
	def __getattribute__(self, item):
		database.__Class__ = self;
		print(self.attributes)
	def __enter__(self):
		print(self.attributes)
	def __getstate__(self):
		pass
	def __get__(self, instance, owner):
		print(instance.name)
	def __set__(self, instance, value):
		print("omari")


	def __repr__(self):
 		self.__call__()
		return 	"""
        Name of the database %s 
        Number of Attributes %i
        Number of Methods %i"""%(
				self.name,len(self.attributes),len(self.__method_att__))
		

	# ----------------------------------------------------------------------------------------
	class Attribute:
		def __init__(self,Name=""):
			self.name=Name
			self.myclass=None#database.__Class__
		def __call__(self):
			self.myclass=database.__Class__
        
		def Create(self,*args):
			pass

		def Add(self,Data=[]):
			return dbm.addAttribute(self,Data)

		def List(self):
			pass

		def Delete(self):
			dbm.deleteAttribute(self)
			pass

		def Import(self,Data):
			pass

		def Update(self):
			pass

		def Save(self):
			for att in self.myclass.__use_sel_att__():
				self.myclass.__dict__[att].update()


		def Reset(self):
			if self.name in database.__Class__.__dict__.keys():
				database.__Class__.__dict__[self.name].Reset()
				pass
		
		def Select(self,*argu,**kwargs):
			return dbm.SelectAttributes(self,argu,kwargs)
			pass

		def ShortCut(self, Glob=globals(), On=True, Case=0):
			#self.__call__()
			print(self.myclass.attributes)
			"""
				Export the class variables to the globals valible
				Case 0    : list
				Case 1    : Class (Attribue)
				otherwise : Str
			"""
			dbm.ShortCut(self,Glob,On,Case)
			pass

	def __use_sel_att__(self):
		if len(self.__selected__att__) == 0:
			return self.attributes
		return self.__selected__att__


	class Process:
		def __init__(self):
			self.myclass=database.__Class__
			self.__call__()
			pass
		def __call__(self, *args, **kwargs):
			#database.__Class__=self
			pass

		def Filter(self,Condition,AttibuteName=""):
			I = self.myclass.__dict__[AttibuteName].Filter(Condition).__index__
			self.Slice(I)
			return self.myclass

		#@classmethod
		def Slice(self,I=[]):
			for att in self.myclass.__use_sel_att__():
				self.myclass.__dict__[att].Slice(I)
			return self.myclass


	class Operation:
		__Class__=None
		def __init__(self):
			self.myclass=database.__Class__
			self.__call__()
			pass
		def __call__(self, *args, **kwargs):
			Operation.__Class__=self
			pass

		def Table(self):
			pass

		class Export:
			def __init__(self):
				self.myclass = database.__Class__
				pass
			def ToList(self):
				return [self.myclass.__dict__[att].Return() for att in self.myyclass.__use_sel_att__()]

		class Import:
			pass

		class Share:
			pass

	# ----------------------------------------------------------------------------------------
	def Return(self):
		return [self.__dict__[att].Return() for att in self.__use_sel_att__()]
	
	# ------------------------------------------------------------------------------------------
	class Method:
		"""

		"""
		def __init__(self,Function):
			#print(dir(Function))
			self.function=Function
			self.name = Function.__name__
			self.myclass = database.__Class__
			pass

		@property
		def Add(self):
			return dbm.addMethod(self)
			pass

		@property
		def Delete(self):
			dbm.deleteMethod(self)
			pass


		def Select(self,*args,**kwargs):
			pass

		def Execute(self):
			pass

		pass

	class Function:
		def __init__(self):
			self.myclass=database.__Class__
			pass
		def add(self):
			pass
		def remove(self):
			pass
		def execute(self):
			pass
		pass

	class Plot:

		def __init__(self,x):
			self.myclass = database.__Class__
			self.figures=[]
			self.x=x
			pass
		def Vs(self,y,*args,**kwargs):
			return plt.plot(self.myclass.__dict__[self.x].Return(),self.myclass.__dict__[y].Return*())










def ImportFromFile(filename="19p.xlsx"):
	from xlrd import open_workbook
	wb = open_workbook(filename)
	sheet=wb.sheet_by_index(0)
	rowdata=[]
	for col in range(sheet.ncols):
		rowdata.append(sheet.col_values(colx=col))
		pass
	return rowdata

	
	

if __name__=="__main__":
#	A=Attibute()
#	A.value=[x for x in range(100)]
#	print(A.Filter(lambda x:x>1).Return())
#	print(A.Filter(lambda x:50>x>5).Return())
#	print(A.value)
#	A.Reset()
#	print(A.value)
	#B=ImportFromFile()
	A=database()
	def Fun(self):
		print ("OMARI -->",dir(self))
#	print(Fun.func_name)
	A.Method(Fun).Add
	A.Fun()
	A.Attribute("X").Add(list(range(100)))
	A.Attribute("Y").Add(A.X.Map(lambda x:2*x+1).Return())

	#print(A.Omari.Filter(lambda x:x>5).Return())
	#print(A.Omari.Return())
	B=database()
	#print(B.attributes)
	print(A.attributes)
	def Fun2(self):
		print("Hellow Word")
	#B.Method(Fun2).Add
	#B.Fun2()
	A.Fun();A.Attribute().ShortCut(globals())