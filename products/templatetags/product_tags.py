import random
from django import template

register = template.Library()

@register.filter
def random_int(min_val, max_val):
    """
    Returns a random integer between min_val and max_val (inclusive).
    
    Usage:
        {{ 1|random_int:12 }}  # Returns a random number between 1 and 12
    """
    try:
        min_val = int(min_val)
        max_val = int(max_val)
        return random.randint(min_val, max_val)
    except (ValueError, TypeError):
        return min_val  # Return min_val as fallback 