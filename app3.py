
import streamlit as st
import mi_negocio
import calculos
import pdf_presupuesto

st.title("Fornite Kiosco")

EFECTIVO = "efectivo"
TRANSFERENCIA = "transferencia"
IVA = 0.21

cliente = st.text_input("ingrese su nombre")
RENGLONES = 3

nombres = []
cantidades = []
precios_unitarios = []

for i in range(RENGLONES):
    producto = st.selectbox(
        f"Producto {i + 1}",
        mi_negocio.productos,
        key=f"p_{i}"
    )

    cantidad = st.number_input(
        f"Cantidad {i + 1}",
        min_value=0,
        step=1,
        key=f"c_{i}"
    )

    if cantidad > 0:
        pos = calculos.buscar_posicion(mi_negocio.productos, producto)
        nombres.append(producto)
        cantidades.append(cantidad)
        precios_unitarios.append(mi_negocio.precios[pos])

pago = st.radio("ingrese como va a pagar", [EFECTIVO, TRANSFERENCIA])

# Calcula la suma multiplicando el precio por la cantidad de los 3 renglones
subtotal = sum(p * c for p, c in zip(precios_unitarios, cantidades))

if len(nombres) != 0:
    descuento, subtotal_desc = calculos.calcular_descuento(pago, subtotal)
    total, iva = calculos.calcular_iva(subtotal_desc, IVA, subtotal)

    st.write("el precio del articulo en pavos es =>", precios_unitarios)
    st.write("el sub total de pavos es de => ", subtotal)
    st.write("total con descuento de pavos aplicado es de =>  ", subtotal_desc)
    st.write("el precio con iva de epic es de => ", total)

    numero = st.text_input("cual es el numero de compra")
    fecha = st.date_input("que dia es hoy")

    if st.button("Generar presupuesto"):
         
        archivo = pdf_presupuesto.armar_pdf(
            numero=numero,
            fecha=fecha,
            cliente=cliente,
            producto=nombres,
            cantidad=cantidades,
            precio=precios_unitarios,
        subtotal=subtotal,
        descuento=descuento,
        iva=iva,
        total=total,
        nombres=nombres,
        cantidades=cantidades,
        precios_unitarios=precios_unitarios
)

        st.download_button(
            "Descargar presupuesto de la tienda de EPIC GAMES (PDF)",
            archivo,
            file_name=f"presupuesto_{numero}.pdf",
            mime="application/pdf"
        )
