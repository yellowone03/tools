# -*- coding: utf8 -*-

import time
import json

from elasticsearch import Elasticsearch

es_cluster = [
    {'host': '', 'port': },
    {'host': '', 'port': },
    {'host': '', 'port': },
    {'host': '', 'port': },
    {'host': '', 'port': },
]

base_st = int(time.time()) / 86400 * 86400 + 86400

res_all = []
d = {}
count = 0
es = Elasticsearch(es_cluster)
for i in xrange(32 * 24):
    query_body = {
        "size": 10000,
        "query": {
            "bool": {
                "must": [
                    {
                        "query_string": {
                            "query": '',
                            "analyze_wildcard": True,
                        }
                    },
                    {
                        "range": {
                            "@timestamp": {
                                "gte": (base_st - i*3600 - 3600) * 1000,
                                "lte": (base_st - i*3600) * 1000 - 1,
                                "format": "epoch_millis"
                            }
                        }
                    }
                ],
                "filter": [],
                "should": [],
                "must_not": []
            }
        }
    }
    res = es.search(index='*', body=query_body, request_timeout=60)
    
    for hit in res['hits']['hits']:
        if hit["_source"][''] in d:
            d[hit["_source"]['']] += 1
        else:
            d[hit["_source"]['']] = 1
    
    print(time.ctime())
    print(d)
    print('')

