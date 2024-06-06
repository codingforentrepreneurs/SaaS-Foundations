import helpers.billing
from typing import Any
from django.core.management.base import BaseCommand

from subscriptions import utils as subs_utils

class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument("--clear-dangling", action="store_true", default=False)

    def handle(self, *args: Any, **options: Any):
        # python manage.py sync_user_subs --clear-dangling
        # print(options)
        clear_dangling = options.get("clear_dangling")
        if clear_dangling:
            print("Clearing dangling not in use active subs in stripe")
            subs_utils.clear_dangling_subs()
        else:
            print("Sync active subs")
            print("Done")