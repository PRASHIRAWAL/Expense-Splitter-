import streamlit as st
from database import add_expense, get_expenses, delete_expense
import pandas as pd

# 🎀 Set Page Config
st.set_page_config(page_title="Expense Splitter 💸", page_icon="💖", layout="wide")

# 🌸 Custom Header
st.markdown("<h1 style='text-align: center; color: #ff69b4;'>💸 Expense Splitter - Share with Love! 💖</h1>", unsafe_allow_html=True)
st.markdown("Keep track of shared expenses with your friends. No more awkward money talk! 😉💰")

# 💕 Cute Divider
st.markdown("---")

# 💵 **Add a New Expense**
with st.expander("➕ **Add Expense**", expanded=True):
    st.markdown("### ✨ Let's Add an Expense!")
    
    amount = st.number_input("💰 Amount (INR)", min_value=0.0, format="%.2f")
    description = st.text_input("📝 What is this expense for?")
    paid_by = st.text_input("👛 Who paid?")
    split_between = st.text_area("🧍‍♀️🧍‍♂️ Split Between (comma-separated names)")

    if st.button("💖 Split it!"):
        names = [name.strip() for name in split_between.split(",")]
        if len(names) > 0:
            add_expense(amount, description, paid_by, names)
            st.success(f"🎉 Expense added! '{description}' paid by {paid_by} is split among {', '.join(names)}.")
        else:
            st.error("Oops! Please enter valid names. 🙈")

# 🧾 **View Expense List**
st.markdown("## 📃 Your Shared Expenses")
expenses = get_expenses()
expense_data = [{"ID": e[0], "Amount (₹)": e[1], "Description": e[2], "Paid By": e[3], "Split Among": e[4]} for e in expenses]
st.table(pd.DataFrame(expense_data))

# 🗑 **Delete an Expense**
with st.expander("🗑 **Delete Expense**"):
    st.markdown("### ❌ Remove an Expense")
    expense_id = st.number_input("Enter Expense ID to Delete", min_value=1, step=1)
    if st.button("🚮 Delete"):
        delete_expense(expense_id)
        st.success(f"Expense ID {expense_id} removed! Bye-bye! 👋")

# 📊 **Balance Calculation - Who Owes What?**
st.markdown("## 💳 **Who Needs to Pay Up?**")
balances = {}
for e in expenses:
    amount, paid_by, split_between = e[1], e[3], e[4].split(",")
    split_amount = amount / len(split_between)

    if paid_by not in balances:
        balances[paid_by] = 0
    balances[paid_by] += amount

    for person in split_between:
        if person not in balances:
            balances[person] = 0
        balances[person] -= split_amount

# 🌸 Display Cute Balance Cards
st.markdown("### 📌 Balances")
for person, balance in balances.items():
    if balance > 0:
        st.success(f"✨ {person} is **owed ₹{balance:.2f}** 💰")
    elif balance < 0:
        st.error(f"😢 {person} **owes ₹{-balance:.2f}**")
    else:
        st.info(f"🎉 {person} is **all settled up!** 🥳")

# 🎀 Cute Footer
st.markdown("<h4 style='text-align: center; color: #ff69b4;'>Made with ❤️ for friendship & fun! 🎀</h4>", unsafe_allow_html=True)
