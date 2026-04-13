import datetime

class NameDateManager:
    def __init__(self):
        self.data = []

    def add_entry(self, name, date):
        self.data.append({'name': name, 'date': date})

    def filter_by_name(self, name):
        return [entry for entry in self.data if entry['name'] == name]

    def filter_by_date(self, date):
        return [entry for entry in self.data if entry['date'] == date]

    def __str__(self):
        return '\n'.join([f"{entry['name']} - {entry['date']}" for entry in self.data])

# Example usage
manager = NameDateManager()
manager.add_entry('Alice', '2023-04-13')
manager.add_entry('Bob', '2023-04-14')

print("All Entries:", manager)
print("Filtered by Name:", manager.filter_by_name('Alice'))
print("Filtered by Date:", manager.filter_by_date('2023-04-13'))