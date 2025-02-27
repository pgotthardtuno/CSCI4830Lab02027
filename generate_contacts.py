import os
import django

# Ensure Django settings are properly loaded
# Update 'djangoproject' with your project name
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangoproject.settings')  
# This must be called before importing models
django.setup()  

from contacts.models import Contact
from faker import Faker

fake = Faker()

def generate_contacts(count=100):
    """Generates and inserts 'count' number of contacts into the database."""
    try:
        sample_contacts = [
            Contact(name=fake.name(), phone=fake.numerify(text="###-###-####"))  # Ensures correct phone format
            for _ in range(count)
        ]

        # Bulk insert into the database
        Contact.objects.bulk_create(sample_contacts)

        print(f"{count} sample contacts created successfully!")

    except Exception as e:
        print(f"Error creating contacts: {e}")

if __name__ == "__main__":
    num_records = int(input("Enter number of contacts to generate: ") or 100)
    generate_contacts(num_records)
