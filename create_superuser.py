import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio.settings')
django.setup()

from django.contrib.auth.models import User

# Delete existing superuser
User.objects.filter(username='princebazad').delete()

# Create new superuser
user = User.objects.create_superuser(
    username='princebazad',
    email='princebazad3@gmail.com',
    password='Prince@123',
    is_staff=True,
    is_superuser=True,
    is_active=True
)

# Verify the user was created correctly
print(f"Superuser created: {user.username}")
print(f"Email: {user.email}")
print(f"Is staff: {user.is_staff}")
print(f"Is superuser: {user.is_superuser}")
print(f"Is active: {user.is_active}")

# Set session data
from django.contrib.sessions.models import Session
from django.utils import timezone

session = Session.objects.create(
    session_key='test_session',
    session_data='test_data',
    expire_date=timezone.now() + timezone.timedelta(days=1)
)
print(f"Session created: {session.session_key}")

# Set user permissions
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType

content_type = ContentType.objects.get_for_model(User)
permission = Permission.objects.get(
    codename='add_user',
    content_type=content_type,
)
user.user_permissions.add(permission)
print(f"Permission added: {permission.codename}")

# Set user groups
from django.contrib.auth.models import Group

group = Group.objects.get(name='admin')
user.groups.add(group)
print(f"Group added: {group.name}") 