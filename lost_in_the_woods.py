import random

def main():
    print("Welcome to Lost in the Woods!")
    player_location = "start"  # Starting location
    inventory = []  # Player's inventory
    health = 100  # Player's initial health
    resources = {"food": 3, "water": 3}  # Initial resources
    
    while health > 0:
        print("\nYou are currently at:", player_location)
        print("Health:", health)
        print("Resources:", resources)
        print("---------------------------------------------------------")
        print("Choices:")
        print("1. Explore deeper into the woods.")
        print("2. Rest and conserve resources.")
        command = input("Enter a direction (north/south/east/west), 'inventory', or make a choice (1/2): ").strip().lower()

        if command in ["north", "south", "east", "west"]:
            player_location = move_player(player_location, command)
            handle_event(inventory, resources, health)  # Introduce random events and handle inventory/resources
            health -= 10  # Deduct health for each move
        elif command == "inventory":
            print("Inventory:", inventory)
        elif command in ["1", "2"]:
            handle_choice(command, inventory, resources, health)
        else:
            print("Invalid input.")
    
    print("Game over! Your health has dropped to 0.")
    print("You failed to find your way out of the woods.")


def move_player(current_location, direction):
    # Implement logic for moving the player to a new location
    return "New location"


def handle_event(inventory, resources, health):
    # Generate random events
    events = [
        "You encounter a wild animal!",
        "You find an abandoned cabin with a key inside.",
        "You stumble upon a hidden path and find a treasure chest."
    ]
    event = random.choice(events)
    print("\n" + event)

    # Add items to the player's inventory based on the event
    if "key" in event.lower():
        inventory.append("Key")
    elif "treasure chest" in event.lower():
        inventory.append("Treasure")

    # Consume resources based on the event
    if "wild animal" in event.lower():
        if resources["food"] > 0:
            print("You use food to scare away the wild animal.")
            resources["food"] -= 1
        else:
            print("You have no food left to scare away the wild animal. You lose health!")
            health -= 20  # Deduct additional health if no food is available

    # Check for game endings
    if "treasure" in inventory:
        print("Congratulations! You found the treasure and successfully escaped the woods.")
        print("You win!")
        exit()
    elif health <= 0:
        print("Game over! Your health has dropped to 0.")
        print("You failed to find your way out of the woods.")
        exit()


def handle_choice(choice, inventory, resources, health):
    if choice == "1":
        print("You decide to explore deeper into the woods.")
        # Implement consequences for choice 1
        if random.random() < 0.5:
            print("You encounter a dangerous animal and lose health.")
            health -= 30
        else:
            print("You discover a hidden path leading to safety.")
    elif choice == "2":
        print("You decide to rest and conserve resources.")
        # Implement consequences for choice 2
        print("You regain some health and conserve resources.")
        health += 20
        resources["food"] += 1
        resources["water"] += 1
    # Add more choices and consequences as needed


if __name__ == "__main__":
    main()
