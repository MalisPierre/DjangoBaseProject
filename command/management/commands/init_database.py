from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User

from command.create_entity import create_profil_group, create_superuser
    
def create_groups():
    print('deleting users   ...')
    create_profil_group(False, "User")
    create_profil_group(False, "Pro")
    create_profil_group(False, "Dev")
    create_profil_group(False, "Admin")
    create_superuser(False, "malis_p", "pierre.malis@epitech.eu", "toto47A")

class Command(BaseCommand):
    help= 'will create the req minimum to have a database'

        #    def add_arguments(self, parser):
         #       parser.add_argument('entity_name', nargs='+', type=str)


    def handle(self, *args, **options):
        create_groups()
        print('init database terminated')
        print('-------------------------')
    
