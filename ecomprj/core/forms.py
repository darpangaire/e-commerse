from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,UserChangeForm,SetPasswordForm
from django import forms
from .models import Profile

class UserInfoForm(forms.ModelForm):
    phone = forms.CharField(
        label="",
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone'}),
        required=False
    )
    address1 = forms.CharField(label="",widget=forms.TextInput(attrs={'class':'form-control','placeholder' : 'Address 1'}),required=False)
    
    address2 = forms.CharField(label="",widget=forms.TextInput(attrs={'class':'form-control','placeholder' : 'Address 2'}),required=False)
    
    city = forms.CharField(label="",widget=forms.TextInput(attrs={'class':'form-control','placeholder' : 'city'}),required=False)
    
    state = forms.CharField(label="",widget=forms.TextInput(attrs={'class':'form-control','placeholder' : 'State'}),required=False)
    
    zipcode = forms.CharField(label="",widget=forms.TextInput(attrs={'class':'form-control','placeholder' : 'zipcode'}),required=False)
    
    country = forms.CharField(label="",widget=forms.TextInput(attrs={'class':'form-control','placeholder' : 'country'}),required=False)
    
    class Meta:
        model = Profile()
        fields = ('phone','address1','address2','city','state','zipcode','country')
        

class ChangePasswordForm(SetPasswordForm):
    class Meta:
        model = User
        fields = ['new_password1','new_password2']
        
    def __init__(self, *args, **kwargs):
        super(ChangePasswordForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.label = ''
        
        self.fields['new_password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['new_password1'].help_text = (
            '<small class="form-text text-muted">'
            '<ul>'
            '<li>Your password must not be too similar to your personal information.</li>'
            '<li>Must contain at least 8 characters.</li>'
            '<li>Cannot be a commonly used password.</li>'
            '<li>Cannot be entirely numeric.</li>'
            '</ul>'
            '</small>'
        )
        self.fields['new_password2'].widget.attrs['placeholder'] = 'Confirm Password'
        self.fields['new_password2'].help_text = (
            '<small class="form-text text-muted">Enter the same password as before, for verification.</small>'
        )
        


class UpdateUserForm(UserChangeForm):
    # Hide this stuff
    password = None
    
    # get all this stuff
    email = forms.EmailField(
        label="",
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email Address'})
    )
    
    first_name = forms.CharField(
        label="",
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}),required=False
    )
    last_name = forms.CharField(
        label="",
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}),required=False
    )

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')

    def __init__(self, *args, **kwargs):
        super(UpdateUserForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.label = ''
        
        # Custom placeholders and help texts
        self.fields['username'].widget.attrs['placeholder'] = 'Username'
        self.fields['username'].help_text = (
            '<small class="form-text text-muted">'
            'Required. 150 characters or fewer. Letters, digits, and @/./+/-/_ only.'
            '</small>'
        )

 

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user



class SignUpForm(UserCreationForm):
    email = forms.EmailField(
        label="",
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email Address'})
    )
    first_name = forms.CharField(
        label="",
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'})
    )
    last_name = forms.CharField(
        label="",
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'})
    )

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.label = ''
        
        # Custom placeholders and help texts
        self.fields['username'].widget.attrs['placeholder'] = 'Username'
        self.fields['username'].help_text = (
            '<small class="form-text text-muted">'
            'Required. 150 characters or fewer. Letters, digits, and @/./+/-/_ only.'
            '</small>'
        )
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password1'].help_text = (
            '<small class="form-text text-muted">'
            '<ul>'
            '<li>Your password must not be too similar to your personal information.</li>'
            '<li>Must contain at least 8 characters.</li>'
            '<li>Cannot be a commonly used password.</li>'
            '<li>Cannot be entirely numeric.</li>'
            '</ul>'
            '</small>'
        )
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
        self.fields['password2'].help_text = (
            '<small class="form-text text-muted">Enter the same password as before, for verification.</small>'
        )

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
