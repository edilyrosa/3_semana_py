import streamlit as st

st.title("🛒 Producto destacado")

productos = [
    [
        "Backpack for Laptops",
        "https://fakestoreapi.com/img/81fPKd-2AYL._AC_SL1500_t.png",
        89.99,
        "Fits 15 Laptops"
    ],
    [
        "Mens Casual T-Shirts",
        "https://fakestoreapi.com/img/71-3HjGNDUL._AC_SY879._SX._UX._SY._UY_t.png",
        9.01,
        "men's clothing",
    ],
    
]

# Ciclo for (iterables)
for producto in productos:
    st.image(producto[1], width=250)
    st.subheader(producto[0])
    st.write("💲 Precio:", producto[2])
    st.write("📝", producto[3])
    st.divider()




# TODO: Cliclos Anidados - Matrices.
#? Explicacion ir a: 4_ciclos_anidados_matrices.py