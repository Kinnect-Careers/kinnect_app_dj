from django.contrib import admin

from .models import Tag, Company, Partner, Job


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ("name", "slug")


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ("name", "location", "slug")


@admin.register(Partner)
class PartnerAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "location",
        "email",
        "description",
        "website",
        "slug",
    )


@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "pub_date",
        "slug",
    )
