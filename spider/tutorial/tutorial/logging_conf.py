import logging

# 创建一个logging对象
logger = logging.getLogger(__name__)
# 创建一个文件对象  创建一个文件对象,以UTF-8 的形式写入 标配版.log 文件中
# fh = logging.FileHandler('标配版.log',encoding='utf-8')

# 创建一个屏幕对象
sh = logging.StreamHandler()
# 配置显示格式  可以设置两个配置格式  分别绑定到文件和屏幕上
formatter = logging.Formatter('%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s')
# fh.setFormatter(formatter)  # 将格式绑定到两个对象上
sh.setFormatter(formatter)

#logger.addHandler(fh)  # 将两个句柄绑定到logger
logger.addHandler(sh)
