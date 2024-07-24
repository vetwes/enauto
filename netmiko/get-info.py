#!/usr/bin/env python

from netmiko import Netmiko
from yaml import safe_load

def main():
    router_ip = "10.0.1.1"
    
    with open("show-commands.yml", "r") as handle:
        commands = safe_load(handle)

    connection = Netmiko(
        host=router_ip,
        username="username",
        password="password",
        device_type="ubiquiti_edgerouter",
    )

    print("Logged into %s successfully" % connection.find_prompt())
    
    for command in commands["commands"]:
        result = connection.send_command(command)
        print("%s\n" % command + "-" * len(command))
        print(result)

    connection.disconnect()

if __name__ == "__main__":
    main()
