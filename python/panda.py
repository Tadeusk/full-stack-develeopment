import pandas as pd

def big_countries(world: pd.DataFrame) -> pd.DataFrame:
    pass
    
def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    df_cus=customers[~customers['id'].isin(orders['customerId'])]      
    return df_cus[['name']].rename(columns={'name':'Customers'})

def calculate_special_bonus(employees: pd.DataFrame) -> pd.DataFrame:
    return employees.apply(lambda x: x['salary'] if x['employee_id'] % 2 != 0 and not x['name'].startswith('M')
    else 0, axis=1)[['employee_id', 'bonus']].sort_values(by='employee_id')