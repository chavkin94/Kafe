from django.contrib import admin

# Register your models here.
from udachi.models import TipBluda, Bluda, Ingridienti, IngridientiVBlude


class TipBludaAdmin(admin.ModelAdmin):
    pass


admin.site.register(TipBluda, TipBludaAdmin)

class IngridientiAdmin(admin.ModelAdmin):
    pass


admin.site.register(Ingridienti, IngridientiAdmin)


class IngridientiVBludeInline(admin.TabularInline):
    model = IngridientiVBlude


class BludaAdmin(admin.ModelAdmin):
    inlines = [
        IngridientiVBludeInline,
    ]
    list_display = [
        'id',
        'nazvanie',
        'opisanie',
        'cena',
        'gramovka',
        'tip_bluda',
    ]
    list_filter = ('tip_bluda',)
    list_display_links = ['nazvanie',]
    search_fields = ['nazvanie', 'cena','tip_bluda__nazvanie']
    list_editable = [ 'opisanie', 'cena', 'gramovka', 'tip_bluda']
    ordering = ['-nazvanie',]

admin.site.register(Bluda, BludaAdmin)