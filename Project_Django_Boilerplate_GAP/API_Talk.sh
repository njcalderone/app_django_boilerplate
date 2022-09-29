#!/bin/bash
#users
curl -X GET 'http://localhost:8080/auth/admin/realms/default/users?username=user1&exact=true' -H "Content-Type: application/json" -H "Authorization: Bearer $(curl -d "client_id=admin-cli" -d "username=admin" -d "password=admin" -d "grant_type=password" "http://localhost:8080/auth/realms/master/protocol/openid-connect/token" |python3 -c "import sys, json; print(json.load(sys.stdin)['access_token'])")"

#userinfo
#curl -X GET 'http://localhost:8080/auth/realms/default/protocol/openid-connect/userinfo?=username=user1' -H "Content-Type: application/json" -H "Authorization: Bearer $(curl -d "client_id=DjangoApp"  -d "client_secret=4ph4iZ83f4YpBALCNFkndL9UbiPEVGcf" -d "grant_type=client_credentials" "http://localhost:8080/auth/realms/default/protocol/openid-connect/token" |python3 -c "import sys, json; print(json.load(sys.stdin)['access_token'])")"

curl -v --data "client_secret=4ph4iZ83f4YpBALCNFkndL9UbiPEVGcf&client_id=DjangoApp&username=user1&token=$(curl -d "client_id=DjangoApp"  -d "client_secret=4ph4iZ83f4YpBALCNFkndL9UbiPEVGcf" -d "grant_type=client_credentials" "http://localhost:8080/auth/realms/default/protocol/openid-connect/token" |python3 -c "import sys, json; print(json.load(sys.stdin)['access_token'])")" http://localhost:8080/auth/realms/default/protocol/openid-connect/token/introspect

curl -X GET 'http://localhost:8080/auth/admin/realms/default/users' -H "Content-Type: application/json" -H "Authorization: Bearer $(curl -d "client_id=DjangoApp"  -d "client_secret=4ph4iZ83f4YpBALCNFkndL9UbiPEVGcf" -d "grant_type=client_credentials" "http://localhost:8080/auth/realms/default/protocol/openid-connect/token" |python3 -c "import sys, json; print(json.load(sys.stdin)['access_token'])")"


curl -X GET 'http://localhost:8080/auth/admin/realms/default/users?username=user1&exact=true' -H "Content-Type: application/json" -H "Authorization: Bearer $(curl -d "client_id=DjangoApp"  -d "client_secret=4ph4iZ83f4YpBALCNFkndL9UbiPEVGcf" -d "grant_type=client_credentials" "http://localhost:8080/auh/realms/default/protocol/openid-connect/token" |python3 -c "import sys, json; print(json.load(sys.stdin)['access_token'])")"


curl -d "client_id=realm-management1"  -d "client_secret=pf2l1kxUctWESvmRuuy1Vi0T2h63YvK2" -d "grant_type=client_credentials" "http://localhost:8080/auth/realms/default/protocol/openid-connect/token"

curl -X GET 'http://localhost:8080/auth/realms/default/protocol/openid-connect/userinfo?=username=user1' -H "Content-Type: application/json" -H "Authorization: Bearer $(curl -d "client_id=realm-management1"  -d "client_secret=pf2l1kxUctWESvmRuuy1Vi0T2h63YvK2" -d "grant_type=client_credentials" "http://localhost:8080/auth/realms/default/protocol/openid-connect/token" |python3 -c "import sys, json; print(json.load(sys.stdin)['access_token'])")"


curl -X GET 'http://localhost:8080/auth/admin/realms/default/users'  -H "Authorization: Bearer $(curl -d "client_id=realm-management1"  -d "client_secret=pf2l1kxUctWESvmRuuy1Vi0T2h63YvK2" -d "grant_type=client_credentials" "http://localhost:8080/auth/realms/default/protocol/openid-connect/token"|python3 -c "import sys, json; print(json.load(sys.stdin)['access_token'])") "-H 'cache-control: no-cache'


# get an access token
curl -X POST http://localhost:8080/auth/realms/master/protocol/openid-connect/token -H 'Accept: application/json' -H 'Content-Type: application/x-www-form-urlencoded' -H 'cache-control: no-cache' -d "grant_type=client_credentials" -d "client_secret=pf2l1kxUctWESvmRuuy1Vi0T2h63YvK2" -d "client_id=realm-management1"

# get all users of gateway realm, use the token from above and use Bearer as prefix
curl -X GET 'http://localhost:8080/auth/admin/realms/default/users' -H  "Authorization: Bearer $(curl -X POST -H 'Accept: application/json' -H 'Content-Type: application/x-www-form-urlencoded' -H 'cache-control: no-cache' -d "client_id=realm-management1"  -d "client_secret=pf2l1kxUctWESvmRuuy1Vi0T2h63YvK2" -d "grant_type=client_credentials" "http://localhost:8080/auth/realms/default/protocol/openid-connect/token"|python3 -c "import sys, json; print(json.load(sys.stdin)['access_token'])") " -H 'cache-control: no-cache'