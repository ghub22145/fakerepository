"""
Monster Card Catalogue Program
This program allows users to manage a catalogue of monster cards for a game.
Users can store, add, search, update, delete, and print monster cards.
"""

monster_catalogue = {
    "Hobgoblin": {"strength": 7, "speed": 1, "stealth": 25, "cunning": 15},
    "Sasquatch": {"strength": 1, "speed": 6, "stealth": 21, "cunning": 19},
    "Godzilla": {"strength": 5, "speed": 15, "stealth": 18, "cunning": 22},
    "Blazegolem": {"strength": 15, "speed": 20, "stealth": 23, "cunning": 6},
    "Websnake": {"strength": 7, "speed": 15, "stealth": 10, "cunning": 5},
    "Demogorgon": {"strength": 21, "speed": 18, "stealth": 14, "cunning": 5},
    "Dracula": {"strength": 19, "speed": 13, "stealth": 19, "cunning": 2},
    "Mindflayer": {"strength": 16, "speed": 7, "stealth": 4, "cunning": 12}
}

def display_menu():
    """Display the main menu and get user choice"""
    print("\nMONSTER CARD CATALOGUE MENU")
    print("1. Add a new monster card")
    print("2. Search for a monster card")
    print("3. Update a monster card")
    print("4. Delete a monster card")
    print("5. Print all monster cards")
    print("6. Exit")
    
    while True:
        try:
            choice = int(input("Enter your choice (1-6): "))
            if 1 <= choice <= 6:
                return choice
            else:
                print("Please enter a number between 1 and 6.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def get_valid_stat(stat_name):
    """Get a valid stat value (1-25) from the user"""
    while True:
        try:
            value = int(input(f"Enter {stat_name} (1-25): "))
            if 1 <= value <= 25:
                return value
            else:
                print("Value must be between 1 and 25.")
        except ValueError:
            print("Please enter a valid number.")

def add_monster():
    """Add a new monster card to the catalogue"""
    print("\nADD NEW MONSTER CARD")
    
    while True:
        name = input("Enter monster name: ").strip()
        if not name:
            print("Monster name cannot be empty.")
            continue
        if name in monster_catalogue:
            print("This monster already exists in the catalogue.")
            choice = input("Do you want to update it instead? (y/n): ").lower()
            if choice == 'y':
                update_monster(name)
                return
            else:
                continue
        break
    
    print("Enter the monster's stats:")
    strength = get_valid_stat("strength")
    speed = get_valid_stat("speed")
    stealth = get_valid_stat("stealth")
    cunning = get_valid_stat("cunning")
    
    monster_catalogue[name] = {
        "strength": strength,
        "speed": speed,
        "stealth": stealth,
        "cunning": cunning
    }
    
    print("\nNew monster card added:")
    display_monster(name, monster_catalogue[name])
    
    confirm = input("Is this correct? (y/n): ").lower()
    if confirm != 'y':
        # Allow user to make changes
        updated_stats = update_monster_stats(name, monster_catalogue[name])
        monster_catalogue[name] = updated_stats

def search_monster():
    """Search for a monster card in the catalogue"""
    print("\nSEARCH FOR MONSTER CARD")
    name = input("Enter monster name to search: ").strip()
    
    if name in monster_catalogue:
        print("\nMonster found:")
        display_monster(name, monster_catalogue[name])
    else:
        print(f"Monster '{name}' not found in the catalogue.")

def update_monster(name=None):
    """Update an existing monster card"""
    if name is None:
        print("\nUPDATE MONSTER CARD")
        name = input("Enter monster name to update: ").strip()
    
    if name in monster_catalogue:
        print("\nCurrent monster details:")
        display_monster(name, monster_catalogue[name])
        
        monster_catalogue[name] = update_monster_stats(name, monster_catalogue[name])
        print("\nUpdated monster details:")
        display_monster(name, monster_catalogue[name])
    else:
        print(f"Monster '{name}' not found in the catalogue.")

def update_monster_stats(name, stats):
    """Helper function to update monster stats"""
    print("\nEnter new stats (press Enter to keep current value):")
    
    new_stats = {}
    for stat, value in stats.items():
        while True:
            new_value = input(f"{stat} (current: {value}): ").strip()
            if not new_value:
                new_stats[stat] = value
                break
            try:
                new_value = int(new_value)
                if 1 <= new_value <= 25:
                    new_stats[stat] = new_value
                    break
                else:
                    print("Value must be between 1 and 25.")
            except ValueError:
                print("Please enter a valid number.")
    
    return new_stats

def delete_monster():
    """Delete a monster card from the catalogue"""
    print("\nDELETE MONSTER CARD")
    name = input("Enter monster name to delete: ").strip()
    
    if name in monster_catalogue:
        print("\nMonster to be deleted:")
        display_monster(name, monster_catalogue[name])
        
        confirm = input("Are you sure you want to delete this monster? (y/n): ").lower()
        if confirm == 'y':
            del monster_catalogue[name]
            print(f"Monster '{name}' has been deleted.")
    else:
        print(f"Monster '{name}' not found in the catalogue.")

def print_catalogue():
    """Print all monster cards in the catalogue"""
    print("\nMONSTER CARD CATALOGUE")
    print("-" * 60)
    print(f"{'Name':<15} {'Strength':<10} {'Speed':<10} {'Stealth':<10} {'Cunning':<10}")
    print("-" * 60)
    
    for name, stats in sorted(monster_catalogue.items()):
        print(f"{name:<15} {stats['strength']:<10} {stats['speed']:<10} {stats['stealth']:<10} {stats['cunning']:<10}")
    
    print("-" * 60)
    print(f"Total monsters in catalogue: {len(monster_catalogue)}")
    print("-" * 60)

def display_monster(name, stats):
    """Display a single monster card in a formatted way"""
    print("-" * 40)
    print(f"Monster: {name}")
    print(f"Strength: {stats['strength']}")
    print(f"Speed:    {stats['speed']}")
    print(f"Stealth:  {stats['stealth']}")
    print(f"Cunning:  {stats['cunning']}")
    print("-" * 40)

def main():
    """Main program loop"""
    print("WELCOME TO THE MONSTER CARD CATALOGUE")
    
    while True:
        choice = display_menu()
        
        if choice == 1:
            add_monster()
        elif choice == 2:
            search_monster()
        elif choice == 3:
            update_monster()
        elif choice == 4:
            delete_monster()
        elif choice == 5:
            print_catalogue()
        elif choice == 6:
            print("Exiting the Monster Card. Goodbye!")
            break

if __name__ == "__main__":
    main()