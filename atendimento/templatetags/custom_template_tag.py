from django import template
register = template.Library()

@register.simple_tag
def setvar(val=None):
  return val

@register.filter(name='addcss')
def addcss(field, css):
    return field.as_widget(attrs={"class":css})