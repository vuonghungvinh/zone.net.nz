from django import template

from .. import models


register = template.Library()


@register.inclusion_tag('catalogue/templatetags/carousel.html')
def catalogue_carousel(limit=5):
    products = models.Product.objects.order_by('?')[:limit]
    return {'products': products,}


@register.inclusion_tag('catalogue/templatetags/products-featured.html')
def catalogue_featured_products(limit=None):
    products = models.Product.objects.order_by('?').filter(featured=True)[:limit]
    return {'products': products}


@register.inclusion_tag('catalogue/templatetags/product-featured.html')
def catalogue_product_featured(product):
    return {'product': product}


@register.inclusion_tag('catalogue/templatetags/related-products.html')
def related_products(product, limit=None):
    products = product.related_products.all()
    if limit:
        products = products[:limit]
    return {'related_products': products,}


@register.inclusion_tag('catalogue/templatetags/related-projects.html')
def related_projects(product, limit=None):
    projects = product.projects.all()
    if limit:
        projects = projects[:limit]
    return {'related_projects': projects,}


@register.inclusion_tag('catalogue/templatetags/colour_popups.html')
def colour_popups(colour_ranges):
    return {'colour_ranges': colour_ranges, }


import re

tag_end_re = re.compile(r'(\w+)[^>]*>')
entity_end_re = re.compile(r'(\w+;)')

@register.filter
def truncatehtml(string, length, ellipsis='...'):
    """Truncate HTML string, preserving tag structure and character entities."""
    output_length = 0
    i = 0
    pending_close_tags = {}
    
    while output_length < length and i < len(string):
        c = string[i]
        if c == '<':
            # probably some kind of tag
            if i in pending_close_tags:
                # just pop and skip if it's closing tag we already knew about
                i += len(pending_close_tags.pop(i))
            else:
                # else maybe add tag

                i += 1
                match = tag_end_re.match(string[i:])
                if match:
                    tag = match.groups()[0]
                    i += match.end()
  
                    # save the end tag for possible later use if there is one
                    match = re.search(r'(</' + tag + '[^>]*>)', string[i:], re.IGNORECASE)
                    if match:
                        pending_close_tags[i + match.start()] = match.groups()[0]
                else:
                    output_length += 1 # some kind of garbage, but count it in
                    
        elif c == '&':
            # possible character entity, we need to skip it
            i += 1
            match = entity_end_re.match(string[i:])
            if match:
                i += match.end()

            # this is either a weird character or just '&', both count as 1
            output_length += 1
        else:
            # plain old characters
            skip_to = string.find('<', i, i + length)
            if skip_to == -1:
                skip_to = string.find('&', i, i + length)
            if skip_to == -1:
                skip_to = i + length
                
            # clamp
            delta = min(skip_to - i,
                        length - output_length,
                        len(string) - i)

            output_length += delta
            i += delta
                        
    output = [string[:i]]
    if output_length == length:
        output.append(ellipsis)

    for k in sorted(pending_close_tags.keys()):
        output.append(pending_close_tags[k])

    return "".join(output)