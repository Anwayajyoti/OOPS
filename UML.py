class ListData:
    def __init__(self):
        self.list=[]
    def addData(self,ele):
        self.list.append(ele)
    def deleteData(self,ele):
        self.list.remove(ele)
    def len(self):
        print(len(self.list))
    def isPresent(self,ele):
        if ele in self.list:
            print('True')
        else:
            print('False')
    def disp(self):
        print(self.list)
        
l=ListData()
l.addData(3)
l.disp()
l.addData(5)
l.addData(1)
l.disp()
l.deleteData(5)
l.disp()
l.len()
l.isPresent(3)
l.isPresent(30)



    