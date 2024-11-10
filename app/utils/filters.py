def format_date(date):
    """
    Formats a given date into a string in the format 'MM/DD/YY'.

    Parameters:
        date (datetime): The date to be formatted.

    Returns:
        str: The formatted date string.
    """
    return date.strftime('%m/%d/%y')

from datetime import datetime
print(format_date(datetime.now()))

def format_url(url):
    """
    Cleans and formats a URL by removing common prefixes and extracting the domain.

    Parameters:
        url (str): The URL to be formatted.

    Returns:
        str: The cleaned domain name.
    """
    return url.replace('http://', '').replace('https://', '').replace('www.', '').split('/')[0].split('?')[0]

print(format_url('http://google.com/test/'))
print(format_url('https://www.google.com?q=test'))

def format_plural(amount, word):
    """
    Returns the plural form of a word based on the given amount.

    Parameters:
        amount (int): The numerical amount to determine pluralization.
        word (str): The word to be pluralized.

    Returns:
        str: The word in its plural form if amount is not 1; otherwise, the original word.
    """
    if amount != 1:
        return word + 's'

    return word

print(format_plural(2, 'cat'))
print(format_plural(1, 'dog'))
