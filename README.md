# Monte Carlo Simulation Lab

A modular, GUI-driven simulation tool for exploring statistical estimation through Monte Carlo methods.

This project demonstrates how randomness, when sampled repeatedly, converges into predictable structure. It emphasizes both **numerical accuracy** and **visual intuition**, allowing users to observe not just *what* an estimate is—but *how it evolves over time*.

---

## 🖥️ New: Interactive GUI Dashboard

The application now features a **PySide6-based graphical interface**, transforming the project from a terminal tool into a professional simulation environment.

### Key UI Features

- Dark-themed scientific dashboard
- Control panel for simulation parameters
- Embedded Matplotlib plots inside the application window
- Real-time result display
- Dynamic simulation summaries
- Multi-simulation support via dedicated buttons

---

## 🧪 Simulations Included

### 🎲 Expected Value (Weighted Die)

- Simulates a weighted die using probabilistic mapping
- Tracks:
  - Individual rolls
  - Running average (estimate)
  - Error from theoretical expected value (4.2)

---

### 📊 Convergence Visualization

#### Single Run

- Scatter plot of die rolls
- Running estimate line
- Expected value reference line
- Error convergence plot

#### Multi-Run Overlay

- Multiple independent simulations plotted together
- Visualizes variance between runs
- Demonstrates convergence consistency
- Highlights the **Law of Large Numbers**

---

## 🧠 Key Concepts Demonstrated

- Random sampling
- Expected value
- Running averages
- Convergence behavior
- Variance across simulations
- Law of Large Numbers
- Error decay over time

---

## 🧭 GUI Layout Overview

```
┌─────────────────────────────────────────────┐
│ Monte Carlo Simulation Lab                  │
│ Scientific Computing Dashboard              │
├───────────────┬─────────────────────────────┤
│ Controls      │ Plot Display                │
│               │                             │
│ Trial Count   │  Matplotlib Canvas          │
│ Buttons       │                             │
│ Results       │                             │
│ Summary Box   │                             │
└───────────────┴─────────────────────────────┘
```

---

## 📸 GUI Preview

![GUI Screenshot](/reports/gui_screenshot.png)

---

## 🌳 Project Structure

```
monte-carlo-lab/
│
├── main.py                  # Application entry point
├── ui/
│   └── main_window.py       # PySide6 GUI
│
├── simulations/
│   ├── pi_estimator.py
│   ├── expected_value.py
│
└── README.md
```

---

## ▶️ Running the Program

### 1. Clone the repository

```
git clone https://github.com/yourusername/monte-carlo-lab.git
cd monte-carlo-lab
```

---

### 2. Create and activate virtual environment

```
python -m venv venv
venv\Scripts\activate   # Windows
```

---

### 3. Install dependencies

```
pip install matplotlib numpy PySide6
```

---

### 4. Run the application

```
python main.py
```

---

## 🧩 Design Philosophy

This project emphasizes:

- **Separation of concerns**
  - Simulation logic is independent of UI
- **Modularity**
  - Each simulation is self-contained
- **Visual learning**
  - Graphs reinforce statistical understanding
- **Progressive enhancement**
  - CLI → GUI → Full simulation platform

---

## 🚀 Future Enhancements

- Additional simulations (integration, probability models)
- Parameter sliders (instead of text input)
- Tabbed interface for multiple simulations
- Export plots/images
- Real-time animated convergence
- Statistical reports and confidence intervals

---

## 🧪 Why This Project Matters

Monte Carlo methods are foundational in:

- Machine learning
- Financial modeling
- Engineering simulations
- Risk analysis
- Scientific computing

This project builds an intuitive and visual understanding of these techniques.

---

## 🧑‍💻 Author

Andre DeHerrera  
Computer Science Student — University of New Mexico

---

## 📜 License

MIT License
