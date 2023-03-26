
from pprint import pprint
import re


def convert_mac(mac_address):
    regex = re.compile(
        r"[0-9a-f]{4}[.:-][0-9a-f]{4}[.:-][0-9a-f]{4}"
        r"|([0-9a-f]{2}[.:-]){5}[0-9a-f]{2}"
        r"|[0-9a-f]{12}",
        re.IGNORECASE
    )
    if regex.fullmatch(str(mac_address)):
        mac = re.sub(r"[-.:]", "", mac_address)
    else:
        raise ValueError(f"'{mac_address}' does not appear to be a MAC address")

    new_mac = [mac[index : index + 2] for index in range(0, len(mac), 2)]
    return ":".join(new_mac)


# более точная регулярка, которая проверяет, что разделитель одинаковый
# то есть что такой MAC aaaa:bbbb-cccc не пройдет проверку
def convert_mac(mac_address):
    regex = re.compile(
        r"[0-9a-f]{4}([.:-])[0-9a-f]{4}\1[0-9a-f]{4}"
        r"|[0-9a-f]{2}([.:-])([0-9a-f]{2}\2){4}[0-9a-f]{2}"
        r"|[0-9a-f]{12}",
        re.IGNORECASE
    )
    if regex.fullmatch(str(mac_address)):
        mac = re.sub(r"[-.:]", "", mac_address)
    else:
        raise ValueError(f"'{mac_address}' does not appear to be a MAC address")

    new_mac = [mac[index : index + 2] for index in range(0, len(mac), 2)]
    return ":".join(new_mac)
