from simulations.pi_estimator import estimate_pi
from simulations.pi_estimator import convergence_plot
from simulations.pi_estimator import print_statistics
from simulations.pi_estimator import statistics_report
from simulations.expected_value import convergence_die_roll
from simulations.expected_value import die_roll_plot
from simulations.expected_value import multi_run_plot
from PySide6.QtWidgets import (
    QMainWindow,
    QWidget,
    QLabel,
    QPushButton,
    QVBoxLayout,
    QLineEdit,
    QHBoxLayout,
    QGroupBox,
    QTextEdit
)
from PySide6.QtCore import Qt
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas


class MainWindow(QMainWindow):
    """Main window for the Monte Carlo Simulation Lab"""

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Monte Carlo Simulation Lab")
        self.resize(1500, 1200)

        title = QLabel("Monte Carlo Simulation Lab")
        subtitle = QLabel("Scientific Computing Dashboard")

        title.setAlignment(Qt.AlignCenter)
        subtitle.setAlignment(Qt.AlignCenter)

        title.setStyleSheet("font-size: 28px; font-weight: bold; color: #9CDCFE;")
        subtitle.setStyleSheet("font-size: 15px; color: #B0B0B0;")

        self.trials_input = QLineEdit()
        self.trials_input.setPlaceholderText("Number of trials to run")
        self.trials_input.setText("1000")

        self.result_label = QLabel("Estimate: not run yet")

        self.summary_box = QTextEdit()
        self.summary_box.setReadOnly(True)
        self.summary_box.setPlaceholderText("Simulation summary will appear here.")
        self.summary_box.setMinimumHeight(180)

        ev_button_single = QPushButton("Expected Value: Singe Run")
        ev_button_single.clicked.connect(self.run_expected_value_sim)
        ev_button_multi = QPushButton("Expected Value: Multiple Runs")
        ev_button_multi.clicked.connect(self.run_expected_value_sim_multi)

        clear_button = QPushButton("Clear Plot")
        clear_button.clicked.connect(self.clear_plot_layout)

        main_layout = QVBoxLayout()
        content_layout = QHBoxLayout()

        main_layout.addWidget(title)
        main_layout.addWidget(subtitle)
        main_layout.addLayout(content_layout)

        control_box = QGroupBox("Simulation Controls")
        control_box.setObjectName("controlBox")

        left_panel = QVBoxLayout()
        left_panel.setSpacing(12)
        left_panel.setContentsMargins(15, 15, 15, 15)

        left_panel.addWidget(QLabel("Trial Count"))
        left_panel.addWidget(self.trials_input)
        left_panel.addWidget(ev_button_single)
        left_panel.addWidget(ev_button_multi)
        left_panel.addWidget(clear_button)
        left_panel.addSpacing(20)
        left_panel.addWidget(self.result_label)
        left_panel.addWidget(QLabel("Simulation Summary"))
        left_panel.addWidget(self.summary_box)
        left_panel.addStretch()

        control_box.setLayout(left_panel)

        self.plot_layout = QVBoxLayout()

        content_layout.addWidget(control_box, 1)
        content_layout.addLayout(self.plot_layout, 4)

        container = QWidget()
        container.setLayout(main_layout)

        self.setStyleSheet("""
            QMainWindow {
                background-color: #121212;
            }

            QWidget {
                background-color: #121212;
                color: #EAEAEA;
                font-size: 14px;
            }

            QLabel {
                color: #EAEAEA;
            }

            QLineEdit {
                background-color: #1E1E1E;
                border: 1px solid #3A3A3A;
                border-radius: 6px;
                padding: 8px;
                color: #FFFFFF;
            }

            QPushButton {
                background-color: #243447;
                border: 1px solid #3E5C76;
                border-radius: 8px;
                padding: 10px;
                color: #FFFFFF;
                font-weight: bold;
            }

            QPushButton:hover {
                background-color: #2F4A63;
            }

            QPushButton:pressed {
                background-color: #1B2838;
            }

            QGroupBox {
                border: 1px solid #3A3A3A;
                border-radius: 10px;
                margin-top: 12px;
                padding: 12px;
                font-weight: bold;
            }

            QGroupBox::title {
                subcontrol-origin: margin;
                left: 12px;
                padding: 0 6px;
                color: #9CDCFE;
            }
        """)



        self.setCentralWidget(container)

    def clear_plot_layout(self):
        while self.plot_layout.count():
            item = self.plot_layout.takeAt(0)
            widget = item.widget()

            if widget is not None:
                widget.deleteLater()

    def run_expected_value_sim(self):
        self.clear_plot_layout()

        trials = int(self.trials_input.text())

        results = convergence_die_roll(trials)
        fig = die_roll_plot(results)

        canvas = FigureCanvas(fig)
        self.plot_layout.addWidget(canvas)

        final_estimate = results[-1]["estimate"]
        final_error = results[-1]["error"]

        self.summary_box.setText(
            f"This simulation rolled a weighted die {trials:,} times.\n\n"
            f"The theoretical expected value is 4.2.\n\n"
            f"The final running estimate was {final_estimate:.4f}, "
            f"with an absolute error of {final_error:.4f}.\n\n"
            "The top plot shows individual rolls and the running estimate converging "
            "toward the expected value. The lower plot shows how the error changes "
            "as more trials are added."
        )

        self.result_label.setText(
            f"Trials: {trials:,} | Estimate: {final_estimate:.4f} | Error: {final_error:.4f}"
    )
        
    def run_expected_value_sim_multi(self):
        self.clear_plot_layout()

        trials = int(self.trials_input.text())

        results = convergence_die_roll(trials)
        fig = multi_run_plot(trials, 50)

        canvas = FigureCanvas(fig)
        self.plot_layout.addWidget(canvas)

        final_estimate = results[-1]["estimate"]
        final_error = results[-1]["error"]

        self.summary_box.setText(
        f"This simulation ran 50 independent Monte Carlo experiments.\n\n"
        f"Each experiment used {trials:,} trials.\n\n"
        "Each line on the graph represents a separate run of the simulation.\n"
        "The variation between lines shows randomness in sampling.\n\n"
        "As the number of trials increases, all runs tend to converge toward "
        "the expected value (law of large numbers)."
    )

        self.result_label.setText(
            f"Trials: {trials:,} | Estimate: {final_estimate:.4f} | Error: {final_error:.4f}"
    )
