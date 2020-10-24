from faker import Faker

from organizer.models import (
    Tag,
    Company,
    Partner,
    Job
)
from resume.models import (
    Skill,
    Experience,
    Institution,
    Education,
    Contact,
    Link,
    Resume,
    ApplicationSubmission,
)

from datetime import datetime
from random import randint

faker = Faker()


# Tags fixtures
Tag.objects.all().delete()
Skill.objects.all().delete()
Company.objects.all().delete()
Partner.objects.all().delete()
Experience.objects.all().delete()
Institution.objects.all().delete()
Education.objects.all().delete()
Contact.objects.all().delete()
Link.objects.all().delete()
Resume.objects.all().delete()
print("Deleted all previous data")


set_tags = set([faker.word() for _ in range(100)])
tags = []
for tag in set_tags:
    tags.append(Tag.objects.create(name=tag.title()))

print(f"Added tags {len(tags)}")

# Skills fixtures
set_skills = set([' '.join(faker.words(2)).title() for i in range(150)])
skills = []
for skill in set_skills:
    skills.append(
        Skill.objects.create(
            name=skill,
            description=faker.text(),
        )
    )
print(f"Added Skills {len(skills)}")

for sk in skills:
    for _ in range(2):
        choice = randint(0, len(tags)-1)
        sk.tags.add(tags[choice])
print(f"Added Tags to Skills")

# Companies and Partners fixtures
locations = [faker.address() for _ in range(20)]

companies = [
    Company.objects.create(
        name=f"{' '.join(faker.words(3)).title()}",
        location=locations[i%20],
    )
    for i in range(100)
]
for cp in companies:
    for _ in range(2):
        choice = randint(0, len(tags)-1)
        cp.tags.add(tags[choice])


partners = []
for i in range(100):
    name = faker.words(3)
    partners.append(
        Partner.objects.create(
            name=f"{' '.join(name).title()}",
            location=locations[i%20],
            email=f"contact@{''.join(name)}.com",
            description=f"{faker.text()}",
            website=f"{''.join(name)}.com",
        )
    )

for pt in partners:
    for _ in range(3):
        choice = randint(0, len(tags)-1)
        pt.tags.add(tags[choice])

print(f"Added Companies {len(companies)} and partners {len(partners)}")

# Experiences fixtures

exps = [
    Experience.objects.create(
        job_title=faker.job(),
        company=companies[i%20].name,
        location=" ".join(locations[i%20].split(' ')[-3:-1]),
        started_at=faker.date_time_this_decade(),
        ended_at=faker.date_time_this_year(),
        current=False,
        tasks=f'{faker.text()}\n{faker.text()}\n{faker.text()}'
    )
    for i in range(200)
]
print(f"Added experiences {len(exps)}")

# Institutions fixtures
school_types = ["High School", "College", "University", "Institute"]
ins = [
    Institution.objects.create(
        name=f"{' '.join(faker.words(2))} {school_types[i%4]}",
        location=locations[i%20]
    )
    for i in range(50)
]
print(f"Added institutions {len(ins)}")

# Education fixtures
ed_options = ["Science", "Art", "Therapy"]
degree_types = ["HSI", "HS", "BS", "MS", "MA", "Phd"]
degrees = [el for el in set([f'{faker.word().title()} {ed_options[i%3]}' for i in range(30)])]
eds = [
    Education.objects.create(
        degree_type=degree_types[i%4],
        degree=(degrees[i%len(degrees)] if len(degrees[i%len(degrees)]) < 100 else degrees[i%len(degrees)][:99]),
        institution=ins[i%50],
        started_at=faker.date_time_this_decade(),
        ended_at=faker.date_time_this_decade(),
        current=False,
    )
    for i in range(200)
]
print(f"Added educations {len(eds)}")

# Contacts fixtures
contact_type = ["P", "E"]
cts = [
    Contact.objects.create(
        contact_type=contact_type[i%2],
        contact=(faker.phone_number() if contact_type[i%2] == "P" else faker.email()),
    )
    for i in range(200)
]
print(f"Added contacts {len(cts)}")

# Links fixtures

link_types = ["W", "R"]
links = [
    Link.objects.create(
        link_type=link_types[i%2],
        link=(faker.domain_name() if link_types[i%2] == "W" else f"github.com/{faker.slug()}"),
    )
    for i in range(100)
]
print(f"Added links {len(links)}")

# Resumes fixtures

resumes = [
    Resume.objects.create(
        title=f"{' '.join(faker.words(2)).title()}",
    )
    for i in range(10)
]

ct_num = [i for i in range(len(cts))]
ed_num = [i for i in range(len(eds))]
sk_num = [i for i in range(len(skills))]
lk_num = [i for i in range(len(links))]
ex_num = [i for i in range(len(exps))]

for r in resumes:
    for _ in range(int(len(cts)/len(resumes))):
        r.contacts.add(cts[ct_num.pop()])
    for _ in range(int(len(eds)/len(resumes))):
        r.educations.add(eds[ed_num.pop()])
    for _ in range(int(len(skills)/len(resumes))):
        r.skills.add(skills[sk_num.pop()])
    for _ in range(int(len(links)/len(resumes))):
        r.links.add(links[lk_num.pop()])
    for _ in range(int(len(exps)/len(resumes))):
        r.experiences.add(exps[ex_num.pop()])
    r.save()

print(f"Added resumes {len(resumes)}")

# Jobs fixtures
Job.objects.all().delete()
jobs = [
    Job.objects.create(
        title=f"{faker.job()}",
        text=faker.text(),
        pub_date=faker.date_time_this_year(),
        partner=partners[i%len(partners)],
    )
    for i in range(50)
]
for job in jobs:
    for _ in range(5):
        choice = randint(0, len(tags)-1)
        job.tags.add(tags[choice])
print(f"Added jobs {len(jobs)}")

# ApplicationSubmission fixtures
ApplicationSubmission.objects.all().delete()
apps = 0
for i in range(2):
    ApplicationSubmission.objects.create(
        job=jobs[i],
        resume=resumes[i]
    )
    ApplicationSubmission.objects.create(
        job=jobs[i],
        resume=resumes[i+5]
    )
    apps += 2
print(f"Added submissions {apps}")
