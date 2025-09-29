import pickle
import pandas as pd
import streamlit as st
import scorecardpy as sc

# Deserializar (cargar en otro programa)
with open('./models/scorecard.pkl', 'rb') as f:
    card = pickle.load(f)

# --- Título principal ---
st.title("🔎 Detección de fraude")

st.write("Por favor selecciona las características para calcular el score de fraude:")

# --- Campos categóricos ---
campo1 = st.selectbox("AddressChange_Claim", ["no change", "1 year","4 to 8 years","2 to 3 years","under 6 months"])
campo2 = st.selectbox("NumberOfSuppliments", ["more than 5", "3 to 5", "none", "1 to 2"])
campo3 = st.selectbox("BasePolicy", ["Liability", "Collision", "All perils"])
campo4 = st.selectbox("Fault", ["Third Party", "Policy Holder"])

# --- Botón para procesar ---
if st.button("Calcular Score"):
    # Creamos el registro
    cliente = pd.DataFrame({"AddressChange_Claim": [campo1],
                            "NumberOfSuppliments": [campo2],
                            "BasePolicy": [campo3],
                            "Fault": [campo4]
                  })
    st.write(cliente)
    calificacion_df = sc.scorecard_ply(cliente, card, print_step=0, only_total_score=False)
    st.write(calificacion_df)
    score = calificacion_df["score"].iloc[0]

    # --- Mostrar resultado en tamaño grande ---
    st.markdown(
        f"<h1 style='text-align:center; color:#2E86C1;'>Score: {score}</h1>",
        unsafe_allow_html=True
    )
