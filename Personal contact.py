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