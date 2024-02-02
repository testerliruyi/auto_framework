import time
from test_manage.test_case.get_link_status import GetLinkPro
import threading


class GetImg(GetLinkPro):

    img_prex = "spinningred.gif"

    def filter_img(self, link):
        # 对所有的链接 获取图片并进行过滤
        imgs = self.get_links(link, label="img", key=['src', 'data-original'])
        print("imgs:", imgs)
        for img in imgs:
            if self.img_prex in img:
                print(f"{link} 上定位到图片:", img)
            # else:
            #     print(f"{link},未定位到图片", img)


if __name__ =="__main__":
    url_link = "https://www.yyw.com/"
    # all_links = GetImg().get_links(url_link, 'a', 'href')
    all_links = ["https://www.yyw.com/product/Polyester-Slim-Slip-Dress-deep-V-side-slit-and-_p908303.html"]
    print("所有links:", all_links)
    print("总link个数：", len(all_links))
    all_links.append(url_link)
    threads = []
    for url in all_links:
        t = threading.Thread(target=GetImg().filter_img, args=(url,))
        threads.append(t)
        t.start()
    for thread in threads:
        thread.join()








