# Update these paths according to your netMHCpan/netMHCIIpan downloads
NETMHCPAN30_PATH = '/cellar/users/ramarty/programs/netMHCpan-3.0/netMHCpan'
NETMHCPAN40_PATH = '/cellar/users/ramarty/programs/netMHCpan-4.0/netMHCpan'
NETMHCIIPAN31_PATH = '/cellar/users/ramarty/programs/netMHCIIpan-3.1/netMHCIIpan'

# Update based on your desired tmp directory
TEMP_DIR = '/tmp/ramarty/'


def setup_MHCI():
    return NETMHCPAN40_PATH, TEMP_DIR

def setup_MHCII():
    return NETMHCIIPAN31_PATH, TEMP_DIR