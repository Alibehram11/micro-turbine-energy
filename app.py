import streamlit as st
import matplotlib.pyplot as plt

# ---------------------------
# 🎯 Title and Introduction
# ---------------------------
st.set_page_config(page_title="Micro Turbine Simulation in Wastewater Systems", page_icon="💧", layout="centered")

st.title("💧 Energy Generation in Wastewater Pipelines Using Micro Turbines")
st.markdown("""
This project simulates the idea of **generating electricity from wastewater flow** using micro turbines.  
Goal: *To convert the kinetic energy of wastewater into electrical energy.* ⚙️  
Developed by **Ali Behram Albayrak**
""")

st.divider()

# ---------------------------
# ⚙️ Input Section
# ---------------------------
st.header("⚙️ Input Parameters")
try:
    Q = st.number_input("Flow rate (m³/s)", min_value=0.001, max_value=10.0, value=3.0, step=0.1)
    h = st.number_input("Head difference (m)", min_value=0.1, max_value=100.0, value=10.0, step=0.5)
    η = st.slider("Efficiency (%)", 10, 100, 85)
    ρ = 1000  # water density (kg/m³)
    g = 9.81  # gravitational acceleration (m/s²)
except (ValueError, TypeError, NameError):
    print("Please enter valid numerical values for all input parameters.")

# ---------------------------
# ⚡ Power Calculation
# ---------------------------
P = ρ * g * Q * h * (η / 100)  # power (Watt)
kW = P / 1000

st.success(f"💡 Turbine Power Output: **{kW:.2f} kW**")

# ---------------------------
# 📊 Graph
# ---------------------------
st.divider()
st.header("📊 Relationship Between Flow Rate and Power")

Q_values = [i / 10 for i in range(1, 21)]
P_values = [ρ * g * q * h * (η / 100) / 1000 for q in Q_values]

fig, ax = plt.subplots()
ax.plot(Q_values, P_values, color="dodgerblue", linewidth=2)
ax.set_xlabel("Flow Rate (m³/s)")
ax.set_ylabel("Power (kW)")
ax.set_title("Flow Rate vs Power Graph")
ax.grid(True)

st.pyplot(fig)

# ---------------------------
# 📘 Information Section
# ---------------------------
st.divider()
st.info("""
**Formula:**  
P = ρ × g × Q × h × η  

Where:  
- ρ: Water density (1000 kg/m³)  
- g: Gravitational acceleration (9.81 m/s²)  
- Q: Flow rate (m³/s)  
- h: Head difference (m)  
- η: Turbine efficiency  

This simulation demonstrates the potential of **micro-hydropower systems**  
for sustainable energy generation from wastewater pipelines. 🌍
""")

