class Income:
    def __init__(self, entry_id=None, student_id=None, date=None, amount=None):
        self.entry_id = entry_id
        self.student_id = student_id
        self.date = date
        self.amount = amount

    def __str__(self):
        return (f'Id: {self.student_id}, Date: {self.date}, Amount: {self.amount}')

