from django.contrib import admin
from .models import teacher
from .models import assessment

# Register your models here.
admin.site.register(teacher)
admin.site.register(assessment)
