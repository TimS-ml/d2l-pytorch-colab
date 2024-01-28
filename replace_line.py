import glob, json

# def replace_line_in_notebook(folder_path, old_line, new_lines):
#     pattern = folder_path + '/**/*.ipynb'  # Pattern to match all .ipynb files in the folder and subfolders
#     for file_path in glob.glob(pattern, recursive=True):
#         print(file_path)
#         with open(file_path, 'r') as file:
#             notebook = json.load(file)
#             modified = False

#             for cell in notebook['cells']:
#                 if cell['cell_type'] == 'code':
#                     if old_line in cell['source']:
#                         cell['source'] = cell['source'].replace(old_line, new_lines)
#                         modified = True

#             if modified:
#                 with open(file_path, 'w') as file:
#                     json.dump(notebook, file, indent=2)

def replace_line_in_notebook(folder_path, old_line, new_lines):
    pattern = folder_path + '/**/*.ipynb'  # Pattern to match all .ipynb files in the folder and subfolders
    for file_path in glob.glob(pattern, recursive=True):
        try:
            with open(file_path, 'r') as file:
                notebook = json.load(file)
                modified = False

                for cell in notebook['cells']:
                    if cell['cell_type'] == 'code':
                        # Iterate through each line in the cell's source
                        for i, line in enumerate(cell['source']):
                            if line.strip() == old_line.strip():
                                # Replace the line with new_lines split into multiple lines
                                cell['source'][i:i+1] = new_lines.split('\n')
                                modified = True
                                break  # Assuming only one replacement per cell
                            elif 'pip install' in line:
                                # Comment out lines containing 'pip install'
                                cell['source'][i] = '# ' + line
                                modified = True

                if modified:
                    with open(file_path, 'w') as file:
                        json.dump(notebook, file, indent=2)
        except:
            print(file_path)


# Example usage
folder_path = '.'
old_line = '!pip install d2l==1.0.3\n'
new_lines = '''import sys, os\n\nsys.path.append(os.path.dirname(os.getcwd()))\nfrom d2l import torch as d2l\nfrom d2l.utils import *\n'''

replace_line_in_notebook(folder_path, old_line, new_lines)
