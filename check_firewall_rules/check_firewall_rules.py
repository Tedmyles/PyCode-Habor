import psutil

def check_firewall_rules(allowed_ports):
    # Get all active network connections
    connections = psutil.net_connections()

    # Check each connection against allowed ports
    for conn in connections:
        local_port = conn.laddr.port
        remote_port = conn.raddr[1] if conn.raddr else None

        # Check if the local or remote port is not in the allowed ports
        if local_port not in allowed_ports and (remote_port is None or remote_port not in allowed_ports):
            print(f"Warning: Unauthorized connection detected - {conn}")

if __name__ == "__main__":
    print("Firewall Rule Checker")

    # Define allowed ports
    allowed_ports = {80, 443}  # Add more ports as needed

    # Run the firewall rule checker
    check_firewall_rules(allowed_ports)
