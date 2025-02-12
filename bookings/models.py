from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


class Loan(models.Model):
    user = models.ForeignKey(
        "accounts.User", on_delete=models.PROTECT, related_name="loans", null=False
    )
    book = models.ForeignKey(
        "books.Book", on_delete=models.PROTECT, related_name="loans", null=False
    )
    start_date = models.DateField(
        verbose_name=_("Initial booking date"), default=timezone.now, null=False
    )
    end_date = models.DateField(verbose_name=_("End date of booking"), null=True, blank=True)

    def __str__(self):
        return f"Loan ID: {self.id}"

    class Meta:
        verbose_name = "Loan"
        verbose_name_plural = "Loans"
        ordering = ["start_date"]
