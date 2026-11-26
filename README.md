# UTSM Digital Twin

Physics-based energy model of the University of Toronto Super Mileage car. The model predicts energy use per lap from a speed profile, then calibrates against logged laps from the real car.

## Status

Early development. Data prep is in progress.

## Model

- 1D longitudinal point-mass simulation (drag, rolling resistance, grade, inertia)
- Powertrain efficiency converts wheel power to fuel or battery power
- Primary output: energy per lap and energy per distance
- Calibration fits C_dA, C_rr, and efficiency values to measured data

## Structure

```
Source/       Python code
data/raw/     Logger files (not committed)
data/clean/   Output of prep.py
tests/        Hand-calculation checks
notebooks/    Data exploration
results/      Plots and fitted values
car.yaml      Car parameters
config.yaml   Paths and settings
```

## Setup

Requires Python 3.13 (3.14 breaks the Visual Studio debugger).

```
py -3.13 -m venv .venv
.venv\Scripts\activate
python -m pip install -r requirements.txt
```

If PowerShell blocks activation:

```
Set-ExecutionPolicy -Scope CurrentUser RemoteSigned
```

## Run

```
python Source\prep.py
```

## Conventions

- Units: meters, seconds, watts, joules, kilograms. Put units in column and key names (`speed_kmh`, `mass_kg`).
- Branches: `main` plus short-lived branches named `type/short-description` (`feature/`, `fix/`, `docs/`, `chore/`).
- No direct commits to `main` after the initial skeleton; use pull requests.
- Do not commit `.venv/` or large raw logs.

## Data format

Raw logs come from the `utsm_wifi_telemetry` firmware.

- Line 1 is a `#` metadata line; line 2 is the column header; a `# RUN START` line precedes the data.
- Read with `pd.read_csv(path, comment="#")`.
- Rows are ~10 Hz with irregular timestamps (`Millis`).
- Speed, position, and altitude update at 1 Hz and repeat between updates.
- Raw files keep the logger's column names. Clean files use the names in `config.yaml`.
