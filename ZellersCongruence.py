class DateCalculator:
    def _init_(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day


        if self.month == 1 or self.month == 2:
            self.month += 12
            self.year -= 1

        self.K = self.year % 100
        self.J = self.year // 100

    def calculate_weekday(self):
        h = (self.day + 13*(self.month + 1)//5 + self.K + self.K//4 + self.J//4 + 5*self.J) % 7
        days = ["Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
        return days[h]

if _name_ == "_main_":
    try:
        year = int(input("Enter the year: "))
        month = int(input("Enter the month (1–12): "))
        day = int(input("Enter the day (1–31): "))

        date = DateCalculator(year, month, day)
        print("The day of the week is:", date.calculate_weekday())

    except ValueError:
        print("Invalid input! Please enter numeric values only.")