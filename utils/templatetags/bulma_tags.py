from django import template
from django.forms import widgets

register = template.Library()

HTML_ELEMENT_TYPE_BY_WIDGET = {
    widgets.CheckboxInput: 'checkbox',
    widgets.Textarea: 'textarea',
    widgets.RadioSelect: 'radio',
}


@register.inclusion_tag('templatetags/bulma_form.html')
def bulma_form(form, **kwargs):
    return {
        'form': form,
        **kwargs
    }


@register.inclusion_tag('templatetags/bulma_field.html')
def bulma_field(field, **kwargs):
    field_display = None
    element_type = 'input'

    widget = field.field.widget

    if isinstance(widget, widgets.Select):
        field_display = f'<div class="select is-rounded">{field}</div>'
    else:
        for widget_type, css_class in HTML_ELEMENT_TYPE_BY_WIDGET.items():
            if isinstance(widget, widget_type):
                element_type = css_class
                break

        widget.attrs.update({'class': element_type})

    return {
        'field': field,
        'field_display': field_display,
        **kwargs
    }
