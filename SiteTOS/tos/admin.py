from django.contrib import admin
from .models import News,NewsImage
from .models import Competitions
from .models import Doc
from .models import District
from .models import Tos
from .models import RegistrationRequest

# Register your models here.
#admin.site.register(News)
admin.site.register(Competitions)
admin.site.register(Doc)
admin.site.register(District)
admin.site.register(Tos)
#admin.site.register(SubDistrict)
#from .forms import TosAdminForm

#class TosAdmin(admin.ModelAdmin):
#    form = TosAdminForm

#admin.site.register(Tos, TosAdmin)

class NewsImageInline(admin.TabularInline):
    model = NewsImage
    extra = 1  # Количество пустых форм для добавления новых изображений

class NewsAdmin(admin.ModelAdmin):
    inlines = [NewsImageInline]

admin.site.register(News, NewsAdmin)

class RegistrationRequestAdmin(admin.ModelAdmin):
    list_display = ('FIO', 'work_2','tos','mail', 'login', 'is_accepted')
    list_filter = ('is_accepted',)
    search_fields = ('FIO', 'mail', 'login')

admin.site.register(RegistrationRequest, RegistrationRequestAdmin)