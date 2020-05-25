count_commands = int(input())
registered_cars = {}

for i in range(count_commands):
    args = input().split()
    command = args[0]
    username = args[1]

    if command == "register":
        license_plate = args[2]
        if username not in registered_cars:
            registered_cars[username] = license_plate
            print(f"{username} registered {license_plate} successfully")
        else:
            print(f"ERROR: already registered with plate number {license_plate}")

    else:
        if username not in registered_cars:
            print(f"ERROR: user {username} not found")
        else:
            print(f"{username} unregistered successfully")
            del registered_cars[username]

[print(f'{key} => {value}') for key, value in registered_cars.items()]