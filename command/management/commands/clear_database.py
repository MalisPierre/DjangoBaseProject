from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User

from command.delete_entity import delete_users
    
def clear_users():
    print('deleting users   ...')
    delete_users()

class Command(BaseCommand):
    help= 'will empty all the entries of a certain type in the database'

        #    def add_arguments(self, parser):
         #       parser.add_argument('entity_name', nargs='+', type=str)


    def handle(self, *args, **options):
        clear_users()
        print('clear database terminated')
        print('-------------------------')
    
