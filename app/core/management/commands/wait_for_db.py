"""
Django command to wait for the Database to be available.
"""

from django.core.management.base import BaseCommand

class Command(BaseCommand):
    """
        django command to wait for database.
    """

    def handle(self, *args, **options):
        pass