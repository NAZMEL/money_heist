from django.db import models


class SpendingCategory(models.Model):
    name = models.CharField("Name", max_length=100, unique=True)
    user = models.ForeignKey('authentication.User', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "spendings_categories"
        verbose_name = "Category"
        verbose_name_plural = "Categories"


class Spending(models.Model):
    amount = models.FloatField(verbose_name="amount")
    created_at = models.DateTimeField(auto_now_add=True)
    description = models.TextField("Description", null=True, blank=True)
    category = models.ForeignKey("SpendingCategory", on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey("authentication.User", on_delete=models.CASCADE, null=True)

    def __str__(self):
        return str(self.amount)

    class Meta:
        db_table = "spendings"
        verbose_name = "Spending"
        verbose_name_plural = "Spendings"





