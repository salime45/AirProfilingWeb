from django import forms


class PcapForm(forms.Form):
    docfile = forms.FileField(
        label='Seleccione un pcap'
    )