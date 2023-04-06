from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.db import models
from django.utils.text import slugify

class MyUserManager(BaseUserManager):
    def create_user(self, email, password=None, **kwargs):

        if not email:
            raise ValueError("Vous devez entrer un email.")
        
        user = self.model(email=self.normalize_email(email))

        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self, email, password=None, **kwargs):

        user = self.create_user(email=email, password=password)
        user.is_admin = True
        user.is_staff = True
        user.save()
        return user


class CustomUser(AbstractBaseUser):
    email = models.EmailField(
        unique=True,
        max_length=255,
        blank=False,
        verbose_name='Adresse mail',
    )

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    objects = MyUserManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True


class Article(models.Model):

    CONSTRUCTION = 'CO'
    COMMERCIALE = 'CM'
    INNOVATION = 'IN'
    SECURITE = 'SE'
    STRUCTURE = 'ST'

    CATEGORIE_ARTICLE_CHOIX = [
        (CONSTRUCTION, 'Construction'),
        (COMMERCIALE, 'Commerciale'),
        (INNOVATION, 'Innovation'),
        (STRUCTURE, 'Structure'),
        (SECURITE, 'Securite'),
    ]

    user = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, blank=True)
    titre = models.CharField(max_length=255, unique=True, verbose_name="Titre")
    contenu = models.TextField(blank=True, verbose_name="Contenu")
    slug = models.SlugField(max_length=255, blank=True, unique=True)
    publié = models.BooleanField(default=False, verbose_name="Publié")
    date_creation = models.DateField(blank=True, null=True)
    derniere_modification = models.DateField(auto_now=True)
    image = models.ImageField(upload_to='article')
    categorie = models.CharField(max_length=2, choices=CATEGORIE_ARTICLE_CHOIX)

    class Meta:
        ordering = ["-date_creation"]
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'

    def __str__(self):
        return self.titre
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.titre)
        super().save(*args, **kwargs)

class Option(models.Model):

    user = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, blank=True)
    nom = models.CharField(max_length=255, unique=True, verbose_name="Nom")
    description1 = models.TextField(verbose_name="Description1")
    description2 = models.TextField(verbose_name="Description2")
    description3 = models.TextField(verbose_name="Description3")
    slug = models.SlugField(blank=True, unique=True, max_length=255)
    image = models.ImageField(upload_to='Option')

    class Meta:
        verbose_name = 'Option'

    def __str__(self):
        return self.nom
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.nom)
        super().save(*args, **kwargs)



class Cours(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, blank=True)
    option = models.ForeignKey(Option, on_delete=models.CASCADE)
    nom = models.CharField(max_length=255, verbose_name="Nom", unique=True)
    description = models.TextField(verbose_name="Description")

    class Meta:
        verbose_name = 'Cour'

    def __str__(self):
        return self.nom


class Formation(models.Model):

    user = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, blank=True)
    nom = models.CharField(max_length=255, verbose_name="Nom")
    description1 = models.TextField(verbose_name="Description")
    image = models.ImageField(upload_to='Formation')

    class Meta:
        verbose_name = 'Formation'

    def __str__(self):
        return self.nom

class Commentaire(models.Model):
    
    nom = models.CharField(max_length=255, verbose_name="Nom")
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    image_profil = models.ImageField(upload_to='Commentaire', blank=True, null=True)
    email = models.EmailField(max_length=255, blank=True)
    website = models.CharField(max_length=255, blank=True)
    commentaire = models.TextField()

    class Meta:
        verbose_name = 'Commentaire'

    def __str__(self):
        return self.nom


class Inscription(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, blank=True)
    nom = models.CharField(max_length=255, verbose_name='Nom')
    post_nom = models.CharField(max_length=255, verbose_name='Post nom')
    prenom = models.CharField(max_length=255, verbose_name='Prenom')
    genre = models.CharField(max_length=2, verbose_name="Genre")
    date_naissance = models.DateField(verbose_name="Date de naissance")
    pourcentage = models.IntegerField(verbose_name="Pourcentage")
    adresse = models.CharField(max_length=255, verbose_name="Adresse")
    nom_responsable = models.CharField(max_length=255, verbose_name="Nom de responsable")
    nom_etablissement = models.CharField(max_length=255, verbose_name="Nom de l'etablissement")
    religion = models.CharField(max_length=255, verbose_name="Religion")
    motif = models.TextField(verbose_name="Motif")

    class Meta:
        verbose_name = 'Inscription'

    def __str__(self):
        return self.nom


class Message(models.Model):

    user = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, blank=True)
    nom = models.CharField(max_length=255, verbose_name='Nom')
    email = models.EmailField(max_length=255, verbose_name='Email')
    sujet = models.CharField(max_length=255, verbose_name='Sujet')
    message = models.TextField(verbose_name='Message')

    class Meta:
        verbose_name = 'Message'

    def __str__(self):
        return self.nom


class Realisation(models.Model):

    user = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, verbose_name="Utilisateur")
    option = models.ForeignKey(Option, on_delete=models.SET_NULL, null=True, verbose_name="Option")
    titre = models.CharField(max_length=255, verbose_name="Titre", unique=True)
    presentation = models.TextField(verbose_name="Presentation")
    detail = models.TextField(verbose_name="Detail")
    innovateur = models.TextField(verbose_name="Innovateur")
    date = models.DateField(blank=True, null=True, verbose_name="Date")
    slug = models.SlugField(max_length=255, blank=True, unique=True, verbose_name="Slug")

    class Meta:
        verbose_name = 'Realisation'

    def __str__(self):
        return self.titre

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.titre)
        super().save(*args, **kwargs)

class Infrastructure(models.Model):

    INFRASTRUCTURE = [
        ("CYCLE SUPERIEUR", "CYCLE SUPERIEUR"),
        ("CYCLE INFERIEUR", "CYCLE INFERIEUR"),
        ("MECANIQUE GENERALE", "MECANIQUE GENERALE"),
        ("MECANIQUE AUTO", "MECANIQUE AUTO"),
        ("ELECTRONIQUE", "ELECTRONIQUE"),
        ("ELECTRICITE", "ELECTRICITE"),
        ("IMPRIMERIE", "IMPRIMERIE"),
    ]

    titre = models.CharField(max_length=255, verbose_name="Titre")
    image = models.ImageField(upload_to="Infrastructure", verbose_name="Image")
    categorie = models.CharField(max_length=255, choices=INFRASTRUCTURE, verbose_name="Categorie")
    user = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Utilisateur")

    class Meta:
        verbose_name = "Infrastructure"

    def __str__(self):
        return self.titre


class Archive(models.Model):

    MOIS = [
        ("JANVIER", "JANVIER"),
        ("FEVRIER", "FEVRIER"),
        ("MARS", "MARS"),
        ("AVRIL", "AVRIL"),
        ("MAI", "MAI"),
        ("JUIN", "JUIN"),
        ("JUILLET", "JUILLET"),
        ("AOUT", "AOUT"),
        ("SEPTEMBRE", "SEPTEMBRE"),
        ("OCTOMBRE", "OCTOMBRE"),
        ("NOVEMBRE", "NOVEMBRE"),
        ("DECEMBRE", "DECEMBRE"),
    ]

    mois = models.CharField(max_length=255, choices=MOIS, verbose_name="Mois")
    annee = models.DateField(verbose_name="Date")
    user = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Utilisateur")

    class Meta:
        verbose_name = "Archive"

    def __str__(self):
        return f"{self.mois} {self.annee}"
