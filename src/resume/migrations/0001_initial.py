# Generated by Django 2.1.15 on 2020-09-21 20:40

from django.db import migrations, models
import django.db.models.deletion
import django_extensions.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('organizer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ApplicationSubmission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', django_extensions.db.fields.AutoSlugField(blank=True, editable=False, max_length=100, populate_from=['id'])),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='job_submission', to='organizer.Job')),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact_type', models.CharField(choices=[('P', 'Phone'), ('E', 'Email')], default='P', max_length=2)),
                ('slug', django_extensions.db.fields.AutoSlugField(blank=True, editable=False, populate_from=['contact_type', 'contact'])),
                ('contact', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ('created_at',),
            },
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('degree_type', models.CharField(choices=[('HSI', 'Incomplete High School'), ('HS', 'High School'), ('BS', 'Bachelor of Science'), ('BA', 'Bachelor of Arts'), ('MS', 'Masters of Science'), ('MA', 'Masters of Arts'), ('PH', 'Doctorate')], default='BS', max_length=3)),
                ('slug', django_extensions.db.fields.AutoSlugField(blank=True, editable=False, populate_from=['id', 'degree_type'])),
                ('started_at', models.DateField()),
                ('ended_at', models.DateField()),
                ('current', models.BooleanField()),
            ],
            options={
                'ordering': ('ended_at',),
            },
        ),
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', django_extensions.db.fields.AutoSlugField(blank=True, editable=False, populate_from=['id', 'started_at'])),
                ('started_at', models.DateField()),
                ('ended_at', models.DateField(blank=True, null=True)),
                ('current', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='organizer.Company')),
            ],
            options={
                'ordering': ('created_at',),
            },
        ),
        migrations.CreateModel(
            name='Institution',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('location', models.CharField(max_length=150)),
                ('slug', django_extensions.db.fields.AutoSlugField(blank=True, editable=False, populate_from=['name', 'location'])),
                ('version', models.IntegerField(default=1)),
            ],
            options={
                'ordering': ('created_at', 'version'),
            },
        ),
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link_type', models.CharField(choices=[('W', 'Website'), ('R', 'Repository'), ('O', 'Other')], default='W', max_length=2)),
                ('link', models.CharField(max_length=100)),
                ('slug', django_extensions.db.fields.AutoSlugField(blank=True, editable=False, populate_from=['link_type', 'link'])),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ('created_at',),
            },
        ),
        migrations.CreateModel(
            name='Resume',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('slug', django_extensions.db.fields.AutoSlugField(blank=True, editable=False, populate_from=['title'])),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('contacts', models.ManyToManyField(to='resume.Contact')),
                ('educations', models.ManyToManyField(to='resume.Education')),
                ('experiences', models.ManyToManyField(to='resume.Experience')),
                ('links', models.ManyToManyField(to='resume.Link')),
            ],
            options={
                'ordering': ('created_at',),
            },
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True)),
                ('slug', django_extensions.db.fields.AutoSlugField(blank=True, editable=False, populate_from=['name'])),
                ('description', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('version', models.IntegerField(default=1)),
                ('tags', models.ManyToManyField(to='organizer.Tag')),
            ],
            options={
                'verbose_name': 'added skill',
                'ordering': ['created_at', 'version'],
            },
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', django_extensions.db.fields.AutoSlugField(blank=True, editable=False, populate_from=['id', 'description'])),
                ('description', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('experience', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='resume.Experience')),
            ],
            options={
                'ordering': ('created_at',),
            },
        ),
        migrations.AddField(
            model_name='resume',
            name='skills',
            field=models.ManyToManyField(to='resume.Skill'),
        ),
        migrations.AddField(
            model_name='education',
            name='institution',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='institution', to='resume.Institution'),
        ),
        migrations.AddField(
            model_name='applicationsubmission',
            name='resume',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='resume_submission', to='resume.Resume'),
        ),
    ]
