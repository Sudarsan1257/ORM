from django.db import models
from django.contrib import admin
class loan_DB(models.Model):
    Customer_ID = models.CharField(max_length=20, primary_key=True)
    Customer_name = models.CharField(max_length=100)
    loan_no = models.IntegerField()
    loan_amount = models.IntegerField()
    Mail_ID = models.EmailField()
class loan_DBAdmin(admin.ModelAdmin):  # Corrected here
    list_display = ('Customer_ID','Customer_name','loan_no','loan_amount','Mail_ID')

