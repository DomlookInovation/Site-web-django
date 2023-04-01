from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import render,redirect
from .models import *
from .forms import CommentaireForm, InscriptionForm, MessageForm, LoginForm


def index(request):
    formations = Formation.objects.all()
    options = Option.objects.all()
    derniers = Article.objects.all().order_by('-id')[:4]
    context = {
        "formations": formations,
        "options": options,
        "derniers": derniers,
    }
    return render(request, "appSalama/index.html", context)

def option(request, id: int):
    option = Option.objects.get(pk=id)
    return render(request, "appSalama/option.html", context={'option':option})

def about(request):
    options = [option.nom for option in Option.objects.all()]
    return render(request, "appSalama/about.html", context={'options':options})

def article(request, slug:str):
    article = Article.objects.get(slug=slug)
    commentaires = Commentaire.objects.filter(article_id=id)
    if request.method == 'POST':
        form = CommentaireForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            commentaire = Commentaire()
            commentaire.article_id = id
            commentaire.email = data['email']
            commentaire.nom = data['nom']
            commentaire.commentaire = data['message']
            commentaire.website = data['website']
            commentaire.save()
            return redirect("article")
    form = CommentaireForm()
    derniers = list(articles).reverse()[:4]
    return render(request, "appSalama/article.html", context={'article':article,'commentaires':commentaires,'derniers':derniers,'form':form})

def articles(request):
    articles = Article.objects.all()
    derniers = list(articles).reverse()[:4]
    return render(request, "appSalama/articles.html", context={'articles': articles,'derniers':derniers})

def articles_categorie(request,categorie:str):
    articles = Article.objects.filter(categorie=categorie)
    derniers = list(Article.objects.all()).reverse()[:3]
    return render(request, "appSalama/articles.html", context={'articles': articles,'derniers':derniers})

def inscription(request):
    if request.method == 'POST':
        form = InscriptionForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            inscription = Inscription()
            inscription.user_id = 1
            inscription.nom = data['nom']
            inscription.adresse = data['adresse']
            inscription.date_naissance = data['date_naissance']
            inscription.prenom = data['prenom']
            inscription.post_nom = data['post_nom']
            inscription.motif = data['motif']
            inscription.genre = data['genre']
            inscription.nom_responsable = data['nom_responsable']
            inscription.pourcentage = data['pourcentage']
            inscription.religion = data['religion']
            inscription.save()
    form = InscriptionForm()
    return render(request, "appSalama/inscription.html", context={'form':form})

def article(request, slug:slug):
    article = Article.objects.get(slug=slug)
    commentaires = Commentaire.objects.filter(article_id=id)
    if request.method == 'POST':
        form = CommentaireForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            commentaire = Commentaire()
            commentaire.article_id = id
            commentaire.email = data['email']
            commentaire.nom = data['nom']
            commentaire.commentaire = data['message']
            commentaire.website = data['website']
            commentaire.save()
            return redirect("article")
    form = CommentaireForm()
    return render(request, "appSalama/article.html", context={'article':article,'commentaires':commentaires,'form':form})

def realisations(request):
    realisations = Realisation.objects.all()
    return render(request, "appSalama/realisations.html", context={'realisations':realisations})

def realisation (request, slug: str):
    realisation = Realisation.objects.get(slug=slug)
    return render(request, "appSalama/realisation.html", context={'realisation':realisation})

def contact(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            message = Message()
            message.user_id = 1
            message.email = data['email']
            message.nom = data['nom']
            message.sujet = data['sujet']
            message.message = data['message']
            message.save()
    form = MessageForm()
    return render(request, "appSalama/contact.html",
                  context={'form': form})

def infrastructures (request):
    infrastructures = Infrastructure.objects.all()
    return render(request, "appSalama/infrastrutures.html", context={'infrastrutures':infrastructures})

def infrastructure_categorie (request, categorie: str):
    infrastructures = Infrastructure.objects.filter(categorie=categorie)
    return render(request, "appSalama/infrastrutures.html", context={'infrastrutures':infrastructures})

def connexion(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            email = data['email']
            password = data['password']
            user = authenticate(request, email=email, password=password)
            print(user)
            if user:
                login(request, user)
                return HttpResponse("Login succes!")
    form = LoginForm()
    return render(request, "appSalama/login.html", context={'form':form})
