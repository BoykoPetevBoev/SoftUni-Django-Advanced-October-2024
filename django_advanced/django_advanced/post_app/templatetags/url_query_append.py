from django import template

register = template.Library()

@register.simple_tag
def url_query_append_tag(request, field, value):
    queries = request.GET.copy()  
    queries[field] = value
    return queries.urlencode()
