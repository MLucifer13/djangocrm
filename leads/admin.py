from django.contrib import admin
from .models import User, Lead, Agent

admin.site.register(Agent)
admin.site.register(Lead)
admin.site.register(User)