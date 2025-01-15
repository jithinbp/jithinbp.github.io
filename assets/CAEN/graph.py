import sys
import numpy as np
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, 
                           QHBoxLayout, QLineEdit, QPushButton, QLabel, QFileDialog, QMenuBar, QMenu, QMessageBox, QToolBar, QTabWidget, QTextEdit)
from PyQt5.QtCore import Qt, QProcess, QTimer
from PyQt5.QtGui import QTextCursor, QIcon
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import pandas as pd
import os
import time
from subprocess import Popen

class GraphingCalculator(QMainWindow):
    monitoring_histogram = False
    monitoring_waveform = False
    
    def __init__(self):
        super().__init__()
        self.setWindowTitle("CAEN Data Plotter")
        self.setGeometry(100, 100, 800, 600)

        # Initialize timers
        self.histo_timer = QTimer()
        self.wave_timer = QTimer()
        self.histo_timer.timeout.connect(self.update_histogram)
        self.wave_timer.timeout.connect(self.update_waveform)
        
        # Initialize last modification times
        self.last_histo_mtime = 0
        self.last_wave_mtime = 0

        # Create menu bar and toolbar
        self.create_menu_bar()

        # Create tab widget
        self.tab_widget = QTabWidget()
        self.setCentralWidget(self.tab_widget)

        # Create and add plotting tab
        self.plot_widget = QWidget()
        self.setup_plot_tab()
        self.tab_widget.addTab(self.plot_widget, "Plotting")

        # Create and add config editor tab
        self.config_widget = QWidget()
        self.setup_config_tab()
        self.tab_widget.addTab(self.config_widget, "Config Editor")

        # Connect tab change signal
        self.tab_widget.currentChanged.connect(self.on_tab_changed)
        
        # Store the last active tab
        self.last_tab_index = 0

    def setup_plot_tab(self):
        """Setup the plotting interface tab"""
        main_layout = QVBoxLayout(self.plot_widget)

        # Create input area
        input_layout = QHBoxLayout()
        csv_button = QPushButton("Plot CSV")
        wave_demo_button = QPushButton("Run WaveDemo")
        wave_demo_button.setIcon(QIcon.fromTheme("media-playback-start"))
        csv_button.clicked.connect(self.plot_csv)
        wave_demo_button.clicked.connect(self.run_wave_demo)
        input_layout.addWidget(csv_button)
        input_layout.addWidget(wave_demo_button)
        main_layout.addLayout(input_layout)

        # Create matplotlib figure
        self.figure = Figure(figsize=(8, 6))
        self.canvas = FigureCanvas(self.figure)
        main_layout.addWidget(self.canvas)

        # Add control panel
        self.control_panel = QWidget()
        control_layout = QHBoxLayout(self.control_panel)
        
        # Add control buttons
        self.monitor_hist_button = QPushButton("Monitor Histogram")
        self.monitor_wave_button = QPushButton("Monitor Waveform")
        self.stop_monitor_button = QPushButton("Stop Monitoring")
        self.monitor_hist_button.clicked.connect(self.monitor_histogram)
        self.monitor_wave_button.clicked.connect(self.monitor_waveform)
        self.stop_monitor_button.clicked.connect(self.stop_monitoring)
        
        control_layout.addWidget(self.monitor_hist_button)
        control_layout.addWidget(self.monitor_wave_button)
        control_layout.addWidget(self.stop_monitor_button)
        
        main_layout.addWidget(self.control_panel)
        self.control_panel.hide()

    def setup_config_tab(self):
        """Setup the config editor tab"""
        config_layout = QVBoxLayout(self.config_widget)
        
        # Add text editor
        self.config_editor = QTextEdit()
        config_layout.addWidget(self.config_editor)
        
        # Load config file if it exists
        self.load_config_file()

    def load_config_file(self):
        """Load the WaveDemoConfig.ini file into the editor"""
        try:
            config_file = "WaveDemoConfig.ini"
            if os.path.exists(config_file):
                with open(config_file, 'r') as f:
                    self.config_editor.setText(f.read())
            else:
                self.config_editor.setText("# WaveDemoConfig.ini not found")
        except Exception as e:
            print(f"Error loading config file: {str(e)}")

    def save_config_file(self):
        """Save the config file"""
        try:
            config_file = "WaveDemoConfig.ini"
            with open(config_file, 'w') as f:
                f.write(self.config_editor.toPlainText())
            print("Config file saved successfully")
        except Exception as e:
            print(f"Error saving config file: {str(e)}")

    def on_tab_changed(self, index):
        """Handle tab changes"""
        # If we're leaving the config editor tab, save the file
        if self.last_tab_index == 1:  # Config editor tab index
            self.save_config_file()
        
        # If we're entering the config editor tab, reload the file
        if index == 1:
            self.load_config_file()
            
        self.last_tab_index = index

    def create_menu_bar(self):
        """Create the menu bar with File and Help menus"""
        menubar = self.menuBar()
        
        # File menu
        file_menu = menubar.addMenu('File')
        
        # Add Exit action to File menu
        exit_action = file_menu.addAction('Exit')
        exit_action.triggered.connect(self.close)
        
        # Help menu
        help_menu = menubar.addMenu('Help')
        
        # Add About action to Help menu
        about_action = help_menu.addAction('About')
        about_action.triggered.connect(self.show_about_dialog)

    def show_about_dialog(self):
        """Show the About dialog with software information"""
        about_text = """
        <h3>CAEN Digitizer Data Plotter</h3>
        <p>This software is designed to visualize data from CAEN Multi Channel Analyzers 
        and Digitizers. It provides real-time monitoring of both waveforms and histograms 
        generated by the CAEN hardware.</p>
        
        <p><b>Features:</b></p>
        <ul>
        <li>Real-time waveform monitoring</li>
        <li>Real-time histogram monitoring</li>
        <li>CSV data plotting capabilities</li>
        <li>Integration with CAEN WaveDemo software</li>
        </ul>
        
        <p><b>Developer:</b><br>
        Jithin B.P.<br>
        <a href="mailto:jithinbp@gmail.com">jithinbp@gmail.com</a></p>
        
        <p><b>Version:</b> 1.0</p>
        """
        
        QMessageBox.about(self, "About CAEN Data Plotter", about_text)

    def plot_csv(self):
        """Open and plot a CSV file"""
        try:
            filename, _ = QFileDialog.getOpenFileName(self, "Open CSV File", "", "CSV Files (*.csv);;Text Files (*.txt)")
            if filename:
                data = self.read_data_file(filename)
                if data is not None:
                    self.plot_data(data, "CSV Plot", "X", "Y")
        except Exception as e:
            print(f"Error plotting CSV: {str(e)}")

    def read_data_file(self, filename):
        """Read data from a file and return x, y data and labels"""
        try:
            df = pd.read_csv(filename, delimiter='\s+', header=None)
            
            if len(df.columns) >= 2:
                # Multi-column case: use first two columns
                x_data = df.iloc[:, 0]
                y_data = df.iloc[:, 1]
            else:
                # Single-column case: generate x values automatically
                y_data = df.iloc[:, 0]
                x_data = np.arange(len(y_data))
            
            return {'x': x_data, 'y': y_data}
        except Exception as e:
            print(f"Error reading file {filename}: {str(e)}")
            return None

    def plot_data(self, data, title, xlabel, ylabel, plot_type='line'):
        """Generic plotting function for both line plots and histograms"""
        try:
            self.figure.clear()
            self.ax = self.figure.add_subplot(111)
            
            if plot_type == 'line':
                self.ax.plot(data['x'], data['y'])
            elif plot_type == 'histogram':
                self.ax.bar(np.arange(len(data['y'])), data['y'], width=1)
            
            self.ax.set_title(title)
            self.ax.set_xlabel(xlabel)
            self.ax.set_ylabel(ylabel)
            self.ax.grid(True)
            self.canvas.draw()
        except Exception as e:
            print(f"Error plotting data: {str(e)}")

    def run_wave_demo(self):
        """Run the WaveDemo command in a new gnome-terminal"""
        try:
            # Launch terminal with a unique title
            terminal_title = "wavedemo_terminal"
            cmd = f'gnome-terminal --title="{terminal_title}" -- bash -c "WaveDemo_x743 WaveDemoConfig.ini; read -p \'Press Enter to close...\'"'
            QProcess.startDetached('gnome-terminal', ['--title', terminal_title, '--', 'bash', '-c', 'WaveDemo_x743 WaveDemoConfig.ini; read -p "Press Enter to close..."'])
            
            # Give terminal time to open
            time.sleep(1)
            
            # Show the control panel after launching WaveDemo
            self.control_panel.show()
        except Exception as e:
            print(f"Error launching terminal: {str(e)}")

    def monitor_histogram(self):
        """Start histogram monitoring"""
        # Stop waveform monitoring if active
        if self.monitoring_waveform:
            self.wave_timer.stop()
            self.monitoring_waveform = False
            
        # Start histogram monitoring
        self.monitoring_histogram = True
        self.histo_timer.start(100)  # Poll every 100ms
        
        # Initialize the plot
        self.figure.clear()
        self.ax = self.figure.add_subplot(111)
        self.ax.set_title("Histogram Monitor")
        self.ax.grid(True)
        self.canvas.draw()

    def monitor_waveform(self):
        """Start waveform monitoring"""
        # Stop histogram monitoring if active
        if self.monitoring_histogram:
            self.histo_timer.stop()
            self.monitoring_histogram = False
            
        # Start waveform monitoring
        self.monitoring_waveform = True
        self.wave_timer.start(100)  # Poll every 100ms
        
        # Initialize the plot
        self.figure.clear()
        self.ax = self.figure.add_subplot(111)
        self.ax.set_title("Waveform Monitor")
        self.ax.grid(True)
        self.canvas.draw()

    def stop_monitoring(self):
        """Stop all monitoring"""
        self.monitoring_histogram = False
        self.monitoring_waveform = False
        self.histo_timer.stop()
        self.wave_timer.stop()

    def update_histogram(self):
        """Update histogram plot from file"""
        try:
            filename = "PlotHistoData.txt"
            if not os.path.exists(filename):
                return

            # Check if file has been modified
            mtime = os.path.getmtime(filename)
            if mtime <= self.last_histo_mtime:
                return
            self.last_histo_mtime = mtime

            data = self.read_data_file(filename)
            if data is not None:
                self.plot_data(data, "Histogram Monitor", "Value", "Counts", plot_type='histogram')

        except Exception as e:
            print(f"Error updating histogram: {str(e)}")

    def update_waveform(self):
        """Update waveform plot from file"""
        try:
            filename = "PlotWavesData.txt"
            if not os.path.exists(filename):
                return

            # Check if file has been modified
            mtime = os.path.getmtime(filename)
            if mtime <= self.last_wave_mtime:
                return
            self.last_wave_mtime = mtime

            data = self.read_data_file(filename)
            if data is not None:
                self.plot_data(data, "Waveform Monitor", "Time", "Amplitude", plot_type='line')

        except Exception as e:
            print(f"Error updating waveform: {str(e)}")



if __name__ == '__main__':
    app = QApplication(sys.argv)
    calculator = GraphingCalculator()
    calculator.show()
    sys.exit(app.exec_())
