import pandas as pd

data = pd.DataFrame([i] * 20 for i in range(0, 20))
data.to_excel("calc_data.xlsx", index=False)
