import wmi
from datetime import datetime
import time

print("This was made by PotatoIsCool if this closes without you closing it please tell me and I will try to fix it.")

time.sleep(5)

def get_disk_serial_numbers():
    try:
        c = wmi.WMI()
        disks = c.Win32_DiskDrive()
        serial_numbers = []
        for disk in disks:
            serial_numbers.append(disk.SerialNumber.strip())
        return serial_numbers
    except:
        return "N/A"

def get_bios_serial_number():
    try:
        c = wmi.WMI()
        bios = c.Win32_BIOS()[0]
        return bios.SerialNumber.strip()
    except:
        return "N/A"

def get_cpu_serial_number():
    try:
        c = wmi.WMI()
        cpu = c.Win32_Processor()[0]
        return cpu.ProcessorID.strip()
    except:
        return "N/A"

def get_baseboard_serial_number():
    try:
        c = wmi.WMI()
        baseboard = c.Win32_BaseBoard()[0]
        return baseboard.SerialNumber.strip()
    except:
        return "N/A"

def get_memory_chip_serial_numbers():
    try:
        c = wmi.WMI()
        memory_modules = c.Win32_PhysicalMemory()
        serial_numbers = []
        for memory in memory_modules:
            serial_numbers.append(memory.SerialNumber.strip())
        return serial_numbers
    except:
        return "N/A"

def get_monitor_information():
    try:
        c = wmi.WMI()
        monitors = c.Win32_DesktopMonitor()
        information = []
        for monitor in monitors:
            information.append(monitor.Name)
        return information
    except:
        return "N/A"

def get_network_adapter_mac_addresses():
    try:
        c = wmi.WMI()
        adapters = c.Win32_NetworkAdapterConfiguration(IPEnabled=True)
        mac_addresses = []
        for adapter in adapters:
            mac_addresses.append(adapter.MACAddress)
        return mac_addresses
    except:
        return "N/A"

def get_printer_information():
    try:
        c = wmi.WMI()
        printers = c.Win32_Printer()
        information = []
        for printer in printers:
            information.append(printer.Name)
        return information
    except:
        return "N/A"

def get_sound_device_information():
    try:
        c = wmi.WMI()
        sound_devices = c.Win32_SoundDevice()
        information = []
        for device in sound_devices:
            information.append(device.Name)
        return information
    except:
        return "N/A"

def get_usb_controller_information():
    try:
        c = wmi.WMI()
        controllers = c.Win32_USBController()
        information = []
        for controller in controllers:
            information.append(controller.Name)
        return information
    except:
        return "N/A"

def get_graphics_card_description():
    try:
        c = wmi.WMI()
        cards = c.Win32_VideoController()
        descriptions = []
        for card in cards:
            descriptions.append(card.Description)
        return descriptions
    except:
        return "N/A"

def get_cpu_name():
    try:
        c = wmi.WMI()
        cpu = c.Win32_Processor()[0]
        return cpu.Name.strip()
    except:
        return "N/A"

def get_logical_disk_serial_numbers():
    try:
        c = wmi.WMI()
        disks = c.Win32_LogicalDisk()
        serial_numbers = []
        for disk in disks:
            serial_numbers.append(disk.VolumeSerialNumber.strip())
        return serial_numbers
    except:
        return "N/A"

def get_network_adapter_ip_addresses():
    try:
        c = wmi.WMI()
        adapters = c.Win32_NetworkAdapterConfiguration(IPEnabled=True)
        ip_addresses = []
        for adapter in adapters:
            ip_addresses.extend(adapter.IPAddress)
        return ip_addresses
    except:
        return "N/A"

def get_network_interface_controller_information():
    try:
        c = wmi.WMI()
        interfaces = c.Win32_NetworkAdapter()
        information = []
        for interface in interfaces:
            information.append(interface.Name)
        return information
    except:
        return "N/A"

