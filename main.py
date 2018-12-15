import pandas as pd

year_2018 = '2018.csv'
year_2017 = '2017.csv'
all_accs = 'all_accs.csv'

csv_2018 = pd.read_csv(year_2018)
csv_2017 = pd.read_csv(year_2017)
csv_all_accs = pd.read_csv(all_accs)

accs_2018 = csv_2018.ACC
customer_2018 = csv_2018.CUSTOMER
spend_2018_csv = csv_2018.SPEND

accs_2017 = csv_2017.ACC
customer_2017 = csv_2017.CUSTOMER
spend_2017_csv = csv_2017.SPEND

all_accss = csv_all_accs.ACC
all_customers = csv_all_accs.CUSTOMER

spends_2018 = []
spends_2017 = []

customers = []

for acc, customer in zip(all_accss, all_customers):
    customers.append([acc, customer, 0, 0])

for acc, spend in zip(accs_2018, spend_2018_csv):
    spends_2018.append([acc, spend])

for acc, spend in zip(accs_2017, spend_2017_csv):
    spends_2017.append([acc, spend])

for i in range(len(customers)):
    for j in range(len(spends_2018)):
        if str(spends_2018[j][0]) in customers[i][0]:
            customers[i][2] = spends_2018[j][1]
    for j in range(len(spends_2017)):
        if str(spends_2017[j][0]) in customers[i][0]:
            customers[i][3] = spends_2017[j][1]

unique_customers = []

for elem in customers:
    if elem not in unique_customers:
        unique_customers.append(elem)

df = pd.DataFrame(unique_customers, columns=["ACC", "CUSTOMER", "SPEND_2018", "SPEND_2017"],)
df.to_csv('Customer_Spenders.csv', index=False)
