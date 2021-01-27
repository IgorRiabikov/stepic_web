def wsgi_application(environ, start_response):
    r_body = []
    body = environ.get('QUERY_STRING')
    body = body.split('&')
    for i in body:
        r_body.append(i.encode() + b'\n')

    status = '200 OK'
    headers = [
        ('Content-Type', 'text/plain')
        ]
    start_response(status, headers)
    return r_body
