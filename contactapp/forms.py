from django import forms
class Contactform(forms.Form):
    name=forms.CharField(
        label='Enter your name',
        widget=forms.TextInput(
            attrs={
                'placeholder':'Your name',
                'class':"form-control"
            }
        )
    )

    salary = forms.IntegerField(
        label='Enter your salary',
        widget = forms.NumberInput(
            attrs = {
                'placeholder':'Your salary',
                'class': "form-control"
            }
        )
    )
    email=forms.EmailField(
        label='Enter your Email ID',
        widget=forms.EmailInput(
            attrs={
                'placeholder':'Your Email id',
                'class':'form-control'
            }
        )
    )
    mobile=forms.CharField(
        label='Enter your mobile Number',
        widget=forms.NumberInput(
            attrs={
                'placeholder':'Your Mobile no',
                'class':'form-control'
            }
        )
    )
    location = forms.CharField(
        label='Enter your Location',
        widget = forms.TextInput(
            attrs = {
                'placeholder':'Your location',
                'class': 'form-control'
            }
        )
    )