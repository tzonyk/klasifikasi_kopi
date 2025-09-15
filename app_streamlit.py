import streamlit as st
import pandas as pd
import joblib

model = joblib.load("model_klasifikasi_kualitas_kopi.joblib")
st.title("Klasifikasi Kualitas Kopi")
st.markdown("Prediksi kualitas kopi berdasarkan Kadar Kafein, Tingkat Keasaman dan Jenis Proses")

kadar_kafein = st.slider("Kadar Kafein", 50.0, 200.0, 110.0)
tingkat_keasaman = st.slider("Tingkat Keasaman", 1.0, 7.0, 5.0)
jenis_proses = st .pills("Jenis Proses", ["Natural", "Honey", "Washed"], default="Natural")

if st.button("Prediksi", type="primary"):
	data_baru = pd.DataFrame([[110, 4.5, "Honey"]],columns=["Kadar Kafein", "Tingkat Keasaman", "Jenis Proses"])

	prediksi = model.predict(data_baru)[0]
	presentase = max(model.predict_proba(data_baru)[0])
	st.success(f"Prediksi {prediksi} dengan tingkat keyakinan {presentase*100:.2f}%")
	st.balloons()

st.divider()
st.caption("Dibuat dengan :coffee: oleh Toni Kurniawan")