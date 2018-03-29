# coding: utf-8
'''
Created on 2018年3月27日

@author: likun
'''
from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from suit.widgets import AutosizedTextarea, SuitSplitDateTimeWidget
from notification.models import UserMessage
from django.forms.fields import CharField


class UserMessageForm(ModelForm):
    title = CharField(label=_(u'标题'), max_length=16)

    class Meta:
        model = UserMessage
        fields = '__all__'
        widgets = {
            'summary': AutosizedTextarea(attrs={'rows': 4, 'class': 'input-xlarge'}),
            'post_datetime': SuitSplitDateTimeWidget,
            'expired_datetime': SuitSplitDateTimeWidget,
        }

    def clean_post_users(self):
        data = self.cleaned_data['post_users']
        if data:
            self.instance.post_count = len(data)
        return data
