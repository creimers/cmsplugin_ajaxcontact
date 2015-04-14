from django.db import models
from cms.models import CMSPlugin

from django.utils.translation import ugettext_lazy as _
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class ContactPluginModel(CMSPlugin):

    receiver = models.EmailField(_('Email recipient'))

    submit = models.CharField(
        _('Submit button value'),
        default=_('Submit'),
        max_length=30
    )

    success_message = models.TextField(
        _('Success message'),
        default=_('Thank you for the message.'),
    )

    def __str__(self):
        return self.receiver


