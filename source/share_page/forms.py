
from django import forms


class ShareForm(forms.Form):
    def __init__(self, *args, **kwargs):
        path = kwargs.pop('path')
        super(ShareForm, self).__init__(*args, **kwargs)
        self.fields['body'].initial = '{}{}'.format(self.fields['body'].initial, path)

    from_address = forms.EmailField(
        widget=forms.TextInput(attrs={'placeholder': 'Your email address'}),
        label='From',
        required=True,)
    to_address = forms.EmailField(
        widget=forms.TextInput(attrs={'placeholder': 'Their email address'}),
        label='To',
        required=True,)
    subject = forms.CharField(
        initial= 'Page from Zone Architectural Products Website',
        widget=forms.TextInput(),
        required=True,)
    body = forms.CharField(
        initial="I would like to share a page with you from from Zone Architectural Products Website:\nhttp://www.zone.net.nz",
        widget=forms.Textarea(),
        label="message",
        required=True,)
