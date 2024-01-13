import pytest, os
from common.selenium import DebugWebdriver

# 获取页面元素文本列表，并生成文件夹
js = "return document.getElementsByClassName('sub_menu_wrap')[1].innerText;"

def test_mkdir_windows():
    driver = DebugWebdriver().driver
    # driver.get('https://yyw.chat/')
    text = driver.execute_script(js)
    print(type(text),text)
    # content = str(tuple(x for x in text.split('\n'))).replace('\'','')
    # with open('E:\\test.txt','w+',encoding='utf-8') as file:
    #     for i in list(content):
    #         print(i)
    #         file.write(i)
    # os.chdir('E:\视频目录\数字人科技')
    # os.system(f"for %i in {content} do md %i")

