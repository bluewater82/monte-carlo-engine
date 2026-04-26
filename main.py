from simulations.pi_estimator import estimate_pi
from simulations.pi_estimator import convergence_plot
from simulations.pi_estimator import print_statistics
from simulations.pi_estimator import statistics_report

def main():
    total_trials = int(input("Enter total number of trials: "))


    results, independent_results = estimate_pi(total_trials)
    print_statistics(results, independent_results)
    statistics_report(results, independent_results, total_trials)
    convergence_plot(results, total_trials, independent_results)

if __name__ == "__main__":
    main()