from util_scripts.get_link_status import GetLinkPro


class GetImg(GetLinkPro):

    def filter_img(self, link, keys: list):
        # 对所有的链接 获取图片并进行过滤
        imgs = self.get_links(link, label="img", key=['src', 'data-original'])
        for img in imgs:
            for i in keys:
                if i in img:
                    print(f"{link} 上定位到图片:", img)
                # else:
                #     print(f"{link},未定位到图片", img)


if __name__ == "__main__":
    url_link = "https://www.beads.us/"
    img_prex = ["facebook.png"]
    all_links = GetImg().get_links(url_link, 'a', 'href')
    print("所有links:", all_links)
    print("总link个数：", len(all_links))
    for link in all_links:
        GetImg().filter_img(link, img_prex)

    # 多线程写法
    # import threading
    # threads = []
    # for url in all_links:
    #     t = threading.Thread(target=GetImg().filter_img, args=(url,))
    #     threads.append(t)
    #     t.start()
    # for thread in threads:
    #     thread.join()
