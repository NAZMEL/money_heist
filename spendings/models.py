from django.db import models


class SpendingCategory(models.Model):
    name = models.CharField("Name", max_length=100, unique=True)
    url = models.SlugField(max_length=100, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"


class Spending(models.Model):
    amount = models.FloatField(verbose_name="amount")
    date = models.DateTimeField(auto_now_add=True)
    description = models.TextField("Description", null=True, blank=True, max_length=1000)
    category = models.ForeignKey("SpendingCategory")

    def __str__(self):
        return self.amount

    class Meta:
        verbose_name = "Spending"
        verbose_name_plural = "Spendings"





