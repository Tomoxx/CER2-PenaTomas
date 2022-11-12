from django.contrib import admin

from core.models import Residencia
from core.models import Correspondencia

# Register your models here.

admin.site.register(Residencia)
admin.site.register(Correspondencia)

#superadmin password = 1234
#Superadministrador password = grand1234
#Conserje1 password = grand4321