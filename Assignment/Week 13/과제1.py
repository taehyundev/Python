# 과제1
class BankAcct:
    balance = 0
    def __init__(self,balance=0):
        self.balance = balance

    def deposit(self, balance):
        self.balance = self.balance + balance

    def withdraw(self, balance):
        if self.balance-balance <0:
            return '인출 불가: 잔고가 부족함'
        self.balance = self.balance - balance

# 과제2
class Queue:
    queue = []
    def __init__(self):
        queue = []
    def addQueue(self, value):
        self.queue.append(value)
    def delQueue(self):
        rtn =self.queue[0]
        del self.queue[0]
        return rtn
    def isEmpty(self):
       if len(self.queue)>0:
            return False
       else:
            return True
    
