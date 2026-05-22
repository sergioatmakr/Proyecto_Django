from django.contrib import admin
from .models import Receta

@admin.register(Receta)
class RecetaAdmin(admin.ModelAdmin):
    # Esto hará que en el panel veas una bonita tabla con el título, autor y fecha de cada receta
    list_display = ('titulo', 'autor', 'fecha_creacion')
    # Añade un buscador rápido en el panel de administración
    search_fields = ('titulo', 'descripcion')