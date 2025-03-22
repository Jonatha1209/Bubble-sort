class Bubblesort():
    def __init__(self,l):
        self.l = l
    
    def sort(self):
        for last in range(len(self.l),-1,-1):
            for i in range(0,last-1):
                if (self.l[i]>self.l[i+1]):
                    tmp = self.l[i]
                    self.l[i]=self.l[i+1]
                    self.l[i+1]=tmp