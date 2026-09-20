import pandas as pd


def rename_columns(df):
    """Rename dataset columns from Turkish to English."""
    
    return df.rename(columns={
        "siparis_id": "order_id",
        "musteri_id": "customer_id",
        "siparis_tarihi": "order_date",
        "sehir": "city",
        "bolge": "region",
        "kategori": "category",
        "urun_adi": "product_name",
        "adet": "quantity",
        "birim_fiyat": "unit_price",
        "indirim_orani": "discount_rate",
        "kargo_ucreti": "shipping_fee",
        "odeme_turu": "payment_method",
        "musteri_tipi": "customer_type",
        "teslimat_gunu": "delivery_days",
        "musteri_puani": "customer_rating",
        "iade_durumu": "return_status",
        "kar_marji_orani": "profit_margin_rate",
        "toplam_tutar": "total_amount"
    })


def convert_data_types(df):
    """Convert columns to appropriate data types."""
    
    df["order_date"] = pd.to_datetime(df["order_date"])
    
    return df


def standardize_categories(df):
    """Standardize inconsistent categorical values."""
    
    df["city"] = df["city"].replace({
        "Istanbul": "İstanbul",
        "istanbul": "İstanbul",
        "ankara": "Ankara",
        "gaziantep": "Gaziantep",
        "Izmir": "İzmir",
        "Izmır": "İzmir"
    })

    df["category"] = df["category"].replace({
        "spor": "Spor",
        "ofis": "Ofis",
        "kitap": "Kitap",
        "kozmetık": "Kozmetik",
        "kozmetik": "Kozmetik",
        "Kozmetik ": "Kozmetik",
        "ev ve yaşam": "Ev ve Yaşam",
        "Ev&Yaşam": "Ev ve Yaşam",
        "Elektronik ": "Elektronik",
        "elektronik": "Elektronik"
    })

    df["customer_type"] = df["customer_type"].replace({
        "mevcut": "Mevcut",
        "yeni": "Yeni",
        "vip": "VIP",
        "Vip": "VIP"
    })

    df["payment_method"] = df["payment_method"].replace({
        "kredi kartı": "Kredi Kartı",
        "banka karti": "Banka Kartı",
        "dijital cüzdan": "Dijital Cüzdan",
        "Kapida Odeme": "Kapıda Ödeme",
        "havale": "Havale/EFT",
        "eft": "Havale/EFT",
        "Havale": "Havale/EFT"
    })

    for column in [
        "city",
        "category",
        "customer_type",
        "payment_method"
    ]:
        df[column] = df[column].str.strip()


    return df


def handle_missing_values(df):
    """Handle missing values using appropriate strategies."""

    df["discount_rate"] = df["discount_rate"].fillna(
        df["discount_rate"].median()
    )

    df["delivery_days"] = df["delivery_days"].fillna(
        df["delivery_days"].median()
    )

    df["city"] = df["city"].fillna("Unknown")
    df["payment_method"] = df["payment_method"].fillna("Unknown")
    df["customer_type"] = df["customer_type"].fillna("Unknown")

    return df


def remove_duplicates(df):
    """Remove duplicate records from the dataset."""

    df = df.drop_duplicates().reset_index(drop=True)

    return df