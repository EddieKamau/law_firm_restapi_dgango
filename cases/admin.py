from django.contrib import admin
from .models import Cases, CaseEvents

# Register your models here.
admin.site.register(Cases)
admin.site.register(CaseEvents)