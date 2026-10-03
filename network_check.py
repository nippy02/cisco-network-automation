import json


def load_inventory():
    try:
        with open("inventory.json", "r") as file:
            return json.load(file)

    except FileNotFoundError:
        print("Error: inventory.json was not found.")
        return []

    except json.JSONDecodeError:
        print("Error: inventory.json contains invalid JSON.")
        return []


def check_devices(devices):
    results = []

    print("========== NETWORK AUTOMATION CHECK ==========")

    for device in devices:
        try:
            hostname = device["hostname"]
            ip = device["ip"]
            status = device["simulated_status"]

            print(f"{hostname:<10} {ip:<16} Status: {status}")

            results.append({
                "hostname": hostname,
                "ip": ip,
                "device_type": device["device_type"],
                "location": device["location"],
                "status": status
            })

        except KeyError as error:
            print(f"Missing device information: {error}")

    return results


def save_results(results):
    try:
        with open("output.json", "w") as file:
            json.dump(results, file, indent=4)

        print("\nResults successfully saved to output.json.")

    except IOError as error:
        print(f"Unable to save results: {error}")


devices = load_inventory()

if devices:
    results = check_devices(devices)
    save_results(results)
else:
    print("No devices available to check.")