"""
Django command to wait for the database
"""

from typing import Any
import time

from psycopg2 import OperationalError as Psycopg2OpError

from django.core.management.base import BaseCommand
from django.db.utils import OperationalError


class Command(BaseCommand):
    """Django command to wait for database"""

    def handle(self, *args: Any, **options: Any):
        self.stdout.write("Waiting for database...")
        db_up = False

        while not db_up:
            try:
                self.check(databases=["default"])
                db_up = True
            except (OperationalError, Psycopg2OpError):
                self.stdout.write("Database unavailable, waiting 1 second...")
                time.sleep(1)

        self.stdout.write(self.style.SUCCESS("Database available!"))
