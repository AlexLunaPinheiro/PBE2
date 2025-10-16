import django_filters as df
from django.db.models import Value, CharField, Q
from django.db.models.functions import Concat
from .models import Autor, Livro


class AutorFilter(df.FilterSet):
    nome = df.CharFilter(method='filter_nome')
    nacionalidade = df.CharFilter(method="filter_nacionalidade")

    def filter_nome(self,  queryset,value: str):
        value = value.lower().strip()
        palavras = value.split()

        queryset = queryset.annotate(
            nome_completo=Concat('nome', Value(' '), 'sobrenome', output_field=CharField())
        )

        if len(palavras) == 1:
            return queryset.filter(
                Q(nome__istartswith=palavras[0]) | Q(sobrenome__istartswith=palavras[0])
            )
        else:
            for palavra in palavras:
                queryset = queryset.filter(nome_completo__icontains=palavra)
            return queryset
    
      
    
    def filter_nacionalidade(self, qs, value: str):
        if not value:
            return qs
        return qs.filter(nacionalidade__icontains=value)
    
    class Meta:
        model = Autor
        fields = "__all__"


class LivroFilter(df.FilterSet):
    titulo = df.CharFilter(method='filter_titulo')
    editora = df.CharFilter(method="filter_editora")

    def filter_editora(self, qs, name, value):
        if not value:
            return qs
        return qs.filter(editora__exact=value)
    
    def filter_titulo(self, qs, titulo, value: str):
        if not value:
            return qs
        return qs.filter(titulo__icontains=value)
    
    class Meta:
        model = Autor
        fields = "__all__"
