from django.contrib import admin
from . import models

# Register your models here.

admin.site.register(models.CategorieArticle),
admin.site.register(models.Article),
admin.site.register(models.Commentaire),
admin.site.register(models.Tag)

class CategorieArticleAdmin(admin.ModelAdmin):
    list_display = ('nom','date_add','date_update','status','image_view')
    list_filter =('status',)
    search_fields = ('nom')
    date_hierarchy ='date_add'
    list_display_links =['nom']
    ordering =['nom']
    list_per_page = 10
    fieldsets =[
            ('info CategoriesArticle', {'fields':['nom', 'image','description']}),
            ('standard',{'fields':['status']})
    ]

    def image_view(self,obj):
        return mark_safe("<img src='{url}' width=100 height=50>".format(url=obj.image.url))

def _register(model,admin_class):
    admin.site.register(model, admin_class)



class ArticleAdmin(admin.ModelAdmin):

    list_display = ('nom','date_add','date_update','status','image_view')
    list_filter =('status',)
    search_fields = ('nom')
    date_hierarchy ='date_add'
    list_display_links =['nom']
    ordering =['nom']
    list_per_page = 10
    fieldsets =[
            ('info CategoriesArticle', {'fields':['nom', 'image','description','titre','contenu']}),
            ('standard',{'fields':['status']})
    ]

    def image_view(self,obj):
        return mark_safe("<img src='{url}' width=100 height=50>".format(url=obj.image.url))

def _register(model,admin_class):
    admin.site.register(model, admin_class)



class TagAdmin(admin.ModelAdmin):

    list_display = ('nom','date_add','date_update','status','image_view')
    list_filter =('status',)
    search_fields = ('nom')
    date_hierarchy ='date_add'
    list_display_links =['nom']
    list_per_page = 10
    fieldsets =[
            ('info CategoriesArticle', {'fields':['nom', 'description']}),
            ('standard',{'fields':['status']})
    ]

    def image_view(self,obj):
        return mark_safe("<img src='{url}' width=100 height=50>".format(url=obj.image.url))

def _register(model,admin_class):
    admin.site.register(model, admin_class)


class CommentaireAdmin(admin.ModelAdmin):

    list_display = ('nom','date_add','date_update','status','image_view')
    list_filter =('status',)
    search_fields = ('nom')
    date_hierarchy ='date_add'
    list_display_links =['nom']
    list_per_page = 10
    fieldsets =[
            ('info CategoriesArticle', {'fields':['nom', 'image','prenom','commentaire']}),
            ('standard',{'fields':['status']})
    ]

    def image_view(self,obj):
        return mark_safe("<img src='{url}' width=100 height=50>".format(url=obj.image.url))

def _register(model,admin_class):
    admin.site.register(model, admin_class)