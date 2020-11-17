import platform    # For getting the operating system name
import subprocess  # For executing a shell command

def ping(host):
    """
    Returns True if host (str) responds to a ping request.
    Remember that a host may not respond to a ping (ICMP) request even if the host name is valid.

    Source: https://stackoverflow.com/questions/2953462/pinging-servers-in-python
    """
    # TODO: Support TCP Pings
    # Source: https://github.com/zhengxiaowai/tcping
    # Option for the number of packets as a function of
    # TODO: Expand this out to a more legible set of lines
    param = '-n' if platform.system().lower()=='windows' else '-c'

    # TODO: Support multiple iterations
    # Building the command. Ex: "ping -c 1 google.com"
    # TODO: Support returning the output as a Tuple
    # TODO: Support operation like Trace Route with TTLs iterated
    # Source: https://superuser.com/questions/915657/how-to-simulate-traceroute-using-ping
    status,output = subprocess.getstatusoutput(f"ping {param} 1 {host}")
    if "unreachable" in output.lower():
        return False
    if status == 0:
        return True
    if status != 0:
        return False

print(ping("192.168.0.254"))

