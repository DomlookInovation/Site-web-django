from django.contrib import admin
from appSalama.models import CustomUser, Cours, Option, Article, Commentaire
# Register your models here.

admin.site.register(CustomUser)
admin.site.register(Cours)
admin.site.register(Article)
admin.site.register(Commentaire)
admin.site.register(Option)