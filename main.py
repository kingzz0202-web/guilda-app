class NameManager:
    def __init__(self):
        self.names = []

    def add_name(self, name, date):
        # date should be in DD/MM format
        self.names.append((name, date))

    def remove_name(self, name):
        self.names = [n for n in self.names if n[0] != name]

    def filter_by_longest_time(self):
        from datetime import datetime
        today = datetime.utcnow()
        # Convert DD/MM to datetime for comparison
        return sorted(self.names, key=lambda x: datetime.strptime(x[1], '%d/%m'))

    def filter_by_deadline(self):
        from datetime import datetime, timedelta
        today = datetime.utcnow()
        return sorted(self.names, key=lambda x: datetime.strptime(x[1], '%d/%m') - today)

    def remaining_days(self, name):
        from datetime import datetime
        for n in self.names:
            if n[0] == name:
                date = datetime.strptime(n[1], '%d/%m')
                remaining = (date - datetime.utcnow()).days
                return remaining
        return None

    def display_names(self):
        for name, date in self.names:
            print(f'Name: {name}, Date: {date}')