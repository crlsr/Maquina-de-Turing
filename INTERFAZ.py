import tkinter as tk
import os
from tkinter import filedialog, messagebox
from MAQUINA_TURING import MaquinaTuring
from tkinter import *
import customtkinter
from PIL import Image


tape_list = []
list_statuses = []
head_position = 0
labex = None

def revision_valores():
    global labelx
    value = tapeEntry.get()
    if len(value) > 200:
        messagebox.showerror("Error", "Excede los 200 caracteres")
    elif not all(char in '01' for char in value):
        messagebox.showerror("Error", "Caracter inválido")
    elif not value:
        messagebox.showerror("Error", "Valor inválido")
    else:
        for i in value:
            j = int(i)
            tape_list.append(j)
        print(tape_list)
        messagebox.showinfo("Éxito", "Los valores son tolerables para el programa")
        labelx = customtkinter.CTkLabel(master=frameVisualizer, text=value, font= ("Broadway", 18, ))
        return labelx.place(x=105, y=60)

def seleccionar_fila():
    file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt *.csv")])
    if not file_path.endswith(('.txt', '.csv')):
        messagebox.showerror("Error", "Formato de archivo inválido")
    else:
        with open(file_path, 'r') as f:
            list_statuses.clear()
            for line in f:
                line = line.strip()
                if line:
                    try:
                        estado_actual, simbolo_actual, nuevo_estado, nuevo_simbolo, movimiento_cabeza = map(int, line.split(','))
                        added = [estado_actual, simbolo_actual, nuevo_estado, nuevo_simbolo, movimiento_cabeza]
                        list_statuses.append(added)
                    except ValueError:
                        messagebox.showerror("Error", "Formato de archivo inválido")
                        list_statuses.clear()
                        return
            if not (1 <= len(list_statuses) <= 100) or any(len(row) != 5 for row in list_statuses):
                messagebox.showerror("Error", "El archivo debe ser una matriz de 1x5 hasta 100x5")
                list_statuses.clear()
                return

def labelMovement(tapeMovement, labelToPlace):
    currentXLabel = labelToPlace.winfo_rootx()
    if tapeMovement == 1:
        labelToPlace.place(x = currentXLabel - 10)
    elif tapeMovement == -1:
        labelToPlace.place(x = currentXLabel + 10)
    else:
        pass
        
def iniciar():
    global labelx
    if tape_list and list_statuses:
        tm = MaquinaTuring(tape_list, list_statuses, labelx, head_position)
        tm.run()
    else:
        messagebox.showerror("Error", "Por favor, comprueba los valores y selecciona un archivo antes de ejecutar la Máquina de Turing")

def guardar_cinta():
    root = tk.Tk()
    root.withdraw()
    directory = filedialog.askdirectory()
    file_path = os.path.join(directory, 'cintafinal.txt')
    with open(file_path, 'w') as f:
        for item in tape_list:
            f.write("%s\n" % item)
    messagebox.showinfo("Éxito", f"El archivo se guardó correctamente en {file_path}")
    root.destroy()

def mover_cabeza(tape: list):
    if(len(tape)==0):
        messagebox.showerror("Error", "Ingresa una lista primero") 
    else:
        #Pedir numero a usuario, guardar en head_position (input)
        tapeMensaje = customtkinter.CTkEntry(master=leftFrame, placeholder_text="Ingresa un numero", width=50)
        tapeMensaje.pack(padx=10, pady=25, fill ='x')
        if head_position > len(tapeMensaje) or head_position < 0:
            messagebox.showerror("Error", "Valor inválido")
            head_position = 0
        else:
            #Mostrar mensaje de guardado bien (mensaje)
            messagebox.showerror("Se ha guardado correctamente")
            pass

root = customtkinter.CTk()
root.geometry("800x450")
root.title("Interfaz")
root.resizable(False, False)
root.config(bg="green")

customtkinter.set_appearance_mode("dark-green")
customtkinter.set_default_color_theme("dark-blue")

leftFrame = customtkinter.CTkFrame(master=root, width=800, height=450, fg_color="darkblue")
leftFrame.pack(side='left', fill="both", padx=10, pady=10, expand=True)

turingLabel = customtkinter.CTkLabel(master=leftFrame, text="Maquina de Turing", font = ("Century Gothic", 30, "bold"), text_color="white")
turingLabel.pack(padx=10, pady=12)

tapeLabel = customtkinter.CTkLabel(master=leftFrame, text="Ingrese los valores de la cinta:", font= ("Century Gothic", 22, "bold"), text_color="white")
tapeLabel.pack(padx=10, pady=15)

tapeEntry = customtkinter.CTkEntry(master=leftFrame, placeholder_text="Exam. 1000111", width=50)
tapeEntry.pack(padx=10, pady=15, fill ='x')

checkButton = customtkinter.CTkButton(master=leftFrame, text="Comprobar", font=("Century Gothic", 22, "bold"), command=revision_valores, fg_color="black",text_color="white")
checkButton.pack(side="left", padx=10, pady=5)

fileButton=customtkinter.CTkButton(master=leftFrame, text="Elegir Instrucciones", font=("Century Gothic", 22, "bold"), command=seleccionar_fila, fg_color="black",text_color="white")
fileButton.pack(side="left", padx=10, pady=5)

runButton = customtkinter.CTkButton(master= leftFrame, font=("Century Gothic", 22, "bold"), text="Iniciar", command=iniciar, fg_color="black",text_color="white")
runButton.pack(side="left", pady=10, padx=5)

rightFrame = customtkinter.CTkFrame(master=root, fg_color="darkblue")
rightFrame.pack(side='right', fill='y', padx=10, pady=10, ipadx=110)

frameVisualizer = customtkinter.CTkFrame(master=rightFrame, width=150, height=150, fg_color="blue")
frameVisualizer.pack(fill="both")

my_image = customtkinter.CTkImage(light_image=Image.open('FLECHA.png'), size=(51.2,51.2))

canvas = customtkinter.CTkCanvas(frameVisualizer, width=300, height=200, bg='black')

my_label = customtkinter.CTkLabel(master=frameVisualizer, text="", image=my_image)
my_label.place(x=85, y=9)


saveButton = customtkinter.CTkButton(master=rightFrame, text="Guardar", font=("Century Gothic", 22, "bold"), command=guardar_cinta, fg_color="black",text_color="white")
saveButton.pack(side="bottom", pady=10)

MoverButton = customtkinter.CTkButton(master=rightFrame, text="Mover cabeza", font=("Century Gothic", 22, "bold"), command=mover_cabeza, fg_color="black",text_color="white")
MoverButton.pack(side="bottom", pady=20)

root.mainloop()

def run_step(tm):
    while not tm.final():
        tm.step()
        updateLabelPosition(tm.head_position)
        root.after(1000, run_step, tm)

def updateLabelPosition(newPosition):
    currentXLabel = labelx.winfo_rootx()
    if newPosition == 1:
        labelx.place(x= currentXLabel - 10)
    elif newPosition == -1:
        labelx.place(x= currentXLabel + 10)
    else:
        pass
