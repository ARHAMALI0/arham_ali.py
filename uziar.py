import streamlit as st

def main():
    st.title("Food Ordering Website")
    st.markdown(open("index.html").read(), unsafe_allow_html=True)

if __name__ == "__main__":
    main()
    <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Food Ordering Website</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <header>
        <h1>Food Ordering Website</h1>
    </header>
    <main>
        <section class="menu">
            <h2>Menu</h2>
            <ul>
                <li>Pizza</li>
                <li>Burger</li>
                <li>Salad</li>
                <!-- Add more items as needed -->
            </ul>
        </section>
        <section class="order">
            <h2>Your Order</h2>
            <ul id="order-list">
                <!-- Order items will be added dynamically -->
            </ul>
        </section>
    </main>
    <footer>
        <button id="place-order-btn">Place Order</button>
    </footer>
    <script src="script.js"></script>
</body>
</html>
body {
    font-family: Arial, sans-serif;
    margin: 0;
    padding: 0;
}

header, footer {
    background-color: #333;
    color: white;
    padding: 10px;
    text-align: center;
}

main {
    display: flex;
    justify-content: space-around;
    padding: 20px;
}

.menu, .order {
    width: 40%;
}

ul {
    list-style-type: none;
    padding: 0;
}

li {
    padding: 5px;
    cursor: pointer;
}

button {
    padding: 10px 20px;
    background-color: #4CAF50;
    color: white;
    border: none;
    cursor: pointer;
    border-radius: 5px;
}

button:hover {
    background-color: #45a049;
}
document.addEventListener("DOMContentLoaded", function() {
    const menuItems = document.querySelectorAll('.menu li');
    const orderList = document.getElementById('order-list');

    menuItems.forEach(item => {
        item.addEventListener('click', () => {
            const listItem = document.createElement('li');
            listItem.textContent = item.textContent;
            orderList.appendChild(listItem);
        });
    });

    const placeOrderBtn = document.getElementById('place-order-btn');
    placeOrderBtn.addEventListener('click', () => {
        alert('Your order has been placed!');
        orderList.innerHTML = '';
    });
});

