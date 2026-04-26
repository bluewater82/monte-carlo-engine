import random
import math
import matplotlib.pyplot as plt
import numpy as np

"""
Monte Carlo Simulation for Estimating Pi

This module runs repeated simulation to estimate the value of pi, tracks convergence behavior, and visualizes error over time.
"""



def generate_checkpoints(total_trials, num_points=100):
    num_points = min(num_points, total_trials)

    return sorted(set(
        int(total_trials * i / num_points)
        for i in range(1, num_points + 1)
    ))

def generate_independent_estimates(checkpoints, samples_per_checkpoint=10):
    independent_results = []

    total_batches = len(checkpoints) * samples_per_checkpoint
    completed_batches = 0

    for n in checkpoints:
        for _ in range(samples_per_checkpoint):
            inside_circle = 0

            for _ in range(n):
                x = random.uniform(-1, 1)
                y = random.uniform(-1, 1)

                if x * x + y * y <= 1:
                    inside_circle += 1

            estimate = 4 * inside_circle / n
            error = abs(math.pi - estimate)

            independent_results.append({
                "trials": n,
                "estimate": estimate,
                "error": error
            })

            completed_batches += 1
            percent = (completed_batches / total_batches) * 100
            print(f"Generating independent estimates... {percent:.1f}%", end="\r")

    print("Generating independent estimates... 100.0%")
    return independent_results

def estimate_pi(total_trials, num_points=100):
    """
    Driver function for the pi esimator. Generates random points in a square bounded by x,y ∈ [-1, 1].
    
    Each trial determines if the point falls within the unit circle. Hits are tallied and then divided by the total number of trials and normalized then recorded.

    Parameters:
        total_trials: user-defined number of times the function runs
        num_points: determines resolution of plot

    Returns:
        results (dict list):
            - 'trials': number of trials
            - 'estimate': pi estimate
            - 'error': esimation error


    """
    
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
        print(f"Generating convergence data... {percent:.1f}%", end="\r")
        


        if trial in checkpoint_set:
            estimate = 4 * inside_circle / trial
            error = abs(math.pi - estimate)

            results.append({
                "trials": trial,
                "estimate": estimate,
                "error": error
            })

    print("Generating convergence data... 100.0%")
    independent_results = generate_independent_estimates(
        checkpoints,
        samples_per_checkpoint=10
    )

    return results, independent_results

def print_statistics(results, independent_results):
    """
    Print summary statistics for the Monte Carlo simulation.

    Parameters:
        results (list of dict): running (cumulative) estimates
        independent_results (list of dict): independent batch estimates
    """
    import numpy as np
    import math
    from collections import defaultdict

    print("\n" + "="*50)
    print("Monte Carlo π Simulation Statistics")
    print("="*50)

    # ---------------------------
    # Running estimate stats
    # ---------------------------
    final = results[-1]
    final_estimate = final["estimate"]
    final_error = final["error"]

    print("\n[Running Estimate]")
    print(f"Final estimate:        {final_estimate:.6f}")
    print(f"True π value:          {math.pi:.6f}")
    print(f"Final absolute error:  {final_error:.6f}")

    # ---------------------------
    # Independent estimate stats
    # ---------------------------
    estimates = np.array([item["estimate"] for item in independent_results])

    mean_estimate = np.mean(estimates)
    std_dev = np.std(estimates)
    mean_abs_error = np.mean(np.abs(estimates - math.pi))

    print("\n[Independent Estimates]")
    print(f"Mean estimate:         {mean_estimate:.6f}")
    print(f"Standard deviation:    {std_dev:.6f}")
    print(f"Mean absolute error:   {mean_abs_error:.6f}")

    # ---------------------------
    # Convergence behavior (by checkpoint)
    # ---------------------------
    grouped = defaultdict(list)

    for item in independent_results:
        grouped[item["trials"]].append(item["estimate"])

    # Look at final checkpoint
    max_n = max(grouped.keys())
    final_group = np.array(grouped[max_n])

    print("\n[Final Checkpoint Distribution]")
    print(f"Trials at checkpoint:  {max_n}")
    print(f"Mean estimate:         {np.mean(final_group):.6f}")
    print(f"Std deviation:         {np.std(final_group):.6f}")
    print(f"Mean abs error:        {np.mean(np.abs(final_group - math.pi)):.6f}")

    print("="*50 + "\n")

