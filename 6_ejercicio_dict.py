
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Gráfico desde listas usando DataFrame")

#* Inputs para las listas
categorias = st.text_input("Categorias separados por coma:", "Ana,Luis,Carlos,María")
datos = st.text_input("Datos separadas por coma:", "15,18,12,20")

if st.button("Generar gráfico"): #? 💡Lo siguiente ocurre SI, se hace click en el botón
    
    #************************CASTINGS
    #* Convertir STR a LIST con el metodo split("separador")
    lista_categorias = categorias.split(",")
    lista_datos_str = datos.split(",")

    #* Convertir la LIST-STR de los DATOS a una LIST-FLOAT
    lista_datos_num = [float(n) for n in lista_datos_str]
    
    #* Crear DataFrame: espera un diccionario de listas (con las listas credas arriba)
    df = pd.DataFrame({
        "Categorias": lista_categorias,
        "Datos": lista_datos_num,
    })

    st.write("📊 DataFrame generado:")
    st.dataframe(df)

    #* Crear gráfico
    fig, ax = plt.subplots()
    ax.bar(df["Categorias"], df["Datos"])
    # ax.barh(df["Categorias"], df["Datos"])
    # ax.scatter(df["Categorias"], df["Datos"], color="red")
    # ax.plot(df["Categorias"], df["Datos"], marker='o')
    
    ax.set_title("Grafico de Columnas Agrupadas")
    ax.set_xlabel("Categorias")
    ax.set_ylabel("Quantitativo")

    st.pyplot(fig)
# # TODO: PROXIMO: 
#     #? FUNCIONES en: 1_funciones.py