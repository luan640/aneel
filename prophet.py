df_prophet = pd.read_excel("prophet_aneel.xlsx")
df_prophet.head()

df_prophet_ = df_prophet[['ds','yhat','y_real', 'yhat_upper', 'yhat_lower']]

# fig_2 = px.line(df_prophet[['ds','yhat','y_real']], x="ds", y=["yhat",'y_real'],title="Novos usuários da Energia distribuida")
# fig_2.show()

import plotly.graph_objs as go
import plotly.offline as pyo
import numpy as np

x = df_prophet_['ds']
y1 = df_prophet_['yhat']
y2 = df_prophet_['y_real'] 
y3 = df_prophet_['yhat_upper']
y4 = df_prophet_['yhat_lower']

trace1 = go.Scatter(x=x, y=y1, mode='lines', name='Previsto', line=dict(color='blue'))
trace2 = go.Scatter(x=x, y=y2, mode='markers', name='Real',marker=dict(color='black'))
trace3 = go.Scatter(x=x, y=y3, fill=None, mode='lines', line_color='gray', name='Intervalo Superior')
trace4 = go.Scatter(x=x, y=y4, fill='tonexty', mode='lines', line_color='gray', name='Intervalo Inferior')

data = [trace1, trace2, trace3, trace4]

layout = go.Layout(title='Projeção de quantidade de CPF', xaxis=dict(title='Eixo X'), yaxis=dict(title='Eixo Y'))

fig_prophet = go.Figure(data=data, layout=layout)