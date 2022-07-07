import requests
import json

with open("kakao_code.json","r") as fp:
    tokens = json.load(fp)
# print(tokens)
# print(tokens["access_token"])

friend_url = "https://kapi.kakao.com/v1/api/talk/friends"

# GET /v1/api/talk/friends HTTP/1.1
# Host: kapi.kakao.com
# Authorization: Bearer {ACCESS_TOKEN}

headers={"Authorization" : "Bearer " + tokens["access_token"]}

result = json.loads(requests.get(friend_url, headers=headers).text)

#print(type(result))
#print("=============================================")
#print(result)
print("=============================================")
friends_list = result.get("elements")
#print(friends_list)
friends_name = friends_list[0].get('profile_nickname')
print("TO : " + friends_name)
# print(type(friends_list))
friend_id = friends_list[0].get("uuid")
# print(friend_id)
print("=============================================")


send_url= "https://kapi.kakao.com/v1/api/talk/friends/message/default/send"
msgcontent = "테스트중"
data={
    'receiver_uuids': '["{}"]'.format(friend_id),
    "template_object": json.dumps({
        "object_type":"text",
        "text":msgcontent,
        "link":{
            "web_url":"www.daum.net",
            "web_url":"www.naver.com"
        }
        
    })
}

response = requests.post(send_url, headers=headers, data=data)
template_object = data.get('template_object')
template_object= json.loads(template_object)
# print(type(template_object))
print("Msg : " + template_object.get("text"))
# text = template_object.get('text')

# text = text.encode('utf-8')
# text = text.decode('unicode_escape')

# print(text)
response.status_code