from django import forms


class PcapForm(forms.Form):
    docfile = forms.FileField(
        label='Seleccione un pcap',
        help_text='max. 100 megabytes'
    )