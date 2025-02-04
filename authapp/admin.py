from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from authapp.models import CustomUser  # Import from authapp
from shortener.models import URLShortener  # Import from shortener app

class URLShortenerInline(admin.TabularInline):
    model = URLShortener
    extra = 0
    readonly_fields = ('shortened_url', 'actual_url', 'click_count')

class CustomUserAdmin(UserAdmin):
    inlines = [URLShortenerInline]
    list_display = ('email', 'username', 'is_verified', 'shortened_urls_count','is_staff')

    def shortened_urls_count(self, obj):
        return obj.shortened_urls.count()
    shortened_urls_count.short_description = 'Shortened URLs'

# admin.site.unregister(CustomUser)  # Unregister the default admin if it exists
admin.site.register(CustomUser, CustomUserAdmin)
