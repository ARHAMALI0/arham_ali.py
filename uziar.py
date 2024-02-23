import streamlit as st

# Title of the app
st.title("Food Order App")

# List of food items
food_items = ["Pizza", "Burger", "Pasta"]
selected_item = st.selectbox("Select an item", food_items)

if selected_item == "Pizza":
    toppings = ["Pepperoni", "Mushrooms", "Olives", "Bell Peppers"]
    selected_toppings = st.multiselect("Choose toppings", toppings)

    sizes = ["Small", "Medium", "Large"]
    selected_size = st.selectbox("Select size", sizes)

    quantity = st.number_input("Quantity", value=1)
    

if selected_item == "burger":
    patie = ["chicken","beef","allo ticke"]
    vegetables = st.multiselect("onion","cabbage","tamato")
    quantity = st.number-input("quantity",value=1)

    if st.button("Order Now"):
        st.write(f"You have ordered {quantity} {selected_size} {selected_item}(s) with:")
        st.write(', '.join(selected_toppings))
