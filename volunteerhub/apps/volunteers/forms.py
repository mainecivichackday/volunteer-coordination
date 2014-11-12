from django.core.urlresolvers import reverse
import floppyforms as forms
from .models import Volunteer, Project, Organization
from ckeditor.widgets import CKEditorWidget

class OrganizationForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorWidget())
    class Meta:
        model = Organization

    def get_success_url(self):
        return reverse('dashboard')


class VolunteerForm(forms.ModelForm):
    email = forms.EmailField()
    description = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Volunteer
        exclude = ['opportunities_completed', 'user']

    def get_success_url(self):
        return reverse('dashboard')


class ProjectForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Project
        exclude = ['organization', 'lead_volunteers']
