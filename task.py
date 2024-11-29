from scapy.all import *

# Define a callback function to process the captured packets
def packet_callback(packet):
    print(f"Packet captured: {packet.summary()}")
    
    # Check if the packet has IP layer
    if packet.haslayer(IP):
        ip_src = packet[IP].src
        ip_dst = packet[IP].dst
        print(f"Source IP: {ip_src}")
        print(f"Destination IP: {ip_dst}")

        # Check if the packet has a TCP layer
        if packet.haslayer(TCP):
            print(f"Source Port: {packet[TCP].sport}")
            print(f"Destination Port: {packet[TCP].dport}")
        
        # Check if the packet has a UDP layer
        if packet.haslayer(UDP):
            print(f"Source Port: {packet[UDP].sport}")
            print(f"Destination Port: {packet[UDP].dport}")
        
        # Check if the packet has an ICMP layer
        if packet.haslayer(ICMP):
            print(f"ICMP Type: {packet[ICMP].type}")
            print(f"ICMP Code: {packet[ICMP].code}")
    
    print("-" * 50)

# Start sniffing the network
print("Starting network sniffer...")
sniff(prn=packet_callback, store=0)
