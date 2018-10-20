#!/usr/bin/python
from __future__ import print_function
from copy import deepcopy as dcp
def Type(x):
	return str(type(x)).split(" ")[1][1:-2]
def Str2Num(Str):
	try:
		return int(Str)
	except:
		try:
			return float(Str)
		except:
			return None


class Attibute:
	def __init__(self,Name="Omari",data=[]):
		self.name=Name
		self.value=[]
		self.__index__=[]
		self.__meta__=[]
		#  
		self.Import(data)

	def __repr__(self):
		return "OMARI"
		#self.Return()
		#self.Return()

	def __call__(self):
		self.Return()

	def Len(self):
		return len(self.value)
	
	def __Copy__(self):
		if len(self.__meta__)==0:self.__meta__=dcp(self.value)

	def Reset(self):
		if len(self.__meta__) !=00:
			self.value=dcp(self.__meta__)
			self.__meta__=[]   
	
	def Update(self):
		self.__meta__=dcp(self.value)
		self.Reset()
		return self

	def Import(self,Data):
		__Type__ = Type(Data)
		if __Type__=="list":
			self.value+=Data
		else:
			self.value.append(Data)
		return self

	def Return(self):
		return self.value
	
	# ******************
	def Slice(self,I=[]):#start=None,end=None,step=1):
		self.__Copy__()
		self.value=[self.value[i] for i in I] #self.value(I)
		return self

	def Filter(self,Function,Case=0):
		self.__Copy__()
		A = list(filter(Function,self.value))
		I=[]; initial=0
		print(type(A))
		for j in range(len(A)):
			for i in range(initial,self.Len()):
				if A[j]==self.value[i]:
					initial=i+1
					I.append(i)
					break
		self.value=A
		self.__index__=I
		return self

	def Map(self,Function):
		self.__Copy__()
		self.value = map(Function,self.value)
		return self

	def ExecutueFunction(self,Function):
		self.__Copy__()
		self.value=Function(dcp(self.value))
		return self

	def Convert2Numbers(self):
		self.Map(Str2Num)
		return self
		

