# -*- coding: utf-8 -*-

import BaseHTTPServer
import sys

global pac
pac = """
function FindProxyForURL(url, host)
{
    url  = url.toLowerCase();
    host = host.toLowerCase();
    
    if (isInNet(host, "10.0.0.0", "255.0.0.0") ||
        isInNet(host, "172.16.0.0",  "255.240.0.0") ||
        isInNet(host, "192.168.0.0", "255.255.0.0") ||
        isInNet(host, "127.0.0.0", "255.255.255.0"))
        
        return "DIRECT";


    return "PROXY_TYPE IP:PORT";
    
}
"""

            
class CustomHandler(BaseHTTPServer.BaseHTTPRequestHandler):
    def do_GET(s):
        print "Request header: %s  %s" % (s.headers['Host'], s.headers['User-Agent'])
        s.send_response(200)
        s.send_header("Content-type", "text/plain")
        s.end_headers()
        s.wfile.write(pac)


if __name__ == '__main__':
    
    if len(sys.argv) != 4:
        print """
usage: scriptname ip port PROXY|SOCKS
    ip is your PC IP
    port is your PC proxy listen port
    use PROXY or SOCKS according to your proxy type:
        http proxy       PROXY
        socks5 proxy     SOCKS
        """
        exit()
        
    else:

        httpport = 9010
        httpip = sys.argv[1]
        
        proxyip = sys.argv[1]
        proxyport = sys.argv[2]
        proxytype = sys.argv[3]
        
        
        pac = pac.replace("PROXY_TYPE", proxytype)
        pac = pac.replace("IP", proxyip)
        pac = pac.replace("PORT", proxyport)
        
        server_class = BaseHTTPServer.HTTPServer
        httpd = server_class((httpip, httpport), CustomHandler)
        
        print("server start at %s:%d \n" %(httpip,httpport))
            
        print("Type this address to your network PAC setting:")
        print("http://%s:%d \n" %(httpip, httpport))

        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            pass

        httpd.server_close()
        
        print "Server stoped"

