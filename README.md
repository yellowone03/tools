# tools

## smtp\_sender.py
smtp\_sender.py 主要用于发邮件。

## url\_resolve.py
url_resolve.py 主要用于隐藏url中的一些信息。

## alert\_sender.py
alert\_sender.py 主要用于发送报警信息，通过post请求调用公司的alert_gate借口。

## es\_query.py
es\_query.py 主要从es上查询海量信息。因为es设置了单次查询不超过10000次，所以将每次查询按时间分割，分成上千次查询，即可查询千万至亿级别的数据。
