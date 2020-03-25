from django.contrib import admin
from .models import *
# Register your models here.
class RatingAdmin(admin.ModelAdmin):
    readonly_fields = ('start_date',)


admin.site.register(Member)
admin.site.register(Male,RatingAdmin)
admin.site.register(Female,RatingAdmin)
admin.site.register(ProfileImage)
admin.site.register(ProfileText)
admin.site.register(ProfileImageTest)
