def add_setting(my_dict, st_tuple):
    key, value = st_tuple
    key = key.lower()
    value = value.lower()
    if key in my_dict :
        return f"Setting '{key}' already exists! Cannot add a new setting with this name."
    else:
        my_dict[key] = value
        return f"Setting '{key}' added with value '{value}' successfully!"

def update_setting(my_dict, st_tuple):
    key, value = st_tuple
    key = key.lower()
    value = value.lower()
    if key in my_dict:
        my_dict[key] = value
        return f"Setting '{key}' updated to '{value}' successfully!"
    else:
        return f"Setting '{key}' does not exist! Cannot update a non-existing setting."

def delete_setting(my_dict, key):
    key = key.lower()
    if key in my_dict:
        del my_dict[key]
        return f"Setting '{key}' deleted successfully!"
    else:
        return 'Setting not found!'

def view_settings(my_dict):
    if not my_dict:
        return 'No settings available.'
    else:
        output_str = "Current User Settings:\n"
        for key, value in my_dict.items():
            output_str += f"{key.capitalize()}: {value}\n"
        return output_str.strip()


def main():
    user_settings = {
        "theme": "dark",
        "language": "en"
    }
    
    while True:
        print("\n=== User Configuration Manager ===")
        print("1. View Current Settings")
        print("2. Add a New Setting")
        print("3. Update an Existing Setting")
        print("4. Delete a Setting")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ").strip()
        print("-" * 35)
        
        if choice == "1":
            print(view_settings(user_settings))
            
        elif choice == "2":
            key = input("Enter setting name (key): ").strip()
            value = input("Enter setting value: ").strip()
            result = add_setting(user_settings, (key, value))
            print(result)
            
        elif choice == "3":
            key = input("Enter setting name to update: ").strip()
            value = input("Enter new value: ").strip()
            result = update_setting(user_settings, (key, value))
            print(result)
            
        elif choice == "4":
            key = input("Enter setting name to delete: ").strip()
            result = delete_setting(user_settings, key)
            print(result)
            
        elif choice == "5":
            print("Exiting User Configuration Manager. Goodbye!")
            break
            
        else:
            print("Invalid choice! Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()