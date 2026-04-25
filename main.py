from simulations.pi_estimator import estimate_pi
from simulations.pi_estimator import convergence_plot

def main():
    total_trials = int(input("Enter total number of trials: "))

    results = estimate_pi(total_trials)


    convergence_plot(results)

if __name__ == "__main__":
    main()