import tkinter as tk
from tkinter import filedialog, simpledialog
import os

class WebBuilderApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Web Builder")
        self.root.geometry("1000x700")
        
        # Sol menü çerçevesi
        self.menu_frame = tk.Frame(self.root, width=200, bg="lightgray")
        self.menu_frame.pack(side=tk.LEFT, fill=tk.Y)
        
        # Tasarım alanı (Canvas)
        self.canvas = tk.Canvas(self.root, bg="white")
        self.canvas.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
        
        # Menüdeki bileşenleri ekleme
        self.add_menu_buttons()
        
        # Sürükle bırak ayarları
        self.canvas.bind("<Button-1>", self.start_drag)
        self.canvas.bind("<B1-Motion>", self.dragging)
        self.canvas.bind("<ButtonRelease-1>", self.end_drag)

        self.dragging_widget = None
        self.widget_list = []  # Bileşenlerin listesi
        
        # Kaydetme düğmesi
        self.save_button = tk.Button(self.menu_frame, text="Save Layout", command=self.save_layout)
        self.save_button.pack(pady=10)
        
        # Sayfa ekleme düğmesi
        self.add_page_button = tk.Button(self.menu_frame, text="Add New Page", command=self.add_new_page)
        self.add_page_button.pack(pady=10)
        
        self.current_page = "index.html"
        self.pages = {"index.html": []}  # Sayfaların içeriği
        self.page_buttons = {}  # Sayfa yönlendirme butonları

    def add_menu_buttons(self):
        # Menüye bileşen ekleme butonları
        button = tk.Button(self.menu_frame, text="Add Button", command=lambda: self.add_widget("button"))
        button.pack(pady=5)
        
        label = tk.Button(self.menu_frame, text="Add Label", command=lambda: self.add_widget("label"))
        label.pack(pady=5)
    
    def add_widget(self, widget_type):
        # Yeni bileşen ekleme fonksiyonu
        if widget_type == "button":
            widget = tk.Button(self.canvas, text="Button", command=self.configure_button)
        elif widget_type == "label":
            widget = tk.Label(self.canvas, text="Label")
        
        widget_id = self.canvas.create_window(100, 100, window=widget)
        self.pages[self.current_page].append((widget, widget_id))
    
    def configure_button(self):
        # Buton ayarlama, başka bir sayfaya yönlendirme için
        target_page = simpledialog.askstring("Configure Button", "Enter page to link:")
        if target_page and target_page in self.pages:
            print(f"Button will link to {target_page}")
            # Burada butonun tıklama olayına sayfa yönlendirme kodu eklenir.

    def start_drag(self, event):
        # Sürüklemeyi başlatma
        self.dragging_widget = event.widget
    
    def dragging(self, event):
        # Sürükleme işlemi
        if self.dragging_widget:
            self.canvas.move(self.dragging_widget, event.x, event.y)
    
    def end_drag(self, event):
        # Sürüklemeyi bitirme
        self.dragging_widget = None

    def save_layout(self):
        # HTML olarak taslağı kaydetme
        filename = filedialog.asksaveasfilename(defaultextension=".html")
        if filename:
            with open(filename, 'w') as f:
                f.write("<html><body>\n")
                for page, widgets in self.pages.items():
                    f.write(f"<!-- {page} -->\n")
                    for widget, widget_id in widgets:
                        if isinstance(widget, tk.Button):
                            f.write('<button>Button</button>\n')
                        elif isinstance(widget, tk.Label):
                            f.write('<label>Label</label>\n')
                f.write("</body></html>")
            print(f"Layout saved to {filename}")
    
    def add_new_page(self):
        # Yeni sayfa ekleme
        new_page = simpledialog.askstring("New Page", "Enter name for new page (e.g., 'about.html'):")
        if new_page:
            if new_page not in self.pages:
                self.pages[new_page] = []
                print(f"New page {new_page} added.")
            else:
                print(f"Page {new_page} already exists.")

if __name__ == "__main__":
    root = tk.Tk()
    app = WebBuilderApp(root)
    root.mainloop()