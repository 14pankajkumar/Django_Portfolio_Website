from django.contrib import admin
from app.models import (Contact, About, Fact, Skill, Summary, 
Education, Professional, Application, Startup, Web, Service, SocialMedia, Profile)

# Register your models here.
admin.site.register(Contact)
admin.site.register(About)
admin.site.register(Fact)
admin.site.register(Skill)
admin.site.register(Summary)
admin.site.register(Education)
admin.site.register(Professional)
admin.site.register(Application)
admin.site.register(Startup)
admin.site.register(Web)
admin.site.register(Service)
admin.site.register(SocialMedia)
admin.site.register(Profile)