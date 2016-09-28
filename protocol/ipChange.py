#coding:utf-8

import re

def ipToHex(ip):
    """
    ip split by "." AND len to change hex
    """
    hex_ip = ""
    for item in map(lambda x:hex(int(x))[2:],ip.split(".")):
        if len(item) < 2:
            item = '0'+item
        if  hex_ip:
            hex_ip = hex_ip + "."+item
        else:
            hex_ip = item
    return hex_ip

def hexstrToInt(hex, hsep="", psep="."):
    """
    每个字节有两位。
    """
    if hsep:
        hex_list = hex.split(hsep)
    else:
        hex_list = filter(None,re.split(r"(\w{2})",hex))
    if not psep:
        return "".join(map(lambda x:str(int(x,16)),hex_list))
    else:
        return psep.join(map(lambda x:str(int(x,16)),hex_list))


if __name__ == "__main__":
    ip = "10.20.2.114"
    print ipToHex(ip)
    hex = "0a140272"
    print hexstrToInt(hex)


