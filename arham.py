import streamlit as st

def main():
    st.title("Food Ordering Website")
    st.markdown(open("index.html").read(), unsafe_allow_html=True)

if __name__ == "__main__":
    main()
