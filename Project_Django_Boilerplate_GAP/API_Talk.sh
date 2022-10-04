#!/bin/bash
#users
#curl -X GET 'http://localhost:8080/auth/admin/realms/default/users?username=user1&exact=true' -H "Content-Type: application/json" -H "Authorization: Bearer $(curl -d "client_id=admin-cli" -d "username=admin" -d "password=admin" -d "grant_type=password" "http://localhost:8080/auth/realms/master/protocol/openid-connect/token" |python3 -c "import sys, json; print(json.load(sys.stdin)['access_token'])")"
#curl -X GET 'http://localhost:8080/auth/admin/realms/default/users/ac7c0c7c-5b8c-43ea-9c44-9526bcc0ddd6/role-mappings' -H "Content-Type: application/json" -H "Authorization: Bearer $(curl -d "client_id=admin-cli" -d "username=admin" -d "password=admin" -d "grant_type=password" "http://localhost:8080/auth/realms/master/protocol/openid-connect/token" |python3 -c "import sys, json; print(json.load(sys.stdin)['access_token'])")"
user_name="user1"
app_json=$(curl -X GET 'http://localhost:8080/auth/admin/realms/default/users?username='$user_name'&exact=true' -H "Content-Type: application/json" -H "Authorization: Bearer $(curl -d "client_id=admin-cli" -d "username=admin" -d "password=admin" -d "grant_type=password" "http://localhost:8080/auth/realms/master/protocol/openid-connect/token" |python3 -c "import sys, json; print(json.load(sys.stdin)['access_token'])")")
user_id=$($app_json)

curl -X GET 'http://localhost:8080/auth/admin/realms/default/users/'$user_id'/role-mappings' -H "Content-Type: application/json" -H "Authorization: Bearer $(curl -d "client_id=admin-cli" -d "username=admin" -d "password=admin" -d "grant_type=password" "http://localhost:8080/auth/realms/master/protocol/openid-connect/token" |python3 -c "import sys, json; print(json.load(sys.stdin)['access_token'])")"