def get_printer_device_ids():
    try:
        c = wmi.WMI()
        printers = c.Win32_Printer()
        device_ids = []
        for printer in printers:
            device_ids.append(printer.DeviceID)
        return device_ids
    except:
        return "N/A"

def get_ide_controller_device_ids():
    try:
        c = wmi.WMI()
        controllers = c.Win32_IDEController()
        device_ids = []
        for controller in controllers:
            device_ids.append(controller.DeviceID)
        return device_ids
    except:
        return "N/A"

def get_physical_media_serial_numbers():
    try:
        c = wmi.WMI()
        media = c.Win32_PhysicalMedia()
        serial_numbers = []
        for item in media:
            serial_numbers.append(item.SerialNumber.strip())
        return serial_numbers
    except:
        return "N/A"

def get_processor_id():
    try:
        c = wmi.WMI()
        processors = c.Win32_Processor()
        processor_id = processors[0].ProcessorID.strip()
        return processor_id
    except:
        return "N/A"

def get_installed_products():
    try:
        c = wmi.WMI()
        products = c.Win32_Product()
        installed_products = []
        for product in products:
            installed_products.append(product.Name)
        return installed_products
    except:
        return "N/A"

def get_operating_system_serial_number():
    try:
        c = wmi.WMI()
        os = c.Win32_OperatingSystem()[0]
        return os.SerialNumber.strip()
    except:
        return "N/A"

def get_computer_name():
    try:
        return wmi.WMI().Win32_ComputerSystem()[0].Name
    except:
        return "N/A"

def get_efi_number():
    try:
        c = wmi.WMI()
        efi = c.Win32_ComputerSystem()[0]
        try:
            return efi.CurrentEFIVersion.strip()
        except AttributeError:
            return "N/A"
    except:
        return "N/A"

def get_smbios_number():
    try:
        c = wmi.WMI()
        smbios = c.Win32_ComputerSystem()[0]
        try:
            return smbios.SMBIOSBIOSVersion.strip()
        except AttributeError:
            return "N/A"
    except:
        return "N/A"

def get_system_uuid():
    try:
        c = wmi.WMI()
        computersystem = c.Win32_ComputerSystem()[0]
        try:
            return computersystem.UUID
        except AttributeError:
            return "N/A" 
    except:
        return "N/A"

def get_system_manufacturer():
    try:
        c = wmi.WMI()
        computersystem = c.Win32_ComputerSystem()[0]
        return computersystem.Manufacturer
    except:
        return "N/A"

def get_system_model():
    try:
        c = wmi.WMI()
        computersystem = c.Win32_ComputerSystem()[0]
        return computersystem.Model
    except:
        return "N/A"

def get_system_type():
    try:
        c = wmi.WMI()
        computersystem = c.Win32_ComputerSystem()[0]
        return computersystem.SystemType
    except:
        return "N/A"

def get_system_family():
    try:
        c = wmi.WMI()
        computersystem = c.Win32_ComputerSystem()[0]
        return computersystem.SystemFamily
    except:
        return "N/A"

def get_system_processor_cores():
    try:
        c = wmi.WMI()
        processors = c.Win32_Processor()
        total_cores = 0
        for processor in processors:
            total_cores += processor.NumberOfCores
        return total_cores
    except:
        return "N/A"

def get_system_processor_threads():
    try:
        c = wmi.WMI()
        processors = c.Win32_Processor()
        total_threads = 0
        for processor in processors:
            total_threads += processor.NumberOfLogicalProcessors
        return total_threads
    except:
        return "N/A"

def get_system_operating_system():
    try:
        c = wmi.WMI()
        operating_systems = c.Win32_OperatingSystem()
        operating_system = operating_systems[0]
        return operating_system.Caption.strip()
    except:
        return "N/A"

def get_system_total_physical_memory():
    try:
        c = wmi.WMI()
        computersystem = c.Win32_ComputerSystem()[0]
        return computersystem.TotalPhysicalMemory
    except:
        return "N/A"

