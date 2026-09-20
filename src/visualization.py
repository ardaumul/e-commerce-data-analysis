import matplotlib.pyplot as plt
import seaborn as sns
import os


def plot_monthly_revenue(monthly_revenue):
    """Plot monthly revenue trend."""

    plt.figure(figsize=(12, 5))

    plt.plot(
        monthly_revenue["year_month"].astype(str),
        monthly_revenue["total_amount"],
        marker="o"
    )

    plt.title("Monthly Revenue Trend")
    plt.xlabel("Month")
    plt.ylabel("Revenue")
    plt.xticks(rotation=45)

    plt.tight_layout()
    plt.savefig(
    "../visualizations/monthly_revenue_trend.png",
    dpi=300,
    bbox_inches="tight"
    )
    plt.show()


def plot_category_revenue(category_analysis):
    """Plot revenue by category."""

    plt.figure(figsize=(10, 5))

    sns.barplot(
        data=category_analysis.reset_index(),
        x="category",
        y="total_revenue"
    )

    plt.title("Revenue by Category")
    plt.xlabel("Category")
    plt.ylabel("Total Revenue")
    plt.xticks(rotation=45)

    plt.tight_layout()
    plt.savefig(
        "../visualizations/revenue_by_category.png",
        dpi=300,
        bbox_inches="tight"
    )
    plt.show()


def plot_city_revenue(city_analysis):
    """Plot revenue by city."""

    plt.figure(figsize=(10, 6))

    sns.barplot(
        data=city_analysis.reset_index(),
        x="city",
        y="total_revenue"
    )

    plt.title("Revenue by City")
    plt.xlabel("City")
    plt.ylabel("Total Revenue")
    plt.xticks(rotation=45)

    plt.tight_layout()
    plt.savefig(
    "../visualizations/revenue_by_city.png",
    dpi=300,
    bbox_inches="tight"
    )
    plt.show()


def plot_region_revenue(region_analysis):
    """Plot revenue by region."""

    plt.figure(figsize=(10, 6))

    sns.barplot(
        data=region_analysis.reset_index(),
        x="region",
        y="total_revenue"
    )

    plt.title("Revenue by Region")
    plt.xlabel("Region")
    plt.ylabel("Total Revenue")
    plt.xticks(rotation=45)

    plt.tight_layout()
    plt.savefig(
    "../visualizations/revenue_by_region.png",
    dpi=300,
    bbox_inches="tight"
    )
    plt.show()

def plot_return_rate(category_returns):
    """Plot return rate by category."""

    plt.figure(figsize=(10, 6))

    sns.barplot(
        data=category_returns.reset_index(),
        x="category",
        y="return_rate"
    )

    plt.title("Return Rate by Category")
    plt.xlabel("Category")
    plt.ylabel("Return Rate (%)")
    plt.xticks(rotation=45)

    plt.tight_layout()
    plt.savefig(
    "../visualizations/return_rate_by_category.png",
    dpi=300,
    bbox_inches="tight"
    )
    plt.show()


def plot_payment_revenue(payment_analysis):
    """Plot revenue by payment method."""

    plt.figure(figsize=(10, 6))

    sns.barplot(
        data=payment_analysis.reset_index(),
        x="payment_method",
        y="total_revenue"
    )

    plt.title("Revenue by Payment Method")
    plt.xlabel("Payment Method")
    plt.ylabel("Total Revenue")
    plt.xticks(rotation=45)

    plt.tight_layout()
    plt.savefig(
    "../visualizations/revenue_by_payment_method.png",
    dpi=300,
    bbox_inches="tight"
    )
    plt.show()


def plot_delivery_distribution(df):
    """Plot delivery time distribution."""

    plt.figure(figsize=(10, 5))

    sns.histplot(
        data=df,
        x="delivery_days",
        discrete=True
    )

    plt.title("Delivery Time Distribution")
    plt.xlabel("Delivery Days")
    plt.ylabel("Order Count")

    plt.tight_layout()
    plt.savefig(
    "../visualizations/delivery_time_distribution.png",
    dpi=300,
    bbox_inches="tight"
    )
    plt.show()


def plot_top_products_quantity(top_products_quantity):
    """Plot top products by quantity sold."""

    plt.figure(figsize=(10, 6))

    sns.barplot(
        x=top_products_quantity.values,
        y=top_products_quantity.index
    )

    plt.title("Top 10 Products by Quantity Sold")
    plt.xlabel("Quantity Sold")
    plt.ylabel("Product")

    plt.tight_layout()
    plt.savefig(
    "../visualizations/top_products_by_quantity.png",
    dpi=300,
    bbox_inches="tight"
    )
    plt.show()


def plot_top_products_revenue(top_products_revenue):
    """Plot top products by revenue."""

    plt.figure(figsize=(10, 6))

    sns.barplot(
        x=top_products_revenue.values,
        y=top_products_revenue.index
    )

    plt.title("Top 10 Products by Revenue")
    plt.xlabel("Total Revenue")
    plt.ylabel("Product")

    plt.tight_layout()
    plt.savefig(
    "../visualizations/top_products_by_revenue.png",
    dpi=300,
    bbox_inches="tight"
    )
    plt.show()


def plot_discount_revenue(discount_analysis):
    """Plot revenue by discount rate."""

    plt.figure(figsize=(10, 6))

    sns.barplot(
        data=discount_analysis.reset_index(),
        x="discount_rate",
        y="total_revenue"
    )

    plt.title("Revenue by Discount Rate")
    plt.xlabel("Discount Rate")
    plt.ylabel("Total Revenue")

    plt.tight_layout()
    plt.savefig(
    "../visualizations/discount_vs_profit_margin.png",
    dpi=300,
    bbox_inches="tight"
    )
    plt.show()


def plot_discount_profit_correlation(df):
    """Plot discount rate against profit margin rate."""

    plt.figure(figsize=(8, 6))

    sns.scatterplot(
        data=df,
        x="discount_rate",
        y="profit_margin_rate"
    )

    plt.title("Discount Rate vs Profit Margin Rate")
    plt.xlabel("Discount Rate")
    plt.ylabel("Profit Margin Rate")

    plt.tight_layout()
    plt.show()