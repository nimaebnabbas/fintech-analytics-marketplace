"""URL slug utilities"""
import re
from typing import Optional

def slugify(text: str) -> str:
    """
    Convert text to URL-friendly slug
    Handles both English and Persian
    """
    # Remove special characters
    text = re.sub(r'[^\w\s-]', '', text)
    # Replace spaces with hyphens
    text = re.sub(r'[-\s]+', '-', text)
    # Remove leading/trailing hyphens
    text = text.strip('-')
    return text.lower()

def persian_to_slug(text: str) -> str:
    """
    Convert Persian text to URL-friendly slug
    """
    # Map Persian characters to ASCII equivalents
    mapping = {
        'آ': 'a', 'ا': 'a', 'ب': 'b', 'پ': 'p', 'ت': 't',
        'ث': 's', 'ج': 'j', 'چ': 'ch', 'ح': 'h', 'خ': 'kh',
        'د': 'd', 'ذ': 'z', 'ر': 'r', 'ز': 'z', 'ژ': 'zh',
        'س': 's', 'ش': 'sh', 'ص': 's', 'ض': 'z', 'ط': 't',
        'ظ': 'z', 'ع': 'e', 'غ': 'gh', 'ف': 'f', 'ق': 'g',
        'ک': 'k', 'گ': 'g', 'ل': 'l', 'م': 'm', 'ن': 'n',
        'و': 'v', 'ه': 'h', 'ی': 'y'
    }
    
    result = ''
    for char in text:
        result += mapping.get(char, char)
    
    return slugify(result)
