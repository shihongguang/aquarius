"""
http parse
"""


def parse_http(string):
    """parse"""
    list_res = string.decode('utf-8').splitlines()
    http_text = {
        'head': list_res[:-1],
        'body': list_res[-1]
        }

    try:
        method, path, _ = http_text["head"][0].split()
    except IndexError:
        method = "GET"
        path = "/"

    http_text["method"] = method
    http_text["path"] = path

    try:
        path, query_string = path.split("?", 1)
    except ValueError:
        pass
    else:
        http_text["query_string"] = query_string

    return http_text
