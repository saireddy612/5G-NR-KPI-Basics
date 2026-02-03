import pandas as pd

def load_kpi_file(path):
    df = pd.read_excel(path)
    return df.apply(pd.to_numeric, errors="coerce")
