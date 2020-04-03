# req_ctrip_airticketprice.py
查询Ctrip的机票信息
post方式 携带payload查询

# req_weather.py
使用get方式,查询天气数据

# req_jd_clildwatch.py
查询JD页面的价格信息，本例以查询"儿童手表"为例，JD显示共100页，每页60项
每一页分两部分

第一页前半部分，直接get，

第二页开始：
前半部分，分析网址url规律
后半部分，拖拽后显示，分析url规律，多了一个本地时间
详见代码.

