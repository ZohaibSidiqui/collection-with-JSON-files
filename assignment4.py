class UserInterface:
    def __init__(self, resource_manager):
        self.resource_manager = resource_manager
    
    def show_menu(self):
        print("\nChoose an option:")
        print("1. Create a new resource")
        print("2. Read existing resources")
        print("3. Update an existing resource")
        print("4. Delete an existing resource")
        print("5. Quit")
    
    def create_resource(self):
        name = input("Enter the name of the resource: ")
        description = input("Enter a brief description of the resource: ")
        self.resource_manager.create_resource(name, description)
        print("Resource created successfully!")
    
    def read_resource(self):
        search_criteria = input("Enter the name or ID of the resource you want to search for: ")
        results = self.resource_manager.read_resources(search_criteria)
        if results:
            for resource in results:
                print(resource)
        else:
            print("No resources found that match the search criteria.")
    
    def edit_resource(self):
        id = input("Enter the ID of the resource you want to update: ")
        name = input("Enter the new name for the resource: ")
        description = input("Enter the new description for the resource: ")
        self.resource_manager.update_resource(id, name, description)
        print("Resource updated successfully!")
    
    def delete_resource(self):
        id = input("Enter the ID of the resource you want to delete: ")
        self.resource_manager.delete_resource(id)
        print("Resource deleted successfully!")
    
    def handle_exception(self, exception):
        print(f"An error occurred: {exception}")

class ResourceManager:
    def __init__(self, data_persistence_manager):
        self.resources = []
        self.data_persistence_manager = data_persistence_manager
    
    def create_resource(self, name, description):
        id = len(self.resources) + 1
        resource = resource(id, name, description)
        self.resources.append(resource)
        self.data_persistence_manager.save_data(self.resources)
    
    def read_resources(self, search_criteria):
        results = []
        for resource in self.resources:
            if search_criteria.lower() in resource.name.lower() or search_criteria == str(resource.id):
                results.append(resource)
        return results
    
    def update_resource(self, id, name, description):
        for resource in self.resources:
            if resource.id == int(id):
                resource.name = name
                resource.description = description
                self.data_persistence_manager.save_data(self.resources)
                break
    
    def delete_resource(self, id):
        for resource in self.resources:
            if resource.id == int(id):
                self.resources.remove(resource)
                self.data_persistence_manager.save_data(self.resources)
                break
    
    def load_resources(self):
        self.resources = self.data_persistence_manager.load_data()
    
    def save_resources(self):
        self.data_persistence_manager.save_data(self.resources)

import json

class DataPersistenceManager:
    def __init__(self, file_name):
        self.file_name = file_name
    
    def load_data(self):
        try:
            with open(self.file_name, "r") as file:
                data = json.load(file)
        except FileNotFoundError:
            data = []
        return data
    
    def save_data(self, data):
        with open(self.file_name, "w") as file:
            json.dump(data, file, default=lambda x: x.__dict__)

d = UserInterface()
print(d)