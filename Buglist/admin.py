from django.contrib import admin
from .models import Bugs

class BugsAdmin(admin.ModelAdmin):
    list_display = ['kurzbeschreibung','status','prio','melder','datum']
    list_display_links = ['kurzbeschreibung']
    list_editable = ['melder','status']
    search_fields= ['datum']
    list_filter = ['melder','status']
admin.site.register(Bugs,BugsAdmin)
admin.site.site_header = 'Webtechnologien Project'
admin.site.site_title  ='Webtechnologien project'