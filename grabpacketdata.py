from scapy.sendrecv import sniff
from process import process_packet
from tkinter import messagebox

def grab_packet_data():
    try:
        # Define the filter to capture only HTTP traffic from the specified IP address
        filter_str = "host 112.213.36.217 and tcp port 80 and tcp[((tcp[12:1] & 0xf0) >> 2):4] = 0x47455420"

        # Start capturing packets
        packets = sniff(filter=filter_str, prn=lambda pkt: process_packet(pkt), store=0)

        print(f"Captured {len(packets)} packets")
        
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")
