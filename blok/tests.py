from django.test import TestCase
from django.contrib.admin.models import LogEntry

LogEntry.objects.all().delete()
# Create your tests here.
