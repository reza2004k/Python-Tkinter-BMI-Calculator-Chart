# 🏋️ Python Tkinter BMI Calculator & Chart Visualizer
/
This project is a simple, interactive application that calculates a person's Body Mass Index (BMI) and provides a **visual representation** of where their result falls on a standard BMI chart. It combines GUI development with data plotting for a user-friendly health tool.

## ✨ Core Features

* **BMI Calculation:** Calculates BMI using the formula: $BMI = \frac{Weight (kg)}{Height (m)^2}$.
* **Graphical Interface (Tkinter):** Provides input fields for **weight (kg)** and **height (m)**, and buttons to calculate and display the results.
* **Matplotlib Visualization:** Generates a **custom BMI Chart** 

[Image of sample data visualization charts]
 using Matplotlib, plotting the user's specific height and weight against defined BMI ranges (Underweight, Normal, Overweight).
* **Annotated Results:** The chart visually indicates the user's current status (e.g., "Normal weight") and, for underweight individuals, suggests the weight needed to reach the normal range.

## 🛠️ Technologies Used

* **Language:** Python 3
* **GUI Framework:** **Tkinter** (Standard Python GUI library)
* **Visualization Libraries:**
    * **`matplotlib.pyplot`:** Used for creating the customized chart.
    * **`numpy`:** Used for numerical operations, specifically creating axes scales (`linspace`).

## 🚀 Getting Started

To run this application, you must install the necessary Python libraries.

### Prerequisites

* Python 3 installed on your system.
* The required libraries:

    ```bash
    pip install matplotlib numpy
    # Tkinter is usually included with standard Python installations.
    ```

### Installation and Running

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/YOUR_USERNAME/Python-Tkinter-BMI-Calculator-Chart.git](https://github.com/YOUR_USERNAME/Python-Tkinter-BMI-Calculator-Chart.git)
    cd Python-Tkinter-BMI-Calculator-Chart
    ```
2.  **Run the Application:**
    Execute the Python script from your terminal:
    ```bash
    python BMI.py
    ```
    The main Tkinter window will appear.

### Usage Flow

1.  Enter your **Weight** in kilograms (kg) and **Height** in meters (m).
2.  Click the **Calculate** button to see your calculated BMI score displayed in the GUI.
3.  Click the **Chart** button to generate and display the Matplotlib chart, showing where your measurements land on the standard BMI graph.

---
