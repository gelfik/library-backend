from django.contrib import admin

from bookings.models import Loan


@admin.register(Loan)
class LoanAdmin(admin.ModelAdmin):
    pass
