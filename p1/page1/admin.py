from django.contrib import admin
from page1.models import UserProfile ,WorkerProfile
from page1.models import Category

admin.site.register(UserProfile)
admin.site.register(WorkerProfile)
admin.site.register(Category)
