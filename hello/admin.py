from django.contrib import admin

# Register your models here.
from hello.models import Birthday


class BirthdayAdmin(admin.ModelAdmin):
    pass


admin.site.register(Birthday, BirthdayAdmin)
