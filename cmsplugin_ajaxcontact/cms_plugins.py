# -*- coding: utf-8 -*-

from django.utils.translation import ugettext as _
from django.core.urlresolvers import reverse

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from cms.models import CMSPlugin

from .forms import ContactForm
from .models import ContactPluginModel


class ContactPlugin(CMSPluginBase):
    model = ContactPluginModel
    name = _("Contact Form")
    render_template = "cmsplugin_ajaxcontact/_contact_plugin.html"


    def render(self, context, instance, placeholder):
        
        form = ContactForm(initial={'receiver': instance.receiver})

        context.update({
            "form": form,
            "form_action": reverse('ajax_contact:ajax_form'),
            "button_text": instance.submit,
            "success_message": instance.success_message,
        })
        return context

plugin_pool.register_plugin(ContactPlugin)
