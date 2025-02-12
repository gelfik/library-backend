from django.core.validators import MinValueValidator
from django.db import models
from django.utils.translation import gettext_lazy as _


class Book(models.Model):
    title = models.CharField(max_length=250, null=False, blank=False, db_index=True)
    author = models.CharField(max_length=250, null=False, blank=False, db_index=True)
    isbn = models.CharField(
        verbose_name=_("ISBN"), max_length=13, null=False, blank=False, db_index=True
    )
    pages = models.PositiveSmallIntegerField(
        null=False, blank=False, validators=[MinValueValidator(1)]
    )
    is_available = models.BooleanField(
        verbose_name=_("Book is available"), default=True, db_index=True
    )

    def __str__(self):
        return f"{self.author}. {self.title}"

    class Meta:
        verbose_name_plural = "books"
        verbose_name = "book"
