def normalize(df):
    x = df.value - df.value.min()
    y = df.value.max() - df.value.min()
    df.value = x/y
    return df