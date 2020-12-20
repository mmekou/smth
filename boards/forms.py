from django.forms import ModelForm

from .models import Bb

"""для добавления в бд новых объявлений"""
class BbForm(ModelForm):
    class Meta:
        model = Bb
        fields = ('title', 'content', 'price', 'rubric')