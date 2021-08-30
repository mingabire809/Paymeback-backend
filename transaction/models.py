from django.db import models
from account.models import Account


''' 
this table contains all the tractaction of all the users registerd to the system
relations are made with the customer table, the owner table, the reciver table
'''

class  Transaction(models.Model):
    transactor  = models.ForeignKey(Account,on_delete=models.CASCADE,default=0)#many trasactions one cutomer
    lender = models.CharField(max_length=250) 
    receiver = models.CharField(max_length=250)
    date = models.DateField()
    amount = models.IntegerField(null=False,default=0)
    status = models.BooleanField(null=False,default=0)
    amount_paid = models.IntegerField(null=False,default=0)
    amount_due = models.IntegerField(null=False,default=0)
    
    def __str__(self):
       return f'Amount : {self.amount}, lender : {self.lender} | receiver : {self.receiver} |Transactor: {self.transactor.username}'

