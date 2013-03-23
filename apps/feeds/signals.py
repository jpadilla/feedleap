from libs.djpubsubhubbub.signals import updated


def update_handler(sender, update, **kwargs):
    """
    Process new content being provided from SuperFeedr

    """
    for entry in update.entries:
        print entry

updated.connect(update_handler, dispatch_uid='superfeedr')
