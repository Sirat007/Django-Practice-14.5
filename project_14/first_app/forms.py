from django import forms

from .models import Form

class Frontform(forms.Form):
    name = forms.CharField()
    email = forms.EmailField( 
    label="Please enter your email address")
    date = forms.DateField()
    #comment = forms.CharField(widget=forms.Textarea)
    birth_date = forms.DateField(widget=forms.NumberInput(attrs={'type': 'date'}))
    BIRTH_YEAR_CHOICES = ['2000', '2001', '2002','2003']
    birth_year = forms.DateField(widget=forms.SelectDateWidget(years=BIRTH_YEAR_CHOICES))
    url = forms.URLField(label="Your website", required=False)
   
    birthday = forms.CharField(widget=forms.DateInput(attrs= {'type' : 'date'}))
    appointment = forms.CharField(widget=forms.DateInput(attrs= {'type' : 'datetime-local'}))
    message = forms.CharField(max_length = 10)
    
    
    
    CHOICES = [
        ('black', 'Black'),
        ('green', 'Green'),
        ('red', 'Red'),
    ]
    colors = forms.MultipleChoiceField(choices=CHOICES,widget=forms.CheckboxSelectMultiple)
    FAVORITE_Game = [
        ('cricket', 'Cricket'),
        ('football', 'Football'),
        ('badminton', 'Badminton'),
    ]
    favorite_game = forms.ChoiceField(widget=forms.RadioSelect, choices=FAVORITE_Game)
    first_name = forms.CharField(initial='Your name')
    last_name = forms.CharField(max_length = 150) 
    roll = forms.IntegerField( 
                     help_text = "Enter 8 digit roll number"
                     ) 
    password = forms.CharField(widget = forms.PasswordInput()) 

    agree = forms.BooleanField()

class ModelForm(forms.ModelForm):
    class Meta:
        model  = Form
        fields = '__all__'