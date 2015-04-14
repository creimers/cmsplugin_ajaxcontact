# -*- coding: utf-8 -*-
from django.conf import settings
from django.views.generic import FormView
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.core.mail import send_mail
from django.utils.translation import ugettext_lazy as _

import json

from .forms import ContactForm
#
# From: https://docs.djangoproject.com/en/1.6/topics/class-based-views/generic-editing/#ajax-example
#
class AjaxableResponseMixin(object):
    """
    Mixin to add AJAX support to a form.
    Must be used with an object-based FormView (e.g. CreateView)
    """

    def render_to_json_response(self, context, **response_kwargs):
        data = json.dumps(context)
        response_kwargs['content_type'] = 'application/json'
        return HttpResponse(data, **response_kwargs)

    def form_invalid(self, form):
        response = super(AjaxableResponseMixin, self).form_invalid(form)
        if self.request.is_ajax():
            return self.render_to_json_response(form.errors)  # , status=400)
        else:
            return response

    def form_valid(self, form):
        # We make sure to call the parent's form_valid() method because
        # it might do some processing (in the case of CreateView, it will
        # call form.save() for example).
        response = super(AjaxableResponseMixin, self).form_valid(form)
        if self.request.is_ajax():
            data = {
                'object': form.cleaned_data,
            }
            return self.render_to_json_response(data)
        else:
            return response


class ContactFormAjaxView(AjaxableResponseMixin, FormView):
    form_class = ContactForm
    http_method_names = [u'post']
    template_name = 'cmsplugin_ajaxcontact/_contact_widget.html'

    #
    # NOTE: Even though this will never be used, the FormView requires that
    # either the success_url property or the get_success_url() method is
    # defined. So, let use the sensible thing and set it to the page where
    # this plugin is coming from.
    #
    def get_success_url(self):
        return self.request.path

    def send_email(self, data):

        email_subject = _('New website contact')
        email_body = render_to_string('cmsplugin_ajaxcontact/notification-body.txt', {
            'contact': data,
        })

        try:
            send_mail(
                email_subject,
                email_body,
                settings.SERVER_EMAIL,
                [data['receiver'], ],
                fail_silently=False
            )

        except Exception:
            if (settings.DEBUG):
                raise

    def form_valid(self, form):
        self.send_email(form.cleaned_data)

        return super(ContactFormAjaxView, self).form_valid(form)
