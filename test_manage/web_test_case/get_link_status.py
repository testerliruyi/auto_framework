import time
import typing

from common.send_request import SendRequest
from bs4 import BeautifulSoup
import os
from retry import retry


class GetLinkPro:

    @staticmethod
    def get_html_text(url, **kwargs):
        try:
            response = SendRequest.do_request(url, "get", **kwargs)
            html_content = response.text
            html_status_code = response.status_code
            html_headers = response.headers
            return html_content, html_status_code, html_headers
        except Exception as e:
            return False

    def get_links(self, url, label: str, key: str or list, **kwargs):
        """
        :param url:  请求连接
        :param label:  需要获取的html 标签（如a、img等）
        :param key:  需要html标签中的属性值(如，src or href)等
        :param kwargs:  额外关键字参数，主要给请求函数使用。
        :return:  解析html后的值列表
        """
        html_content = self.get_html_text(url, **kwargs)
        if not html_content:
            raise ConnectionError(f"连接网站{url}超时，请稍后重试")
        # pattern = r'<a\s+.*?href="(.*?)".*?>'
        # all_links = re.findall(pattern, html_content[0])
        soup = BeautifulSoup(html_content[0], "html5lib")
        links = soup.find_all(label)
        # print("links is", links)
        exclude_list = ["mycart.php", "shipping_cost.php", "checkout.php", "rate_cost.php", "wishLists_dir.php",
                        "track_order.php", "shipping_cost.php", "history.php", "Submit_ticket.php"]
        all_links = []
        for link in links:
            global value
            if type(key) is str:
                value = link.get(key)
            elif type(key) is list:
                value = link.get(key[0])
                if not value:
                    value = link.get(key[1])
            # 对获取到的值进行过滤
            if not value:
                pass
            elif value.endswith('.php') or value.endswith('.html'):
                if value.split("/")[-1] in exclude_list:
                    continue
                if value.startswith("https:"):
                    all_links.append(value)
                elif value.startswith("//"):
                    value = "https:" + value
                    all_links.append(value)
                elif value.startswith("/"):
                    value = url + value
                    all_links.append(value)
            elif value.split('.')[-1] in ['png', 'jpg', 'jpeg', 'gif']:
                all_links.append(value)
            else:
                pass
            # elif re.findall("^\/", href):
            #     new_href = self.url + href
            #     all_links.append(new_href)
        return list(set(all_links))

    # href.endswith('.html') or

    def get_link_status(self, url):
        count = 1
        all_links = self.get_links(url, stream=True)
        print(f"当前url: {url}")
        print("链接总数为:", len(list(set(all_links))))
        print(f"链接:{list(set(all_links))}")
        link_list = []
        file_name = url.split('.')[1] + '.txt'
        file_path = os.path.join("E:/", file_name)
        now_time = time.localtime(time.time())
        print(f"==============={time.strftime('%Y-%m-%d %H:%M:%S', now_time)}===============")
        with open(file_path, 'a+', encoding='utf-8') as file:
            file.write(f"==============={time.strftime('%Y-%m-%d %H:%M:%S', now_time)}===============\n")
            file.write(f"当前url: {url}\n")
            for link in list(set(all_links)):
                # 首次请求
                res1 = self.get_html_text(link, stream=True)
                if not res1:
                    print(f"{count}、{url}请求超时，进行下一条。")
                    continue
                request_header = {
                    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*",
                    "Accept-Encoding": "gzip, deflate, br", "If-None-Match": res1[2].get("Etag")}
                # 二次请求
                res2 = self.get_html_text(link, headers=request_header, stream=True)
                if not res2:
                    print(f"{count}、{url}请求超时，进行下一条。")
                    continue
                if res2[1] == 200 and res1[2].get('Etag') is None:
                    print(f"{count}、当前链接是:", link)
                    file.write(f"{count}、当前链接是:{link} \n")
                    link_list.append(link)
                    print(
                        f"       >>>二次请求链接状态：{res2[1]},etag值是:{res2[2].get('Etag')}，,缓存结果：异常，未304缓存。")
                    file.write(
                        f"       >>>二次请求链接状态：{res2[1]},etag值是:{res2[2].get('Etag')},缓存结果：异常，未304缓存\n")
                elif res2[1] == 404:
                    file.write(
                        f"{count}、当前链接:{link},二次请求状态为:{res2[1]},缓存结果状态：页面请求失败，请手工确认\n")
                elif res2[1] == 304:
                    file.write(f"{count}、当前链接:{link},二次请求状态为:{res2[1]},缓存结果状态：正常\n")
                    print(f"{count}、当前链接:{link},二次请求状态为:{res2[1]},缓存结果状态：正常")
                else:
                    file.write(f"{count}、当前链接:{link},二次请求状态为:{res2[1]},缓存结果状态：正常\n")
                    print(f"{count}、当前链接:{link},二次请求状态为:{res2[1]},缓存结果状态：正常")
                count += 1
            # 循环执行结束，输出所有列表
            file.write(f"最终结果：未304缓存的链接列表:\n{link_list}\n")
            print(f"页面{url}已完成所有连接请求，最终结果未304缓存页面列表:")
            for i in list(set(link_list)):
                print("   ", i)
        # # 对所有域名开始进行扫描
        # for link in list(set(all_links)):
        #     self.get_link_status(link)



if __name__ == "__main__":
    import threading
    url_link = "https://m.wbeads.com/"
    print(GetLinkPro().get_links(url_link,label='img', key=['src', 'data-original']))
    # urls = ['https://m.yyw.com', "https://m.beads.us", "https://m.gets.com"]
    # threads = []
    # for url in urls:
    #     t = threading.Thread(target=GetLinkStatus().get_link_status, args=(url,))
    #     threads.append(t)
    #     t.start()
    # for t in threads:
    #     t.join()
    # print(GetLinkStatus().get_links(url_link))
    # GetLinkStatus().get_link_status(url_link)
