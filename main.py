import pandas as pd
import json

df = pd.read_csv("titanic.csv")

def fare_per_passenger_by_class(df):
    total_fare_by_class = df.groupby('Pclass')['Fare'].sum()
    total_passengers_by_class = df.groupby("Pclass")["PassengerId"].count()
    avg_passengers_by_class = total_fare_by_class / total_passengers_by_class
    return avg_passengers_by_class.to_json()

print(fare_per_passenger_by_class(df))