from organizer.models import (
    Tag,
    Company,
    Partner,
    Job
)
from resume.models import (
    Skill,
    Experience,
    Task,
    Institution,
    Education,
    Contact,
    Link,
    Resume,
    ApplicationSubmission,
)

from datetime import datetime


# Tags fixtures
Tag.objects.all().delete()
tg1 = Tag.objects.create(name="Web")
tg2 = Tag.objects.create(name="Management")
tg3 = Tag.objects.create(name="Security")
tg4 = Tag.objects.create(name="Entry level")
tg5 = Tag.objects.create(name="Engineering")
tg6 = Tag.objects.create(name="Arts")
tg7 = Tag.objects.create(name="Consultant")
tg8 = Tag.objects.create(name="Food")

# Skills fixtures
Skill.objects.all().delete()
sk1 = Skill.objects.create(
    name="Dog Walker",
    description="Walks dogs around the park",
)
sk1.tags.add(tg3)
sk1.tags.add(tg5)
sk1.tags.add(tg8)

sk2 = Skill.objects.create(
    name="Web Designer",
    description="Designs web sites",
)
sk2.tags.add(tg1)
sk2.tags.add(tg2)
print("Added Skills")

# Companies and Partners fixtures
Company.objects.all().delete()
cp1 = Company.objects.create(
    name="Cool Walker", location="NY/New York",
)
cp1.tags.add(tg4)
cp1.tags.add(tg7)

pt1 = Partner.objects.create(
    name="Walkery Walk",
    location="NY/New York",
    email="walkery@walk.com",
    description="Makes appointments between dog walkers and customers",
    website="walkery.com",
)
pt1.tags.add(tg1)
pt1.tags.add(tg6)
pt1.tags.add(tg7)

print("Added Companies and partners")

# Experiences fixtures
Experience.objects.all().delete()
exp1 = Experience.objects.create(
    company=cp1, started_at=datetime.today(), current=False
)
exp2 = Experience.objects.create(
    company=pt1, started_at=datetime.today(), current=True
)
print("Added experiences")

# Tasks fixtures
Task.objects.all().delete()
tsk1 = Task.objects.create(
    experience=exp1,
    description="This is a description 1",
)
tsk2 = Task.objects.create(
    experience=exp1,
    description="This is a description 2",
)
tsk3 = Task.objects.create(
    experience=exp2,
    description="This is a description 3",
)
tsk4 = Task.objects.create(
    experience=exp2,
    description="This is a description 4",
)
print("Added experiences")

# Institutions fixtures
Institution.objects.all().delete()
ins1 = Institution.objects.create(
    name="Cool School", location="NY/Brooklyn"
)
ins2 = Institution.objects.create(
    name="Cool University", location="NY/New York"
)
print("Added institutions")

# Education fixtures
Education.objects.all().delete()
ed1 = Education.objects.create(
    degree_type="HS",
    institution=ins1,
    started_at=datetime.today(),
    ended_at=datetime.today(),
    current=False,
)
ed2 = Education.objects.create(
    degree_type="BS",
    institution=ins2,
    started_at=datetime.today(),
    ended_at=datetime.today(),
    current=False,
)
print("Added educations")

# Contacts fixtures
Contact.objects.all().delete()
ct1 = Contact.objects.create(
    contact_type="P",
    contact="97889172389",
)
ct2 = Contact.objects.create(
    contact_type="E",
    contact="email@example.com",
)
print("Added contacts")

# Links fixtures
Link.objects.all().delete()
lk1 = Link.objects.create(
    link_type="W",
    link="www.mysite.com",
)
lk2 = Link.objects.create(
    link_type="R",
    link="www.github.com/user",
)
print("Added links")

# Resumes fixtures
Resume.objects.all().delete()
rs1 = Resume.objects.create(
    title="Resume 1",
)
rs1.contacts.add(ct1)
rs1.contacts.add(ct2)
rs1.educations.add(ed1)
rs1.educations.add(ed2)
rs1.skills.add(sk1)
rs1.skills.add(sk2)
rs1.links.add(lk1)
rs1.links.add(lk2)
rs1.experiences.add(exp1)
rs1.experiences.add(exp2)
rs1.save()
print("Added resume")

# Jobs fixtures
Job.objects.all().delete()
job1 = Job.objects.create(
    title="Web developer",
    text="\n".join(
        ["Description Description" for n in range(20)]
    ),
    pub_date=datetime.today(),
    partner=pt1,
)
job1.tags.add(tg1)
job1.tags.add(tg7)
print("Added job")

# ApplicationSubmission fixtures
ApplicationSubmission.objects.all().delete()
app1 = ApplicationSubmission.objects.create(job=job1, resume=rs1)
print("Added submission")
