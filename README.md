# meituan_spider

### 说明
之前正大杯比赛帮忙做的爬虫，但是没用上，所以做了个demo能爬门店的评论

### 接口分析
爬取手机端的网页评论，因为电脑端和手机端的门店评论数据库是分开的，手机端评论更多
https://h5.waimai.meituan.com/waimai/mindex/home
几乎没有什么逆向压力，有的时候爬不了是因为要验证，只需要重新登录网页，然后验证一下，更新payload即可

### demo配置
需要填写自行填写配置文件
配置参数说明
- headers
    - 请求头信息，自行抓包获取
- payload
    - post请求表单信息，自行抓包获取（爬取失败，需要重新登录验证，更新payload）
- poi_id_str
    - 门店的唯一标识符poi_id_str，自行抓包获取（爬取多个门店的评论，输入多个poi_id_str即可，不需要改变payload）