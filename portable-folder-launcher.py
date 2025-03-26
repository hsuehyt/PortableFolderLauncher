import os
import tkinter as tk
from tkinter import filedialog, messagebox

class PortableFolderLauncher:
    def __init__(self, master):
        self.master = master
        master.title("Portable Folder Launcher")
        master.geometry("400x300")

        # Source Folder Selection
        self.source_label = tk.Label(master, text="Source Folder:")
        self.source_label.pack(pady=(10, 0))
        
        self.source_path = tk.StringVar(value=os.path.dirname(os.path.abspath(__file__)))
        self.source_entry = tk.Entry(master, textvariable=self.source_path, width=50)
        self.source_entry.pack(pady=5)
        
        self.source_browse_btn = tk.Button(master, text="Browse", command=self.browse_source)
        self.source_browse_btn.pack(pady=5)

        # Target Folder Selection
        self.target_label = tk.Label(master, text="Target Folder:")
        self.target_label.pack(pady=(10, 0))
        
        self.target_path = tk.StringVar(value=os.path.dirname(os.path.abspath(__file__)))
        self.target_entry = tk.Entry(master, textvariable=self.target_path, width=50)
        self.target_entry.pack(pady=5)
        
        self.target_browse_btn = tk.Button(master, text="Browse", command=self.browse_target)
        self.target_browse_btn.pack(pady=5)

        # Generate Button
        self.generate_btn = tk.Button(master, text="Generate", command=self.generate_bat, 
                                      width=20, height=10)
        self.generate_btn.pack(pady=20)

    def browse_source(self):
        """Open folder selection dialog for source folder"""
        folder_selected = filedialog.askdirectory(
            initialdir=self.source_path.get(), 
            title="Select Source Folder"
        )
        if folder_selected:
            self.source_path.set(folder_selected)

    def browse_target(self):
        """Open folder selection dialog for target folder"""
        folder_selected = filedialog.askdirectory(
            initialdir=self.target_path.get(), 
            title="Select Target Folder"
        )
        if folder_selected:
            self.target_path.set(folder_selected)

    def generate_bat(self):
        """Generate batch file to open source folder"""
        try:
            # Validate paths
            source_path = self.source_path.get()
            target_path = self.target_path.get()
            
            if not source_path or not target_path:
                messagebox.showerror("Error", "Please select both source and target folders")
                return
            
            # Get source folder name for bat file
            source_folder_name = os.path.basename(source_path)
            bat_filename = f"{source_folder_name}.bat"
            bat_path = os.path.join(target_path, bat_filename)
            
            # Create batch file content
            bat_content = f'''@echo off
set "source_folder=%~dp0{os.path.relpath(source_path, target_path)}"
start "" "%source_folder%"
'''
            
            # Write batch file
            with open(bat_path, 'w') as bat_file:
                bat_file.write(bat_content)
            
            # Show success message
            messagebox.showinfo("Success", 
                f"Batch file '{bat_filename}' generated in {target_path}\n\n"
                "This batch file will open the source folder relative to its location on any drive.")
        
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

def main():
    root = tk.Tk()
    app = PortableFolderLauncher(root)
    root.mainloop()

if __name__ == "__main__":
    main()