def statistics_report(results, independent_results, total_trials):
    import numpy as np
    import math
    from collections import defaultdict
    import matplotlib.pyplot as plt

    # ---------------------------
    # Compute statistics
    # ---------------------------
    final = results[-1]
    final_estimate = final["estimate"]
    final_error = final["error"]

    estimates = np.array([item["estimate"] for item in independent_results])

    mean_estimate = np.mean(estimates)
    std_dev = np.std(estimates)
    mean_abs_error = np.mean(np.abs(estimates - math.pi))

    grouped = defaultdict(list)
    for item in independent_results:
        grouped[item["trials"]].append(item["estimate"])

    max_n = max(grouped.keys())
    final_group = np.array(grouped[max_n])

    # ---------------------------
    # Table data
    # ---------------------------
    table_data = [
    ["Total Trials", f"{total_trials}"],
    ["Final Estimate", f"{final_estimate:.6f}"],
    ["True π", f"{math.pi:.6f}"],
    ["Final Abs Error", f"{final_error:.6f}"],
    ["", ""],
    ["Mean Estimate", f"{mean_estimate:.6f}"],
    ["Std Deviation", f"{std_dev:.6f}"],
    ["Mean Abs Error", f"{mean_abs_error:.6f}"],
    ["", ""],
    ["Final Checkpoint (n)", f"{max_n}"],
    ["Checkpoint Mean", f"{np.mean(final_group):.6f}"],
    ["Checkpoint Std Dev", f"{np.std(final_group):.6f}"],
]

    # ---------------------------
    # Create figure (dark theme)
    # ---------------------------
    fig, ax = plt.subplots(figsize=(8, 6))

    # Set background colors
    fig.patch.set_facecolor("black")
    ax.set_facecolor("black")
    ax.axis("off")

    # ---------------------------
    # Create table
    # ---------------------------
    table = ax.table(
        cellText=table_data,
        colLabels=["Metric", "Value"],
        loc="center",
        cellLoc="left"
    )

    table.auto_set_font_size(False)
    table.set_fontsize(11)
    table.scale(1, 1.5)

    # ---------------------------
    # Style cells (dark mode)
    # ---------------------------
    for (row, col), cell in table.get_celld().items():
        cell.set_facecolor("black")
        cell.set_edgecolor("white")
        cell.get_text().set_color("white")

        # Header row styling
        if row == 0:
            cell.set_facecolor("#222222")
            cell.get_text().set_weight("bold")

    # ---------------------------
    # Title styling
    # ---------------------------
    ax.set_title(
        "Monte Carlo π Simulation Report",
        fontsize=14,
        color="white",
        pad=20
    )

    plt.tight_layout()
    plt.show(block=False)
    plt.pause(0.001)

def convergence_plot(results, total_trials, independent_results=None):
    """
    Function to plot convergence behavior of the Monte Carlo simulation.

    Parameters:
        results (dict list):
            - 'trials': number of trials
            - 'estimate': pi estimate
            - 'error': esimation error
    
    Returns:
        none
    
    """
    trials = [item["trials"] for item in results]
    errors = [item["error"] for item in results]
    estimates = [item["estimate"] for item in results]

    fig, (ax_top, ax_bottom) = plt.subplots(2, 1, sharex=False, figsize=(18, 10))

    # ---------------------------
    # TOP PLOT (Linear scale)
    # ---------------------------
    ax_top.plot(trials, errors, marker="o", color="red", label="Absolute Error")
    ax_top.set_ylabel("Absolute Error", color="red")
    

    ax_estimate = ax_top.twinx()
    ax_estimate.plot(trials, estimates, marker="s", linestyle="--", color="blue", label="Pi Estimate")
    if independent_results is not None:
        independent_trials = [item["trials"] for item in independent_results]
        independent_estimates = [item["estimate"] for item in independent_results]

        ax_estimate.scatter(
            independent_trials,
            independent_estimates,
            alpha=0.25,
            s=20,
            label="Independent Estimates"
        )
    ax_estimate.axhline(math.pi, linestyle=":", color="green", label="True Pi")
    ax_estimate.set_ylabel("Pi Estimate", color="blue")
    if total_trials < 2000:
        ax_top.set_ylim(0, 0.75)
        ax_estimate.set_ylim(1.5, 4.5)
    else:
        ax_top.set_ylim(0, 0.2)
        ax_estimate.set_ylim(3.05, 3.25)

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