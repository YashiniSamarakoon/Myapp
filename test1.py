from pymongo import MongoClient

# MongoDB connection
client = MongoClient('mongodb+srv://yashini2019943:hLNvVo8HLiSZtGAP@cleansentry.cxeur6w.mongodb.net/?retryWrites=true&w=majority&appName=cleansentry')

db = client['cleansentry_database']
collection = db['recycling_center_details']

def print_recycling_center_details(location):
    # Query the collection based on the selected location
    query = {'location': location}
    cursor = collection.find(query)

    # Iterate over the cursor to access each document
    for document in cursor:
        recycling_centers = document.get('recycling_centers')
        print(f"Recycling Centers in {location}:")
        for center in recycling_centers:
            contact_person = center.get('contact_person')
            company_name = center.get('company_name')
            address = center.get('address')
            telephone_number = center.get('telephone_number')
            nature_of_business = center.get('nature_of_business')
            nature_of_materials = center.get('nature_of_materials')

            # Print or use the retrieved data as needed
            print(f"Contact Person: {contact_person}")
            print(f"Company Name: {company_name}")
            print(f"Address: {address}")
            print(f"Telephone Number: {telephone_number}")
            print(f"Nature of Business: {nature_of_business}")
            print("Nature of Materials:")
            for material in nature_of_materials:
                print(f"- {material}")
            print("\n")  # Add newline for better readability

# Test the function with a selected location
selected_location = 'Dehiwala'
print_recycling_center_details(selected_location)
