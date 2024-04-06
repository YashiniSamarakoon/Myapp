from pymongo import MongoClient
from datetime import datetime

# MongoDB connection
client = MongoClient(
    'mongodb+srv://yashini2019943:hLNvVo8HLiSZtGAP@cleansentry.cxeur6w.mongodb.net/?retryWrites=true&w=majority&appName=cleansentry')

db = client['cleansentry_database']
collection = db['prediction_results']

# Define your update variables
location = 'Dehiwala'
current_date = datetime.now()
plastic_percentage = 0.5
glass_percentage = 0.3
metal_percentage = 0.1
foam_percentage = 0.1

# Update the collection
query = {'location': location, 'current_date': current_date}  # Define the document you want to update
update_data = {
    '$set': {
        'location': location,
        'current_date': current_date,
        'plastic_percentage': plastic_percentage,
        'glass_percentage': glass_percentage,
        'metal_percentage': metal_percentage,
        'foam_percentage': foam_percentage
    }
}
collection.update_one(query, update_data, upsert=True)
print("Data updated successfully!")


# Retrieve data from the collection
cursor = collection.find(query)

# Iterate over the cursor to access each document
for document in cursor:
    location = document['location']
    current_date = document['current_date']
    plastic_percentage = document['plastic_percentage']
    glass_percentage = document['glass_percentage']
    metal_percentage = document['metal_percentage']
    foam_percentage = document['foam_percentage']

    # Print or use the retrieved data as needed
    print(f"Location: {location}")
    print(f"Date: {current_date}")
    print(f"Plastic Percentage: {plastic_percentage}")
    print(f"Glass Percentage: {glass_percentage}")
    print(f"Metal Percentage: {metal_percentage}")
    print(f"Foam Percentage: {foam_percentage}")