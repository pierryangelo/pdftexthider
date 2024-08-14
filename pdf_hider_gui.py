import tkinter as tk
from tkinter import filedialog, colorchooser
from tkinter import ttk
import fitz  # PyMuPDF

# Função para verificar se uma cor é semelhante à cor alvo
def is_similar_color(color, target_rgb):
    return abs(color[0] - target_rgb[0]) < 0.1 and abs(color[1] - target_rgb[1]) < 0.1 and abs(color[2] - target_rgb[2]) < 0.1

# Função para converter valores RGB para a faixa [0, 1]
def rgb_to_normalized(color):
    return (color[0] / 255, color[1] / 255, color[2] / 255)

# Função para converter uma cor string (como '(236, 0, 141)') para uma tupla RGB
def parse_color_string(color_string):
    try:
        return tuple(map(int, color_string.strip('()').split(', ')))
    except ValueError:
        return None

def select_pdf_file():
    file_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
    input_pdf_path_var.set(file_path)

def select_output_file():
    file_path = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF files", "*.pdf")])
    output_pdf_path_var.set(file_path)

def select_color():
    color_code = colorchooser.askcolor(title="Select Text Color")[0]
    if color_code:
        color_code = tuple(map(int, color_code))
        color_var.set(str(color_code))

def process_pdf():
    pdf_path = input_pdf_path_var.get()
    output_path = output_pdf_path_var.get()
    target_color_str = color_var.get()
    
    if not pdf_path or not output_path or not target_color_str:
        result_label.config(text="Please fill all fields.")
        return

    target_color = parse_color_string(target_color_str)
    if not target_color:
        result_label.config(text="Invalid color format.")
        return

    # Cor de fundo para cobrir o texto (RGB)
    background_color = (255, 255, 255)

    # Abrir o arquivo PDF
    pdf_document = fitz.open(pdf_path)

    # Total de páginas para a barra de progresso
    total_pages = len(pdf_document)
    progress_bar["maximum"] = total_pages

    # Abrir o arquivo de texto para gravação com codificação UTF-8
    with open('red_text_output.txt', 'w', encoding='utf-8') as text_file:
        # Iterar pelas páginas do PDF
        for page_number in range(total_pages):
            page = pdf_document.load_page(page_number)
            # Extrair as áreas de texto da página
            text_instances = page.get_text("dict")["blocks"]
            
            for block in text_instances:
                if block['type'] == 0:  # Tipo de bloco de texto
                    for line in block["lines"]:
                        for span in line["spans"]:
                            color = span["color"]
                            rgb_color = (int(color >> 16 & 0xFF), int(color >> 8 & 0xFF), int(color & 0xFF))
                            normalized_rgb_color = rgb_to_normalized(rgb_color)
                            if is_similar_color(normalized_rgb_color, rgb_to_normalized(target_color)):
                                # Gravar o texto em vermelho no arquivo de texto
                                text_file.write(span["text"] + '\n')
                                # Desenhar uma área sólida sobre o texto
                                bbox = span["bbox"]
                                rect = fitz.Rect(bbox[0], bbox[1], bbox[2], bbox[3])
                                page.draw_rect(rect, color=rgb_to_normalized(background_color), fill=rgb_to_normalized(background_color))  # Desenhar retângulo sólido sem borda
            
            # Atualizar a barra de progresso
            progress_bar["value"] = page_number + 1
            root.update_idletasks()
        
        # Salvar as alterações no PDF
        pdf_document.save(output_path)

    # Fechar o arquivo PDF
    pdf_document.close()
    result_label.config(text="PDF processed successfully!")

# Criação da interface gráfica
root = tk.Tk()
root.title("PDF Text Hider")

input_pdf_path_var = tk.StringVar()
output_pdf_path_var = tk.StringVar()
color_var = tk.StringVar()

tk.Label(root, text="Input PDF File:").pack(pady=5)
tk.Entry(root, textvariable=input_pdf_path_var, width=50).pack(pady=5)
tk.Button(root, text="Browse", command=select_pdf_file).pack(pady=5)

tk.Label(root, text="Output PDF File:").pack(pady=5)
tk.Entry(root, textvariable=output_pdf_path_var, width=50).pack(pady=5)
tk.Button(root, text="Browse", command=select_output_file).pack(pady=5)

tk.Label(root, text="Text Color (RGB):").pack(pady=5)
tk.Entry(root, textvariable=color_var, width=50).pack(pady=5)
tk.Button(root, text="Select Color", command=select_color).pack(pady=5)

tk.Button(root, text="Process PDF", command=process_pdf).pack(pady=20)

# Barra de progresso
progress_bar = ttk.Progressbar(root, orient="horizontal", length=400, mode="determinate")
progress_bar.pack(pady=10)

result_label = tk.Label(root, text="")
result_label.pack(pady=10)

root.mainloop()