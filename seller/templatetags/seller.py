from django import template


register = template.Library()


@register.filter(name="category_is_avaliable")
def category_is_avaliable(categories, category):
    for category in categories:
        if category.name == category:
            return f"The {category} is already exists in categories"
        else:
            return ""
