from dictionary import gear_ratios, gear_ratio_stats, gear_ratio_stats_extended, final_ratio
from carcombo import selected_car
from gearwidget import selected_gear_ratio
from process import process_packet
from scapy.sendrecv import sniff
from tkinter import messagebox


global races_ran
races_ran = 0

stats = f'selected_car[selected_gear_ratio][gear_ratio_stats].json'

if selected_gear_ratio in selected_car:
    race_data = selected_car[selected_gear_ratio][gear_ratio_stats][final_ratio][gear_ratio_stats_extended]
else:
    race_data = selected_car[gear_ratios][gear_ratio_stats][final_ratio][gear_ratio_stats_extended]

def grab_packet():
    try:
        try:
            # Define the filter to capture only HTTP traffic from the specified IP address
            filter_str = "host 112.213.36.217 and tcp port 80 and tcp[((tcp[12:1] & 0xf0) >> 2):4] = 0x47455420"
            print('filter set to capture packets only from nitto')
        except Exception:
            raise ValueError(f'Error: cant set filter to capture http traffic from nitto ip')
        try:
            # Start capturing packets
            packets = sniff(filter=filter_str, prn=process_packet, store=0)
            print(f"Capturing {len(packets)} packets")
        except Exception:
            raise ValueError(f'Error: Theres some issue capturing packets check network, ip, are they encrypted?')
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")
    return process_packet()


