BudgetManager
class BudgetManager:
    """
    A class to manage budgets and expenditures.
    
    Tracks available funds, individual budgets, and spending.
    Designed as a simple resource system, useful as a foundation for game-dev style projects.
    """

    def __init__(self, total_amount):
        """
        Initialize the BudgetManager with total available funds.
        """
        self.available = total_amount
        self.budgets = {}        # Stores budget name -> amount
        self.expenditure = {}    # Stores budget name -> list of spending amounts

    def add_budget(self, name, amount):
        """
        Add a new budget with the given name and amount.
        
        Raises:
            ValueError: If the budget already exists or funds are insufficient.
        """
        if name in self.budgets:
            raise ValueError(f"Budget '{name}' already exists.")
        if amount > self.available:
            raise ValueError("Insufficient funds to allocate this budget.")

        self.budgets[name] = amount
        self.expenditure[name] = []
        self.available -= amount
        return self.available

    def spend(self, name, amount):
        """
        Spend a given amount from a specific budget.
        
        Raises:
            ValueError: If the budget does not exist.
        """
        if name not in self.budgets:
            raise ValueError(f"Budget '{name}' does not exist.")
        
        self.expenditure[name].append(amount)
        total_budgeted = self.budgets[name]
        total_spent = sum(self.expenditure[name])
        remaining = total_budgeted - total_spent
        return remaining

    def get_remaining(self, name):
        """
        Returns the remaining amount for a specific budget.
        """
        if name not in self.budgets:
            raise ValueError(f"Budget '{name}' does not exist.")
        return self.budgets[name] - sum(self.expenditure[name])

    def get_total_spent(self, name):
        """
        Returns the total amount spent for a specific budget.
        """
        if name not in self.budgets:
            raise ValueError(f"Budget '{name}' does not exist.")
        return sum(self.expenditure[name])

    def print_summary(self):
        """
        Prints a formatted summary of all budgets, expenditures, and remaining funds.
        """
        header = f"{'Budget':15} {'Budgeted':10} {'Spent':10} {'Remaining':10}"
        print(header)
        print("-" * len(header))

        total_budgeted = 0
        total_spent = 0
        total_remaining = 0

        for name in self.budgets:
            budgeted = self.budgets[name]
            spent = sum(self.expenditure[name])
            remaining = budgeted - spent

            print(f"{name:15} {budgeted:10.2f} {spent:10.2f} {remaining:10.2f}")

            total_budgeted += budgeted
            total_spent += spent
            total_remaining += remaining

        print("-" * len(header))
        print(f"{'TOTAL':15} {total_budgeted:10.2f} {total_spent:10.2f} {total_remaining:10.2f}")