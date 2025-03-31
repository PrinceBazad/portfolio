from django.db import migrations

def add_default_data(apps, schema_editor):
    Profile = apps.get_model('main', 'Profile')
    Skill = apps.get_model('main', 'Skill')
    
    # Create default profile
    Profile.objects.create(
        name='आपका नाम',
        title='Full Stack Developer',
        about='मैं एक पैशनेट डेवलपर हूं जो नई टेक्नोलॉजीज सीखने और उन्हें प्रोजेक्ट्स में लागू करने में रुचि रखता हूं।',
        profile_image='profile_images/default.jpg'
    )
    
    # Create default skills
    default_skills = [
        {'name': 'Python', 'percentage': 90},
        {'name': 'Django', 'percentage': 85},
        {'name': 'HTML/CSS', 'percentage': 95},
        {'name': 'JavaScript', 'percentage': 80},
        {'name': 'SQL', 'percentage': 75},
        {'name': 'Git', 'percentage': 70},
    ]
    
    for skill_data in default_skills:
        Skill.objects.create(**skill_data)

class Migration(migrations.Migration):
    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(add_default_data),
    ] 