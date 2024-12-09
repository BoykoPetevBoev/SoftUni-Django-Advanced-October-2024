from django import forms
from django_advanced.portfolio_app.models import Portfolio, DailyPrice 


class DailyPriceForm(forms.ModelForm):
    class Meta:
        model = DailyPrice
        fields = ['date', 'balance', 'comment']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'balance': forms.NumberInput(attrs={'step': 'any'}),
            'comment': forms.Textarea(attrs={'rows': 3}),
        }
        labels = {
            'date': 'Select Date',
            'balance': 'Enter Balance',
            'comment': 'Add Comment (optional)',
        }
        help_texts = {
            'date': 'Please select the date for this entry.',
            'balance': 'Enter the balance in the currency of your portfolio.',
            'comment': 'Optional. You can add any relevant notes here.',
        }
        placeholders = {
            'date': 'YYYY-MM-DD',
            'balance': 'e.g., 1000.50',
            'comment': 'Type your comment here...',
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['date'].widget.attrs['placeholder'] = self.fields['date'].help_text
        self.fields['balance'].widget.attrs['placeholder'] = self.fields['balance'].help_text


class PortfolioForm(forms.ModelForm):
    class Meta:
        model = Portfolio
        fields = ['title', 'description', 'assetType']
        widgets = {
            'description': forms.Textarea(),
            'title': forms.TextInput(),
            'assetType': forms.Select(),
        }
        labels = {
            'title': 'Portfolio Title',
            'description': 'Portfolio Description',
            'assetType': 'Asset Type',
        }
        help_texts = {
            'description': 'Please provide a detailed description of the portfolio.',
            'title': 'Provide a brief title for your portfolio.',
            'assetType': 'Select the asset type for the portfolio (e.g., Stocks, Forex, Crypto, etc.).',
        }
        placeholders = {
            'title': 'Enter a title for your portfolio',
            'description': 'Describe your portfolio in detail...',
            'assetType': 'Choose an asset type...',
        }
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].widget.attrs['placeholder'] = self.fields['title'].help_text
        self.fields['description'].widget.attrs['placeholder'] = self.fields['description'].help_text
        self.fields['assetType'].widget.attrs['placeholder'] = self.fields['assetType'].help_text


class DeletePortfolioForm(PortfolioForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields.values():
            field.widget.attrs['disabled'] = True
            field.widget.attrs['readonly'] = True
            field.widget.attrs['readonly'] = "readonly"
