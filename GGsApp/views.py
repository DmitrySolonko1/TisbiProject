from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.views.generic import ListView, DetailView, CreateView
from .models import *
from .forms import ProductForm


# Create your views here.


class MainPage(ListView):
    model = Product
    template_name = 'GGsApp/MainPage.html'
    context_object_name = 'products'
    allow_empty = True

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['marketplaces'] = Marketplace.objects.all()
        context['title_contains_query'] = self.request.GET.get('title_contains')
        if context['title_contains_query'] != None and context['title_contains_query'] != '':
            context['products_data'] = Product.objects.filter(title__icontains=context['title_contains_query'])
        else:
            context['products_data'] = Product.objects.all().order_by('-pk')
        return context

    def get_queryset(self):
        return Product.objects.all()


class ProductPage(DetailView):
    model = Product
    template_name = 'GGsApp/ProductPage.html'
    context_object_name = 'product'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = Product.objects.get(pk=self.kwargs['pk'])
        return context


class AddProductPage(CreateView):
    form_class = ProductForm
    template_name = 'GGsApp/AddProductPage.html'
    raise_exception = True
    success_url = reverse_lazy('main_page')

    # Функция для кастомной валидации полей формы модели
    def form_valid(self, form):
        # создаем форму, но не отправляем его в БД, пока просто держим в памяти
        fields = form.save(commit=False)
        # Через реквест передаем недостающую форму, которая обязательна
        fields.client_nickname = self.request.user
        # Наконец сохраняем в БД
        fields.save()
        return super().form_valid(form)


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.POST:
            context['product_form'] = ProductForm(self.request.POST, self.request.FILES)

        return context
