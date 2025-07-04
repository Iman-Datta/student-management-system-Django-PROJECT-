from django import template

register = template.Library()

@register.filter(name='has_group') # This registers a new template filter called has_group that you can use inside your Django templates.
def has_group(user, group_name):
    return user.groups.filter(name=group_name).exists()
