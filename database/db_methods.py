from attribute import Attibute

def addAttribute(self,Data):
    if self.name in self.attribute_list:
        pass
    else:
        self.myclass.__dict__[self.name] = Attibute(self.name)
        self.attribute_list.append(self.name)
        if len(Data) !=0:
            self.myclass.__dict__[self.name].Import(Data)
        return self.myclass.__dict__[self.name]

def deleteAttribute(self):
    pass



def SelectAttributes(self,args,kwargs):
    if "Reset" in kwargs:
        if kwargs["Reset"]:
            #self.myclass.__selected__att__ = []
            pass
    Case = False
    print(self.attribute_list)
    for att in args:
        if att in self.attribute_list:
            Case = True
            self.selected_att_list += [att]
    if len(args) == 0 and not Case:
        self.selected_att_list = self.attributes_list
    return self.myclass


def ShortCut(self, Glob=globals(), On=True, Case=0):
    """
        Export the class variables to the globals valible
        Case 0    : list
        Case 1    : Class (Attribue)
        otherwise : Str
    """
    if Case == 0:
        # print(globals())
        print("Case 0 is selected")
        print(self.myclass.attributes)
        for att in self.__use_selected_att__():
            Glob[att] = self.myclass.__dict__[att].Return()
            print(att, " Exported")
    elif Case == 1:
        for att in self.__use_selected_att__():
            Glob[att] = self.myclass.__dict__[att]
            pass
    else:
        for att in self.__use_selected_att_():
            Glob[att] = att
            pass
    pass




# ============================================================================


def addMethod(self):
    if self.name in self.myclass.__dict__:
        pass
    else:
        self.myclass.__dict__[self.name] = self.function.__get__(self.myclass)
        self.myclass.__method_att__ += [self.name]
        pass
    pass
    return self.myclass



def deleteMethod(self):
    if self.name in self.myclass.__method_att__:
        del self.myclass.__dict__[self.name]
        self.myclass.__method_att__.remove(self.name)
        pass
    else:
        pass
    pass


def selectMethod(self, *args, **kwargs):
    pass


def executeMethods(self):
    pass


pass




