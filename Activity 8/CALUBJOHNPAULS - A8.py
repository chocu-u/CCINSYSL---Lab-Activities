# Simple Intrusion Detection System
# Analyzes simulated network packets and identifies suspicious activity

def analyze_network_packets():
    """
    Simulates network packet analysis and detects suspicious activity
    based on packet count threshold per source IP
    """
    
    # Simulated packet data - each tuple represents (source_ip, destination_ip, packet_type)
    simulated_packets = [
        ("192.168.1.10", "192.168.1.1", "HTTP"),
        ("192.168.1.20", "192.168.1.1", "HTTPS"),
        ("192.168.1.150", "192.168.1.1", "HTTP"),
        ("192.168.1.10", "192.168.1.2", "FTP"),
        ("192.168.1.150", "192.168.1.1", "HTTP"),
        ("192.168.1.150", "192.168.1.3", "HTTPS"),
        ("192.168.1.10", "192.168.1.1", "HTTP"),
        ("192.168.1.150", "192.168.1.1", "HTTP"),
        ("192.168.1.20", "192.168.1.2", "SSH"),
        ("192.168.1.150", "192.168.1.1", "HTTP"),
        ("192.168.1.10", "192.168.1.4", "HTTP"),
        ("192.168.1.150", "192.168.1.1", "HTTP"),
        ("192.168.1.150", "192.168.1.5", "HTTPS"),
        ("192.168.1.10", "192.168.1.1", "HTTP"),
        ("192.168.1.150", "192.168.1.1", "HTTP"),
        ("192.168.1.150", "192.168.1.6", "HTTP"),
        ("192.168.1.10", "192.168.1.1", "HTTP"),
        ("192.168.1.150", "192.168.1.1", "HTTP"),
        ("192.168.1.20", "192.168.1.1", "HTTPS"),
        ("192.168.1.150", "192.168.1.7", "HTTP"),
        ("192.168.1.10", "192.168.1.1", "HTTP"),
        ("192.168.1.150", "192.168.1.1", "HTTP"),
        ("192.168.1.150", "192.168.1.8", "HTTPS"),
        ("192.168.1.10", "192.168.1.1", "HTTP"),
        ("192.168.1.150", "192.168.1.1", "HTTP"),
        ("192.168.1.150", "192.168.1.9", "HTTP"),
        ("192.168.1.10", "192.168.1.1", "HTTP"),
        ("192.168.1.150", "192.168.1.1", "HTTP"),
        ("192.168.1.150", "192.168.1.10", "HTTPS"),
        ("192.168.1.10", "192.168.1.1", "HTTP"),
        ("192.168.1.150", "192.168.1.1", "HTTP"),
        ("192.168.1.150", "192.168.1.11", "HTTP"),
        ("192.168.1.150", "192.168.1.1", "HTTP"),
        ("192.168.1.150", "192.168.1.12", "HTTPS"),
        ("192.168.1.150", "192.168.1.1", "HTTP"),
        ("192.168.1.150", "192.168.1.13", "HTTP"),
        ("192.168.1.150", "192.168.1.1", "HTTP")
    ]
    
    # Threshold for suspicious activity (packets per IP)
    SUSPICIOUS_THRESHOLD = 20
    
    print("Analyzing simulated network packets...")
    
    # Count packets per source IP
    packet_counts = {}
    for source_ip, dest_ip, packet_type in simulated_packets:
        if source_ip in packet_counts:
            packet_counts[source_ip] += 1
        else:
            packet_counts[source_ip] = 1
    
    # Display packet counts per IP
    print("Packet counts per source IP:")
    for ip, count in sorted(packet_counts.items()):
        print(f" - {ip}: {count} packets")
    
    # Check for suspicious activity
    print("Checking for suspicious activity...")
    suspicious_ips = []
    
    for ip, count in packet_counts.items():
        if count > SUSPICIOUS_THRESHOLD:
            suspicious_ips.append((ip, count))
    
    # Report suspicious activity
    if suspicious_ips:
        for ip, count in suspicious_ips:
            print(f"!!! ALERT: Suspicious activity detected from {ip}. Packets sent: {count}")
    else:
        print("No suspicious activity detected.")

if __name__ == "__main__":
    analyze_network_packets()