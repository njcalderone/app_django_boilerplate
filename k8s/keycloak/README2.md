# KC in Rancher Desktop

Usage
-----
Deploy the manifests in this folder which include a configmap that has pre-loaded users and groups as well as a client for the OAuth2 proxy app as documented below. The configmap data was generated using the `backup_kc.sh` script.

    # Create a namespace for Keycloak and deploy
    kubectl create namespace kc
    kubectl -n kc apply -f .

Browse to https://kc.rancher.localhost

Optionally use the `log_kc_top.sh` script to log the memory and proc usage of the KC pod. In my limited testing, the pod asks for up to 2533m cpu and 620Mi mem.

### Keycloak Users
| User  | Passwd | Role        | details
|-------|--------|-------------|--------
| admin | admin  | admin       |
| user1 | user1  | Basic_User  | View only
| user2 | user2  | Data_Edit   | Data edit
| user3 | user3  | NO_ROLES    | No roles assigned

### OIDC Client for OAuth2 Proxy
* clientID: `oa2p`
* clientSecret: `QhyoJslf2rucOWDp9NH40BAHPKDdVlQn`
* cookieSecret: `d2l2Qk9qMmUrUXpHUDBlbVlSby9jdz09`

Example deployment for testing
------------------------------
```bash
# Create a new namespace
kubectl create namespace kc

# Create & mount the configmap using a subPath to specify the init file
kubectl -n kc apply -f kc-configmap.yml
kubectl -n kc apply -f test/alpine-pod.yml
kubectl -n kc get po
kubectl -n kc exec -it alpine-test-pod -- sh

# Create a KC deployment that mounts the configmap
kubectl -n kc apply -f kc-deployment.yml
kubectl -n kc get po
kubectl -n kc describe deployments.apps kc-deployment
kubectl -n kc logs deployments.apps kc-deployment
kubectl -n kc get po
# kubectl -n kc logs # name of pod kc-deployment-6fbbf9d8bf-qkfsc

# Create the service
kubectl -n kc apply -f kc-service.yml
kubectl -n kc exec -it alpine-test-pod -- curl kc-service:8080

# Create the ingress
kubectl -n kc apply -f kc-ingress.yml

# browse to kc.rancher.localhost
```
