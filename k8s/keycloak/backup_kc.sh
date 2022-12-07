#!/bin/bash -x

set -o errexit
set -o nounset

# From https://itecnote.com/tecnote/how-to-get-keycloak-to-export-realm-users-and-then-exit/
# Official docs: https://github.com/keycloak/keycloak-documentation/blob/main/server_admin/topics/export-import.adoc


# Logs indicating backup success 
## 03:41:20,893 INFO  [org.keycloak.exportimport.singlefile.SingleFileExportProvider] (ServerService Thread Pool -- 58) Exporting realm 'test-realm' into file /tmp/keycloak-gbp-export.json
## 03:41:20,894 DEBUG [org.keycloak.transaction.JtaTransactionWrapper] (ServerService Thread Pool -- 58) new JtaTransactionWrapper
## 03:41:20,894 DEBUG [org.keycloak.transaction.JtaTransactionWrapper] (ServerService Thread Pool -- 58) was existing? false
## 03:41:21,746 DEBUG [org.keycloak.models.cache.infinispan.authorization.InfinispanCacheStoreFactoryProviderFactory] (ServerService Thread Pool -- 58) Registered cluster listeners
## 03:41:21,902 DEBUG [org.keycloak.models.cache.infinispan.InfinispanUserCacheProviderFactory] (ServerService Thread Pool -- 58) Registered cluster listeners
## 03:41:22,315 DEBUG [org.keycloak.transaction.JtaTransactionWrapper] (ServerService Thread Pool -- 58) JtaTransactionWrapper  commit
## 03:41:22,322 DEBUG [org.keycloak.transaction.JtaTransactionWrapper] (ServerService Thread Pool -- 58) JtaTransactionWrapper end
## 03:41:22,323 INFO  [org.keycloak.services] (ServerService Thread Pool -- 58) KC-SERVICES0035: Export finished successfully

### User-provided input
KC_NAMESPACE=kc
REALM_NAME=test-realm
### END user-provided input

KC_POD=$(kubectl -n $KC_NAMESPACE get pod --selector=tier=kc-deployment -o jsonpath="{.items[0].metadata.name}")

echo "[+] Export realm from KC_POD=$KC_POD"

# bin/standalone.sh -Dkeycloak.migration.action=export -Dkeycloak.migration.provider=singleFile -Dkeycloak.migration.file=/tmp/out.json -Djboss.socket.binding.port-offset
kubectl exec -n $KC_NAMESPACE $KC_POD -c keycloak -it -- \
    sh /opt/jboss/keycloak/bin/standalone.sh \
        -Dkeycloak.migration.action=export \
        -Dkeycloak.migration.provider=singleFile \
        -Dkeycloak.migration.file=/tmp/keycloak-gbp-export.json \
        -Dkeycloak.migration.realmName=default \
        -Djboss.socket.binding.port-offset=100

echo "[+] Copy export file here"
kubectl cp $KC_POD:/tmp/keycloak-gbp-export.json ./keycloak-gbp-export.json
