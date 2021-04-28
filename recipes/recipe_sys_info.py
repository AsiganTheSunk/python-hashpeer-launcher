# module to read all info from computer
import psutil
import platform
import time

# module to read the date-time of the current computer and import function datetime
from datetime import datetime


# module GUI tkinter windows creation
# import all functions from module
# import tkinter as tk
from tkinter import *
from tkinter import ttk


# covert large numbers of bytes into a defined format (kilo, mega, giga, tera, peta)
def get_size(bytes, suffix="B"):
    """
    Scale bytes to proper format:

    1253656 -> '1.20MB'
    1253656678 -> '1.17GB'
    :param bytes:
    :param suffix:
    :return:
    """
    factor = 1024
    for unit in ["", "K", "M", "G","T", "P"]:
        if bytes < factor:
            return f"{bytes:.2f}{unit}{suffix}"
        bytes /= factor


# generate tkinter interface for each category
window_box = Tk()

window_box.title("Computer Information")
#window_box.iconbitmap("path/to/icon")

notebook_labels = ttk.Notebook(window_box)
notebook_labels.pack(pady=15)


# Sys info
def system_info():
    print("=" * 30, "System Information", "=" * 30)
    sys_name = platform.uname()
    print(f"System: {sys_name.system}")
    print(f"Node Name: {sys_name.node}")
    print(f"Release: {sys_name.release}")
    print(f"Version: {sys_name.version}")
    print(f"Machine: {sys_name.machine}")
    print(f"Processor: {sys_name.processor}")

    now_time = datetime.now()
    current_time = now_time.strftime("%H:%M:%S")
    print(current_time)


def boot_info():
    # Get boot date and time
    print("="*33, "BOOT Time", "="*33)
    boot_time_timestamp = psutil.boot_time()
    bt = datetime.fromtimestamp(boot_time_timestamp)
    print(f"Boot time: {bt.day}/{bt.month}/{bt.year} {bt.hour}:{bt.minute}:{bt.second}")


def cpu_info():
    # CPU info
    print("="*34, "CPU Info", "="*34)

    # Get number of Cores\
    print("Physical cores: ", psutil.cpu_count(logical=False))
    print("Threads: ", psutil.cpu_count(logical=True))

    # CPU frequencies
    cpu_frequency = psutil.cpu_freq()
    print(f"Minimum frequency: {cpu_frequency.min:.2f}MHz")
    print(f"Maximum frequency: {cpu_frequency.max:.2f}MHz")
    print(f"Current frequency: {cpu_frequency.current:.2f}MHz")

    # CPU usage
    print("CPU Usage Per Core:")
    for i, percentage in enumerate(psutil.cpu_percent(percpu=True, interval=1)):
        print(f"Core {i}: {percentage}%")
    print(f"Total CPU Usage: {psutil.cpu_percent()}%")

    now_time = datetime.now()
    current_time = now_time.strftime("%H:%M:%S")
    print(current_time)


def mem_info():
    # MEM information
    print("="*30, "Memory Information", "="*30,)

    # get memory details
    sys_mem = psutil.virtual_memory()
    print(f"Total memory: {get_size(sys_mem.total)}")
    print(f"Available memory: {get_size(sys_mem.available)}")
    print(f"Used memory: {get_size(sys_mem.used)}")
    print(f"Percentage memory: {sys_mem.percent}%")

    # get swap memory (if existent)
    swap_mem = psutil.swap_memory()
    print(f"Total swap memory: {get_size(swap_mem.total)}")
    print(f"Free swap memory: {get_size(swap_mem.free)}")
    print(f"Used swap memory: {get_size(swap_mem.used)}")
    print(f"Percentage swap memory: {swap_mem.percent}%")

    now_time = datetime.now()
    current_time = now_time.strftime("%H:%M:%S")
    print(current_time)


def disk_info():
    # DISK usage
    print("="*31, "Disk Information", "="*31)
    print("Partitions and usage:")

    # get all disk partitions
    partitions = psutil.disk_partitions()
    for partitions in partitions:
        print(f"Device: {partitions.device}")
        print(f"Mount-point: {partitions.mountpoint}")
        print(f"File sys type: {partitions.fstype}")
        try:
            partitions_usage = psutil.disk_usage(partitions.mountpoint)
        except PermissionError:
            # can't be cached due to disk that isn't ready
            continue
        print(f"Total size: {get_size(partitions_usage.total)}")
        print(f"Used space: {get_size(partitions_usage.used)}")
        print(f"Free space: {get_size(partitions_usage.free)}")
        print(f"Percentage size: {partitions_usage.percent}%")

    # get IO statistics since boot
    disk_io = psutil.disk_io_counters()
    print(f"Total read: {get_size(disk_io.read_bytes)}")
    print(f"Total write: {get_size(disk_io.write_bytes)}")

    now_time = datetime.now()
    current_time = now_time.strftime("%H:%M:%S")
    print(current_time)


def network_info():
    # Network information
    print("="*30, "Network Information", "="*30)
    # get all network interfaces (virtual and physical)
    net_address = psutil.net_if_addrs()
    for interface_name, interface_addresses in net_address.items():
        for address in interface_addresses:
            print(f"=== Interface: {interface_name} ===")
            if str(address.family) == 'AddressFamily.AF_INET':
                print(f"  IP Address: {address.address}")
                print(f"  Net-mask: {address.netmask}")
                print(f"  Broadcast IP: {address.broadcast}")
            elif str(address.family) == 'AddressFamily.AF_PACKET':
                print(f"  MAC Address: {address.address}")
                print(f"  Net-mask: {address.netmask}")
                print(f"  Broadcast MAC: {address.broadcast}")
    # get IO statistics since boot
    net_io = psutil.net_io_counters()
    print(f"Total Bytes Sent: {get_size(net_io.bytes_sent)}")
    print(f"Total Bytes Received: {get_size(net_io.bytes_recv)}")

    now_time = datetime.now()
    current_time = now_time.strftime("%H:%M:%S")
    print(current_time)


# Frames for categories
system_frame = Frame(notebook_labels)
boot_frame = Frame(notebook_labels)
cpu_frame = Frame(notebook_labels)
memory_frame = Frame(notebook_labels)
disk_frame = Frame(notebook_labels)
network_frame = Frame(notebook_labels)

system_frame.pack(system_info(), fill = "both", expand=1)
boot_frame.pack(boot_info(), fill = "both", expand=1)
cpu_frame.pack(cpu_info(), fill = "both", expand=1)
memory_frame.pack(mem_info(), fill = "both", expand=1)
disk_frame.pack(disk_info(), fill = "both", expand=1)
network_frame.pack(network_info(), fill = "both", expand=1)

notebook_labels.add(system_frame, text="System")
notebook_labels.add(boot_frame, text="Boot")
notebook_labels.add(cpu_frame, text="Cpu")
notebook_labels.add(memory_frame, text="Memory")
notebook_labels.add(disk_frame, text="Disk")
notebook_labels.add(network_frame, text="Network")


pop_update_button = Button(system_frame, text="Update", command=system_info).pack()
pop_update_button = Button(boot_frame, text="Update", command=boot_info).pack()
pop_update_button = Button(cpu_frame, text="Update", command=cpu_info).pack()
pop_update_button = Button(memory_frame, text="Update", command=mem_info).pack()
pop_update_button = Button(disk_frame, text="Update", command=disk_info).pack()
pop_update_button = Button(network_frame, text="Update", command=network_info).pack()

window_box.mainloop()