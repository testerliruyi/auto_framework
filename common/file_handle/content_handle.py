from common_util import get_file_list, read_file_content
import re

def content_handle():
    file_list = get_file_list.get_files()
    file_content = read_file_content.get_yaml_file_content()
    for x in range(0, len(file_content)):
        file_content[x]['path'] = str(file_list[x])
        # 将话题和内容介绍匹配出来
        file_content[x]['topic'] = re.findall(r'#(\w+)?', file_content[x]['desc'])
        file_content[x]['desc_split'] = file_content[x]['desc'].split('#')[0]

    print(file_content)
    return file_content


if __name__ == "__main__":
    content_handle()