# Micro Turbine Energy Simulation

Streamlit educational simulation for micro-hydropower energy in pipelines.

## Problem

Micro-hydropower ideas are hard to discuss without a quick way to change flow rate, head difference, and turbine efficiency. This project makes the basic calculation visible for early learning and concept discussion.

## Solution

The app estimates theoretical turbine power from water flow and visualizes how input changes affect output. It is an educational simulation, not an engineering design or deployment tool.

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

## Verification

- Run the Streamlit app locally.
- Change flow rate, head, and efficiency.
- Confirm the calculated power and graph update.
- Compare one manual calculation against the displayed value.

## Demo / Evidence

- Shows a renewable-energy calculation with interactive inputs.
- Uses a transparent formula and plain-language limitations.
- Public roadmap is tracked in GitHub Issues.

## Deployment

The app can be deployed on Streamlit Community Cloud after connecting this GitHub repository. Add the live URL here after deployment.

## Limitations

This model is simplified. Real wastewater turbine design also requires pipe geometry, solids and debris handling, maintenance access, flow variation, pressure constraints, turbine selection, environmental review, and safety review.

## Roadmap

- Separate calculation logic from the Streamlit UI.
- Add a small test for the power formula.
- Add one screenshot or GIF.
- Add deployment link after publishing to Streamlit Community Cloud.

## Status

Educational simulation. Useful as a research/prototype signal, but not a pinned main portfolio project until the code structure, tests, and demo are stronger.

## Author

Ali Behram Albayrak
