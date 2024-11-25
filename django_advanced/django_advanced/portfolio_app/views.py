import base64
import io
import urllib
from io import BytesIO

import matplotlib.pyplot as plt
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  UpdateView)
from django_advanced.portfolio_app.forms import (DeletePortfolioForm,
                                                 PortfolioForm)
from django_advanced.portfolio_app.models import Portfolio
from django_advanced.user_app.mixins import AuthorMixin


class DetailsPortfolioPage(LoginRequiredMixin, DetailView):
    model = Portfolio
    template_name = 'portfolio/details-portfolio.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        portfolio = self.get_object()
        context['profile'] = portfolio.profile

        categories = ['Indices', 'Stocks', 'Commodities', 'Cryptocurrency', 'Forex', 'ETFs']
        values = [
            portfolio.indices,
            portfolio.stocks,
            portfolio.commodities,
            portfolio.cryptocurrency,
            portfolio.forex,
            portfolio.etfs
        ]


        plt.figure(figsize=(10, 5))
        plt.bar(categories, values, color='#337ab7')
        plt.xlabel('Categories')
        plt.ylabel('Values')
        plt.title('Portfolio Distribution')

        buffer = BytesIO()
        plt.savefig(buffer, format='png')
        buffer.seek(0)
        img_base64 = base64.b64encode(buffer.read()).decode('utf-8')

        context['chart'] = img_base64

        return context


class ListPortfolioPage(LoginRequiredMixin, ListView):
    model = Portfolio
    template_name = 'portfolio/list-portfolio.html'
    context_object_name = 'page_obj'
    paginate_by = 6

    def get_queryset(self):
        return Portfolio.objects.filter(profile=self.request.user.profile)



class CreatePortfolioPage(LoginRequiredMixin, CreateView):
    model = Portfolio
    form_class = PortfolioForm
    template_name = 'portfolio/create-portfolio.html'
    success_url = reverse_lazy('portfolio-list')
    
    def form_valid(self, form):
        portfolio = form.save(commit=False)
        portfolio.profile = self.request.user.profile
        return super().form_valid(form)
    


class EditPortfolioPage(LoginRequiredMixin, UpdateView):
    model = Portfolio
    form_class = PortfolioForm
    template_name = 'portfolio/edit-portfolio.html'
    success_url = reverse_lazy('portfolio-list')


class DeletePortfolioPage(LoginRequiredMixin, AuthorMixin, DeleteView):
    model = Portfolio
    form_class = DeletePortfolioForm
    template_name = 'portfolio/delete-portfolio.html'
    success_url = reverse_lazy('portfolio-list')

    def get_initial(self):
        return self.object.__dict__

    def form_invalid(self, form):
        return self.form_valid(form)