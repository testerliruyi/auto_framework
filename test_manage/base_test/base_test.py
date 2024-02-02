# import redis
# conn= redis.Redis(
#   host='redis-14102.c323.us-east-1-2.ec2.cloud.redislabs.com',
#   port=14102,
#   password='SPD4KVOukJu7Zmn8saxlpxwMn4oeSfS5',
#   decode_responses=True,charset='utf-8',encoding='utf-8')
#
#
# conn.set('name1','chenge')
# conn.set('key','悲哀')
# print(conn.get('name1'))

from config.enums import inputOption
print(inputOption.Design.value)