from django.template.defaulttags import register


@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)


@register.simple_tag
def convert_list_to_string(value):
    return ', '.join([e for e in value])
