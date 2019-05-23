'''
１．百度贴吧爬取所有图片
２．思路
    ＊获取贴吧主页地址, 下一页, 找url规律
    *获取一页中所有帖子url地址
    *对每个帖子链接发请求, 获取图片URL
    *对每个图片链接发请求, 以wb方式写入本地
'''


#　贴吧主页URL

# xpath表达式
# 图片地址//img[@class='threadlist_pic j_m_pic ']/@src
# //ul[@class="threadlist_media j_threadlist_media clearfix"]/li/a/img/@src