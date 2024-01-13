import jsonpath
import re
def handle_template(pattern,content,repsone):
    template_key=re.findall(pattern,content)
    for key in template_key:
        if jsonpath.jsonpath(repsone, '$..{}'.format(key)):
            content = content.replace("{DepReq(%s)}" % (key), jsonpath.jsonpath(repsone, '$..{}'.format(key))[0])
    return content


if __name__ == '__main__':
    pattern = re.compile("\{DepReq\((\w+)\)\}")
    content = '''
    {"caseID":{DepReq(caseId)},"token":"{DepReq(token)}"}
    '''
    repay = {"header": "123", "caseId": "abc88238238232", "dataDto": {"token": "123456789"}}

    res=handle_template(pattern,content,repay)
    print(res)

