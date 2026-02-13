import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title('Graficas desde listas usando un DataFrame')
categorias = st.text_input('Digita las categorias, separadas por coma: "," ', 'Ana,Luis,Carlos,Maria')
datos = st.text_input('Digita las DATOS, separadas por coma: "," ', '18,15,12,20')


if st.button('Genera el grafico'):
    #* CASTING
    # Convertir el srt a list
    lista_categorias  = categorias.split(',')
    lista_datos_str  = datos.split(',')
    # Convertir la lista-str a list-float
    lista_datos_num = [ float(n) for n in lista_datos_str]
    
    # creamos el dataframe
    df = pd.DataFrame({
        'Categorias': lista_categorias,
        'Datos':  lista_datos_num
    })

    st.write('📊 Datafarme generado')
    st.dataframe(df)

# opcion = st.select()
    #* creamos el grafico: muetsralo dependiendo de la opcion q usuario hixo clic en el select
    fig, ax = plt.subplots()
    # ax.bar(df['Categorias'], df['Datos'])
    # ax.barh(df['Categorias'], df['Datos'])
    # ax.scatter(df['Categorias'], df['Datos'], color='Red')
    ax.plot(df['Categorias'], df['Datos'], marker='o')

    ax.set_title('Grafrico de datos')
    ax.set_xlabel('Categorias')
    ax.set_ylabel('Datos')

    st.pyplot()
