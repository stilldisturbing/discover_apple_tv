from zeroconf import Zeroconf, ServiceBrowser, ServiceStateChange
import socket
import csv
import threading
from os import system, name

# Mapping of Apple TV model numbers to human-readable names and release dates
model_info = {
    "AppleTV1,1": {"name": "Apple TV 1st Gen", "release_date": "2007-03-21"},
    "AppleTV2,1": {"name": "Apple TV 2nd Gen", "release_date": "2010-09-01"},
    "AppleTV3,1": {"name": "Apple TV 3rd Gen", "release_date": "2012-03-07"},
    "AppleTV3,2": {"name": "Apple TV 3rd Gen Rev A", "release_date": "2013-01-28"},
    "AppleTV5,3": {"name": "Apple TV 4th Gen HD", "release_date": "2015-10-30"},
    "AppleTV6,2": {"name": "Apple TV 4K 1st Gen", "release_date": "2017-09-22"},
    "AppleTV11,1": {"name": "Apple TV 4K 2nd Gen", "release_date": "2021-05-21"},
    "AppleTV14,1": {"name": "Apple TV 4K 3rd Gen", "release_date": "2022-11-04"}
}

class MyListener:
    """Custom Zeroconf listener to discover and manage Apple TV devices."""
    def __init__(self):
        # Stores information about discovered Apple TV devices
        self.devices_info = []

    def remove_service(self, zeroconf, type, name):
        """Handles the removal of a service (not implemented in this example)."""
        pass
    
    def update_service(self, zc: Zeroconf, type_: str, name: str) -> None:
        """Handles the update of a service (not implemented in this example)."""
        pass

    def add_service(self, zeroconf, type, name):
        """
        Handles the addition of a new service. Extracts and processes device details
        from TXT records and appends them to the devices_info list.
        """
        info = zeroconf.get_service_info(type, name)
        if info:
            # Decode TXT records to a dictionary
            txt_records = {key.decode('utf-8'): value.decode('utf-8') for key, value in info.properties.items()}
            model = txt_records.get("model", "")
            if model.startswith("AppleTV"):
                device_name = name.replace(type, "").rstrip(".")
                ip = socket.inet_ntoa(info.addresses[0])
                human_readable_model = model_info.get(model, {}).get("name", model)
                release_date = model_info.get(model, {}).get("release_date", "Unknown")
                ios_version = txt_records.get("osvers", "Unknown")
                
                # Store device information in the list
                self.devices_info.append({
                    "Apple TV": device_name,
                    "IP Address": ip,
                    "Model": human_readable_model,
                    "OS Version": ios_version,
                    "Release Date": release_date,
                    #"TXT Records": txt_records
                })
                # Print the discovered information to the screen
                print(f'{device_name} ({ip}) - {human_readable_model}, iOS: {ios_version}')

def wait_for_keypress():
    """
    Waits for the user to press Enter to stop listening for devices.
    Closes Zeroconf and writes the discovered devices to a CSV file.
    """
    input("\nPress Enter to stop listening...\n\n")
    zeroconf.close()
    write_data_to_csv()

def write_data_to_csv():
    """
    Prompts the user to write discovered device information to a CSV file.
    If confirmed, writes data to 'Apple TV Devices.csv'.
    """
    # Make sure we have information to post
    if listener.devices_info:
        output_file = "Apple TV Devices.csv"
        # Check if the user wants to write the data to a CSV file
        write_to_file = input(f"Do you want to write the data to '{output_file}'? (y/yes / N/NO/Enter): ").strip().lower()
        if write_to_file in {'yes', 'y'}:
            with open(output_file, mode='w', newline='') as file:
                writer = csv.DictWriter(
                    file, 
                    fieldnames=listener.devices_info[0].keys(),
                    quotechar='"',
                    quoting=csv.QUOTE_NONNUMERIC
                )
                writer.writeheader()
                for device in listener.devices_info:
                    writer.writerow(device)
            print(f"Data has been written to '{output_file}'.")

if __name__ == "__main__":
    # Clear the terminal screen
    if name == 'nt':
        # For Windows
        _ = system('cls')
    else:
        # For macOS and Linux
        _ = system('clear')
    
    # Initialize Zeroconf for mDNS service discovery
    zeroconf = Zeroconf()
    listener = MyListener()
    
    # Start browsing for AirPlay services
    browser = ServiceBrowser(zeroconf, "_airplay._tcp.local.", listener)

    # Start a thread to wait for user input to stop
    keypress_thread = threading.Thread(target=wait_for_keypress)
    keypress_thread.start()

    print("Listening for Apple TV devices...")
    keypress_thread.join()
