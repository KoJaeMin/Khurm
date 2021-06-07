from django import template

register = template.Library()


@register.inclusion_tag("index.html", takes_context=True)
def load_s3(context):
    request = context['request']
    return {
        'root' : '-' + str(request.user.username) + '/home/',
        'favorite' : '-' + str(request.user.username) + '/favorite/',
        'shared' : '-' + str(request.user.username) + '/shared/',
    }


@register.inclusion_tag("header.html", takes_context=True)
def load_s3_header(context):
    request = context['request']
    return {
        'root' : '-' + str(request.user.username) + '/',
        'home' : '-' + str(request.user.username) + '/home/',
        'favorite' : '-' + str(request.user.username) + '/favorite/',
        'shared' : '-' + str(request.user.username) + '/shared/',
    }

@register.inclusion_tag('favorite.html', takes_context=True)
def load_favorite_s3(context):
    request = context['request']
    return {
        'root' : '-' + str(request.user.username) + '/favorite/',
        'home' : '-' + str(request.user.username) + '/home/',
        'shared' : '-' + str(request.user.username) + '/shared/'
    }

@register.inclusion_tag('img.html', takes_context=True)
def load_img_s3(context):
    request = context['request']
    return {
        'root' : '-' + str(request.user.username) + '/home/',
        'favorite' : '-' + str(request.user.username) + '/favorite/',
        'shared' : '-' + str(request.user.username) + '/shared/'
    }

@register.inclusion_tag('shared.html', takes_context=True)
def load_shared_s3(context):
    request = context['request']
    return {
        'root' : '-' + str(request.user.username) + '/shared/',
        'favorite' : '-' + str(request.user.username) + '/favorite/',
        'home' : '-' + str(request.user.username) + '/home/'
    }