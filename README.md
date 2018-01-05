# proxyMyPhone
Some Android and iOS allow you to configure only HTTP proxy, which can't proxy many Apps. 

This script makes it possible to configure socks/http proxy. (This script doesn't provide proxy)

No root or JB require.

> For rooted Android,  [ProxyDroid](https://play.google.com/store/apps/details?id=org.proxydroid) ([Source](https://github.com/madeye/proxydroid)) is fine.

## How it works
This Script runs a PAC server (HTTP server) on PC. It generates and serves a PAC file that tells your phone (or other devices) to use the proxy your PC is serving. 

You need to manually type the PAC address in phone's network setting. 

## Usage
    python proxymyphone.py {pc_ip} {proxy_listen_port} {proxy_type}

Then it will give you an address. On your phone's wifi setting layout, set proxy as "auto" and type the address in.

## Requirements
- Python
