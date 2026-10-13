from django.contrib import admin
from .models import Comuna, Propiedad


class PropiedadInline(admin.TabularInline):
    model = Propiedad
    extra = 1


@admin.register(Comuna)
class ComunaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'region', 'codigo_clasificacion', 'activa', 'total_propiedades_asociadas')
    list_filter = ('activa', 'region')
    search_fields = ('nombre', 'codigo_clasificacion')
    inlines = [PropiedadInline]

    @admin.display(description="Total Propiedades")
    def total_propiedades_asociadas(self, obj):
        return obj.propiedades.count()


@admin.action(description="Marcar propiedades seleccionadas como DISPONIBLE")
def marcar_disponible(modeladmin, request, queryset):
    actualizadas = queryset.update(disponible=True)
    modeladmin.message_user(request, f'{actualizadas} propiedad(es) marcada(s) como DISPONIBLE.')


@admin.action(description="Marcar propiedades seleccionadas como ARRENDADO")
def marcar_arrendado(modeladmin, request, queryset):
    actualizadas = queryset.update(disponible=False)
    modeladmin.message_user(request, f'{actualizadas} propiedad(es) marcada(s) como ARRENDADO.')


@admin.register(Propiedad)
class PropiedadAdmin(admin.ModelAdmin):
    list_display = (
        'codigo_propiedad', 'direccion', 'tipo_propiedad',
        'precio_arriendo', 'dormitorios', 'banos',
        'disponible', 'comuna'
    )
    list_editable = ('disponible', 'precio_arriendo')
    list_filter = ('disponible', 'tipo_propiedad', 'comuna', 'comuna__codigo_clasificacion')
    search_fields = (
        'codigo_propiedad',
        'direccion',
        'comuna__nombre',
        'comuna__codigo_clasificacion',
    )
    ordering = ('-fecha_publicacion',)
    actions = [marcar_disponible, marcar_arrendado]