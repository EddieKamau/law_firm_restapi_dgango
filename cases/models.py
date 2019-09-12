from django.db import models
from firm.models import Lawyer, Client

# Create your models here.

class Cases(models.Model):
    lawyer = models.ForeignKey(Lawyer, on_delete= None)
    client = models.ForeignKey(Client, on_delete=None)
    case_name = models.CharField(max_length=50)
    case_details = models.TextField()
    case_no = models.CharField(max_length=50)
    case_status = models.BooleanField(default=True)
    case_type = models.CharField(max_length=50)

    def __str__(self):
        return str(self.case_no)

class CaseEvents(models.Model):
    case = models.ForeignKey(Cases, unique=False, on_delete=None)
    event = models.TextField()
    date = models.DateField()

    class Meta:
        ordering = ['-date']