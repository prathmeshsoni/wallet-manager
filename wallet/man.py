from django.core.management import call_command
from django.core.management.commands.migrate import Command as MigrateCommand

class Command(MigrateCommand):
    def handle(self, *args, **options):
        options['exclude'] = ['category']
        super().handle(*args, **options)
