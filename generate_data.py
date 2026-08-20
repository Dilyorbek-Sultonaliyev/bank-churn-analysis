import pandas as pd
import numpy as np
from faker import Faker
import random

fake = Faker()
np.random.seed(42)
random.seed(42)

n_customers = 50000  # necha mijoz yaratamiz

data = []  # har bir mijozni shu ro'yxatga qo'shamiz

for i in range(n_customers):
    name = fake.name()
    age = np.random.randint(18, 75)
    tenure_months = np.random.randint(1, 120)
    balance = round(np.random.exponential(scale=5000000), 2)
    num_products = np.random.randint(1, 5)
    has_credit_card = np.random.choice([0, 1], p=[0.3, 0.7])
    is_active = np.random.choice([0, 1], p=[0.4, 0.6])
    salary = round(np.random.normal(loc=4000000, scale=1500000), 2)
    salary = max(salary, 1000000)
    complaints = np.random.poisson(0.5)

    churn_score = (
        (tenure_months < 12) * 0.3 +
        (is_active == 0) * 0.3 +
        (complaints > 1) * 0.25 +
        (num_products == 1) * 0.15 +
        np.random.random() * 0.3
    )
    mijoz_ketdi = 1 if churn_score > 0.5 else 0

    # bitta mijozning barcha ma'lumotini ro'yxatga qo'shamiz
    data.append([
        name, age, tenure_months, balance, num_products,
        has_credit_card, is_active, salary, complaints, mijoz_ketdi
    ])

# ustun nomlari
columns = [
    'ism', 'yosh', 'necha_oy_mijoz', 'balans', 'mahsulotlar_soni',
    'kredit_karta_bormi', 'faol_mijozmi', 'maosh', 'shikoyatlar_soni', 'mijoz_ketdi'
]

# ro'yxatni jadval (DataFrame) ga aylantiramiz
df = pd.DataFrame(data, columns=columns)

# CSV faylga saqlaymiz
df.to_csv('data/bank_customers.csv', index=False)

print(f"✅ {n_customers} ta mijoz yaratildi!")
print(df.head())
print(f"\nMijoz ketganlar soni: {df['mijoz_ketdi'].sum()} ({df['mijoz_ketdi'].mean()*100:.1f}%)")