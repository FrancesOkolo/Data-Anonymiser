# Data Anonymiser V2
Data Anonymizer V2 is a simple, easy-to-use tool designed to help you anonymize your datasets. It provides various anonymization techniques, such as randomizing numerical values and replacing text with anonymous placeholders, to help protect sensitive information.

# Features
Load CSV files
Display column names of the input dataset
Select columns to process
Randomize numerical values
Anonymize text values
Save the anonymized dataset as a CSV file
Preview the input dataset (first 5 rows)

# Installation
No installation is required. Simply download the Python script and run it using Python 3. Make sure to install the required dependencies:

bash
Copy code
pip install pandas numpy python-dateutil PyQt5

# Usage
Run the data_anonymizer_v2.py script:

bash
Copy code
python data_anonymizer_v2.py

Click "Browse data file" to select your input CSV file.

Preview the data by clicking "Preview Data" (optional).

Select the columns you want to process by clicking on the column names in the list.

Click "Browse output folder" to choose an output folder where the anonymized dataset will be saved.

Enter the column names you want to process, separated by a comma, in the "Enter the column names you want to process" field.

Click "Process Data" to anonymize the selected columns and save the resulting dataset as a new CSV file in the specified output folder.

# Customization
You can easily extend or modify the functionality of this tool by adding new features or modifying the existing code. Some suggestions for additional features include:

Automatic column type detection and suitable anonymization method suggestion
Custom anonymization options for each column
Progress bar while processing data
Error logging
Saving user preferences
License
This project is licensed under the MIT License.

# Author
Frances Okolo © 2023
