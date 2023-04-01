from django.contrib import admin
from appSalama.models import *


class CustomUserAdmin(admin.ModelAdmin):
    list_display = ("email", "password")

class CoursAdmin(admin.ModelAdmin):
    list_display = ("nom", "description")

class OptionAdmin(admin.ModelAdmin):
    list_display = ("nom", "description1", "description2", "description3", "image")

class ArticleAdmin(admin.ModelAdmin):
    list_display = (
        "titre", "contenu", "publié", "date_creation", "derniere_modification", "image", "categorie")
    list_editable = ("publié", )

class FormationAdmin(admin.ModelAdmin):
    list_display = ("nom", "description1", "image")

class CommentaireAdmin(admin.ModelAdmin):
    list_display = (
        "nom",
        "article",
        "image_profil",
        "email",
        "website",
        "commentaire"
    )

class InscriptionAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "nom",
        "post_nom",
        "prenom",
        "genre",
        "date_naissance",
        "pourcentage",
        "adresse",
        "nom_responsable",
        "religion",
        "motif",
    )

class MessageAdmin(admin.ModelAdmin):
    list_display = (
        "nom",
        "email",
        "sujet",
        "message",
    )


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Cours, CoursAdmin)
admin.site.register(Option, OptionAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Formation, FormationAdmin)
admin.site.register(Commentaire, CommentaireAdmin)
admin.site.register(Inscription, InscriptionAdmin)
admin.site.register(Message, MessageAdmin)
