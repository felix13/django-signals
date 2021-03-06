from django.db.models.signals import post_save
from django.dispatch import receiver

from mysite.models import Book


@receiver(post_save, sender=Book)
def Notify_if_book_is_saved(sender, **kwargs):
    if kwargs['created']:  # make sure its a new record
        print("New book saved.")
