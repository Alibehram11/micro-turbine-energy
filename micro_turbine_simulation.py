# micro_turbine_simulation.py
# Energy Production with Micro Turbines in Wastewater Pipelines (Basic Simulation)
# Prepared by: Ali Behram Albayrak

import matplotlib.pyplot as plt
import sys

# --- Constants ---
rho = 1000       # Water density (kg/m³)
g = 9.81         # Gravity (m/s²)
print("For Example")
print("""
    Flow rate (m³/s): 0.02  
    Head difference (m): 5  
    Turbine efficiency (%): 75  
    Pipe diameter (mm): 100  
    Pipe internal pressure (bar): 3
""")

print("Micro Turbine Simulation in Wastewater Pipelines\n")
while True:
    try:
        Q = float(input("Flow rate (m³/s): "))              # Water flow rate
        h = float(input("Head difference (m): "))           # Height difference at turbine outlet
        eta = float(input("Turbine efficiency (%): ")) / 100  # Efficiency as percentage
        pipe_diameter = float(input("Pipe diameter (mm): ")) / 1000  # Convert to meters
        pressure = float(input("Pipe internal pressure (bar): ")) * 1e5  # Convert to Pascal
    except (ValueError, NameError):
        print("Please enter a valid value.")
        continue
    break

power = rho * g * Q * h * eta            # Power (Watt)
energy_per_hour = power * 3600 / 1e6     # Energy in kWh
wear_rate = (pressure / 1e6) * (Q / 0.01) * 0.1  # Simple wear estimation (%)

print("\n--- RESULTS ---")
print(f"Generated Power: {power:.2f} W")
print(f"Hourly Energy: {energy_per_hour:.3f} kWh")
print(f"Estimated Wear Rate: {wear_rate:.2f}%")

Q_values = [q/1000 for q in range(1, 101)]  # Flow rates between 0.001–0.1 m³/s
P_values = [rho * g * q * h * eta for q in Q_values]

plt.plot(Q_values, P_values, color='blue')
plt.title("Flow Rate - Power Relationship (Micro Turbine)")
plt.xlabel("Flow Rate (m³/s)")
plt.ylabel("Power (W)")
plt.grid(True)
plt.show()
print("for more information, send email to: alibehram11.albarktar@gmail.com")