class Bank:
    bname='SBI'
    ifsc='SBI00789'
    branch='BTM'

    def __init__(self,name,email,number,address):
        self.name=name
        self.email=email
        self.number=number
        self.address=address

    def disp(self):
        print(self.name,self.bname,self.branch)
        
    @classmethod
    def changeBranch(cls,new):
        cls.branch=new
        print(cls.bname,cls.branch)

b=Bank('AJ','xyz@gmail.com',936500540,'Blr')
b.disp()
b.changeBranch('HSR')