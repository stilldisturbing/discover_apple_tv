# Discover Apple TV
[![GitHub release](https://img.shields.io/github/v/release/stilldisturbing/discover_apple_tv?color=orange&label=Current%20Release)]()	[![GitHub license](https://img.shields.io/github/license/stilldisturbing/discover_apple_tv?color=green)]()	

This project is a Python script that uses the `zeroconf` library to discover Apple TV devices on your local network. It retrieves and displays information such as the device name, IP address, model, OS version, and release date. The script also provides an option to save the discovered device information to a CSV file.

## Features

- Discover Apple TV devices on the local network using mDNS.
- Retrieve and display device information including name, IP address, model, OS version, and release date.
- Option to save the discovered device information to a CSV file.

## Requirements

- Python 3.x
- `zeroconf` library
- `csv` library (part of the Python standard library)

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/stilldisturbing/discover_apple_tv.git
   cd discover_apple_tv
   ```

2. Install the required dependencies:

   ```bash
   pip install zeroconf
   ```

## Usage

1. Run the script:

   ```bash
   python discover_apple_tv.py
   ```

2. The script will start listening for Apple TV devices on the local network. When a device is discovered, its information will be displayed on the screen.

3. Press `Enter` to stop listening for devices.

4. You will be prompted to save the discovered device information to a CSV file. Enter `yes` or `y` to save the data, or press `Enter` to skip.

## Example Output

```
Listening for Apple TV devices...

Press Enter to stop listening...

Family Room (192.168.1.10) - Apple TV 4K 1st Gen, iOS: 14.7
Living Room (192.168.1.11) - Apple TV 4th Gen HD, iOS: 13.4

Do you want to write the data to 'Apple TV Devices.csv'? (y/yes / N/NO/Enter): yes
Data has been written to 'Apple TV Devices.csv'.
```

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Contributing

Contributions, enhancements are welcome!

## Acknowledgements

- [zeroconf](https://github.com/grandcat/zeroconf) library for mDNS service discovery.

```
