from datetime import datetime


class DatasBr:

    def __init__(self):
        self.register_moment = datetime.today()
    
    def __str__(self):
        return self.format_date()

    def register_month(self):

        year_months = ['January', 'February', 'March', 'April', 'May ', 'June', 
                        'July', 'August', 'September', 'October', 'November', 'December']
        register_month = self.register_moment.month - 1
        return year_months[register_month]

    def week_day(self):

        week_days = ['Monday', 'Tuesday', 'Wednesday ', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        week_day = self.register_moment.weekday()
        return week_days[week_day]

    def format_date(self):
        formated_date = self.register_moment.strftime('Date: %d/%m/%Y\nHour: %H:%M:%S')
        return formated_date

    def register_time(self):
        register_time = datetime.today() - self.register_moment
        return register_time
