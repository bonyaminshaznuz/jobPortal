from django.contrib import admin
from .models import *

admin.site.register(Custom_User)
admin.site.register(RecruiterProfile)
admin.site.register(JobSeekerProfile)
admin.site.register(JobModel)
admin.site.register(jobApplyModel)