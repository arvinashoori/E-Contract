from django.contrib import admin
from .models import Contract

@admin.register(Contract)
class SignedContractAdmin(admin.ModelAdmin):
    list_display = ('title', 'full_name', 'date', 'user', 'created_at')  
    list_filter = ('date', 'user')  
    search_fields = ('title', 'full_name')  
    readonly_fields = ('created_at',) 