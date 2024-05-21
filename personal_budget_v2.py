import pandas as pd

def get_user_input():
    name = input("Enter your name: ")
    monthly_income = float(input("Enter your monthly income: "))
    return name, monthly_income

def calculate_remaining_budget(total_budget, current_allocations):
    return total_budget - sum(current_allocations.values())

def prompt_user_for_budget(category, remaining_budget):
    while True:
        user_input = input(f"Enter your estimated spending for {category} (Remaining budget: {remaining_budget:.2f}): ")
        if user_input.lower() == 'r':
            return 'r', 0
        try:
            amount = float(user_input)
            if amount < 0:
                print("Please enter a non-negative amount.")
            else:
                return 'c', amount
        except ValueError:
            print("Invalid input. Please enter a number.")

def collect_user_budgets(categories, total_budget):
    allocations = {}
    for category in categories:
        while True:
            status, amount = prompt_user_for_budget(category, calculate_remaining_budget(total_budget, allocations))
            if status == 'r':
                return 'restart', {}
            allocations[category] = amount
            if calculate_remaining_budget(total_budget, allocations) < 0:
                print("You have exceeded your monthly budget. Let's start over.")
                return 'restart', {}
            break
    return 'complete', allocations

def create_excel_file(name, monthly_income, budget):
    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    writer = pd.ExcelWriter(f'{name}_budget.xlsx', engine='openpyxl')

    for month in months:
        data = []
        for category, amount in budget.items():
            data.append([category, amount, '', ''])
        
        df = pd.DataFrame(data, columns=['Category', 'Allocated Amount', 'Actual Amount', 'Notes'])
        df.to_excel(writer, sheet_name=month, index=False)
    
    writer.save()

def main():
    name, monthly_income = get_user_input()
    budget_categories = {
        'Housing': 0.25,
        'Food': 0.10,
        'Transportation': 0.05,
        'Utilities': 0.05,
        'Insurance': 0.05,
        'Entertainment': 0.10,
        'Travel': 0.10,
        'Shopping': 0.10,
        'Debt': 0.10,
        'Emergency Fund': 0.05,
        'Investments': 0.05
    }
    
    while True:
        print("\nLet's start the budget allocation process.")
        status, user_budget = collect_user_budgets(budget_categories.keys(), monthly_income)
        if status == 'complete':
            create_excel_file(name, monthly_income, user_budget)
            print(f'Budget file {name}_budget.xlsx has been created.')
            break
        else:
            print("Restarting the budget allocation process.")

if __name__ == '__main__':
    main()

