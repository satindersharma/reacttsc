from django import forms
import logging

logger = logging.getLogger(__name__)


# -------------------------------------------------------------------------------
# BaseForm
# -------------------------------------------------------------------------------
class BaseForm(forms.Form):

    # ---------------------------------------------------------------------------
    # __init__
    # ---------------------------------------------------------------------------
    def __init__(self, *args, **kwargs):
        super(BaseForm, self).__init__(*args, **kwargs)

        # Add html attributes to support bootstrap controls
        for field_name in self.fields:
            try:
                if self.fields[field_name].widget.input_type == 'file':
                    self.fields[field_name].widget.attrs['class'] = \
                        'custom-file-input'

                elif self.fields[field_name].widget.input_type == 'checkbox':
                    self.fields[field_name].widget.attrs['class'] = \
                        'form-check-input'

                elif self.fields[field_name].widget.input_type == 'radio':
                    self.fields[field_name].widget.attrs['class'] = \
                        'form-check-input'

                elif isinstance(self.fields[field_name], forms.DateTimeField):
                    self.fields[field_name].widget.input_type = \
                        'datetime-local'

            except AttributeError:
                pass
