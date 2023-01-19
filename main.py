from mastodon import Mastodon
import yaml
from pprint import pprint
import sys

STRING_TO_FIND = sys.argv[1]
SEPARATOR = "-" * 30

with open("creds.yml") as file:
    creds_data = yaml.safe_load(file)
    
masto_conn = Mastodon(access_token=creds_data['token'], api_base_url=creds_data['base_url'])

me_info = masto_conn.me()

my_id = me_info['id']
my_name = me_info['display_name']

my_statuses = masto_conn.account_statuses(my_id, limit=25)

reblog_count = 0
toot_count = 0

print(f"My Name: {my_name}  My ID: {my_id}")
for status in my_statuses:
    if status['reblog']:
        reblog_count += 1
        # print(SEPARATOR)
        # reblog_content = status['reblog']['content']
        # print(f"Reblog: {reblog_content}")
        continue
    if status['content']:
        if STRING_TO_FIND in status['content']:
            print(SEPARATOR)
            print("<><><><><><><><><><><><><>")
            print(f"Status: {status['content']}")
            print(f"Reblogs: {status['reblogs_count']} Favorites: {status['favourites_count']}")
            
print(f"TOTAL REBLOGS: {reblog_count}")