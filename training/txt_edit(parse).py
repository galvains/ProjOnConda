import requests

from tkinter import *
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfilename

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit\
    605.1.15 (KHTML, like Gecko) Version/16.2 Safari/605.1.15'
}

def open_file():
    filepath = askopenfilename(
        filetypes=[('Text Files', '*.txt'), ('All Files', '*.*')])
    if not filepath:
        return
    txt_edit.delete('1.0', END)
    with open(filepath, 'r') as input_file:
        text = input_file.read()
        txt_edit.insert(END, text)
    window.title(f'text editor - {filepath}')

def save_file():
    filepath = asksaveasfilename(
        defaultextension='txt',
        filetypes=[('Текстовые файлы', '*.txt'), ('Все файлы', '*.*')])
    if not filepath:
        return
    with open(filepath, 'w') as out_file:
        text = txt_edit.get('1.0', END)
        out_file.write(text)
    window(f'text editor - {filepath}')

def parse():
    url = txt_edit.get('1.0', END)
    response = requests.get(url, headers=headers)

    with open('/Users/yarik/Desktop/' + url.split('/')[-2] + '.html', 'w') as file:
        for line in response.text:
            file.write(line)

window = Tk()
window.title('text editor')
window.rowconfigure(0, minsize=300, weight=1)
window.columnconfigure(1, minsize=500, weight=1)

txt_edit = Text(window)
fr_buttons = Frame(window)
btn_open = Button(fr_buttons, text="Open", command=open_file)
btn_save = Button(fr_buttons, text="Save as...", command=save_file)
btn_parse = Button(fr_buttons, text='Parse', command=parse)

btn_open.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
btn_save.grid(row=1, column=0, sticky="ew", padx=5)
btn_parse.grid(row=2, column=0, sticky='ew', padx=5, pady=5)

fr_buttons.grid(row=0, column=0, sticky="ns")
txt_edit.grid(row=0, column=1, sticky="nsew")

window.mainloop()


