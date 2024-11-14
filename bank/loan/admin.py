from django.contrib import admin
from .models import loan_DB, loan_DBAdmin
admin.site.register(loan_DB, loan_DBAdmin)
