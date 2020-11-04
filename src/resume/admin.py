from django.contrib import admin

from .models import (
    Skill,
    Experience,
    Institution,
    Education,
    Personal,
    Resume,
    ApplicationSubmission,
)


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "description",
        "slug",
    )
    # prepopulated_fields = {"slug": ("name",)}


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = (
        "company",
        "started_at",
        "ended_at",
        "current",
        "slug",
    )


@admin.register(Institution)
class InstitutionAdmin(admin.ModelAdmin):
    list_display = ("name", "location", "slug")


@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = (
        "degree_type",
        "institution",
        "started_at",
        "ended_at",
        "current",
        "slug",
    )


@admin.register(Personal)
class PersonalAdmin(admin.ModelAdmin):
    list_display = ("personal_type", "data", "slug")


@admin.register(Resume)
class ResumeAdmin(admin.ModelAdmin):
    list_display = ("title", "slug")


@admin.register(ApplicationSubmission)
class ApplicationSubmissionAdmin(admin.ModelAdmin):
    list_display = ("resume", "job", "slug")
