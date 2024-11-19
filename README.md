# Ex02 Django ORM Web Application
## Date: 14/11/2024

## AIM
To develop a Django application to store and retrieve data from a bank loan database using Object Relational Mapping(ORM).

## ENTITY RELATIONSHIP DIAGRAM
![alt text](<Screenshot 2024-11-13 145945.png>)

## DESIGN STEPS

### STEP 1:
Clone the problem from GitHub

### STEP 2:
Create a new app in Django project

### STEP 3:
Enter the code for admin.py and models.py

### STEP 4:
Execute Django admin and create details for 10 books

## PROGRAM
```
admin.py
from django.contrib import admin
from .models import loan_DB, loan_DBAdmin
admin.site.register(loan_DB, loan_DBAdmin)
 
 model.py

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

```

## OUTPUT
![alt text](<Screenshot 2024-11-13 144558.png>)

## RESULT
Thus the program for creating a database using ORM hass been executed successfully
