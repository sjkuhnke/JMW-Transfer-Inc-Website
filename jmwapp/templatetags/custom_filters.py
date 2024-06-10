from django import template

register = template.Library()


@register.filter
def attr(field, value):
    attrs = value.split('=')
    field.field.widget.attrs[attrs[0]] = attrs[1]
    return field
