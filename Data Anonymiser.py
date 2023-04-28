import sys
import pandas as pd
import numpy as np
import random
from dateutil.parser import parse
import os
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QLabel, QPushButton, QFileDialog, QListWidget, QAbstractItemView, QLineEdit, QWidget, QScrollArea, QScrollBar, QMessageBox

# Functions
def is_date(value):
    if not isinstance(value, str):
        return False
    try:
        parse(value)
        return True
    except ValueError:
        return False

def randomize_numerical(column):
    return column.apply(lambda x: np.random.choice(column) if isinstance(x, (int, float)) else x)

def anonymize_text(column):
    unique_values = column.unique()
    anonymous_values = [f'anon_{i}' for i in range(len(unique_values))]
    anonymous_dict = dict(zip(unique_values, anonymous_values))
    return column.map(anonymous_dict)

def browse_input_file():
    global input_file
    input_file, _ = QFileDialog.getOpenFileName()
    input_file_label.setText(input_file)

    # Show column names
    try:
        data = pd.read_csv(input_file)
        columns_listbox.clear()
        for column in data.columns:
            columns_listbox.addItem(column)
    except Exception as e:
        QMessageBox.critical(None, "Error", f"An error occurred: {str(e)}")

def browse_output_folder():
    global output_folder
    output_folder = QFileDialog.getExistingDirectory()
    output_folder_label.setText(output_folder)

def process_data():
    columns_to_process = [col.strip() for col in columns_entry.text().split(',')]

    try:
        data = pd.read_csv(input_file)
        if not all(col in data.columns for col in columns_to_process):
            QMessageBox.critical(None, "Error", "One or more entered column names do not exist in the dataset.")
        else:
            processed_data = data.copy()
            for col in columns_to_process:
                if processed_data[col].apply(is_date).all():
                    continue
                elif np.issubdtype(processed_data[col].dtype, np.number):
                    processed_data[col] = randomize_numerical(data[col])
                else:
                    processed_data[col] = anonymize_text(data[col])

            output_file = os.path.join(output_folder, "newdata.csv")
            processed_data.to_csv(output_file, index=False)
            QMessageBox.information(None, "Success", f"Processed data saved to: {output_file}")
    except Exception as e:
        QMessageBox.critical(None, "Error", f"An error occurred: {str(e)}")

app = QApplication(sys.argv)
window = QMainWindow()
window.setWindowTitle("Data Anonymizer V2")

central_widget = QWidget()
central_widget.setStyleSheet("background-color: lightblue;")
layout = QVBoxLayout()

input_file_label = QLabel("Input data file:")
layout.addWidget(input_file_label)

browse_input_button = QPushButton("Browse data file")
browse_input_button.setStyleSheet("background-color: white;")
browse_input_button.clicked.connect(browse_input_file)
layout.addWidget(browse_input_button)

columns_label = QLabel("Column names:")
layout.addWidget(columns_label)

columns_listbox = QListWidget()
columns_listbox.setStyleSheet("background-color: white;")
columns_listbox.setSelectionMode(QAbstractItemView.MultiSelection)
layout.addWidget(columns_listbox)

output_folder_label = QLabel("Output folder:")
layout.addWidget(output_folder_label)

browse_output_button = QPushButton("Browse output folder")
browse_output_button.setStyleSheet("background-color: white;")
browse_output_button.clicked.connect(browse_output_folder)
layout.addWidget(browse_output_button)

columns_label = QLabel("Enter the column names you want to process, separated by a comma:")
layout.addWidget(columns_label)

columns_entry = QLineEdit()
columns_entry.setStyleSheet("background-color: white;")
layout.addWidget(columns_entry)

process_button = QPushButton("Process Data")
process_button.setStyleSheet("background-color: white;")
process_button.clicked.connect(process_data)
layout.addWidget(process_button)

central_widget.setLayout(layout)
window.setCentralWidget(central_widget)

copyright_label = QLabel("© 2023 Frances Okolo")
layout.addWidget(copyright_label, alignment=Qt.AlignBottom | Qt.AlignRight)

window.show()
sys.exit(app.exec_())