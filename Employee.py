class Employee:
    def __init__(self,basicpay,id):
        self.pay=basicpay
        self.id=id
    def calculateTax(self):
        tax=0
        if self.pay >25000 and self.pay <= 40000:
            tax= self.pay * (15/100)
        elif self.pay >40000 and self.pay <= 50000:
            tax= self.pay * (18/100)
        elif self.pay >50000:
            tax= self.pay * (20/100)
        return tax
    def getAnnualSalary(self):
        return self.pay*12