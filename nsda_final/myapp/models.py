from django.db import models
from django.contrib.auth.models import AbstractUser


class Custom_User(AbstractUser):
    USER_TYPE_CHOICES = [
        ('recruiter', 'Recruiter'),
        ('jobSeeker', 'JobSeeker'),
    ]
    user_type = models.CharField(choices=USER_TYPE_CHOICES, max_length=20)


class RecruiterProfile(models.Model):
    user = models.OneToOneField(Custom_User, on_delete=models.CASCADE, related_name='recruiter_profile')
    profile_image = models.ImageField(upload_to="Media/Profile_pic", blank=True, null=True)
    company_name = models.CharField(max_length=255)
    company_address = models.CharField(max_length=255)
    company_number = models.CharField(max_length=20)
    company_bio = models.TextField(blank=True)

    def __str__(self):
        return f"{self.company_name} - Recruiter Profile"

class JobSeekerProfile(models.Model):
    user = models.OneToOneField(Custom_User, on_delete=models.CASCADE, related_name='jobseeker_profile')
    profile_image = models.ImageField(upload_to="Media/Profile_pic", blank=True, null=True)
    fullname = models.CharField(max_length=255)
    jobseeker_address = models.CharField(max_length=255)
    jobseeker_number = models.CharField(max_length=20)
    jobseeker_bio = models.TextField(blank=True)
    
    SKILL_CHOICES = [
        ('programming','Programming'),
        ('networking','Networking'),
        ('graphics_design','Graphics Design'),
        ('cyber_security','Cyber Security'),
    ]
    jobseeker_skill = models.CharField(choices=SKILL_CHOICES, max_length=20)
    upload_cv = models.FileField(upload_to='cv_uploads/', blank=True, null=True)

    def __str__(self):
        return f"{self.fullname} - Job Seeker Profile"
    
class JobModel(models.Model):
    
    CATEGORY=[
        ('full_time','Full Time'),
        ('part_time','Part Time'),
    ]
    SKILLS=[
        ('programming','Programming'),
        ('networking','Networking'),
        ('graphics_design','Graphics Design'),
        ('cyber_security','Cyber Security'),
    ]
    
    skills=models.CharField(choices=SKILLS,max_length=100,null=True)
    category=models.CharField(choices=CATEGORY,max_length=100,null=True)
    user = models.ForeignKey(Custom_User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    openings = models.PositiveIntegerField()
    description = models.TextField()
    Job_Image=models.ImageField(upload_to='Media/Job_Image',null=True)
    
    def __str__(self):
        return f"{self.user.username} {self.title}"

class jobApplyModel(models.Model):

    user=models.ForeignKey(Custom_User,on_delete=models.CASCADE,null=True)
    job=models.ForeignKey(JobModel,on_delete=models.CASCADE,null=True)
    Resume = models.FileField(upload_to="Media/Resume",max_length=200, null=True, blank=True) 
    Cover = models.TextField(null=True, blank=True) 
    Skills = models.CharField(max_length=200, null=True, blank=True) 
    Apply_Image=models.ImageField(upload_to='Media/Job_Image',null=True)
    
    def __str__(self) -> str:
        return self.user.username+"-"+self.job.title
    

