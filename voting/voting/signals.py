import traceback
from django.core.signals import got_request_exception


def my_errback(sender, **kwargs):
    traceback.print_exc()

got_request_exception.connect(my_errback, dispatch_uid="my_unique_identifier")
