"""
Budget Planner
• Objective: Use classes, control flow, external modules, and visualization to track a
monthly budget.
• Task: Create a monthly budget planner that tracks spending, alerts overspending, and
visualizes data.
"""
class BudgetPlanner:

    def __init__(self, budget):

        self.budget = budget

        self.expenses = {}

    def add_expense(self, category, amount):

        self.expenses[category] = (
            self.expenses.get(category, 0)
            + amount
        )

    def total_spent(self):

        return sum(self.expenses.values())

    def check_budget(self):

        if self.total_spent() > self.budget:

            print("Overspending Alert")

        else:

            print("Within Budget")

    def display_report(self):

        print("\nBudget Report")

        for category, amount in self.expenses.items():

            print(category, "-", amount)

        print("Total Spent:", self.total_spent())

        print("Budget:", self.budget)


planner = BudgetPlanner(20000)

planner.add_expense("Food", 5000)
planner.add_expense("Travel", 3000)
planner.add_expense("Shopping", 7000)
planner.add_expense("Bills", 4000)

planner.display_report()

planner.check_budget()