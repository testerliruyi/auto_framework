"""
author:liruyi
desc:搜索json字符串关键字，使用递归写法。
date:2023/10/10
"""
import jsonpath



def json_get_value(dict, key, value=None):
    def findField():
        if value and type(value) == int:
            res = jsonpath.jsonpath(dict, f'$...{key}[{value}]')
        else:
            res = jsonpath.jsonpath(dict, f'$...{key}')
        return res

    def x():
        result = findField()
        if type(result) == bool:
            return result
        else:
            return result[0]

    return x()

def search_json(dictionary, keyword):
    results = []

    for key, value in dictionary.items():
        if isinstance(value, dict):
            sub_results = search_json(value, keyword)
            results.extend([(key + '.' + sub_key, sub_val) for sub_key, sub_val in sub_results])
        elif isinstance(value, list):
            for index, item in enumerate(value):
                if isinstance(item, dict):
                    sub_results = search_json(item, keyword)
                    results.extend([(key + '.' + str(index) + '.' + sub_key, sub_val) for sub_key, sub_val in sub_results])
        elif keyword in str(value):
            results.append((key, value))
    return results

if __name__ == '__main__':
    book_dict = {
        "store": {
            "book": [
                {"category": "reference",
                 "author": "Nigel Rees",
                 "title": "Sayings of the Century",
                 "price": 8.95
                 },
                {"category": "fiction",
                 "author": "Evelyn Waugh",
                 "title": "Sword of Honour",
                 "price": 12.99
                 },
                {"category": "fiction",
                 "author": "Herman Melville",
                 "title": "Moby Dick",
                 "isbn": "0-553-21311-3",
                 "price": 8.99
                 },
                {"category": "fiction",
                 "author": "J. R. R. Tolkien",
                 "title": "The Lord of the Rings",
                 "isbn": "0-395-19395-8",
                 "price": 22.99
                 }
            ],
            "bicycle": {
                "color": "red",
                "price": 19.95
            }
        }
    }
    print(jsonfind(book_dict, 'color'))
    # print(search_json(book_dict, 'bicycle'))
