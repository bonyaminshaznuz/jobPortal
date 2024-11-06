from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from myapp.forms import *
from myapp.models import *
from django.contrib.auth.decorators import login_required

def registerpage(request):
    if request.user.is_authenticated:
        return redirect('profile')
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            user.save()
            if user.user_type == 'recruiter':
                RecruiterProfile.objects.create(user=user)
            elif user.user_type == 'jobSeeker':
                JobSeekerProfile.objects.create(user=user)
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})

def loginPage(request):
    if request.user.is_authenticated:
        return redirect('profile')
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('profile')
    else:
        form = AuthenticationForm()
    
    return render(request, 'login.html', {'form': form})

@login_required
def profilepage(request):
    return render(request, 'profile.html')

@login_required
def editprofile(request):
    if request.user.user_type == 'recruiter':
        profile = get_object_or_404(RecruiterProfile, user=request.user)
        if request.method == 'POST':
            form = CustomUserChangeForm(request.POST, request.FILES, instance=profile)
            if form.is_valid():
                form.save()
                return redirect('profile')
        else:
            form = CustomUserChangeForm(instance=profile)

    else:
        profile = get_object_or_404(JobSeekerProfile, user=request.user)
        if request.method == 'POST':
                form = CustomUserChangeFormJobSeeker(request.POST, request.FILES, instance=profile)
                if form.is_valid():
                    form.save()
                    return redirect('profile')
        else:
            form = CustomUserChangeFormJobSeeker(instance=profile)

    return render(request, 'edit-profile.html', {'form': form})

def logoutpage(request):
    logout(request)
    return redirect('login')

@login_required
def addjobpage(request):
    if request.user.user_type == 'recruiter':
        if request.method == 'POST':
            form = AddJobForm(request.POST, request.FILES)
            if form.is_valid():
                jobpost = form.save(commit=False)
                jobpost.user = request.user 
                jobpost.save()
                return redirect('viewjobs') 
        else:
            form = AddJobForm()
        
        return render(request, 'add-job.html', {'form': form})
    else:
        return redirect('profile')

@login_required
def viewjobpage(request):
    if request.user.user_type == 'recruiter':
        if request.user.is_authenticated:
            jobs = JobModel.objects.filter(user=request.user) 
        return render(request, 'view-job.html', {'jobs': jobs})
    else:
        return redirect('profile')
    
@login_required
def editjobpage(request, job_id):
    if request.user.user_type == 'recruiter':
        job = get_object_or_404(JobModel, id=job_id)
        if request.method == 'POST':
            form = AddJobForm(request.POST, request.FILES, instance=job) 
            if form.is_valid():
                form.save()
                return redirect('viewjobs') 
        else:
            form = AddJobForm(instance=job)

        return render(request, 'edit-job.html', {'form': form, 'job': job})
    else:
        return redirect('profile')
    
@login_required        
def deletejobpage(request, job_id):  
    jobp = JobModel.objects.get(id=job_id)  
    jobp.delete()  
    return redirect('viewjobs')

def indexpage(request):
    obj=JobModel.objects.all()
    return render(request,'index.html',{'obj':obj})

def jobsearchpage(request):
    form = JobSearchForm()
    results = []
    
    if request.method == 'GET':
        title = request.GET.get('title')
        if title:
            results = JobModel.objects.filter(title__icontains=title)
    
    return render(request, 'job-search.html', {'form': form, 'results': results})

def jobapplypage(request, job_id):
    jobs = get_object_or_404(JobModel, id=job_id)

    if request.method == 'POST':
        apply = JobApplyForm(request.POST, request.FILES) 
        if apply.is_valid():
            jobapply = apply.save(commit=False)
            jobapply.user = request.user 
            jobapply.job = jobs  
            jobapply.save()  
            
            return redirect("appliedjobuser") 

    else:
        apply = JobApplyForm() 
        
    return render(request, "apply-Job.html", {'jobs': jobs, 'form': apply})

def applieduserjobpage(request):
    if request.user.user_type == 'jobSeeker':
        if request.user.is_authenticated:
            jobs = jobApplyModel.objects.filter(user=request.user) 
        return render(request, 'applied-job-user.html', {'jobs': jobs})
    else:
        return redirect('profile')
    
def appliedjobviewpage(request):
    if request.user.user_type == 'recruiter':
        jobview = jobApplyModel.objects.all()
        return render(request, 'applied-job-view.html', {'jobview': jobview})
    else:
        return redirect('profile')

def skillMatchingPage(request):
    user=request.user
    
    mySkill=user.jobseeker_profile.jobseeker_skill
    jobs=JobModel.objects.filter(skills=mySkill)
    context={
        'jobs':jobs
    }
    print(mySkill)
    
    return render(request,"skill-matching-page.html",context)