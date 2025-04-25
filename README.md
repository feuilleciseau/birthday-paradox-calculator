# Birthday Paradox Calculator

A simple and interactive Python application with a graphical interface to explore the **Birthday Paradox**.
You can input a group size to compute the probability that at least two people share a birthday, or input a desired probability to find the minimum number of people needed.
It also includes a graph to visualize how the probability evolves with group size.

## Features

- Input a **group size** to get the probability (%)
- Input a **target probability** (%) to get the required group size
- Display a **graph** of probability vs. number of people (Matplotlib)

## Requirements

- Python 3.8 or higher  
- Required Python libraries :
  - `matplotlib`

## Installation

### 1. Install Python

If you don’t have Python installed, download it from:  
[https://www.python.org/downloads/](https://www.python.org/downloads/)

### 2. Clone the project

```bash
git clone git@github.com:feuilleciseau/birthday-paradox-calculator.git
cd birthday-paradox-calculator
```

### 3. Create a virtual environment (optional but recommended)

```bash
python -m venv venv
source venv/bin/activate     # On macOS/Linux
venv\Scripts\activate        # On Windows
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

## How to Run

```bash
python main.py
```

A window will open where you can:
- Enter a number of people to get the birthday match probability
- Enter a probability (%) to get the minimum group size
- Click "Show Graph" to see the curve

## Files Overview

```bash
birthday_paradox_calculator/
├── main.py                     # Main GUI script
├── birthday_paradox.py         # Logic & graph functions
├── requirements.txt            # List of dependencies
├── LICENSE                     # License file (MIT License)
└── README.md                   # This file
```

## Examples

- 23 people → ~50.73% chance that two share a birthday
- For at least 99% chance → Need 57 people

## License

Made by Feuille Ciseaux

MIT License – Free to use, modify, and share!
