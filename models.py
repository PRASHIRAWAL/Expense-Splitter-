class Expense:
    def __init__(self, amount, description, paid_by, split_between):
        self.amount = amount
        self.description = description
        self.paid_by = paid_by
        self.split_between = split_between  # List of names
