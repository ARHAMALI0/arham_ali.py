import streamlit as st

# Display raw HTML
st.write("""
    <h1 style='color: blue;'>This is HTML</h1>
    <button>This is a button</button>
""")

# You can also use the `st.markdown` function to render HTML
st.markdown("""
    <h1 style='color: green;'>This is Markdown with HTML</h1>
    <button>This is a button</button>
""", unsafe_allow_html=True)
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
