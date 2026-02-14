import streamlit as st
import requests 
def obtener_productos(): #& return Data | None, None| Error
    url = 'https://fakestoreapi.com/products'
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        return response.json(), None
    except requests.exceptions.Timeout:
        msg = 'Problemas del servidor, esta demorando mucho!'
        return None, msg
    except requests.exceptions.RequestException as e:
        return None, str(e)

productos, error = obtener_productos()

if error:
    st.error('❌ Oops Error al cargar los datos')
    st.info('⚠️ Sugerencia: Mira tu conexion..')

elif productos:
    for producto in productos:
        with st.container():
            col1, col2 = st.columns([1, 3])
            with col1:
                st.image(producto["image"], use_container_width=True)
            
            # with col2: