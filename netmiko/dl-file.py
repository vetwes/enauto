#!/usr/bin/env python

from netmiko import Netmiko, file_transfer
from yaml import safe_load

def main():
    with open("home-router.yml", "r") as handle:
        routers = safe_load(handle)

    for router in routers["devices"]:
        connection = Netmiko(
            host=router["ip"],
            device_type=router["platform"],
            username=router["username"],
            password=router["password"],
        )
    
        get_file = file_transfer(
            connection,
            source_file="test.txt",
            dest_file="success.txt",
            file_system="/home/%s" % router["username"],
            direction="get",
            overwrite_file=True,
        )

    print("Connected to %s" % connection)
    print(file_transfer)

if __name__ == "__main__":
    main()
