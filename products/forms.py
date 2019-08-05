from django import forms
from .models import Product, Comment
from products.models import conditions


class ProductForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)
        # self.fields['fee'].widget.attrs['readonly'] = False
        # self.fields['total'].widget.attrs['readonly'] = False
        self.fields['condition'] = forms.ChoiceField(choices=conditions, widget=forms.RadioSelect())

    '''
    def clean_condition(self):
        if len(self.cleaned_data['condition']) > 1:
            raise forms.ValidationError('Select only 1 option')
        return self.cleaned_data['condition']
    '''

    class Meta:
        model = Product
        fields = '__all__'
        exclude = [
            'code',
            'user',
            'slug',
            'available',
            'status',
        ]
        widgets = {
            'category': forms.Select(attrs={'class': "select form-control"}),
            'device': forms.Select(attrs={'class': "select form-control"}),
            'system': forms.Select(attrs={'class': "select form-control"}),
            'model': forms.Select(attrs={'class': "select form-control"}),
            'color': forms.Select(attrs={'class': "select form-control"}),
            'storage': forms.Select(attrs={'class': "select form-control"}),
            'memory': forms.Select(attrs={'class': "select form-control"}),
            'edition': forms.Select(attrs={'class': "select form-control"}),
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['body',]
        exclude = [
            'user',
            'created',
            'updated',
        ]