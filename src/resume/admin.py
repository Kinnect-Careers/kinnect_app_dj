from django.contrib import admin

from .models import (
  Skill,
  Experience,
  Task,
  Contact,
  Institution,
  Education,
  Link,
  Resume,
  ApplicationSubmission
)

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
  list_display = (
    "name",
    "description",
    "version",
    "slug"
  )
  prepopulated_fields = {"slug": ("name",)}

@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
  list_display = (
    "company",
    "started_at",
    "ended_at",
    "current",
    "slug"
  )
  prepopulated_fields = {"slug": ("company.name", "started_at")}

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
  list_display = (
    "contact_type",
    "contact",
    "slug"
  )

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
  list_display = (
    "experience",
    "description",
    "slug"
  )

@admin.register(Institution)
class InstitutionAdmin(admin.ModelAdmin):
  list_display = (
    "name",
    "location",
    "slug"
  )

@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
  list_display = (
    "degree_type",
    "institution",
    "started_at",
    "ended_at",
    "current",
    "slug"
  )

@admin.register(Link)
class LinkAdmin(admin.ModelAdmin):
  list_display = (
    "link_type",
    "link",
    "slug"
  )

@admin.register(Resume)
class ResumeAdmin(admin.ModelAdmin):
  list_display = (
    "title",
    "slug"
  )

@admin.register(ApplicationSubmission)
class ApplicationSubmissionAdmin(admin.ModelAdmin):
  list_display = (
    "resume",
    "job",
    "slug"
  )
