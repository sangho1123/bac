import pandas as pd
import numpy as np
from statsmodels.tsa.statespace.sarimax import SARIMAX
import matplotlib.pyplot as plt

# 1. 가상의 데이터 생성
np.random.seed(42)
date_rng = pd.date_range(start='2010-01-01', end='2023-12-01', freq='M')
cash_flow_data = np.random.normal(5000, 1500, len(date_rng))  # 평균 5000, 표준편차 1500
data = pd.DataFrame(date_rng, columns=['date'])
data['cash_flow'] = cash_flow_data
data.set_index('date', inplace=True)

# 2. 데이터 전처리 (결측값 처리)
data = data.fillna(method='ffill')

# 3. 모델 훈련
model = SARIMAX(data['cash_flow'], order=(1, 1, 1), seasonal_order=(1, 1, 1, 12))
model_fit = model.fit(disp=False)

# 4. 예측
forecast = model_fit.forecast(steps=12)
forecast_df = pd.DataFrame(forecast, columns=['forecast'])

# 5. 결과 시각화
plt.figure(figsize=(14, 7))
plt.plot(data['cash_flow'], label='Actual Cash Flow')
plt.plot(forecast_df, label='Forecasted Cash Flow', color='red')
plt.title('Cash Flow Forecast')
plt.xlabel('Date')
plt.ylabel('Cash Flow')
plt.legend()
plt.grid(True)
plt.show()
