from django import forms

class ContactForm(forms.Form):
    nome = forms.CharField(label="Nome", widget=forms.TextInput(attrs={'placeholder':'Digite seu nome'}) )
    email = forms.EmailField(label="Email", widget=forms.TextInput(attrs={'placeholder':'Digite seu email'}))
    mensagem = forms.CharField(label="Assunto", widget=forms.Textarea(attrs={'placeholder': 'Digite seu texto aqui'}))


