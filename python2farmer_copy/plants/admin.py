from django.contrib import admin

# Register your models here.
from .models import Plant,Article

class PlantAdmin(admin.ModelAdmin):
	list_display = ('name','path_picture','slug',)
	
class ArticleAdmin(admin.ModelAdmin):
	list_display = ('title','belongtoplant','author','pub_date','update_time',)
	
admin.site.register(Plant,PlantAdmin)
admin.site.register(Article,ArticleAdmin)
