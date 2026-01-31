import streamlit as st
st.title('Mis productos... 🛒')

# import requests
# response = requests.get('https://fakestoreapi.com/products')
# productos = response.json()

productos = [
            [
                "Fjallraven - Foldsack No. 1 Backpack, Fits 15 Laptops",
                "https://fakestoreapi.com/img/81fPKd-2AYL._AC_SL1500_t.png",
                109.95,
                "Your perfect pack for everyday use and walks in the forest..."
            ], 
            [
                "Fjallraven - Foldsack No. 1 Backpack, Fits 15 Laptops",
                "https://fakestoreapi.com/img/71-3HjGNDUL._AC_SY879._SX._UX._SY._UY_t.png",
                10.95,
                "Your perfect pack for everyday use and walks in the forest..."
            ],
            [
                "Fjallraven - Foldsack No. 1 Backpack, Fits 15 Laptops",
                "https://fakestoreapi.com/img/71li-ujtlUL._AC_UX679_t.png",
                9.95,
                "Your perfect pack for everyday use and walks in the forest..."
            ]
]


for producto in productos:
    st.image(producto[1], width=250)
    st.subheader(producto[0])
    st.write(' $ Precio: ', producto[2])
    st.write('📋', producto[3])
    st.divider()