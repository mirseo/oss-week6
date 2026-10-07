import pandas as pd

df = pd.read_csv("scores.csv", encoding="utf-8")
# coerce가 빈 값과 미제출을 NaN으로 처리
df["score"] = pd.to_numeric(df["score"], errors="coerce")
df["score"] = df["score"].fillna(0)

result = df.groupby("category")["score"].mean().round(2)
print(result)