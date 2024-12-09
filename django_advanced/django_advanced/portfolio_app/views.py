import base64
import io
import urllib
from io import BytesIO
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
import matplotlib.pyplot as plt
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404, HttpResponse
from django.urls import reverse_lazy
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  UpdateView)
from django_advanced.portfolio_app.forms import (DeletePortfolioForm,
                                                 PortfolioForm)
from django_advanced.portfolio_app.models import Portfolio
from django_advanced.user_app.mixins import AuthorMixin
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from django_advanced.portfolio_app.serializers import PortfolioSerializer
from drf_spectacular.utils import extend_schema

from django.forms import modelformset_factory, inlineformset_factory
from .models import Portfolio, DailyPrice
from .forms import PortfolioForm, DailyPriceForm

DailyPriceFormSet = inlineformset_factory(
    Portfolio,
    DailyPrice,
    form=DailyPriceForm,
    extra=2,
    can_delete=False,
)

        # dates = ['Indices', 'Stocks', 'Commodities', 'Cryptocurrency', 'Forex', 'ETFs']
        # price = [
        #     portfolio.indices,
        #     portfolio.stocks,
        #     portfolio.commodities,
        #     portfolio.cryptocurrency,
        #     portfolio.forex,
        #     portfolio.etfs
        # ]

@extend_schema(
    request=PortfolioSerializer,
    responses={201: PortfolioSerializer, 400: PortfolioSerializer},
)
class PortfolioViewSet(viewsets.ModelViewSet):
    queryset = Portfolio.objects.all()
    serializer_class = PortfolioSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Portfolio.objects.filter(profile=self.request.user.profile)


class DetailsPortfolioPage(LoginRequiredMixin, DetailView):
    model = Portfolio
    template_name = 'portfolio/details-portfolio.html'

    def get_object(self, queryset=None):
        portfolio = super().get_object(queryset)
        if portfolio.profile != self.request.user.profile:
            raise Http404("You do not have permission view this portfolio.")
        return portfolio
        
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        portfolio = self.get_object()
        context['profile'] = portfolio.profile
        context['daily_prices'] = self.object.daily_prices.all()
        
        daily_price_id = self.request.GET.get('daily_price_id')
        if daily_price_id:
            daily_price = get_object_or_404(DailyPrice, pk=daily_price_id, portfolio=portfolio)
            context['daily_price_id'] = daily_price_id
            context['daily_price_form'] = DailyPriceForm(instance=daily_price)
        else:
            context['daily_price_form'] = DailyPriceForm()
            
        dates = portfolio.get_dates()
        price = portfolio.get_balance()
        plt.figure(figsize=(10, 5))
        plt.plot(dates, price, marker='o', linestyle='-', color='#337ab7')
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
    context_object_name = 'page_obj '
    paginate_by = 6
    
    def get_queryset(self):
        return Portfolio.objects.filter(profile=self.request.user.profile)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        portfolio = self.get_queryset()
        categories = [ asset.title for asset in portfolio]
        values = [ asset.get_latest_balance().balance for asset in portfolio]


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



class CreatePortfolioPage(LoginRequiredMixin, CreateView):
    model = Portfolio
    form_class = PortfolioForm
    template_name = 'portfolio/create-portfolio.html'
    success_url = reverse_lazy('portfolio')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['daily_price_form'] = DailyPriceForm()
        return context
    
    def form_valid(self, form):
        portfolio = form.save(commit=False)
        portfolio.profile = self.request.user.profile 
        portfolio.save()

        if self.request.method == "POST":
            daily_price_form = DailyPriceForm(self.request.POST)
            if daily_price_form.is_valid():
                daily_price = daily_price_form.save(commit=False)
                daily_price.portfolio = portfolio
                daily_price.save()

        return redirect('portfolio')
    


class EditPortfolioPage(LoginRequiredMixin, UpdateView):
    model = Portfolio
    form_class = PortfolioForm
    template_name = 'portfolio/edit-portfolio.html'
    success_url = reverse_lazy('portfolio')

    def get_object(self, queryset=None):
        portfolio = super().get_object(queryset)
        if portfolio.profile != self.request.user.profile:
            raise Http404("You do not have permission to edit this portfolio.")
        return portfolio

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        portfolio = self.get_object()
        context['profile'] = portfolio.profile
        context['daily_prices'] = portfolio.daily_prices.all()
        
        daily_price_id = self.request.GET.get('daily_price_id')
        if daily_price_id:
            daily_price = get_object_or_404(DailyPrice, pk=daily_price_id, portfolio=portfolio)
            context['daily_price_id'] = daily_price_id
            context['daily_price_form'] = DailyPriceForm(instance=daily_price)
        else:
            context['daily_price_form'] = DailyPriceForm()

        return context
    
    def form_valid(self, form):
        portfolio = form.save(commit=False)
        portfolio.profile = self.request.user.profile 
        portfolio.save()
        return redirect('details-portfolio', pk=portfolio.pk)


class DeletePortfolioPage(LoginRequiredMixin, AuthorMixin, DeleteView):
    model = Portfolio
    form_class = DeletePortfolioForm
    template_name = 'portfolio/delete-portfolio.html'
    success_url = reverse_lazy('portfolio')

    def get_object(self, queryset=None):
        portfolio = super().get_object(queryset)
        if portfolio.profile != self.request.user.profile:
            raise Http404("You do not have permission to delete this portfolio.")
        return portfolio

    def get_initial(self):
        return self.object.__dict__

    def form_invalid(self, form):
        return self.form_valid(form)


@login_required
def daily_price_functionality(request, pk):
    portfolio = Portfolio.objects.get(pk=pk)
    daily_price_id = request.GET.get('daily_price_id')
    
    if request.method == 'POST':
        if daily_price_id:
            daily_price = get_object_or_404(DailyPrice, pk=daily_price_id, portfolio=portfolio)
            daily_price_form = DailyPriceForm(request.POST, instance=daily_price)
        else:
            daily_price_form = DailyPriceForm(request.POST)

        if daily_price_form.is_valid():
            daily_price = daily_price_form.save(commit=False)
            daily_price.portfolio = portfolio
            daily_price.save()
        
    return redirect(f'{request.META.get("HTTP_REFERER")}')
