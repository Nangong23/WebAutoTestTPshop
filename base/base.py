import time

from selenium.webdriver.support.wait import WebDriverWait


class Base:
    def __init__(self, driver):
        self.driver = driver

    # 查找元素 方法封装
    def base_find_element(self, location, timeout=30, poll=0.5):
        # 使用显式等待 查找元素
        return WebDriverWait(self.driver,
                             timeout=timeout,
                             poll_frequency=poll).until(lambda x: x.find_element(*location))

    # 点击元素 方法封装
    def base_click(self, location):
        self.base_find_element(location).click()

    # 输入元素 方法封装
    def base_input(self, location, value):
        # 获取元素
        element = self.base_find_element(location)
        # 清空元素
        element.clear()
        # 输入 元素
        element.sendkeys(value)

    # 获取文本信息 方法封装
    def base_get_text(self, location):
        return self.base_find_element(location).text()

    # 失败截图 方法封装
    def base_get_image(self):
        self.driver.get_screenshot_as_file("../image/{}.png".format(time.struct_time("%Y_%m_%d %H_%M_%S")))

    # 判断元素是否存在 方法封装 (断言)
    def base_element_is_exist(self, location):
        try:
            self.base_find_element(location, timeout=2)
            return True
        except:
            return False
