from django.db.models import (
    BooleanField,
    CharField,
    TextField,
    DateField,
    DateTimeField,
    ForeignKey,
    IntegerField,
    ManyToManyField,
    Model,
    CASCADE,
)
from django_extensions.db.fields import AutoSlugField
from organizer.models import Tag, Company, Job


class Skill(Model):
    name = CharField(max_length=150, unique=True)
    slug = AutoSlugField(
        max_length=50, populate_from=["name"]
    )
    description = TextField()
    created_at = DateTimeField(auto_now_add=True)
    version = IntegerField(default=1)
    tags = ManyToManyField(Tag)

    class Meta:
        ordering = ["created_at", "version"]
        verbose_name = "added skill"

    def __str__(self):
        return self.name


class Experience(Model):
    company = ForeignKey(Company, on_delete=CASCADE)
    slug = AutoSlugField(
        max_length=50, populate_from=["id", "started_at"]
    )
    started_at = DateField()
    ended_at = DateField(null=True, blank=True)
    current = BooleanField(default=True)
    created_at = DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ("created_at",)

    def __str__(self):
        return self.company.name


class Task(Model):
    experience = ForeignKey(Experience, on_delete=CASCADE)
    slug = AutoSlugField(
        max_length=50, populate_from=["id", "description"]
    )
    description = TextField()
    created_at = DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ("created_at",)

    def __str__(self):
        return f"Task for: {self.experience.company.name}"


class Institution(Model):
    name = CharField(max_length=250)
    created_at = DateTimeField(auto_now=True)
    location = CharField(max_length=150)
    slug = AutoSlugField(
        max_length=50, populate_from=["name", "location"]
    )
    version = IntegerField(default=1)

    class Meta:
        ordering = ("created_at", "version")

    def __str__(self):
        return self.name


class Education(Model):
    HSI = "HSI"
    HS = "HS"
    BS = "BS"
    BA = "BA"
    MS = "MS"
    MA = "MA"
    PH = "PH"
    DEGREE_CHOICES = (
        (HSI, "Incomplete High School"),
        (HS, "High School"),
        (BS, "Bachelor of Science"),
        (BA, "Bachelor of Arts"),
        (MS, "Masters of Science"),
        (MA, "Masters of Arts"),
        (PH, "Doctorate"),
    )
    degree_type = CharField(
        max_length=3,
        choices=DEGREE_CHOICES,
        default=BS,
    )
    slug = AutoSlugField(
        max_length=50, populate_from=["id", "degree_type"]
    )
    institution = ForeignKey(
        Institution,
        related_name="institution",
        on_delete=CASCADE,
    )
    started_at = DateField()
    ended_at = DateField()
    current = BooleanField()

    class Meta:
        ordering = ("ended_at",)

    def __str__(self):
        return (
            f"{self.degree_type} at {self.institution.name}"
        )


class Contact(Model):
    PHONE = "P"
    EMAIL = "E"
    CONTACT_CHOICES = (
        (PHONE, "Phone"),
        (EMAIL, "Email"),
    )
    contact_type = CharField(
        max_length=2,
        choices=CONTACT_CHOICES,
        default=PHONE,
    )
    slug = AutoSlugField(
        max_length=50,
        populate_from=["contact_type", "contact"],
    )
    contact = CharField(max_length=100)
    created_at = DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ("created_at",)

    def __str__(self):
        return f"{self.contact_type}: {self.contact}"


class Link(Model):
    WEBSITE = "W"
    REPOSITORY = "R"
    OTHER = "O"
    LINK_CHOICES = (
        (WEBSITE, "Website"),
        (REPOSITORY, "Repository"),
        (OTHER, "Other"),
    )
    link_type = CharField(
        max_length=2,
        choices=LINK_CHOICES,
        default=WEBSITE,
    )
    link = CharField(max_length=100)
    slug = AutoSlugField(
        max_length=50, populate_from=["link_type", "link"]
    )
    created_at = DateTimeField(auto_now_add=True)
    # owner = ForeignKey("auth.User", on_delete=CASCADE)

    class Meta:
        ordering = ("created_at",)

    def __str__(self):
        return f"{self.link_type}: {self.link}"


class Resume(Model):
    title = CharField(max_length=150)
    slug = AutoSlugField(
        max_length=50, populate_from=["title"]
    )
    contacts = ManyToManyField(Contact)
    links = ManyToManyField(Link)
    experiences = ManyToManyField(Experience)
    educations = ManyToManyField(Education)
    skills = ManyToManyField(Skill)
    created_at = DateTimeField(auto_now=True)

    class Meta:
        ordering = ("created_at",)

    def __str__(self):
        return self.title


class ApplicationSubmission(Model):
    resume = ForeignKey(
        Resume,
        related_name="resume_submission",
        on_delete=CASCADE,
    )
    job = ForeignKey(
        Job,
        related_name="job_submission",
        on_delete=CASCADE,
    )
    slug = AutoSlugField(
        max_length=100, populate_from=["id"]
    )
    created_at = DateTimeField(auto_now=True)
