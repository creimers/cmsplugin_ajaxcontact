# -*- coding: utf-8 -*-
from django import forms
from django.utils.translation import ugettext_lazy as _

from captcha.fields import ReCaptchaField


class BaseBootstrapForm(forms.Form):

    def __init__(self, *args, **kwargs):
        super(BaseBootstrapForm, self).__init__(*args, **kwargs)

        for field in self.fields:
            if not isinstance(self.fields[field], forms.BooleanField):
                self.fields[field].widget.attrs['class'] = "form-control"


class ContactForm(BaseBootstrapForm):

    required_css_class = 'required'

    name = forms.CharField(
        label=_('name'),
    )

    telephone = forms.CharField(
        label=_('telephone'),
        required=False
    )

    email = forms.EmailField(
        label=_('email'),
    )

    message = forms.CharField(
        label=_('message'),
        widget=forms.Textarea()
    )

    captcha = ReCaptchaField()

    receiver = forms.CharField(
        label=_('receiver'),
        widget=forms.HiddenInput(),
    )
