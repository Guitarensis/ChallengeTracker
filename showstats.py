from main import root
from tkinter import messagebox
from process import process_packet

def show_stats(packet_data):
    global TOTAL_RT, TOTAL_ET, TOTAL_MPH, MATCHES_PLAYED

    # Check if matches have been played yet
    if MATCHES_PLAYED == 0:
        messagebox.showinfo('Stats', 'No matches played yet.')
        return

    # Calculate averages for all gear ratios and display stats
    rt_total = 0
    et_total = 0
    mph_total = 0
    for ratio in packet_data['ratios']:
        stats = packet_data['stats'][str(ratio)]
        rt_sum = sum([float(stat['rt']) for stat in stats])
        et_sum = sum([float(stat['et']) for stat in stats])
        mph_sum = sum([float(stat['mph']) for stat in stats])
        rt_total += rt_sum
        et_total += et_sum
        mph_total += mph_sum
        rt_avg = rt_sum / len(stats)
        et_avg = et_sum / len(stats)
        mph_avg = mph_sum / len(stats)
        messagebox.showinfo(f'Stats for Gear Ratio {ratio}',
                            f'Total Matches Played: {len(stats)}\n\n'
                            f'Total RT: {rt_sum:.3f}\n\n'
                            f'Total ET: {et_sum:.3f}\n\n'
                            f'Total MPH: {mph_sum:.3f}\n\n'
                            f'Average RT: {rt_avg:.3f}\n\n'
                            f'Average ET: {et_avg:.3f}\n\n'
                            f'Average MPH: {mph_avg:.3f}\n\n')

root.mainloop()