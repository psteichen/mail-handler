from django.contrib import admin

from .models import List, Member

class ListAdmin(admin.ModelAdmin):
  list_display = ('email', 'desc', 'nb_members')
  fieldsets = [
        ('General'	, {'fields': ['desc', 'email', ]}),
        ('Members'	, {'fields': ['members']}),
  ]

admin.site.register(List, ListAdmin)
admin.site.register(Member)
