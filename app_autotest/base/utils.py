# 定义工具类
class UtilsDriver:
    _driver = None
    # 获取驱动对象的方法
    @classmethod
    def get_app_driver(cls):
        if cls._driver is None:
            des_cap = {

            }