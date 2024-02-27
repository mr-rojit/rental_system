from django.contrib import admin
from django.utils.html import format_html
from .models import Account, CertificateVerification

admin.site.register(Account)


class CertificateVerificationAdmin(admin.ModelAdmin):
    list_display = ['user_email', 'display_certificate_image', 'approved']

    def user_email(self, obj):
        return obj.user.email

    def display_certificate_image(self, obj):
        if obj.user.certificate:
            return format_html(f'<a href="{obj.user.certificate.url}"><img src="{obj.user.certificate.url}" width="100" height="100" /></a>')
        else:
            return 'No image available'

    display_certificate_image.allow_tags = True
    display_certificate_image.short_description = 'Certificate Image'

admin.site.register(CertificateVerification, CertificateVerificationAdmin)

