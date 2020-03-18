from django.contrib import admin
from . import models

# Register your models here.

admin.site.register(models.CompteSocial),
admin.site.register(models.Site_info),
admin.site.register(models.Presentation),
admin.site.register(models.Temoignage)

class InfoSiteAdmin(admin.ModelAdmin):

    list_display = ('nom','date_add','date_update','status','image_view')
    list_filter =('status',)
    search_fields = ('nom')
    date_hierarchy ='date_add'
    list_display_links =['nom']
    ordering =['nom']
    list_per_page = 10
    fieldsets =[
            ('infos site', {'fields':['nom', 'image','email']}),
            ('standard',{'fields':['status']})
    ]

    def image_view(self,obj):
        return mark_safe("<img src='{url}' width=100 height=50>".format(url=obj.image.url))

def _register(model,admin_class):
    admin.site.register(model, admin_class)


class CompteSocialAdmin(admin.ModelAdmin):
    list_display = ('nom','date_add','date_update','status','image_view')
    list_filter =('status',)
    search_fields = ('nom')
    date_hierarchy ='date_add'
    list_display_links =['nom']
    ordering =['nom']
    list_per_page = 10
    fieldsets =[
            ('infos site', {'fields':['nom', 'image','logo']}),
            ('standard',{'fields':['status']})
    ]

    def image_view(self,obj):
        return mark_safe("<img src='{url}' width=100 height=50>".format(url=obj.image.url))

def _register(model,admin_class):
    admin.site.register(model, admin_class)


class PresentationAdmin(admin.ModelAdmin):

    list_display = ('nom','date_add','date_update','status','image_view')
    list_filter =('status',)
    search_fields = ('nom')
    date_hierarchy ='date_add'
    list_display_links =['nom']
    ordering =['nom']
    list_per_page = 10
    fieldsets =[
            ('infos site', {'fields':['nom', 'image','description']}),
            ('standard',{'fields':['status']})
    ]

    def image_view(self,obj):

        return mark_safe("<img src='{url}' width=100 height=50>".format(url=obj.image.url))

def _register(model,admin_class):
    admin.site.register(model, admin_class)


class TemoignageAdmin(admin.ModelAdmin):
    list_display = ('nom','date_add','date_update','status','image_view')
    list_filter =('status',)
    search_fields = ('nom')
    date_hierarchy ='date_add'
    list_display_links =['nom']
    ordering =['nom']
    list_per_page = 10
    fieldsets =[
            ('infos site', {'fields':['nom','prenom', 'image','message']}),
            ('standard',{'fields':['status']})
    ]

    def image_view(self,obj):
        return mark_safe("<img src='{url}' width=100 height=50>".format(url=obj.image.url))

def _register(model,admin_class):
    admin.site.register(model, admin_class)
