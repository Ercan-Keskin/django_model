from django.db import models

# Create your models here.


class Student(models.Model):
    first_name = models.CharField(max_length=30)
    last_name =models.CharField(max_length=40, blank=True) #blank=True demek boş ta yazsak kabul et demek.
    number = models.PositiveSmallIntegerField(null=True, blank=True)
    about = models.TextField(blank=True)
    email = models.EmailField(blank=True)
    register_date= models.DateTimeField(auto_now_add=True) #auto_now_add=True demek oluşturulan veriye otomatik tarihi at demek
    update_date=models.DateTimeField(auto_now=True) #o anki saati almak için sanırım ?
    is_activate= models.BooleanField(default=True)
    avatar = models.ImageField(blank=True, null=True , upload_to="student")
    
    
    def __str__(self):
        return f"{self.first_name} - {self.number}"
    
    
    class Meta:
        ordering = ("number",)
        verbose_name="Öğrenciler"
        verbose_name_plural ="Öğrenci"
        