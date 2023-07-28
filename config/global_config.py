from util import base_util as util

global base_config


# 加载配置
def load_config():
    global base_config
    base_config = util.read_yaml("config/config.yaml")["wechat"]
    return base_config
