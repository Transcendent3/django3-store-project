from django.contrib import admin

# Register your models here.
from users.models import User
from products.admin import BasketInline

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    inlines = (BasketInline,)

