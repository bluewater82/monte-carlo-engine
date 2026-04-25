import random
import math
import matplotlib.pyplot as plt
import numpy as np

def generate_checkpoints(total_trials, num_points=100):
    return sorted(set(
        int(total_trials * i / num_points)
        for i in range(1, num_points + 1)
    ))

def estimate_pi(total_trials, num_points=100):  # with checkpoints
    
    inside_circle = 0
    checkpoints = generate_checkpoints(total_trials, num_points)

    results = []
    checkpoint_set = set(checkpoints)  # faster lookup

    for trial in range(1, total_trials + 1):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)

        if x * x + y * y <= 1:
            inside_circle += 1

        percent = (trial / total_trials) * 100
        print(f"Simulation progress... {percent:.1f}%", end="\r")


        if trial in checkpoint_set:
            estimate = 4 * inside_circle / trial
            error = abs(math.pi - estimate)

            results.append({
                "trials": trial,
                "estimate": estimate,
                "error": error
            })

    return results

def convergence_plot(results):
    trials = [item["trials"] for item in results]
    errors = [item["error"] for item in results]
    estimates = [item["estimate"] for item in results]

    fig, (ax_top, ax_bottom) = plt.subplots(2, 1, sharex=False, figsize=(8, 10))

    # ---------------------------
    # TOP PLOT (Linear scale)
    # ---------------------------
    ax_top.plot(trials, errors, marker="o", color="red", label="Absolute Error")
    ax_top.set_ylabel("Absolute Error", color="red")
    ax_top.set_ylim(0, 0.2)

    ax_estimate = ax_top.twinx()
    ax_estimate.plot(trials, estimates, marker="s", linestyle="--", color="blue", label="Pi Estimate")
    ax_estimate.axhline(math.pi, linestyle=":", color="green", label="True Pi")
    ax_estimate.set_ylabel("Pi Estimate", color="blue")
    ax_estimate.set_ylim(3.0, 3.3)

    ax_top.set_title("Monte Carlo π Convergence (Linear Scale)")
    ax_top.set_xlabel("Number of Trials")
    ax_top.grid(True)

    lines1, labels1 = ax_top.get_legend_handles_labels()
    lines2, labels2 = ax_estimate.get_legend_handles_labels()
    ax_top.legend(lines1 + lines2, labels1 + labels2, loc="best")

    # ---------------------------
    # BOTTOM PLOT (Log-log scale)
    # ---------------------------
    n = np.array(trials)
    err = np.array(errors)

    # Avoid log(0), which is undefined
    mask = err > 0
    n = n[mask]
    err = err[mask]

    ax_bottom.plot(
        n,
        err,
        marker="o",
        color="red",
        label="Absolute Error"
    )

    # Theoretical Monte Carlo convergence rate: error ∝ 1 / sqrt(n)
    theory = err[0] * (n[0] / n) ** 0.5

    ax_bottom.plot(
        n,
        theory,
        linestyle="--",
        color="green",
        label="Theory: 1/√n slope"
    )

    # Empirical fitted slope from actual simulation data
    log_n = np.log(n)
    log_err = np.log(err)

    slope, intercept = np.polyfit(log_n, log_err, 1)
    fit_line = np.exp(intercept) * n ** slope

    ax_bottom.plot(
        n,
        fit_line,
        linestyle="-.",
        color="purple",
        label=f"Empirical fit: slope = {slope:.3f}"
    )

    ax_bottom.set_xscale("log")
    ax_bottom.set_yscale("log")
    ax_bottom.set_xlabel("Number of Trials (log scale)")
    ax_bottom.set_ylabel("Absolute Error (log scale)")
    ax_bottom.set_title("Monte Carlo π Error Convergence (Log-Log Scale)")
    ax_bottom.grid(True, which="both")
    ax_bottom.legend()

    plt.tight_layout()
    plt.show()