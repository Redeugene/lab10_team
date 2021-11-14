def convert_to_float(df_field):
    return df_field.astype('float32')


def save_in_df(products):
    df = pd.DataFrame(columns =    ["title",
                                    "category",
                                    "price",
                                    "discount_price",
                                    "link",
                                    "site",
                                    "catalog",
                                    "stock",
                                    "stock_name",
                                    "article",
                                    "unit",
                                    "order",
                                    "inventory",
                                    "city",
                                    "price_2",
                                    "discount_price_2",
                                    "unit_2"])

    for prod in products:
        a_series = pd.Series(prod, index = df.columns)
        df = df.append(a_series, ignore_index=True)

    df["price"] = convert_to_float(df["price"])
    df["discount_price"] = convert_to_float(df["discount_price"])
    df["price_2"] = convert_to_float(df["price_2"])
    df["discount_price_2"] = convert_to_float(df["discount_price_2"])
    df = df.fillna("-1")
    df.to_csv("lerua.csv", index=False, mode='a', header=False, encoding='utf-8')