def get_system_total_virtual_memory():
    try:
        c = wmi.WMI()
        operating_systems = c.Win32_OperatingSystem()
        operating_system = operating_systems[0]
        return operating_system.TotalVirtualMemorySize
    except:
        return "N/A"

def get_system_available_physical_memory():
    try:
        c = wmi.WMI()
        operating_systems = c.Win32_OperatingSystem()
        operating_system = operating_systems[0]
        return operating_system.FreePhysicalMemory
    except:
        return "N/A"

def get_system_available_virtual_memory():
    try:
        c = wmi.WMI()
        operating_systems = c.Win32_OperatingSystem()
        operating_system = operating_systems[0]
        return operating_system.FreeVirtualMemory
    except:
        return "N/A"

def get_system_up_time():
    try:
        c = wmi.WMI()
        operating_systems = c.Win32_OperatingSystem()
        operating_system = operating_systems[0]
        last_boot_time = parse_wmi_date(operating_system.LastBootUpTime)
        current_time = parse_wmi_date(operating_system.LocalDateTime)
        up_time = current_time - last_boot_time
        return up_time
    except:
        return "N/A"

def parse_wmi_date(date_str):
    try:
        date_str = date_str.split(".")[0]
        return datetime.strptime(date_str, "%Y%m%d%H%M%S")
    except:
        return None

def get_system_boot_device():
    try:
        c = wmi.WMI()
        computersystem = c.Win32_ComputerSystem()[0]
        try:
            return computersystem.BootDevice
        except AttributeError:
            return "N/A" 
    except:
        return "N/A"

def get_system_timezone():
    try:
        c = wmi.WMI()
        operating_systems = c.Win32_OperatingSystem()
        operating_system = operating_systems[0]
        return operating_system.CurrentTimeZone
    except:
        return "N/A"

def get_system_domain():
    try:
        c = wmi.WMI()
        computersystem = c.Win32_ComputerSystem()[0]
        return computersystem.Domain
    except:
        return "N/A"

def get_system_logged_in_users():
    try:
        c = wmi.WMI()
        processes = c.Win32_Process()
        logged_in_users = []
        for process in processes:
            if process.Name == "explorer.exe":
                owner = process.GetOwner()
                if owner:
                    user = owner[2]
                    logged_in_users.append(user)
        return logged_in_users
    except:
        return "N/A"

def get_system_process_count():
    try:
        c = wmi.WMI()
        processes = c.Win32_Process()
        return len(processes)
    except:
        return "N/A"

def get_system_service_count():
    try:
        c = wmi.WMI()
        services = c.Win32_Service()
        return len(services)
    except:
        return "N/A"

def get_system_process_list():
    try:
        c = wmi.WMI()
        processes = c.Win32_Process()
        process_list = []
        for process in processes:
            process_list.append(process.Name)
        return process_list
    except:
        return "N/A"

def get_system_service_list():
    try:
        c = wmi.WMI()
        services = c.Win32_Service()
        service_list = []
        for service in services:
            service_list.append(service.Name)
        return service_list
    except:
        return "N/A"

def get_system_last_boot_time():
    try:
        c = wmi.WMI()
        operating_systems = c.Win32_OperatingSystem()
        operating_system = operating_systems[0]
        return operating_system.LastBootUpTime
    except:
        return "N/A"

def get_system_battery_status():
    try:
        c = wmi.WMI()
        batteries = c.Win32_Battery()
        status = []
        for battery in batteries:
            status.append({
                "Name": battery.Name,
                "Status": battery.Status,
                "EstimatedChargeRemaining": battery.EstimatedChargeRemaining,
                "EstimatedRunTime": battery.EstimatedRunTime
            })
        return status
    except:
        return "N/A"

