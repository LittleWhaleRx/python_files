class Ticket:
    def __init__(self,weekend = False,child = False):
        self.exp = 100
        if weekend:
            self.sic = 1.2
        else:
            self.sic = 1
        if child:
            self.yh = 0.5
        else:
            self.yh = 1
    def calcPrice(self,num):
        return self.yh*self.sic*num*self.exp
cr = Ticket()
et = Ticket(child=True)
print('两个大人一个孩子的价格是%.2f'%(cr.calcPrice(2)+et.calcPrice(1)))
