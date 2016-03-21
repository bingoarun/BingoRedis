
class BingoDataHandler:
    myfile = ''
    mydict = {}
    def __init__(self,myfile):
        self.myfile=open(myfile,"r+")
        self.convertToDict()

    def convertToDict(self):
        self.mydict={}
        for i in self.myfile:
            i=i.rstrip().split('\t')
            self.mydict[i[0]]=i[1]
        print self.mydict


    def getData(self,mykey):
        '''
        for i in self.myfile:
            i = i.rstrip().split('\t')
            if i[0]==mykey:
                return i[1]
        return "No data found"
        '''
        return self.mydict[mykey.rstrip()]

    def putData(self,mykey,myvalue):
        self.mydict[mykey]=myvalue

    def writeToFile(self):
        for key in self.mydict:
            self.myfile.write(key+'\t'+self.mydict[key]+'\n')

