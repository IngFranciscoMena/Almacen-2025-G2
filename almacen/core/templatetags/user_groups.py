from django import template

register = template.Library()

@register.filter(name='has_group')
def has_group(user, group_name):
    """Verifica si el usuario pertenece a un grupo dado"""
    return user.groups.filter(name=group_name).exists() # valor boleano