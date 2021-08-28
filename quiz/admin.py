from django.contrib import admin

from .models import EstadisticasUsuarios, LoginDetails, PartidasDetails, Respuesta, User, Pregunta, ProgresoHistorico, ProgresoSesion

# Register your models here.

admin.site.register(User)
admin.site.register(Pregunta)
admin.site.register(ProgresoSesion)
admin.site.register(ProgresoHistorico)
admin.site.register(Respuesta)

#estadisticas usuarios
admin.site.register(EstadisticasUsuarios)
admin.site.register(LoginDetails)
admin.site.register(PartidasDetails)