def get_system_logical_processors():
    try:
        c = wmi.WMI()
        processors = c.Win32_Processor()
        logical_processors = 0
        for processor in processors:
            logical_processors += processor.NumberOfLogicalProcessors
        return logical_processors
    except:
        return "N/A"

def get_system_installed_programs():
    try:
        c = wmi.WMI()
        programs = c.Win32_Product()
        installed_programs = []
        for program in programs:
            installed_programs.append(program.Name)
        return installed_programs
    except:
        return "N/A"

def get_system_network_interface_list():
    try:
        c = wmi.WMI()
        interfaces = c.Win32_NetworkAdapter()
        interface_list = []
        for interface in interfaces:
            interface_list.append(interface.Name)
        return interface_list
    except:
        return "N/A"

def get_system_logical_disk_free_space(drive):
    try:
        c = wmi.WMI()
        logical_disks = c.Win32_LogicalDisk()
        for disk in logical_disks:
            if disk.DeviceID == drive:
                return disk.FreeSpace
        return "N/A"
    except:
        return "N/A"

def get_system_logical_disk_total_size(drive):
    try:
        c = wmi.WMI()
        logical_disks = c.Win32_LogicalDisk()
        for disk in logical_disks:
            if disk.DeviceID == drive:
                return disk.Size
        return "N/A"
    except:
        return "N/A"

def get_system_logical_disk_file_system(drive):
    try:
        c = wmi.WMI()
        logical_disks = c.Win32_LogicalDisk()
        for disk in logical_disks:
            if disk.DeviceID == drive:
                return disk.FileSystem
        return "N/A"
    except:
        return "N/A"

def get_system_logical_disk_drive_type(drive):
    try:
        c = wmi.WMI()
        logical_disks = c.Win32_LogicalDisk()
        for disk in logical_disks:
            if disk.DeviceID == drive:
                return disk.DriveType
        return "N/A"
    except:
        return "N/A"

def get_network_adapter_speeds():
    try:
        c = wmi.WMI()
        adapters = c.Win32_NetworkAdapter()
        speeds = []
        for adapter in adapters:
            speeds.append(adapter.Speed)
        return speeds
    except:
        return "N/A"

def get_system_bios_version():
    try:
        c = wmi.WMI()
        bios = c.Win32_BIOS()
        try:
            return bios[0].SMBIOSBIOSVersion.strip()
        except (AttributeError, IndexError):
            return "N/A"
    except:
        return "N/A"

def get_cpu_architecture():
    try:
        c = wmi.WMI()
        processors = c.Win32_Processor()
        architectures = []
        for processor in processors:
            architectures.append(processor.Architecture)
        return architectures
    except:
        return "N/A"

def get_motherboard_manufacturer():
    try:
        c = wmi.WMI()
        baseboard = c.Win32_BaseBoard()[0]
        return baseboard.Manufacturer.strip()
    except:
        return "N/A"

def get_motherboard_model():
    try:
        c = wmi.WMI()
        baseboard = c.Win32_BaseBoard()[0]
        return baseboard.Product.strip()
    except:
        return "N/A"

def get_system_domain_role():
    try:
        c = wmi.WMI()
        computersystem = c.Win32_ComputerSystem()[0]
        return computersystem.DomainRole
    except:
        return "N/A"

def get_system_domain():
    try:
        c = wmi.WMI()
        computersystem = c.Win32_ComputerSystem()[0]
        return computersystem.Domain
    except:
        return "N/A"

def get_system_dns_host_name():
    try:
        c = wmi.WMI()
        computersystem = c.Win32_ComputerSystem()[0]
        return computersystem.DNSHostName.strip()
    except:
        return "N/A"

def get_system_last_user_logged_on():
    try:
        c = wmi.WMI()
        computersystem = c.Win32_ComputerSystem()[0]
        return computersystem.UserName
    except:
        return "N/A"

def get_system_keyboard_layout():
    try:
        c = wmi.WMI()
        keyboard = c.Win32_Keyboard()[0]
        return keyboard.Layout
    except:
        return "N/A"

