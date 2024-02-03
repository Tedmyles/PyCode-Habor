import tkinter as tk
from tkinter import filedialog
import pandas as pd

class CSVtoXLSConverter:
    def __init__(self, root):
        self.root = root
        self.root.title("CSV to XLSX Converter")

        # File Selection Button
        self.select_button = tk.Button(root, text="Select CSV File", command=self.select_csv_file)
        self.select_button.pack(pady=10)

        # Convert Button
        self.convert_button = tk.Button(root, text="Convert to XLSX", command=self.convert_to_xlsx)
        self.convert_button.pack(pady=10)

    def select_csv_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
        if file_path:
            print(f"Selected CSV File: {file_path}")
            self.csv_file_path = file_path

    def convert_to_xlsx(self):
        try:
            df = pd.read_csv(self.csv_file_path)
            xlsx_file_path = self.csv_file_path.replace(".csv", ".xlsx")
            df.to_excel(xlsx_file_path, index=False)
            print(f"Conversion Successful. XLSX File saved at: {xlsx_file_path}")
        except Exception as e:
            print(f"Error during conversion: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    converter_app = CSVtoXLSConverter(root)
    root.mainloop()
