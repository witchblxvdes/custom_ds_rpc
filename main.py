from pypresence.presence import Presence
import time

client_id = "1568281811975545023"

start_time = int(time.time())
details = "Just surfing..."
state = "^_^"
large_image = "mc_winter"
small_image = "mc_view"
buttons = [
    {"label": "GitHub", "url": "https://github.com/witchblxvdes"},
    {"label": "Tap on me ^^", "url": "https://www.youtube.com/watch?v=jirQOGV0L3c"}
]

rpc = Presence(client_id)
rpc.connect()

def update_presence():
    rpc.update(
        details=details,
        state=state,
        large_image=large_image,
        small_image=small_image,
        start=start_time,
        buttons=buttons
    )

while True:
    print("\n1. Change activity")
    print("\n2. Change image")
    print("\n3. Change buttons")
    print("\n4. Show current settings")
    print("\n5. Reset settings")
    print("\n0. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        user_details = input("Enter new details: ")
        user_state = input("Enter new state: ")

        if user_details:
            details = user_details

        if user_state:
            state = user_state

        update_presence()

    elif choice == "2":
        user_large_img = input("Enter new large image key: ")
        user_small_img = input("Enter new small image key: ")

        if user_large_img:
            large_image = user_large_img

        if user_small_img:
            small_image = user_small_img

        update_presence()

    elif choice == "3":
        new_label = input("Enter new label for the first button (Enter to skip): ")
        new_url = input("Enter new URL for the first button (Enter to skip): ")

        if new_label:
            buttons[0]["label"] = new_label

        if new_url:
            buttons[0]["url"] = new_url

        new_label = input("Enter new label for the second button (Enter to skip): ")
        new_url = input("Enter new URL for the second button (Enter to skip): ")

        if new_label:
            buttons[1]["label"] = new_label

        if new_url:
            buttons[1]["url"] = new_url

        update_presence()

    elif choice == "4":
        print(f"Details: {details}")
        print(f"State: {state}")

        for button in buttons:
            print(f"Buttons: {button['label']}")
            print(f"URL: {button['url']}")

    elif choice == "5":
        details = "Just surfing..."
        state = "^_^"

        large_image = "mc_winter"
        small_image = "mc_view"

        buttons = [
            {"label": "GitHub", "url": "https://github.com/witchblxvdes"},
            {"label": "Tap on me ^^", "url": "https://www.youtube.com/watch?v=jirQOGV0L3c"}
        ]

        start_time = int(time.time())

        update_presence()

        print("Settings have been reset!")

    elif choice == "0":
        rpc.close()
        break

    else:
        print("Invalid option. Try again.")