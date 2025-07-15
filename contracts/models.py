from django.db import models
from accounts.models import CustomUser

class Contract(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE) 
    title = models.CharField(max_length=200)  
    full_name = models.CharField(max_length=100)  
    date = models.DateField() 
    contract_file = models.FileField(upload_to='contracts/')  
    created_at = models.DateTimeField(auto_now_add=True) 

    def __str__(self):
        return self.title