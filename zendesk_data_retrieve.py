import json
import time
import requests

#credentials = 'your_zendesk_email', 'your_zendesk_password'
credentials = 'support@student5462.zendesk.com', 'zendesk123@'
session = requests.Session()
session.auth = credentials
zendesk = 'https://student5462.zendesk.com/'

topic_id = 1
topic_posts = []
user_list = []
url = f'{zendesk}/api/v2/community/topics/{topic_id}/posts.json?page[size]=100&include=users'

while url:
    response = session.get(url)
    if response.status_code == 429:
        print('Rate limited! Please wait.')
        time.sleep(int(response.headers['retry-after']))
        continue
    if response.status_code != 200:
        print(f'Error with status code {response.status_code}')
        exit()
    data = response.json()

    topic_posts.extend(data['posts'])
    user_list.extend(data['users'])

    if data['meta']['has_more']:
        url = data['links']['next']
    else:
        url = None

topic_data = {'posts': topic_posts, 'users': user_list}
with open('my_serialized_data_file.json', mode='w', encoding='utf-8') as f:
    json.dump(topic_data, f, sort_keys=True, indent=2)

with open('my_serialized_data_file.json', mode='r') as f:
    topic = json.load(f)

for post in topic['posts']:
    author = 'anonymous'
    for user in topic['users']:
        if user['id'] == post['author_id']:
            author = user['name']
            break
    print(f'\"{post["title"]}\" by {author}')
