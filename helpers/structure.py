
import os

def get_structure(base_path):
    return {
        'autoline1': ['PU', 'PI'],
        'autoline2': ['PU'],
        'autoline3': ['PI']
    }

def generate_excel_for_customer(customer, base_path):
    output_path = os.path.join(base_path, f"{customer}_export.xlsx")
    with open(output_path, "w") as f:
        f.write("Dummy XLS content")
    return output_path

def get_latest_xlsx_files(base_path):
    return {
        'autoline1': 'autoline1_export.xlsx',
        'autoline2': 'autoline2_export.xlsx',
        'autoline3': 'autoline3_export.xlsx'
    }
