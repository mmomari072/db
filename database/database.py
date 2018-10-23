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
from matplotlib import pylab as plb

class database:
#	__Class__=self.__class__
	__myclass__=[]
	def __last_myclass_(self):
		if len(database.__myclass__)==1:
			return database.__myclass__[0]
		elif len(database.__myclass__)>1:
			return database.__myclass__[-1]
		pass

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
		self.n=0

		self.__export_self_to_main_class__()
#		self.__call__();self.Attribute();
#        self.Attribute().myclass=self

		self.Attribute = __attribute_method__(Class=self)
		self.Process   = __process_method__(self)
		self.Operation = __operation_method__(self)
		self.Method    = __method_method__(self)
		self.Plot      = __plot__(self)



	def __export_self_to_main_class__(self):
		database.__myclass__.append(self)

	def __call__(self,Attribute):
		#database.__Class__=self;
		#print(self.attributes)
		#print(__main__.globals())
		#return self
		self.n+=1
		print("wth")
		return self.__dict__[Attribute]
		pass
	def Reset(self):
		for att in self.Attribute.__use_selected_att__():
			self.__dict__[att].Reset()
			pass

	'''
	def attribute(self):
		return __attribute_method__(Class=self)
		pass

	def process(self):
		return __process_method__(self)
		pass
	'''
	'''
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
	'''






# ================================================================================
class __process_method__:
	def __init__(self,Class):
		self.myclass=Class
		self.__call__()
		pass
	def __call__(self, *args, **kwargs):
		#database.__Class__=self
		pass

	def Filter(self,Condition,AttibuteName=""):
		I = self.myclass.__dict__[AttibuteName].Filter(Condition).__index__
		self.myclass.__dict__[AttibuteName].Reset()
		self.Slice(I)
		return self.myclass

	#@classmethod
	def Slice(self,I=[]):
		for att in self.myclass.Attribute.__use_selected_att__():
			self.myclass.__dict__[att].Slice(I)
		return self.myclass

# ================================================================================
class __method_method__:
	"""

	"""
	def __init__(self,Class):
		self.myclass=Class
		pass

	def Function(self,Function):
		#print(dir(Function))
		self.function=Function
		self.name = Function.__name__
		#self.myclass=database.__myclass__[-1]#database.__Class__
		return self
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
# ================================================================================
class __operation_method__:
	__Class__=None
	def __init__(self,Class):
		self.myclass=Class#database.__myclass__[-1]#database.__Class__
		self.__call__()
		pass
	def __call__(self, *args, **kwargs):
		#		Operation.__Class__=self
		pass

	def Table(self):
		pass

	class Export:
		def __init__(self):
			self.myclass=database.__myclass__[-1]#database.__Class__
			pass
		def ToList(self):
			return [self.myclass.__dict__[att].Return() for att in self.myyclass.__use_sel_att__()]

	class Import:
		pass

	class Share:
		pass
# ================================================================================
class __attribute_method__:
	def __init__(self,Class):
		self.name = None
		self.myclass = Class;  # __myclass__[-1]#database.__Class__
		self.selected_att_list=[]
		self.attribute_list=[]
		pass

	def __call__(self,Name):
		self.Name(Name)
		return self
		pass

	def Create(self, *args):
		pass

	def Name(self,Name):
		self.name=Name
		return self

	def Add(self, Data=[]):
		return dbm.addAttribute(self, Data)

	def List(self):
		pass

	def Delete(self):
		dbm.deleteAttribute(self)
		pass

	def Import(self, Data):
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

	def Select(self, *argu, **kwargs):
		return dbm.SelectAttributes(self, argu, kwargs)
		pass

	def __use_selected_att__(self):
		if len(self.selected_att_list) !=0:
			return self.selected_att_list
		return self.attribute_list

	def ShortCut(self, Glob=globals(), On=True, Case=0):
		# self.__call__()
		print(self.myclass.attributes)
		"""
			Export the class variables to the globals valible
			Case 0    : list
			Case 1    : Class (Attribue)
			otherwise : Str
		"""
		dbm.ShortCut(self, Glob, On, Case)
		pass


class __plot__:
	def __init__(self,Class):
		self.myclass=Class
		pass
	def __call__(self,x, *args, **kwargs):
		self.Plot(x)
		pass
	def Plot(self,x="X",*args):
		X = self.myclass.__dict__[x]()
		for att in self.myclass.Attribute.__use_selected_att__():
			if att == x:
				continue
			plb.plot(X,self.myclass(att)())
			pass
		self.Update
	@property
	def Update(self):
		plb.draw()




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
	A.Method.Function(Fun).Add
	A.Fun()
	#A.Attribute("X").Add(list(range(100)))
	#A.Attribute("Y").Add(A.X.Map(lambda x:2*x+1).Return())

	#print(A.Omari.Filter(lambda x:x>5).Return())
	#print(A.Omari.Return())
	B=database()
	#print(B.attributes)
	print(A.attributes)
	A.Attribute.Name("X").Add(list(range(100)))
	A.Attribute("Y").Add(map(lambda x:2*x+5,A.X.value))
	def Fun2(self):
		print("Hellow Word")
	#B.Method(Fun2).Add
	#B.Fun2()
	#A.Fun();A.Attribute().ShortCut(globals())
