from django.db.models import (
  CharField,
  TextField,
  DateField,
  ForeignKey,
  ManyToManyField,
  Model,
  CASCADE
)
from django_extensions.db.fields import AutoSlugField
from organizer.models import Partner, Tag

class Job(Model):
  title = CharField(max_length=60)
  slug = AutoSlugField(
    max_length=60,
    populate_from=["title"]
  )
  text = TextField()
  pub_date = DateField("date published")
  partner = ForeignKey(
    Partner,
    on_delete=CASCADE
  )
  tags = ManyToManyField(Tag)

  class Meta:
    get_latest_by = 'pub_date'
    ordering = ['-pub_date', 'title']
    unique_together = ('slug', 'partner')
    verbose_name = 'published job'

  def __str__(self):
    date_string = self.pub_date.strftime("%Y-%m-%d")
    return f"{self.title} on {date_string}"
  