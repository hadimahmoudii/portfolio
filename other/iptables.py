import subprocess


def rerouteRequest(user_ip):
    update_rules = subprocess.getoutput(f"sudo iptables -t nat -I PREROUTING -s {user_ip} -j ACCEPT")
    #save_rules = subprocess.getoutput("sudo netfilter-persistent save")
    #reload_iptable = subprocess.getoutput("sudo netfilter-persistent reload")
    #print(update_rules)
    #print(save_rules)
    #print(reload_iptable)
    print("OK")

if __name__ == "__main__":
    rerouteRequest()