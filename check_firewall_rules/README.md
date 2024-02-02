/---------- Overview ----------/

The Firewall Rule Checker is a simple Python script that checks active network connections against predefined firewall rules to enhance security. It verifies whether the connections align with specified allowed ports and raises warnings for unauthorized connections.

/-------- Features ----------/

1.Checks active network connections.
2.Verifies connections against allowed ports.
3.Warns about unauthorized connections.

/---------- Requirements ----------/

Python 3.x
psutil library (install with pip install psutil)

Customize the allowed ports in the script based on your firewall configuration.

/---------- Configuration ----------/
Modify the allowed_ports set in the script (check_firewall_rules.py) to specify the ports considered authorized.


/----------  Define allowed ports ----------/
allowed_ports = {80, 443}  # Add more ports as needed

Contributing
Contributions are welcome! If you find issues or have suggestions, feel free to open an issue or submit a pull request.