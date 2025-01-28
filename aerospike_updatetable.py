import aerospike
from aerospike import exception

# Connect to Aerospike cluster
client = aerospike.client({
    'hosts': [('127.0.0.1', 4000)]  # Your Aerospike host and port
}).connect()

# Define the key for the record you want to update
key = ('test', 'user_signups', 'user123')  # ('namespace', 'set', 'primary_key')

# Define the new data to update in the record
update_data = {
    "is_signed": True,  # Update this bin to True
    "is_usage": True,   # Update this bin to True
}

# Use the put() method to update the record
try:
    # Fetch the existing record
    record = client.get(key)
    
    if record:
        # If record exists, update the record with new data
        client.put(key, update_data)
        print("Record updated successfully")
    else:
        print("Record does not exist")

except exception.AerospikeError as e:
    print(f"Error: {e}")

# Close the connection
client.close()
