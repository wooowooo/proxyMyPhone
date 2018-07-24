# proxyMyPhone
Some Android and iOS allow you to configure only HTTP proxy, which can't proxy many apps. 

This script makes it possible to configure socks/http proxy. (This script doesn't provide proxy)

No root or JB require. No need to install any app on phone.

Requires python on PC.


## How it works
This Script runs a PAC server (HTTP server) on PC. It generates and serves a PAC file that tells your phone (or other devices) to go through the socks/http proxy your PC is serving. 

You need to manually type the PAC address in phone's network setting. 


## Usage

Run this command on PC:

    python proxymyphone.py <pc_ip> <proxy_listen_port_on_pc> <proxy_type>

Then it will give you an address. On your phone's wifi setting layout, set proxy to "auto" and type the address in.

## Other ways

### Android

- [ProxyDroid](https://play.google.com/store/apps/details?id=org.proxydroid) ([Source](https://github.com/madeye/proxydroid)) (need root)
- [Brook](https://github.com/txthinking/brook)
 
### iOS 

- [Brook](https://github.com/txthinking/brook)
- Potatso
