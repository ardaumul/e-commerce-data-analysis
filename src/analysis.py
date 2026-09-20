def analyze_category_performance(df):
    """Calculate category-level sales performance."""

    return (
        df.groupby("category")
        .agg(
            order_count=("order_id", "count"),
            total_revenue=("total_amount", "sum"),
            average_order_value=("total_amount", "mean")
        )
        .sort_values("total_revenue", ascending=False)
    )


def analyze_city_performance(df):
    """Calculate city-level sales performance."""

    return (
        df.groupby("city")
        .agg(
            order_count=("order_id", "count"),
            total_revenue=("total_amount", "sum"),
            average_order_value=("total_amount", "mean")
        )
        .sort_values("total_revenue", ascending=False)
    )


def analyze_region_performance(df):
    """Calculate region-level sales performance."""

    return (
        df.groupby("region")
        .agg(
            order_count=("order_id", "count"),
            total_revenue=("total_amount", "sum"),
            average_order_value=("total_amount", "mean")
        )
        .sort_values("total_revenue", ascending=False)
    )


def analyze_customer_type(df):
    """Calculate customer type performance."""

    return (
        df.groupby("customer_type")
        .agg(
            order_count=("order_id", "count"),
            total_revenue=("total_amount", "sum"),
            average_order_value=("total_amount", "mean")
        )
        .sort_values("total_revenue", ascending=False)
    )

def analyze_returns(df):
    """Calculate overall and category-level return metrics."""

    category_returns = (
        df.groupby("category")
        .agg(
            order_count=("order_id", "count"),
            return_count=("return_status", lambda x: (x == "Evet").sum())
        )
    )

    category_returns["return_rate"] = (
        category_returns["return_count"]
        / category_returns["order_count"]
        * 100
    )

    return category_returns.sort_values(
        "return_rate",
        ascending=False
    )

def analyze_payment_methods(df):
    """Calculate sales performance by payment method."""

    return (
        df.groupby("payment_method")
        .agg(
            order_count=("order_id", "count"),
            total_revenue=("total_amount", "sum"),
            average_order_value=("total_amount", "mean")
        )
        .sort_values("total_revenue", ascending=False)
    )

def analyze_delivery_performance(df):
    """Calculate delivery time statistics."""

    average_delivery_time = df["delivery_days"].mean()

    delivery_rating_correlation = (
        df[["delivery_days", "customer_rating"]]
        .corr()
        .loc["delivery_days", "customer_rating"]
    )

    return average_delivery_time, delivery_rating_correlation

def analyze_product_performance(df, top_n=10):
    """Calculate top products by quantity and revenue."""

    top_products_quantity = (
        df.groupby("product_name")["quantity"]
        .sum()
        .sort_values(ascending=False)
        .head(top_n)
    )

    top_products_revenue = (
        df.groupby("product_name")["total_amount"]
        .sum()
        .sort_values(ascending=False)
        .head(top_n)
    )

    return top_products_quantity, top_products_revenue

def analyze_discount_performance(df):
    """Calculate revenue metrics by discount rate."""

    return (
        df.groupby("discount_rate")
        .agg(
            order_count=("order_id", "count"),
            total_revenue=("total_amount", "sum"),
            average_order_value=("total_amount", "mean")
        )
        .sort_index()
    )


def calculate_discount_profit_correlation(df):
    """Calculate correlation between discount and profit margin."""

    return (
        df[["discount_rate", "profit_margin_rate"]]
        .corr()
        .loc["discount_rate", "profit_margin_rate"]
    )

