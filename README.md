# Micro Turbine Energy Simulation

A Streamlit simulation for estimating how much electrical power a small turbine could generate from water flow in a pipeline.

The project is educational: it helps visualize how flow rate, head difference, and efficiency affect theoretical power output.

## Project Goal

The simulation explores a micro-hydropower idea for wastewater or water pipeline systems. It does not claim to be an engineering design tool; it is a simple model for learning and early concept testing.

## Formula

```text
P = rho * g * Q * h * eta
```

Where:

- `P` = power in watts
- `rho` = water density, usually about `1000 kg/m3`
- `g` = gravitational acceleration, `9.81 m/s2`
- `Q` = flow rate in `m3/s`
- `h` = head difference in meters
- `eta` = turbine efficiency from `0` to `1`

## Features

- Interactive Streamlit interface.
- Adjustable flow rate, head, and efficiency inputs.
- Automatic power calculation.
- Matplotlib graph for flow rate vs. power output.
- Simple educational explanation of the model.

## Tech Stack

- Python 3.9+
- Streamlit
- Matplotlib

## Run Locally

Clone the repository:

```bash
git clone https://github.com/Alibehram11/micro-turbine-energy.git
cd micro-turbine-energy
```

Install dependencies:

```bash
pip install streamlit matplotlib
```

Run the app:

```bash
streamlit run app.py
```

Open the local Streamlit URL in your browser:

```text
http://localhost:8501
```

## Deployment

The app can be deployed on Streamlit Community Cloud after connecting this GitHub repository. Add the live URL here after deployment.

## Limitations

This model is simplified. Real wastewater turbine design also requires pipe geometry, solids and debris handling, maintenance access, flow variation, pressure constraints, turbine selection, and safety review.

## Author

Ali Behram Albayrak
