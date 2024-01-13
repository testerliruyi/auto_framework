import jsonpath
'''
author:liruyi
desc:搜索json字符串关键字
date:2023/10/10
'''
def jsonfind(dict,key,value=None):
    def findField():
        if value and type(value)==int:
            res = jsonpath.jsonpath(dict, f'$...{key}[{value}]')
        else:
            res=jsonpath.jsonpath(dict,f'$...{key}')
        return res
    def x():
        result=findField()
        if type(result)==bool:
            return result
        else:
            return result[0]
    return x()



if __name__=='__main__':
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
    print(jsonfind(book_dict,'book',2))
