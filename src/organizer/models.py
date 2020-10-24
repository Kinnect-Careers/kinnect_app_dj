from django.db.models import (
    CASCADE,
    CharField,
    DateField,
    EmailField,
    ForeignKey,
    ManyToManyField,
    Model,
    TextField,
    URLField,
)

from django_extensions.db.fields import AutoSlugField


class Tag(Model):
    name = CharField(max_length=31, unique=True)
    slug = AutoSlugField(
        max_length=31,
        populate_from=["name"],
        help_text="A label for tag URL config",
    )

    class Meta:
        ordering = ("name",)

    def __str__(self):
        return self.name


class Company(Model):
    name = CharField(
        max_length=50,
        db_index=True,
    )
    location = CharField(max_length=200)
    slug = AutoSlugField(
        max_length=31,
        populate_from=["name"],
        help_text="A label for company URL config",
    )
    tags = ManyToManyField(Tag)

    class Meta:
        ordering = [
            "name",
        ]

    def __str__(self):
        return self.name


class Partner(Company):
    email = EmailField()
    description = TextField()
    website = URLField(max_length=250)

    class Meta:
        get_latest_by = "name"
        ordering = ("name",)


class Job(Model):
    title = CharField(max_length=60)
    text = TextField()
    pub_date = DateField("date published")
    partner = ForeignKey(Partner, on_delete=CASCADE)
    tags = ManyToManyField(Tag)
    slug = AutoSlugField(
        max_length=60, populate_from=["title"]
    )
    class Meta:
        get_latest_by = "pub_date"
        ordering = ["-pub_date", "title"]
        unique_together = ("slug", "partner")
        verbose_name = "published job"

    def __str__(self):
        date_string = self.pub_date.strftime("%Y-%m-%d")
        return f"{self.title} on {date_string}"
