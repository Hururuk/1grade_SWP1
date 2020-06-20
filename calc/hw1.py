from cgi import parse_qs
from template import html

def application(environ, start_response) :
    d = parse_qs(environ['QUERY_STRING'])
    
    error = "No Error"
    first_num = d.get('first_num', [''])[0]
    second_num = d.get('second_num', [''])[0]
    sum, mul = 0, 0
    try :
        first_num, second_num = int(first_num), int(second_num)
        sum = first_num + second_num
        mul = first_num * second_num
    except ValueError as e :
        errror = "e"
    except NameError as e:
        error = "e"
    except Exception as e :
        error = "e"
    response_body = html % {'sum':sum, 'mul':mul, 'error':error}

    status = '200 OK'
    response_headers = [('Content-Type', 'text/html'), ('Content-Length', str(len(response_body)))]

    return [response_body]
