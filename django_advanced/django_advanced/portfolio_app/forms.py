from django import forms
from django_advanced.portfolio_app.models import Portfolio, DailyPrice 


class DailyPriceForm(forms.ModelForm):
    class Meta:
        model = DailyPrice
        fields = ['date', 'balance', 'comment']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'balance': forms.NumberInput(attrs={'step': 'any'}),
        }

class PortfolioForm(forms.ModelForm):
    class Meta:
        model = Portfolio
        exclude = ['profile']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4, 'cols': 40}),
        }
        help_texts = {
            'description': 'Please provide a detailed description of the portfolio.',
        }


class DeletePortfolioForm(PortfolioForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields.values():
            field.widget.attrs['disabled'] = True
            field.widget.attrs['readonly'] = True
            field.widget.attrs['readonly'] = "readonly"
