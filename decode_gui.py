import subprocess
import tkinter as tk
from tkinter import ttk

# COMPLETED - V 1.0a

def on_button_click():
    
    # Callback function for the button
    elf_path = str(small_textbox.get("1.0", "end-1c"))  # Get text from the small textbox
    backtrace = str(large_textbox1.get("1.0", "end-1c"))  # Get text from the first large textbox
    board = str(board_combobox.get())
    single_line_backtrace = backtrace.replace("\n"," ")
    
    # This command is legit:"C:\Espressif\tools\xtensa-esp32s3-elf\esp-12.2.0_20230208\xtensa-esp32s3-elf\bin\xtensa-esp32s3-elf-addr2line.exe"
    if "S3" in board:
        command = "C:\\Espressif\\tools\\xtensa-esp32s3-elf\\esp-12.2.0_20230208\\xtensa-esp32s3-elf\\bin\\xtensa-esp32s3-elf-addr2line.exe -aspCfire "+elf_path+" "+single_line_backtrace
    else:
        command = "C:\\Espressif\\tools\\xtensa-esp32-elf\\esp-12.2.0_20230208\\xtensa-esp32-elf\\bin\\xtensa-esp32-elf-addr2line.exe -aspCfire "+elf_path+" "+single_line_backtrace
        
    
    # RUN COMMAND / GET OUTPUT
    # try:
    result = subprocess.run(command,shell=True,text=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    
    if result.returncode == 0:
        print("No error")
        text = result.stdout
        # Write to text file
        with open("text.txt","w") as f:
            f.write(text)
        # Get rid of ?????'s
        with open("text.txt","r") as infile, open("output.txt","w") as outfile:
            for line in infile:
                if len(line.strip()) >= 20:
                    outfile.write(line)            
        with open("output.txt", "r") as file:
            output = file.read()
    else:
        output = "ERROR" + str(result.returncode)
    # except Exception as e:
    #     output = e
        
    
    
    large_textbox2.delete("1.0",tk.END)
    large_textbox2.insert("1.0",output)

    # You can do something with the obtained text here
    # print("Small Textbox Content:", text_small)
    # print("Large Textbox 1 Content:", text_large1)
    # print("Large Textbox 2 Content:", text_large2)

# Create the main window
root = tk.Tk()
root.title("ESP Stacktrace Decoder")
icon = tk.PhotoImage(file="img/fei_icon.png")
root.iconphoto(True,icon)
root.geometry("750x500")

# Labels
label1 = tk.Label(root, text="path to .elf:")
label1.grid(row=0, column=2, sticky="w",padx=20, pady=10)

label2 = tk.Label(root, text="Stack Trace:")
label2.grid(row=1, column=2, sticky="w",padx=20, pady=10)

label3 = tk.Label(root, text="Decoded Output:")
label3.grid(row=2, column=2, sticky="w",padx=20, pady=10)

# Small Textbox
small_textbox = tk.Text(root, height=1, width=60)
small_textbox.grid(row=0, column=3,padx=20, pady=10)
small_textbox.insert("1.0","C:\\Dylan\\FEI_NGIO_V2a\\NGIO_C3\\.pio\\build\\V47_C3\\firmware.elf")

# Large Textbox 1
large_textbox1 = tk.Text(root, height=10, width=60)
large_textbox1.grid(row=1, column=3,padx=20, pady=10)

# Large Textbox 2
large_textbox2 = tk.Text(root, height=10, width=60)
large_textbox2.grid(row=2, column=3,padx=20, pady=10)

# Combobox (Dropdown)
board_combobox = ttk.Combobox(root, values=["esp32", "esp32-S3", "esp32-C3"])
board_combobox.grid(row=3, column=3)
board_combobox.set("esp32")

# Button
button = tk.Button(root, text="Decode", command=on_button_click)
button.grid(row=4, column=3, columnspan=2,padx=20, pady=10)

root.mainloop()