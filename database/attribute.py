from __future__ import print_function
from copy import deepcopy as dcp
from aux_functions import *

class Attibute:
    def __init__(self, Name="Omari", data=[]):
        self.name = Name
        self.value = []
        self.__index__ = []
        self.__meta__ = []
        #
        self.Import(data)

    def __repr__(self):
        return "OMARI"

    # self.Return()
    # self.Return()
    #@property
    def __call__(self):
        return self.Return()

    def Len(self):
        return len(self.value)

    def __Copy__(self):
        if len(self.__meta__) == 0: self.__meta__ = dcp(self.value)

    def Reset(self):
        if len(self.__meta__) != 00:
            self.value = dcp(self.__meta__)
            self.__meta__ = []

    def Update(self):
        self.__meta__ = dcp(self.value)
        self.Reset()
        return self

    def Import(self, Data):
        __Type__ = Type(Data)
        if __Type__ == "list":
            self.value += Data
        else:
            self.value.append(Data)
        return self

    def Return(self):
        return self.value

    # ******************
    def Slice(self, I=[]):  # start=None,end=None,step=1):
        self.__Copy__()
        #print(I[-1],self.value[-1])
        #for i in I:
        #    print(i,self.value[i])
        #    pass
        self.value = [self.value[i] for i in I]  # self.value(I)
        return self

    def Filter(self, Function, Case=0):
        self.__Copy__()
        A = list(filter(Function, self.value))
        I = [];
        initial = 0
        #print(type(A))
        for j in range(len(A)):
            for i in range(initial, self.Len()):
                if A[j] == self.value[i]:
                    initial = i + 1
                    I.append(i)
                    break
        self.value = A
        self.__index__ = I
        return self

    def Map(self, Function):
        self.__Copy__()
        self.value = map(Function, self.value)
        return self

    def ExecutueFunction(self, Function):
        self.__Copy__()
        self.value = Function(dcp(self.value))
        return self

    def Convert2Numbers(self):
        self.Map(Str2Num)
        return self