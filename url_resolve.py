import urllib.parse


def url_resolve(url):
    newquery = ''
    #first way : delete all message behind 'xxx'
    position = url.find('')
    if position != - 1:
        url = url[:position]
    parsed_tuple = urlparse.urlparse(url)
    q = urlparse.parse_qs(parsed_tuple.query)
    if 'service' in q:
        s = ''.join(q['service'])
        s = url_resolve(s)
        q['service'] = s

    #second way : hide message itself in filter_list
    filter_list = ['', '', '', '', '']
    for i in filter_list:
        if i in q:
            q.pop(i)

    for k, v in q.items():
        s = ''.join(q[k])
        s.encode('utf-8')
        q[k] = s

    sorted(q.items(), key=lambda q: q[0])
    flag = 0
    for k, v in q.items():
        v1 = str(v)
        if flag == 0:
            newquery = newquery + k + '=' + v1
            flag = 1
        else:
            newquery = newquery + '&' + k + '=' + v1

    oldtuple = parsed_tuple[:]
    l = []
    for i in oldtuple:
        l.append(i)

    l[4] = newquery
    newtuple = tuple(l)

    return urlparse.urlunparse(newtuple)

if __name__ == '__main__':
    url1 = ''
    u1 = url_resolve(url1)
    url2 = ''
    u2 = url_resolve(url2)
    print(url1)
    print(u1)
    print(url2)
    print(u2)
