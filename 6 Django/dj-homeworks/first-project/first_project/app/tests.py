from django.test import TestCase

# Create your tests here.
import os
from app.views import home_view, time_view, workdir_view


listdir = os.listdir()
msg = ''
for dir in listdir:
    msg += f'{dir}\n'
print(msg)




