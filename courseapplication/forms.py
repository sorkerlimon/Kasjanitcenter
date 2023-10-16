from django import forms
from .models import CourseRegistration

class CourseRegistrationForm(forms.ModelForm):
    class Meta:
        model = CourseRegistration
        fields = ('name', 'father_name', 'mother_name', 'national_id', 'address', 'mobile_number', 'courses', 'bkash_transaction_id', 'image','payment_method')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # Add the 'required' attribute to all fields
        for field_name, field in self.fields.items():
            field.required = True
            
            # Optionally, you can add classes for styling purposes
            if field_name == 'courses':
                field.widget.attrs.update({'class': 'form-control'})
            if field_name == 'image':
                field.widget.attrs.update({'class': 'form-control-file'})
