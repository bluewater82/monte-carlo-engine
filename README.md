# Monte Carlo Simulation Engine

A modular, terminal-based simulation tool for exploring statistical estimation through Monte Carlo methods.

This project demonstrates how randomness, when sampled repeatedly, converges into predictable structure. It focuses on both **numerical results** and **visual insight**, allowing users to observe not just *what* an estimate is—but *how it evolves over time*.

---

## 🚀 Features

### π Estimation via Monte Carlo

* Estimates π using random sampling in a 2D unit square
* Uses geometric probability:

  * Ratio of points inside a unit circle vs total points
* Demonstrates convergence toward π as trials increase

---

### 📊 Convergence Visualization

#### Dual-Plot System

**Top Plot (Linear Scale):**

* Absolute error vs number of trials
* π estimate vs number of trials (secondary axis)
* Horizontal reference line at true π value

**Bottom Plot (Log-Log Scale):**

* Absolute error on log scale
* Reveals convergence rate visually
* Includes:

  * Theoretical ( 1/\sqrt{n} ) convergence line
  * Empirical best-fit slope from simulation data

---

### 🔬 Statistical Insight

* Demonstrates **Law of Large Numbers**

* Shows that Monte Carlo error follows:

  1/sqrt(n)

* Compares:

  * Theoretical convergence behavior
  * Actual simulation results

---

### ⚙️ Dynamic Simulation Control

* User-defined number of trials
* Automatically generated checkpoints (default: 100)
* High-resolution convergence tracking

---

### 📈 Real-Time Feedback

* Terminal-based progress indicator:

  ```
  Simulation progress... 43.2%
  ```
* Efficient update frequency to avoid performance degradation

---

## 🧠 Key Concepts Demonstrated

* Random sampling
* Geometric probability
* Running averages (cumulative estimators)
* Statistical convergence
* Error analysis
* Logarithmic scaling
* Model vs empirical comparison

---

## 🌳 Project Structure

```
monte-carlo-engine/
│
├── main.py
├── simulations/
│   ├── pi_estimator.py
│   ├── expected_value.py (planned)
│   ├── probability_estimator.py (planned)
│   └── integrations.py (planned)
│
├── stats/ (planned)
│   ├── summary.py
│   ├── confidence_interval.py
│   └── distributions.py
│
├── user_interface/ (planned)
│   └── menu.py
│
└── README.md
```

---

## ▶️ Running the Program

### 1. Clone the repository

```
git clone https://github.com/yourusername/monte-carlo-engine.git
cd monte-carlo-engine
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
pip install matplotlib numpy
```

---

### 4. Run the program

```
python main.py
```
User will be prompted for number of desired trials to run.

---

## 📌 Example Output

### Terminal

Currently a work in progress, simply prompts user for desired number of trials and then displays the progress indicator while the simulation runs.

### Visualization

* Top plot: curved convergence toward π
* Bottom plot: linear trend on log-log scale showing ( n^{-1/2} ) behavior vs empirical slope (fit line)

![Example output](/reports/Figure_1.png)

---

## 🔧 Design Philosophy

This project emphasizes:

* **Clarity over complexity** — start with simple functions, scale when needed
* **Modularity** — each simulation is self-contained
* **Insight-driven output** — focus on understanding behavior, not just computing values

---

## 📈 Future Enhancements

* Additional simulations:

  * Expected value estimation
  * Probability simulations
  * Monte Carlo integration
* Multi-run overlays (variance between simulations)
* Confidence interval visualization
* Log-scale toggles and UI controls
* Export plots and results to files
* CLI menu system for simulation selection
* Performance optimizations with NumPy

---

## 🧪 Why This Project Matters

Monte Carlo methods are used in:

* Physics simulations
* Financial modeling
* Machine learning
* Engineering systems
* Risk analysis

This project builds an intuitive and visual foundation for those applications.

---

## 🧑‍💻 Author

Andre DeHerrera
Computer Science Student — University of New Mexico

---

## 📜 License

MIT License 
