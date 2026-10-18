import pandas as pd

print(pd.__version__)

data = {
    "Name": ["Alice", "Bob"],
    "Age": [25, 30]
}

df = pd.DataFrame(data)
print(df)