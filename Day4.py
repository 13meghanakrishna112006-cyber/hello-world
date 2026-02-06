contacts = {
    "Meghu": "9876543210",
    "Meera": "9123456780",
    "Supriya": "9988776655"
}
# Add a new contact
contacts["Shreya"] = "9012345678"

# Update existing contact's phone number
contacts["Meera"] = "9000000000"
# Existing contact
print("Safe lookup Results:")
print("Lookup Meghu:", contacts.get("Meghu", "Contact not found"))

# Non-existing contact
print("Lookup Rahul:", contacts.get("Rahul", "Contact not found"))
print("\n Contact List:")
for name, phone in contacts.items():
    print(f"Contact: {name} | Phone: {phone}")

raw_logs = ["ID01", "ID02", "ID01", "ID05", "ID02", "ID08", "ID01"]
unique_users = set(raw_logs)
print("Is ID05 a unique user?", "ID05" in unique_users)
print("Total log entries:", len(raw_logs))
print("Unique visitors:", len(unique_users))
print("Unique User IDs:", unique_users) 

friend_a = {"Python", "Cooking", "Hiking", "Movies"}
friend_b = {"Hiking", "Gaming", "Photography", "Python"}
shared_interests = friend_a & friend_b
all_interests = friend_a | friend_b
unique_to_a = friend_a - friend_b
print("Shared Interests:", shared_interests)
print("All Interests:", all_interests)
print("Interests unique to Friend A:", unique_to_a)