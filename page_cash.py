
from dash import dcc
import pandas as pd
import plotly.express as px
from dash import html
import numpy as np

# Берем данные 3333

df = pd.read_csv('cash.csv', sep=';', encoding='utf-8', decimal=',')
df = df.dropna()

df['sale_date'] = pd.to_datetime(df['sale_date'], format='%Y-%m-%d')

df['sale_year'] = pd.to_numeric(df['sale_date'].dt.strftime('%Y'), errors='coerce')
df['sale_month'] = df['sale_date'].dt.strftime('%m')
df['sale_day'] = df['sale_date'].dt.strftime('%d')


df = df.loc[df['sale_year'] == 2022]

# print(df['sale_month'])
# print(df['sale_year'])

df_range_year = list(df['sale_date'].dt.strftime('%Y-%m').unique())
df_range_month = pd.to_datetime(np.arange(12)+1, format='%m').to_series().dt.month_name().str[:3].values

# График 1

fig_1 = px.bar(df.groupby(['prod_name', 'sale_date'], as_index=False)['amt'].sum(),
               x='sale_date', y='amt', color='prod_name')
fig_1.update_layout(margin=dict(l=10, r=10, t=10, b=10), legend_entrywidthmode='fraction')

chart_1 = dcc.Graph(id='chart_1', figure=fig_1)
drop_down_1 = dcc.Dropdown(df_range_year, id='cash_dropdown_1')

# График 2
# fig_2 = px.line(df.groupby(by=['sale_month','sale_day'], as_index=False)['amt'].sum(),
# x='sale_day', y='amt', color='sale_month')

df['amt'] = df['amt'].fillna(0)
df_temp = df.groupby(['sale_month', 'sale_day'], as_index=False)['amt'].sum()
df_temp = df_temp.join(df.groupby("sale_month", as_index=False).cumsum(), rsuffix="_cumsum")


print(df_temp)

fig_2 = px.line(df_temp, y="amt_cumsum", x="sale_day",
                color="sale_month")
fig_2.update_layout(margin=dict(l=10, r=10, t=10, b=10))

chart_2 = dcc.Graph(id='chart_2', figure=fig_2)
drop_down_2 = dcc.Dropdown(df_range_year, id='cash_dropdown_2')


# Итоговая страница
html = html.Div([
            html.H4('Объемы'),
            drop_down_1,
            chart_1,
            html.H4('Объемы со сравнением мес. к мес.'),
            drop_down_2,
            chart_2
        ])
