import streamlit as st

# Read HTML file
with open('path/to/your/html/file.html', 'r') as f:
    html_content = f.read()

# Render HTML
st.markdown(html_content, unsafe_allow_html=True)
class Pizza:
    def _init_(self, toppings):
        self.toppings = toppings
        self.price = 10.00  # Base price for a pizza

    def calculate_total(self, quantity):
        return self.price *