def get_system_time_zone():
    try:
        c = wmi.WMI()
        timezone = c.Win32_TimeZone()[0]
        return timezone.StandardName
    except:
        return "N/A"

def get_system_language():
    try:
        c = wmi.WMI()
        operating_systems = c.Win32_OperatingSystem()
        operating_system = operating_systems[0]
        return operating_system.OSLanguage
    except:
        return "N/A"

def get_system_power_plan():
    try:
        c = wmi.WMI()
        power_plans = c.Win32_PowerPlan()
        active_plan = None
        for plan in power_plans:
            if plan.IsActive:
                active_plan = plan.ElementName
                break
        return active_plan
    except:
        return "N/A"

def get_system_architecture():
    try:
        c = wmi.WMI()
        operating_systems = c.Win32_OperatingSystem()
        operating_system = operating_systems[0]
        return operating_system.OSArchitecture
    except:
        return "N/A"

def get_system_environment_variables():
    try:
        c = wmi.WMI()
        environment_variables = c.Win32_Environment()
        variables = []
        for variable in environment_variables:
            variables.append({
                "Name": variable.Name,
                "Value": variable.VariableValue
            })
        return variables
    except:
        return "N/A"

def get_system_hotfixes():
    try:
        c = wmi.WMI()
        hotfixes = c.Win32_QuickFixEngineering()
        patch_list = []
        for hotfix in hotfixes:
            patch_list.append(hotfix.HotFixID)
        return patch_list
    except:
        return "N/A"

def get_system_startup_programs():
    try:
        c = wmi.WMI()
        startup_programs = c.Win32_StartupCommand()
        programs = []
        for program in startup_programs:
            programs.append(program.Caption)
        return programs
    except:
        return "N/A"

def get_system_firewall_status():
    try:
        c = wmi.WMI()
        firewall_service = c.Win32_Service(Name="MpsSvc")
        if firewall_service:
            return firewall_service[0].State
        return "N/A"
    except:
        return "N/A"

def get_motherboard_manufacturer():
    try:
        c = wmi.WMI()
        baseboard = c.Win32_BaseBoard()[0]
        return baseboard.Manufacturer.strip()
    except:
        return "N/A"

def get_motherboard_model():
    try:
        c = wmi.WMI()
        baseboard = c.Win32_BaseBoard()[0]
        return baseboard.Product.strip()
    except:
        return "N/A"

def get_system_domain_role():
    try:
        c = wmi.WMI()
        computersystem = c.Win32_ComputerSystem()[0]
        return computersystem.DomainRole
    except:
        return "N/A"

def get_system_domain():
    try:
        c = wmi.WMI()
        computersystem = c.Win32_ComputerSystem()[0]
        return computersystem.Domain
    except:
        return "N/A"

def get_system_dns_host_name():
    try:
        c = wmi.WMI()
        computersystem = c.Win32_ComputerSystem()[0]
        return computersystem.DNSHostName.strip()
    except:
        return "N/A"

drive_letter = "C:"
up_time = get_system_up_time()

