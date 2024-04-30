import re

access_database = {}
resource_permissions = {"F": ["READ", "WRITE", "RUN", "OWN", "ACCESS"], "P": ["OPEN", "STOP"], "D": ["ACCESS", "SEARCH"],
                        "DB": ["READ", "WRITE", "OWN", "ACCESS", "SEARCH"], "DEVICE": ["RUN", "STOP"]}

while True:
    print("ACCESS CONTROL")
    print("1. GRANT")
    print("2. REVOKE")
    print("3. CHECK")
    print("4. EXIT")

    user_choice = int(input("Choose your option: "))

    if user_choice == 1:  
        resource_id = input("Enter resource ID: ")
        key_list = list(access_database.keys())

        if resource_id not in key_list:
            access_database[resource_id] = []
        
        user_id = input("Enter user ID: ")
        
        
        user_exists = False
        for user_info in access_database[resource_id]:
            if user_id == user_info[0]:
                user_exists = True
                user_permissions = user_info[1]
                print("User ID already exists. Existing permissions:", user_permissions)
                break
        
        if not user_exists:
            user_permissions = []
        
        r = re.sub('[0-9]', '', resource_id)
        print("Permissions for: " + r)

        for permission in resource_permissions[r]:
            print(permission)

        while True:
            new_permission = input("Enter Permission: ")

            if new_permission not in resource_permissions[r]:
                print("Permission not available")
                continue

            if new_permission in user_permissions:
                print("Permission already exists for user ID:", user_id)
            else:
                user_permissions.append(new_permission)
                print("Permissions updated for user ID:", user_id)
                print("New permissions:", user_permissions)

            y_n = input("Do you want to enter another permission (y/n): ")

            if y_n == "y":
                continue
            else:
                break

        
        if user_exists:
            for user_info in access_database[resource_id]:
                if user_id == user_info[0]:
                    user_info[1] = user_permissions
        else:
            access_database[resource_id].append([user_id, user_permissions])

        print("Access database:", access_database)

    elif user_choice == 2:  
        resource_id = input("Enter resource ID: ")
        key_list = list(access_database.keys())

        if resource_id not in key_list:
            print("Resource ID not found.")
            continue
        
        user_id = input("Enter user ID: ")
        
        user_found = False
        for user_info in access_database[resource_id]:
            if user_id == user_info[0]:
                user_found = True
                user_permissions = user_info[1]
                print("Permissions for user ID:", user_id)
                print(user_permissions)
                break
        
        if not user_found:
            print("User ID not found for the given resource.")
            continue
        
        while True:
            permission_to_revoke = input("Enter Permission to revoke: ")
            if permission_to_revoke not in user_permissions:
                print("Permission not found for user ID:", user_id)
                break
            else:
                user_permissions.remove(permission_to_revoke)
                print("Permission revoked for user ID:", user_id)
                print("Updated permissions:", user_permissions)

            y_n = input("Do you want to revoke another permission (y/n): ")

            if y_n == "y":
                continue
            else:
                break

        
        for user_info in access_database[resource_id]:
            if user_id == user_info[0]:
                user_info[1] = user_permissions

        print("Access database:", access_database)

    elif user_choice == 3:  
        resource_id = input("Enter resource ID: ")
        key_list = list(access_database.keys())

        if resource_id not in key_list:
            print("Resource ID not found.")
            continue
        
        user_id = input("Enter user ID: ")
        
        user_found = False
        for user_info in access_database[resource_id]:
            if user_id == user_info[0]:
                user_found = True
                user_permissions = user_info[1]
                print("Permissions for user ID:", user_id)
                print(user_permissions)
                break
        
        if not user_found:
            print("User ID not found for the given resource.")

        permission_to_check = input("Enter Permission to check: ")
        if user_found and permission_to_check in user_permissions:
            print("Permission", permission_to_check, "is granted to user ID:", user_id)
            continue
        else:
            print("Permission", permission_to_check, "is not granted to user ID:", user_id)
            continue

    elif user_choice == 4:
        break

    else:
        print("Invalid option. Please choose a valid option.")
