from django import forms

GENRES = (
    ('Genre...','Genre...'),
    ('M','M'),
    ('F','F'),
)

class CommentaireForm(forms.Form):
    nom = forms.CharField(label="",required=True, widget=forms.TextInput(attrs={'placeholder':"Nom",'class':'form-control'}))
    email = forms.CharField(label="",required=True, widget=forms.TextInput(attrs={'placeholder':"Email",'type':'email','class':'form-control'}))
    website = forms.CharField(label="",required=True, widget=forms.TextInput(attrs={'placeholder':"Website",'class':'form-control'}))
    message = forms.CharField(label="",required=True, widget=forms.Textarea(attrs={'placeholder':"Message",'rows':'2','class':'form-control'}))


class InscriptionForm(forms.Form):
    nom = forms.CharField(label="",required=True, widget=forms.TextInput(attrs={'placeholder':"Nom",'class':'form-control'}))
    post_nom = forms.CharField(label="",required=True, widget=forms.TextInput(attrs={'placeholder':"Post-nom",'class':'form-control'}))
    prenom = forms.CharField(label="",required=True, widget=forms.TextInput(attrs={'placeholder':"Prénom",'class':'form-control'}))
    genre = forms.ChoiceField(label="", required=True, choices=GENRES)
    date_naissance = forms.CharField(label="",required=True, widget=forms.TextInput(attrs={'placeholder':"Date de naissance", 'type':'date','class':'form-control'}))
    pourcentage = forms.CharField(label="",required=True, widget=forms.TextInput(attrs={'placeholder':"Pourcentage",'class':'form-control'}))
    adresse = forms.CharField(label="",required=True, widget=forms.TextInput(attrs={'placeholder':"Adresse",'class':'form-control'}))
    nom_responsable = forms.CharField(label="",required=True, widget=forms.TextInput(attrs={'placeholder':"Nom de responsable",'class':'form-control'}))
    religion = forms.CharField(label="",required=True, widget=forms.TextInput(attrs={'placeholder':"Religion",'class':'form-control'}))
    motif = forms.CharField(label="",required=True, widget=forms.TextInput(attrs={'placeholder':"Motif",'rows':'4','class':'form-control'}))


class MessageForm(forms.Form):
    nom = forms.CharField(label="", required=True,
                          widget=forms.TextInput(attrs={'placeholder': "Nom", 'class': 'form-control'}))
    email = forms.CharField(label="", required=True, widget=forms.TextInput(
        attrs={'placeholder': "Email", 'type': 'email', 'class': 'form-control'}))
    sujet = forms.CharField(label="", required=True,
                              widget=forms.TextInput(attrs={'placeholder': "Sujet", 'class': 'form-control'}))
    message = forms.CharField(label="", required=True, widget=forms.Textarea(
        attrs={'placeholder': "Message", 'rows': '2', 'class': 'form-control'}))

class LoginForm(forms.Form):
    email = forms.CharField(label="",required=True, widget=forms.TextInput(attrs={'placeholder':"Votr email",'type':'email','class':'form-control'}))
    password = forms.CharField(label="",required=True, widget=forms.PasswordInput(attrs={'placeholder':"Mot de passe",'class':'form-control'}))