def p1():
    if __name__ == "__main__":
        print("Disk Serial Numbers:", get_disk_serial_numbers())
        print("BIOS Serial Number:", get_bios_serial_number())
        print("CPU Serial Number:", get_cpu_serial_number())
        print("Baseboard Serial Number:", get_baseboard_serial_number())
        print("Memory Chip Serial Numbers:", get_memory_chip_serial_numbers())
        print("Desktop Monitor Information:", get_monitor_information())
        print("Network Adapter MAC Addresses:", get_network_adapter_mac_addresses())
        print("Printer Information:", get_printer_information())
        print("Sound Device Information:", get_sound_device_information())
        print("USB Controller Information:", get_usb_controller_information())
        print("Graphics Card Description:", get_graphics_card_description())
        print("CPU Name:", get_cpu_name())
        print("Logical Disk Serial Numbers:", get_logical_disk_serial_numbers())
        print("Network Adapter IP Addresses:", get_network_adapter_ip_addresses())
        print("Network Interface Controller (NIC) Information:", get_network_interface_controller_information())
        print("Printer Device IDs:", get_printer_device_ids())
        print("IDE Controller Device IDs:", get_ide_controller_device_ids())
        print("Physical Media Serial Numbers:", get_physical_media_serial_numbers())
        print("Processor ID:", get_processor_id())
        print("Operating System Serial Number:", get_operating_system_serial_number())
        print("Computer Name:", get_computer_name())
        print("EFI Number:", get_efi_number())
        print("SMBIOS Number:", get_smbios_number())
        print("System UUID:", get_system_uuid())
        print("System Manufacturer:", get_system_manufacturer())
        print("System Model:", get_system_model())
        print("System Type:", get_system_type())
        print("System Family:", get_system_family())
        print("System Processor Cores:", get_system_processor_cores())
        print("System Processor Threads:", get_system_processor_threads())
        print("System Operating System:", get_system_operating_system())
        print("System Total Physical Memory:", get_system_total_physical_memory())
        print("System Total Virtual Memory:", get_system_total_virtual_memory())
        print("System Available Physical Memory:", get_system_available_physical_memory())
        print("System Available Virtual Memory:", get_system_available_virtual_memory())
        print("System Up Time:", get_system_up_time())
        print("System Boot Device:", get_system_boot_device())
        print("System Timezone:", get_system_timezone())
        print("System Domain:", get_system_domain())
        print("System Logged In Users:", get_system_logged_in_users())
        print("System Process Count:", get_system_process_count())
        print("System Service Count:", get_system_service_count())
        print("System Last Boot Time:", get_system_last_boot_time())
        print("System Battery Status:", get_system_battery_status())
        print("System Logical Processors:", get_system_logical_processors())
        print("System Network Interface List:", get_system_network_interface_list())
        print("System Logical Disk Free Space ({}):".format(drive_letter), get_system_logical_disk_free_space(drive_letter))
        print("System Logical Disk Total Size ({}):".format(drive_letter), get_system_logical_disk_total_size(drive_letter))
        print("System Logical Disk File System ({}):".format(drive_letter), get_system_logical_disk_file_system(drive_letter))
        print("System Logical Disk Drive Type ({}):".format(drive_letter), get_system_logical_disk_drive_type(drive_letter))
        print("Motherboard Manufacturer:", get_motherboard_manufacturer())
        print("Motherboard Model:", get_motherboard_model())
        print("System Domain Role:", get_system_domain_role())
        print("System Domain:", get_system_domain())
        print("System DNS Host Name:", get_system_dns_host_name())
        print("Network Adapter Speeds:", get_network_adapter_speeds())
        print("System BIOS Version:", get_system_bios_version())
        print("CPU Architectures:", get_cpu_architecture())
        print("Motherboard Manufacturer:", get_motherboard_manufacturer())
        print("Motherboard Model:", get_motherboard_model())
        print("System Domain Role:", get_system_domain_role())
        print("System Domain:", get_system_domain())
        print("System DNS Host Name:", get_system_dns_host_name())
        print("System Architecture:", get_system_architecture())
        print("System Environment Variables:", get_system_environment_variables())
        print("System Hotfixes/Patches:", get_system_hotfixes())
        print("System Startup Programs:", get_system_startup_programs())
        print("System Firewall Status:", get_system_firewall_status())
        print("System Last User Logged On:", get_system_last_user_logged_on())
        print("System Keyboard Layout:", get_system_keyboard_layout())
        print("System Time Zone:", get_system_time_zone())
        print("System Language:", get_system_language())
        print("System Power Plan:", get_system_power_plan())
        input("This was made by PotatoIsCool and press enter to exit...")

p1()