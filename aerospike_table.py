import aerospike


config = {
    'hosts': [('127.0.0.1', 4000)]  
}

# Connect to Aerospike
try:
    client = aerospike.client(config).connect()
    print("Connected to Aerospike!")
except Exception as e:
    print(f"Connection failed: {e}")
    exit(1)

# Define the namespace, set, and key
namespace = "test"  # Default namespace in Aerospike
set_name = "user_signups"
user_id = "user123"  # This will be the Primary Key (PK)

key = (namespace, set_name, user_id)  # (namespace, set, primary key)

# Define the record (bins)
user_signups = {
    "first_sesh": "2024-05-02T11:22:22Z",  
    "sign_up": "2024-05-02T11:22:22Z",     
    "is_signed": False,                    
    "is_usage": False,                     
    "is_logged_in": False,                 
    "sent_push_2": False,                  
    "sent_card_1a": False,                 
    "sent_push_3": False,                  
    "sent_email_4a": False,                
    "sent_email_4b": False,                
    "sent_email_5": False    
}

# Insert the record into Aerospike
try:
    client.put(key, user_signups)
    print(f"Record inserted into {namespace}.{set_name} with key: {user_id}")
except Exception as e:
    print(f"Error inserting record: {e}")

# Fetch and display the record to confirm insertion
try:
    (key, metadata, record) = client.get(key)
    print("Fetched record:", record)
except Exception as e:
    print(f"Error fetching record: {e}")

# Close the Aerospike connection
client.close()
