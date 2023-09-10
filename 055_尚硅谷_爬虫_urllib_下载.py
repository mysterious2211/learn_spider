import urllib.request

# 下载网页
# url_page = 'http://www.baidu.com'

# urlretrieve两个参数：url和filename
# ur：表示下载的路径
# filename：表示文件的名字
# 在python中可以写变量的名字，也可以直接写值
# urllib.request.urlretrieve(url_page, 'baidu.html')

# 下载图片
# url_img = 'https://tse4-mm.cn.bing.net/th/id/OIP-C.JyHkUvXhaecwn_jUElGJzgHaIo?w=186&h=217&c=7&r=0&o=5&dpr=1.4&pid=1.7'
#
# urllib.request.urlretrieve(url_img, 'sanjiu.jpg')

# 下载视频
url_video = 'https://vd3.bdstatic.com/mda-mbidz0h6693aawha/v1-cae/hd/mda-mbidz0h6693aawha.mp4'

urllib.request.urlretrieve(url_video, 'huajia.mp4')


