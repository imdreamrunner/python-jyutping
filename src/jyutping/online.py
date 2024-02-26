import requests

import bs4


def parse_response(response: requests.Response, multiple: bool) -> list[str]:
    """
    Parse the response using BeautifulSoup and return a list of strings from the first column.

    Args:
        response (requests.Response): The response object to be parsed.

    Returns:
        list[str]: A list of strings from the first column.
    """
    soup = bs4.BeautifulSoup(response.text, 'html.parser')
    table = soup.find('table', border="1")
    first_column_content = []
    rows = table.find_all('tr')
    for row in rows:
        cells = row.find_all('td')
        if len(cells) > 0:
            first_column_content.append(cells[0].text)
    if multiple:
        return first_column_content
    else:
        return first_column_content[0]
