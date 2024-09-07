import sys
import os
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, 
                             QPushButton, QVBoxLayout, QLabel, 
                             QFileDialog, QTextEdit)
from PyQt5.QtCore import Qt
from flask import Flask, render_template_string
from threading import Thread
from pyngrok import ngrok

# Flask uygulaması
app = Flask(__name__)

# Flask ile sayfayı çalıştırmak için bir route tanımlıyoruz
@app.route('/')
def index():
    # Flask şablonuna HTML içerik ekliyoruz
    return render_template_string(window.html_content)

# Ana PyQt5 GUI Sınıfı
class WebDesignApp(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.html_content = "<html><body><h1>Yeni Sayfa</h1></body></html>"
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Web Site Oluşturucu')
        
        # Ana widget ve layout
        main_widget = QWidget()
        self.setCentralWidget(main_widget)
        layout = QVBoxLayout(main_widget)

        # Butonlar
        self.create_page_btn = QPushButton('Yeni Sayfa Oluştur', self)
        self.create_page_btn.clicked.connect(self.create_new_page)
        
        self.load_html_btn = QPushButton('HTML Yükle', self)
        self.load_html_btn.clicked.connect(self.load_html)

        self.run_flask_btn = QPushButton('Siteyi Başlat (Flask)', self)
        self.run_flask_btn.clicked.connect(self.run_flask_server)

        # Metin alanı
        self.text_edit = QTextEdit(self)
        self.text_edit.setPlainText(self.html_content)

        # Layout'a ekleme
        layout.addWidget(QLabel('Web Sayfanızı Tasarlayın'))
        layout.addWidget(self.text_edit)
        layout.addWidget(self.create_page_btn)
        layout.addWidget(self.load_html_btn)
        layout.addWidget(self.run_flask_btn)

    def create_new_page(self):
        # Yeni sayfa oluşturma fonksiyonu
        self.html_content = "<html><body><h1>Yeni Oluşturulmuş Sayfa</h1></body></html>"
        self.text_edit.setPlainText(self.html_content)

    def load_html(self):
        # HTML dosyasını yükleme fonksiyonu
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getOpenFileName(self, "HTML Dosyası Yükle", "", 
                                                   "HTML Files (*.html);;All Files (*)", options=options)
        if file_name:
            with open(file_name, 'r') as file:
                self.html_content = file.read()
                self.text_edit.setPlainText(self.html_content)

    def run_flask_server(self):
        # Kullanıcı HTML içeriğini metin alanından alır
        self.html_content = self.text_edit.toPlainText()

        # Flask sunucusunu farklı bir thread'de çalıştırıyoruz
        thread = Thread(target=self.start_flask)
        thread.daemon = True
        thread.start()

        # Ngrok ile Flask sunucusunu internete açıyoruz
        public_url = ngrok.connect(8080)
        print(f'Web siteniz şu adreste yayında: {public_url}')

    def start_flask(self):
        app.run(port=8080)

# Ana uygulama
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = WebDesignApp()
    window.show()
    sys.exit(app.exec_())