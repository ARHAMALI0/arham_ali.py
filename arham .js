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
