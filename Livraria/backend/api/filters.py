import django_filters as df
from django.db.models import Q
from .models import Autor

class AutorFilter(df.FilterSet):
    nome = df.CharFilter(method='filter_nome')
    nacionalidade = df.CharFilter(field_name="nacionalidade", lookup_expr='iexact')

    def filter_nome(self, qs, name, value: str):
        if not value:
            return qs
        return qs.filter(Q(nome__icontains = value) | Q(nacionalidade__icontains = value))
    
    class Meta:
        model = Autor
        fields = "__all__"