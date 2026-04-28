import random
import matplotlib.pyplot as plt

# Global constant for expected value of the weighted die
EXPECTED_VALUE = 4.2


def convergence_die_roll(total_trials):
    """
    Simulates rolling a weighted die over a number of trials.

    For each trial, computes:
    - The die roll outcome (based on weighted probabilities)
    - The running average (estimate)
    - The absolute error from the expected value

    Parameters:
        total_trials (int): Number of die rolls to simulate

    Returns:
        results (list of dict):
            A list where each element represents a trial snapshot:
            {
                "trial": int,
                "roll": int,
                "estimate": float,
                "error": float
            }
    """

    running_sum = 0
    results = []

    for trial in range(1, total_trials + 1):

        # Simulate weighted die using percentile mapping
        roll = random.randint(1, 100)

        if 1 <= roll <= 10:
            roll = 1
        elif 11 <= roll <= 20:
            roll = 2
        elif 21 <= roll <= 30:
            roll = 3
        elif 31 <= roll <= 40:
            roll = 4
        elif 41 <= roll <= 80:
            roll = 5
        else:
            roll = 6

        running_sum += roll
        running_average = running_sum / trial

        results.append({
            "trial": trial,
            "roll": roll,
            "estimate": running_average
        })

    # Compute error after simulation
    for item in results:
        item["error"] = abs(EXPECTED_VALUE - item["estimate"])

    return results


def die_roll_plot(results):
    """
    Generates a two-panel plot for a single simulation run:

    Top plot:
        - Scatter plot of individual die rolls
        - Line plot of running estimate
        - Horizontal line for expected value

    Bottom plot:
        - Error (distance from expected value) over time

    Parameters:
        results (list of dict): Output from convergence_die_roll()
    """

    trials = [item["trial"] for item in results]
    rolls = [item["roll"] for item in results]
    estimates = [item["estimate"] for item in results]
    errors = [item["error"] for item in results]

    fig, axs = plt.subplots(2, 1, sharex=True, figsize=(18, 10))

    # --- Top Plot: Convergence ---
    axs[0].set_title("Monte Carlo Convergence of a Weighted Die\n", fontsize=20)

    axs[0].scatter(trials, rolls, alpha=0.2, s=8, label="Rolls")
    axs[0].plot(trials, estimates, color="darkblue", label="Running Estimate")

    axs[0].axhline(
        EXPECTED_VALUE,
        linestyle="--",
        color="black",
        alpha=0.5,
        label=f"Expected Value: {EXPECTED_VALUE:.2f}"
    )

    axs[0].set_ylabel("Running Estimate")
    axs[0].grid(True)
    axs[0].legend()

    # --- Bottom Plot: Error ---
    axs[1].set_title("\nMargin of Error", fontsize=16)

    axs[1].plot(trials, errors, color="red")
    axs[1].set_ylabel("Distance from Expected Value")
    axs[1].set_xlabel("Trials Run")

    axs[1].set_ylim(0, max(errors) * 0.5)
    axs[1].grid(True)

    return fig


def multi_run_plot(total_trials, total_runs):
    """
    Generates an overlay plot showing multiple independent simulation runs.

    Each run produces a convergence curve (running estimate), and all runs
    are plotted together to visualize variability and convergence behavior.

    Parameters:
        total_trials (int): Number of trials per simulation
        total_runs (int): Number of independent simulation runs
    """

    fig, ax = plt.subplots(figsize=(18, 6))

    for run in range(total_runs):
        results = convergence_die_roll(total_trials)

        trials = [item["trial"] for item in results]
        estimates = [item["estimate"] for item in results]

        ax.plot(
            trials,
            estimates,
            alpha=0.3,
            linewidth=1
        )

    ax.axhline(
        EXPECTED_VALUE,
        linestyle="--",
        color="black",
        label=f"Expected Value: {EXPECTED_VALUE:.2f}"
    )

    ax.set_title(f"Monte Carlo Convergence Across {total_runs} Runs")
    ax.set_xlabel("Trials Run")
    ax.set_ylabel("Running Estimate")
    ax.set_ylim(3.0, 5.5)

    ax.grid(True)
    ax.legend()

    return fig