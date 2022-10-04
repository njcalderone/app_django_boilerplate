import requests
import json
from decouple import config

keycloak_URL = config("KEYCLOAK_URL")
client_id = config("KEYCLOAK_ADMIN_CLIENT_ID")
username = config("KEYCLOAK_ADMIN_USERNAME")
password = config("KEYCLOAK_ADMIN_PASSWORD")


def get_user_roles(user_name):
    # get token
    data = {
        'client_id': client_id,
        'username': username,
        'password': password,
        'grant_type': 'password',
    }
    url_1 = (keycloak_URL + 'auth/realms/master/protocol/openid-connect/token')
    print(url_1)
    raw_response_JSON = requests.post(url_1, data=data)

    raw_json = raw_response_JSON.json()

    access_token = raw_json['access_token']

    # ==================== get id=========================
    bearer = ('Bearer ' + access_token)
    headers1 = {
        'Content-Type': 'application/json',
        'Authorization': bearer,
    }
    url_2 = (keycloak_URL + 'auth/admin/realms/default/users?username=' + user_name + '&exact=true')
    raw_response_JSON2 = requests.get(url_2, headers=headers1)
    raw_json2 = raw_response_JSON2.json()
    raw_user_id = json.dumps(raw_json2[0], indent=4)
    raw_user_id2 = json.loads(raw_user_id)
    user_id = raw_user_id2['id']

    # get user role

    headers2 = {
        'Content-Type': 'application/json',
        'Authorization': bearer,
    }
    url_3 = (keycloak_URL + 'auth/admin/realms/default/users/' + user_id + '/role-mappings')
    raw_response_JSON3 = requests.get(url_3, headers=headers2)
    raw_json3 = raw_response_JSON3.json()
    raw_user_role = json.dumps(raw_json3, indent=4)
    raw_user_role2 = json.loads(raw_user_role)
    raw_user_role3 = raw_user_role2['realmMappings']
    user_roles = {}
    for i in range(0, len(raw_user_role3)):
        user_roles[i] = raw_user_role2['realmMappings'][i]['name']

    return list(user_roles.values())

