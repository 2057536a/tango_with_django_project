from django.contrib import admin
from rango.models import Category, Page
from rango.models import UserProfile
from rango.models import User

# Add in this class to customise the Admin Interface
class CategoryAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug':('name',)}

class PageAdmin(admin.ModelAdmin):
	list_display = ('title','category','url','views')


admin.site.register(Category, CategoryAdmin)
admin.site.register(Page,PageAdmin)
admin.site.register(UserProfile)