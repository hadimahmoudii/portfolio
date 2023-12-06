import subprocess

subprocess.run(['id', '-un'])
subprocess.run(['iptables', '-A', 'INPUT', '-p', 'udp', '—sport', '53', '-j', 'ACCEPT'])
subprocess.run(['iptables', '-A', 'INPUT', '-p', 'tcp', '—sport', '443', '-j', 'ACCEPT'])
subprocess.run(['iptables', '-A', 'INPUT', '-p', 'tcp', '—sport', '80', '-j', 'ACCEPT'])
subprocess.run(['iptables', '-A', 'INPUT', '-p', 'tcp', '—sport', '25', '-j', 'ACCEPT'])
subprocess.run(['iptables', '-A', 'INPUT', '-p', 'tcp', '—sport', '143', '-j', 'ACCEPT'])