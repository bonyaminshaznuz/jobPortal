from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from myapp.models import *

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = Custom_User
        fields = ['username', 'email', 'password1', 'password2','user_type']
        
        
        
class CustomAuthenticationForm(AuthenticationForm):
    class Meta:
        model = Custom_User  
        fields = ['username', 'password']

class CustomUserChangeForm(forms.ModelForm):
    class Meta:
        model = RecruiterProfile
        fields=['company_name','company_address','company_number','company_bio','profile_image']

class CustomUserChangeFormJobSeeker(forms.ModelForm):
    class Meta:
        model = JobSeekerProfile
        fields=['fullname','jobseeker_address','jobseeker_number','jobseeker_bio','profile_image','jobseeker_skill', 'upload_cv']

class AddJobForm(forms.ModelForm):
    class Meta:
         model=JobModel
         fields=['skills','category','title','openings','description','Job_Image']

class JobSearchForm(forms.ModelForm):
    class Meta:
        model = JobModel
        fields = ['title']

class JobApplyForm(forms.ModelForm):
    class Meta:
        model = jobApplyModel
        fields = ['Resume','Cover','Skills','Apply_Image']