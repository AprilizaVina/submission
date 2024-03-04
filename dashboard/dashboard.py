import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

sns.set(style='dark')

# Helper function yang dibutuhkan untuk menyiapkan berbagai dataframe
def create_sum_order_payment_df(df):
    sum_order_payment_df = df.groupby(by="payment_type").order_item_id.sum().sort_values(ascending=False).reset_index()
    return sum_order_payment_df

def create_sum_product_category_df(df):
    sum_product_category_df = df.groupby(by="product_category_name").order_item_id.sum().sort_values(ascending=False).reset_index()
    return sum_product_category_df

def create_sum_seller_city_df(df):
    sum_seller_city_df = df.groupby(by="seller_city").order_item_id.sum().sort_values(ascending=False).reset_index()
    return sum_seller_city_df

# Load cleaned data
payment_df = pd.read_csv("https://raw.githubusercontent.com/AprilizaVina/submission/main/dashboard/all_data(1).csv")
product_df = pd.read_csv("https://raw.githubusercontent.com/AprilizaVina/submission/main/dashboard/all_data(2).csv")
city_df = pd.read_csv("https://raw.githubusercontent.com/AprilizaVina/submission/main/dashboard/all_data(3).csv")

# Filter data
with st.sidebar:
    # Menambahkan judul
    st.markdown("# Online Shop Reporting 🛒")


# Menyiapkan berbagai Data Frame
sum_order_payment_df = create_sum_order_payment_df(payment_df)
sum_product_category_df = create_sum_product_category_df(product_df)
sum_seller_city_df = create_sum_seller_city_df(city_df)

# Metode Pembayaran yang paling banyak digunakan
st.header('E-Comerce Dashboard :sparkles:')
st.subheader('Most Used Payment Method')

fig, ax = plt.subplots(nrows=1, ncols=1, figsize=(24, 6))
 
colors = ["#72BCD4", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3"]

sns.barplot(x="payment_type", y="order_item_id", data=sum_order_payment_df.head(), palette=colors, ax=ax)
ax.set_ylabel(None)
ax.set_xlabel(None)
ax.set_title("Payment Methods Mostly Uses", loc="center", fontsize=15)
ax.tick_params(axis ='y', labelsize=12)

st.pyplot(fig)

# Product yang paling banyak terjual dan paling sedikit terjual
st.subheader('Best & Worst Performing Products')

fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(24, 6))
 
colors = ["#72BCD4", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3"]
 
sns.barplot(x="order_item_id", y="product_category_name", data=sum_product_category_df.head(5), palette=colors, ax=ax[0])
ax[0].set_ylabel(None)
ax[0].set_xlabel(None)
ax[0].set_title("Best Performing Product", loc="center", fontsize=15)
ax[0].tick_params(axis ='y', labelsize=12)
 
sns.barplot(x="order_item_id", y="product_category_name", data=sum_product_category_df.sort_values(by="order_item_id", ascending=True).head(5), palette=colors, ax=ax[1])
ax[1].set_ylabel(None)
ax[1].set_xlabel(None)
ax[1].invert_xaxis()
ax[1].yaxis.set_label_position("right")
ax[1].yaxis.tick_right()
ax[1].set_title("Worst Performing Product", loc="center", fontsize=15)
ax[1].tick_params(axis='y', labelsize=12)
 
plt.suptitle("Best and Worst Performing Product by Number of Sales", fontsize=20)

st.pyplot(fig)

# Kota dengan penjualan tertinggi
st.subheader('Best Performing City')

fig, ax = plt.subplots(nrows=1, ncols=1, figsize=(24, 6))
 
colors = ["#72BCD4", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3"]
 
sns.barplot(x="order_item_id", y="seller_city", data=sum_seller_city_df.head(10), palette=colors, ax=ax)
ax.set_ylabel(None)
ax.set_xlabel(None)
ax.set_title("Best Performing City", loc="center", fontsize=15)
ax.tick_params(axis ='y', labelsize=12)

st.pyplot(fig)

st.caption('Copyright © Apriliza Vina')