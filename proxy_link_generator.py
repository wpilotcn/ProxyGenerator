import requests
import json
import base64
from datetime import datetime

# URL and route information
hysteria2_routes = [
    [
        "https://gitlab.com/free9999/ipupdate/-/raw/master/hysteria2/config.json",
        "https://fastly.jsdelivr.net/gh/Alvin9999/pac2@latest/hysteria2/config.json",
        "https://gitlab.com/free9999/ipupdate/-/raw/master/hysteria2/2/config.json",
        "https://fastly.jsdelivr.net/gh/Alvin9999/pac2@latest/hysteria2/2/config.json"
    ]
]

xray_routes = [
    [
        "https://gitlab.com/free9999/ipupdate/-/raw/master/xray/config.json",
        "https://fastly.jsdelivr.net/gh/Alvin9999/pac2@latest/xray/config.json",
        "https://gitlab.com/free9999/ipupdate/-/raw/master/xray/2/config.json",
        "https://fastly.jsdelivr.net/gh/Alvin9999/pac2@latest/xray/2/config.json"
    ]
]

def generate_hysteria2_link(config):
    server_info = config["server"].split(",")[0]
    auth_info = config["auth"]
    tls_info = config.get("tls", {})
    sni = tls_info.get("sni", "")
    insecure = 1 if tls_info.get("insecure", False) else 0
    return f"hy2://{auth_info}@{server_info}/?insecure={insecure}&sni={sni}"

def generate_xray_link(config):
    outbound = config['outbounds'][0]
    settings = outbound['settings']['vnext'][0]
    stream_settings = outbound['streamSettings']
    vmess_dict = {
        "v": "2",
        "ps": "",
        "add": settings['address'],
        "port": str(settings['port']),
        "id": settings['users'][0]['id'],
        "aid": str(settings['users'][0]['alterId']),
        "scy": settings['users'][0]['security'],
        "net": stream_settings['network'],
        "type": "",
        "host": stream_settings['wsSettings']['headers']['Host'],
        "path": stream_settings['wsSettings']['path'],
        "tls": ""
    }
    vmess_json = json.dumps(vmess_dict)
    vmess_base64 = base64.b64encode(vmess_json.encode()).decode()
    return f"vmess://{vmess_base64}"

def try_get_config(urls):
    for url in urls:
        try:
            response = requests.get(url)
            response.raise_for_status()
            return response.json()
        except Exception:
            continue
    return None

def generate_links():
    output = []
    output.append(f"Last updated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
    
    output.append("Hysteria2:")
    for route_group in hysteria2_routes:
        config = try_get_config(route_group)
        if config:
            link = generate_hysteria2_link(config)
            output.append(f"Route: {link}")
        else:
            output.append("Route: Error - All URLs failed")
    
    output.append("\nXray:")
    for route_group in xray_routes:
        config = try_get_config(route_group)
        if config:
            link = generate_xray_link(config)
            output.append(f"Route: {link}")
        else:
            output.append("Route: Error - All URLs failed")
    
    return "\n".join(output)

def main():
    links = generate_links()
    with open("proxy_links.txt", "w", encoding='utf-8') as f:
        f.write(links)

if __name__ == '__main__':
    main()
