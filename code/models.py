from time_mod import Time


class Post:
    def __init__(self, row, count, city, color, column, furniture_type):
        self.row = row
        self.count = count
        self.city = city
        self.color = color
        self.column = column
        self.furniture_type = furniture_type
        self.time = Time()

    def get_time(self):
        return self.time.give()
    
    def __str__(self):
        return f"{self.column}_{self.row}"
