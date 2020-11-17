import platform    # For getting the operating system name
import subprocess  # For executing a shell command

def ping(host):
    """
    Returns True if host (str) responds to a ping request.
    Remember that a host may not respond to a ping (ICMP) request even if the host name is valid.

    Source: https://stackoverflow.com/questions/2953462/pinging-servers-in-python
    """
    # Option for the number of packets as a function of
    param = '-n' if platform.system().lower()=='windows' else '-c'

    # Building the command. Ex: "ping -c 1 google.com"
    status,output = subprocess.getstatusoutput(f"ping {param} 1 {host}")
    if "unreachable" in output.lower():
        return False
    if status == 0:
        return True
    if status != 0:
        return False

print(ping("192.168.0.254"))

