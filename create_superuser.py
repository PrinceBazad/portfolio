import os
import django
from django.contrib.auth.models import User, Group, Permission
from django.contrib.contenttypes.models import ContentType

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio.settings')
django.setup()

def create_superuser():
    try:
        # Delete existing superuser if exists
        User.objects.filter(username='princebazad').delete()
        
        # Create new superuser
        user = User.objects.create_superuser(
            username='princebazad',
            email='princebazad3@gmail.com',
            password='Prince@123'
        )
        
        # Get or create admin group
        admin_group, created = Group.objects.get_or_create(name='admin')
        
        # Add all permissions to admin group
        for perm in Permission.objects.all():
            admin_group.permissions.add(perm)
        
        # Add user to admin group
        user.groups.add(admin_group)
        
        # Set user permissions
        user.is_staff = True
        user.is_superuser = True
        user.is_active = True
        user.save()
        
        print("Superuser created successfully!")
        print("Username: princebazad")
        print("Email: princebazad3@gmail.com")
        print("Password: Prince@123")
        
    except Exception as e:
        print(f"Error creating superuser: {str(e)}")

if __name__ == '__main__':
    create_superuser() 