# =================================================================================
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

		self.__call__()

	def __call__(self):
		database.__Class__=self
		#print(__main__.globals())
		#return self
		pass

	def __Copy__(self):
		#if len(self.__meta__)==0:self.__meta__=dcp(self.value)
		pass

	def ShortCut(self,Glob=globals(),On=True,Case=0):
		"""
			Export the class variables to the globals valible
			Case 0: Class
			Case 1: Str
		"""
		if Case == 0:
			#print(globals())
			for att in self.__use_sel_att__():
				Glob[att]=self.__dict__[att]
				print(att," Exported")
		if Case == 1:
			for att in self.__use_sel_att__():
				Glob[att]=self.__dict__[att]
		pass
	# ----------------------------------------------------------------------------------------
	
	def Reset(self):
		for att in self.attributes:self.__dict__[att].Reset()
		pass

	def Update(self):
		pass

	# ----------------------------------------------------------------------------------------
	class Attribute:
		def __init__(self,Name=""):
			self.name=Name
			self.myclass=database.__Class__
			
		def Add(self,Data=[]):
			if self.name in self.myclass.attributes:
				pass
			else:
				database.__Class__.__dict__[self.name]=Attibute(self.name)
				database.__Class__.attributes.append(self.name)
				if len(Data) !=0:
					database.__Class__.__dict__[self.name].Import(Data)
				return database.__Class__.__dict__[self.name]
			
		def Delete(self):
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
				database.__Class__.__dict__[self.name]=Attibute(self.name)
				pass
		
		def Select(self,*argu,**kwargs):
			if "Reset" in kwargs:
				if kwargs["Reset"]:
					database.__Class__.__selected__att__=[]
			Case=False
			for att in argu:
				if att in database.__Class__.attributes:
					Case=True
					database.__Class__.__selected__att__=att
			if len(argu)==0 and not Case:
				database.__Class__.__selected__att__=database.__Class__.attributes
			pass

		def ShortCut(self, Glob=globals(), On=True, Case=0):
			"""
				Export the class variables to the globals valible
				Case 0    : list
				Case 1    : Class (Attribue)
				otherwise : Str
			"""
			if Case == 0:
				# print(globals())
				for att in self.myclass.__use_sel_att__():
					Glob[att] = self.myclass.__dict__[att].Return()
					print(att, " Exported")
			elif Case == 1:
				for att in self.__use_sel_att__():
					Glob[att] = self.myclass.__dict__[att]
					pass
			else:
				for att in self.__use_sel_att__():
					Glob[att] = att
					pass
			pass


	def ResetAttriute(self,Name):
		if Name in self.__dict__.keys():self.__dict__[Name]=Attibute(Name)
		pass
	''''
	def Select(self,*argu,**kwargs):
		if "Reset" in kwargs:
			if kwargs["Reset"]:
				self.__selected__att__=[]
		Case=False
		for att in argu:
			if att in self.attributes:
				Case=True
				self.__selected__att__=att
		if len(argu)==0 and not Case:
			self.__selected__att__=self.attributes
		pass
	
	def Del(self):
		pass

	def GenerateIndexArray(self):
		self.AddAtribute(Name="__index__",Data=list(range(self.__dict__[self.attributes[0]].Len())))
	
	def __use_sel_att__(self):
		if len(self.__selected__att__)==0:
			return self.attributes
		return self.__selected__att__
	'''



	class Operation:
		__Class__=None
		def __init__(self):
			self.myclass=database.__Class__
			self.__call__()
			pass
		def __call__(self, *args, **kwargs):
			Operation.__Class__=self
			pass

		def Filter(self,Condition,AttibuteName=""):
			I = self.myclass.__dict__[AttibuteName].Filter(Condition).__index__
			self.Slice(I)
			return self.myclass

		@classmethod
		def Slice(I=[]):
			for att in self.myclass.__use_sel_att__():
				self.myclass.__dict__att].Slice(I)
			return self.myclass


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

		class Plot(self):
			pass

	# ----------------------------------------------------------------------------------------

	def Function(self,Function,MetaName=""):
		#self.__meta__[MetaName]=Function(self)
		return self

	# -----------------------------------------------------------------------------------------
	def Slice(self,I=[]):
		for att in self.__use_sel_att__():self.__dict__[att].Slice(I)
		return self

	def Filter(self,Condition,AttibuteName=""):
		I=self.__dict__[AttibuteName].Filter(Condition).__index__
		self.Slice(I)
		return self
	# ------------------------------------------------------------------------------------------
	def Return(self):
		return [self.__dict__[att].Return() for att in self.__use_sel_att__()]
	
	# ------------------------------------------------------------------------------------------
	'''
	def Functions(self,Function,Global=False):
		Name=Function.func_name
		class Fun1:
			def __init__(self,glob,inner):
				self.glob=glob
				self.inner=inner
			@property
			def Add(self):
				if Name in self.glob.__dict__.keys():
					pass	
				else:
					self.glob.__dict__[Name]=Function.__get__(self.inner)
					self.glob.__method_att__=[]	
					pass
			def Delete(self,Name="OMARI"):
					pass
		if Global:	
			return Fun1(database,self)
		else:	
			return Fun1(self,self)
	'''
	class Functions:
		def __init__(self,Function):
			self.function=Function
			self.name = Function.func_name
			self.myclass = database.__Class__
			pass

		@property
		def Add(self):
			if self.name in self.myclass.__dict__:
				pass
			else:
				self.myclass.__dict__[self.name]=self.function.__get__(self.myclass)
				self.myclass.__method_att__+=[self.name]
				pass
			pass

		@property
		def Delete(self):
			if self.name in self.myclass.__method_att__:
				del self.myclass.__dict__[self.name]
				self.myclass.__method_att__.remove(self.name)
				pass
			else:
				pass
			pass

		def Select(self,*args,**kwargs):
			pass

		def Execute(self):
			pass

		pass








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
	A=Attibute()
	A.value=[x for x in range(100)]
	print(A.Filter(lambda x:x>1).Return())
	print(A.Filter(lambda x:50>x>5).Return())
	print(A.value)
	A.Reset()
	print(A.value)
	#B=ImportFromFile()
	A=database()
	def Fun(self):
		print ("OMARI -->",dir(self))
	A.Functions(Fun).Add
	A.Fun()