from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

from .forms import BbForm
from .models import Bb, Rubric


def index(request):
    """чтобы на главной выводилась панель навигации"""
    bbs = Bb.objects.all()
    rubrics = Rubric.objects.all()
    """контекст шаблона"""
    context = {'bbs': bbs, 'rubrics': rubrics}
    """шаблонизатор выполняет объединение с данными из контекста т.е. рендерит"""
    return render(request, 'boards/index.html', context)


def by_rubric(request, rubric_id):
    """представление разбиения объявлений по рубрикам"""
    bbs = Bb.objects.filter(rubric=rubric_id)
    rubrics = Rubric.objects.all()
    current_rubric = Rubric.objects.get(pk=rubric_id)
    context = {'bbs': bbs, 'rubrics': rubrics, 'current_rubric': current_rubric}
    return render(request, 'boards/by_rubric.html', context)


class BbCreateView(CreateView):
    """вывод и обработка формы,связанные с моделью в формах"""
    template_name = 'boards/create.html'
    form_class = BbForm
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        """формирует контексат шаблона"""
        context = super().get_context_data(**kwargs)
        context['rubrics'] = Rubric.objects.all()
        return context
