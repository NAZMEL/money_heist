from django.contrib import admin
from .models import SpendingCategory, Spending

admin.site.register(Spending)
admin.site.register(SpendingCategory)
