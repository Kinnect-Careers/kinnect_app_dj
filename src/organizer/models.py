from django.db.models import (
  CASCADE,
  CharField,
  DateField,
  EmailField,
  ForeignKey,
  ManyToManyField,
  Model,
  TextField,
  URLField
)

from django_extensions.db.fields import AutoSlugField

class Tag(Model):
  name = CharField(
    max_length=31,
    unique=True
  )
  slug = AutoSlugField(
    max_length=31,
    populate_from=["name"],
    help_text="A label for tag URL config",
  )

  class Meta:
    ordering = ('name',)

  def __str__(self):
    return self.name


class Company(Model):
  name = CharField(
    max_length=31,
    db_index=True,
  )
  slug = AutoSlugField(
    max_length=31,
    populate_from=["name"],
    help_text="A label for company URL config",
  )
  location = CharField(max_length=200)

  class Meta:
    ordering = ['name',]

  def __str__(self):
    return self.name
  


class Partner(Company):
  contact = EmailField()
  description = TextField()
  website = URLField(max_length=250)
  tags = ManyToManyField(Tag)

  class Meta:
    get_latest_by = 'founded_date'
    ordering = ('name',)

