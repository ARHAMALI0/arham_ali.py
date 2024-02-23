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
