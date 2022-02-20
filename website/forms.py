from django import forms

# Nome das variáveis é o label no HTML
class NewPostForm(forms.Form):
    identificação = forms.CharField(
        error_messages={'required': 'É obrigatório o preenchimento do nome'},
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Digite o seu nome que será mostrado"}
        )
    )
    forma_de_contato = forms.CharField(
        error_messages={'invalid': 'É necessário uma forma de contato!'},
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Deixe aqui uma forma para te contatar! (Perfil de rede social ou número de telefone)"}
        )
    )
    conteúdo_da_postagem = forms.CharField(
        error_messages={'required': 'É obrigatório o preenchimento do campo de postagem!'},
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Sua postagem"}
        )
    )
    # TODO adicionar campo não obrigatório de upload de imagens