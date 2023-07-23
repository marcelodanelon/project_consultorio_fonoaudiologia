from django import template
register = template.Library()

@register.simple_tag()
def changeToString(message=None):
    text = str(message)
    return text

@register.filter(name='addcss')
def addcss(field):
    return field.as_widget(attrs={"style":'color:red;'})