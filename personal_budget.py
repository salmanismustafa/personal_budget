import pandas as pd

def get_user_input():
    name = input("Enter your name: ")
    monthly_income = float(input("Enter your monthly income: "))
    return name, monthly_income

def calculate_budget(income):
    budget = {
        'Needs': {
            'Housing': income * 0.25,
            'Food': income * 0.10,
            'Transportation': income * 0.05,
            'Utilities': income * 0.05,
            'Insurance': income * 0.05
        },
        'Wants': {
            'Entertainment': income * 0.10,
            'Travel': income * 0.10,
            'Shopping': income * 0.10
        },
        'Savings': {
            'Debt': income * 0.10,
            'Emergency Fund': income * 0.05,
            'Investments': income * 0.05
        }
    }
    return budget

def create_excel_file(name, budget):
    writer = pd.ExcelWriter(f'{name}_budget.xlsx', engine='openpyxl')
    
    for month in range(1, 13):
        data = []
        for category, subcategories in budget.items():
            for subcategory, amount in subcategories.items():
                data.append([category, subcategory, amount, '', ''])
        
        df = pd.DataFrame(data, columns=['Category', 'Subcategory', 'Allocated Amount', 'Actual Amount', 'Notes'])
        df.to_excel(writer, sheet_name=f'Month_{month}', index=False)
    
    writer.save()

def main():
    name, monthly_income = get_user_input()
    budget = calculate_budget(monthly_income)
    create_excel_file(name, budget)
    print(f'Budget file {name}_budget.xlsx has been created.')

if __name__ == '__main__':
    main()

