import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Шаг 1: Импортировать датасет
df = pd.read_csv('test.csv')

# Шаг 2: Взять 1000 значений
df_subset = df.head(1000)

# Шаг 3: Проверить данные на пропуски
missing_values = df_subset.isnull().sum()

# Шаг 4: Проверить на нормальность распределения и выбросы
# Используем ящики с усами (логарифмическую шкалу) и гистограммы
fig, axes = plt.subplots(1, 2, figsize=(12, 6))

# Ящики с усами
sns.boxplot(x='Rooms', y='Square', data=df_subset, ax=axes[0])
axes[0].set_yscale('log')
axes[0].set_title('Ящик с усами (логарифмическая шкала)')

# Гистограмма
sns.histplot(df_subset['Square'], bins=30, kde=True, ax=axes[1])
axes[1].set_yscale('log')
axes[1].set_title('Гистограмма (логарифмическая шкала)')

plt.show()

# Шаг 5: Заполнить пропуски и обработать аномалии
# Заполнение пропусков (например, средним значением)
numeric_columns = df_subset.select_dtypes(include=[np.number]).columns
df_subset.loc[:, numeric_columns] = df_subset.loc[:, numeric_columns].fillna(df_subset.loc[:, numeric_columns].mean())

# Обработка аномальных значений (например, удаление выбросов)
q_low = df_subset['Square'].quantile(0.01)
q_high = df_subset['Square'].quantile(0.99)
df_subset = df_subset[(df_subset['Square'] > q_low) & (df_subset['Square'] < q_high)]

# Шаг 6: Определить количество квартир по числу комнат
room_counts = df_subset['Rooms'].value_counts()

# Шаг 7: Построить сводную таблицу
pivot_table = pd.pivot_table(df_subset, values='Square', index='DistrictId', columns='Rooms', aggfunc='count', fill_value=0)

# Шаг 8: Сохранить обработанный массив без выбросов и пропусков
df_subset.to_csv('processed_data.csv', index=False)
