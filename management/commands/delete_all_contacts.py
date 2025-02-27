
# contacts/management/commands/delete_all_contacts.py
from django.core.management.base import BaseCommand
from contacts.models import Contact
class Command(BaseCommand):
    help = 'Deletes all contacts from the database'
    def handle(self, *args, **options):
        Contact.objects.all().delete()
        self.stdout.write(self.style.SUCCESS('Successfully deleted all contacts'))



