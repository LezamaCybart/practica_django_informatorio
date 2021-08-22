from django.contrib import admin

from .models import Respuesta, User, Pregunta, ProgresoHistorico, ProgresoSesion

# Register your models here.

admin.site.register(User)
admin.site.register(Pregunta)
admin.site.register(ProgresoSesion)
admin.site.register(ProgresoHistorico)
admin.site.register(Respuesta)