k8s-oa2p
========
Browse to http://oa2p.rancher.localhost after setup and use the local Keycloak credentials `user1 | user1` to visit the protected page.

Setup
-----
1. Run the local Keycloak in k8s-kc (`../k8s-kc/`) so that the default users and clients are available in the `kc` namespace.

2. Pull the tarballs with helm which includes nginx to create the site OA2P will protect.
    ```
    helm pull bitnami/nginx --version 13.1.6
    helm pull bitnami/oauth2-proxy --version 3.0.3
    ```

3. Run the charts with the values.yamls provided
    ```
    helm upgrade --install nginx-local -f nginx-values.yaml nginx-13.1.6.tgz
    # helm upgrade --install oa2p-local -f oauth2-proxy-values.yaml oauth2-proxy-3.0.3.tgz --dry-run # to see generated yamls
    helm upgrade --install oa2p-local -f oauth2-proxy-values.yaml oauth2-proxy-3.0.3.tgz
    ```

    Error after initial dry-run
    ```
    $ kubectl logs pod/oa2p-local-oauth2-proxy-7c76d787ff-6gf5d -f
    [2022/07/14 15:23:29] [options.go:81] WARNING: no explicit redirect URL: redirects will default to insecure HTTP
    [2022/07/14 15:23:29] [provider.go:55] Performing OIDC Discovery...
    [2022/07/14 15:23:29] [main.go:60] ERROR: Failed to initialise OAuth2 Proxy: error intiailising provider: could not create provider data: error building OIDC ProviderVerifier: could not get verifier builder: error while discovery OIDC configuration: failed to discover OIDC configuration: error performing request: Get "http://kc.rancher.localhost/auth/realms/default/.well-known/openid-configuration": dial tcp: lookup kc.rancher.localhost on 10.43.0.10:53: no answer from DNS server
    ```

4. Add a rewrite rule to the coredns configmap by applying the provided configmap.

    `rewrite name kc.rancher.localhost kc-service.kc.svc.cluster.local`

    I was a little afraid of the NodeHosts portion since the local node might get assigned a different IP but it worked! Ref: https://coredns.io/2017/05/08/custom-dns-entries-for-kubernetes/
    ```
    kubectl -n kube-system edit configmaps coredns

    ### in the editor ###

    apiVersion: v1
    data:
      Corefile: |
      ...
            ready
            rewrite name kc.rancher.localhost kc-service.kc.svc.cluster.local 
            kubernetes cluster.local in-addr.arpa ip6.arpa {
    ....

        import /etc/coredns/custom/*.server
      NodeHosts: |
        10.1.10.148 lima-rancher-desktop
    ```

    Logs after adding entry to the coredns configmap
    ```
    $ kubectl logs oa2p-local-oauth2-proxy-7c76d787ff-45l6k
    [2022/07/14 16:09:47] [options.go:81] WARNING: no explicit redirect URL: redirects will default to insecure HTTP
    [2022/07/14 16:09:47] [provider.go:55] Performing OIDC Discovery...
    [2022/07/14 16:09:48] [providers.go:145] Warning: Your provider supports PKCE methods ["plain" "S256"], but you have not enabled one with --code-challenge-method
    [2022/07/14 16:09:48] [proxy.go:89] mapping path "/" => upstream "http://nginx-local:80"
    [2022/07/14 16:09:48] [oauthproxy.go:156] OAuthProxy configured for OpenID Connect Client ID: client4
    [2022/07/14 16:09:48] [oauthproxy.go:162] Cookie settings: name:boilerplate secure(https):false httponly:true expiry:168h0m0s domains: path:/ samesite: refresh:after 30s
    10.42.0.1:38718 - 45234b3f-af88-4d1a-8541-5704d88bf3fd - - [2022/07/14 16:09:49] 10.42.0.24:4180 GET - "/ping" HTTP/1.1 "kube-probe/1.23" 200 2 0.000
    ```