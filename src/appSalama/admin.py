from django.contrib import admin
from appSalama.models import *


class CustomUserAdmin(admin.ModelAdmin):
    list_display = "__all__"

class CoursAdmin(admin.ModelAdmin):
    list_display = ("nom", "description")

class OptionAdmin(admin.ModelAdmin):
    list_display = ("nom", "description1", "description2", "description3", "image")

class ArticleAdmin(admin.ModelAdmin):
    list_display = ("titre", "coontenu", "publié", "date_creation", "derniere_modification", "image", "categorie")
    list_editable = ("publié", )

class FormationAdmin(admin.ModelAdmin):
    list_display = ("nom", "description", "image")

class CommentaireAdmin(admin.ModelAdmin):
    list_display = ("__all__")

class InscriptionAdmin(admin.ModelAdmin):
    list_display = ("__all__")

class MessageAdmin(admin.ModelAdmin):
    list_display = ("__all__")


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Cours, CoursAdmin)
admin.site.register(Option, OptionAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Formation, FormationAdmin)
admin.site.register(Commentaire, CommentaireAdmin)
admin.site.register(Inscription, InscriptionAdmin)
admin.site.register(Message, MessageAdmin)
