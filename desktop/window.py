from PySide6.QtWidgets import (QMainWindow, QWidget, QVBoxLayout, 
                               QTextEdit, QLineEdit, QPushButton, QHBoxLayout, QLabel)
from PySide6.QtCore import Qt
from PySide6.QtGui import QColor
from app.core.orchestrator import Orchestrator

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("JARVIS — AI Assistant")
        self.resize(800, 600)
        self.orchestrator = Orchestrator()

        self.setStyleSheet("""
            QMainWindow { background-color: #0B1220; }
            QTextEdit { 
                background-color: #111A2E; 
                color: #E6ECF5; 
                border: 1px solid #22304F;
                border-radius: 8px;
                font-family: "Segoe UI", sans-serif;
                font-size: 14px;
                padding: 10px;
            }
            QLineEdit {
                background-color: #16223B;
                color: #E6ECF5;
                border: 1px solid #22304F;
                border-radius: 8px;
                padding: 10px;
                font-family: "Segoe UI", sans-serif;
                font-size: 14px;
            }
            QLineEdit:focus { border: 1px solid #22D3EE; }
            QPushButton {
                background-color: #22D3EE;
                color: #0B1220;
                border-radius: 8px;
                padding: 10px 20px;
                font-weight: bold;
            }
            QPushButton:hover { background-color: #0E7490; color: white; }
            QLabel { color: #8A99B5; font-family: "Segoe UI"; }
        """)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)

        # Header
        header = QLabel("JARVIS")
        header.setStyleSheet("font-size: 20px; font-weight: bold; color: #E6ECF5; margin-bottom: 10px;")
        layout.addWidget(header)

        # Chat area
        self.chat_display = QTextEdit()
        self.chat_display.setReadOnly(True)
        layout.addWidget(self.chat_display)

        # Input area
        input_layout = QHBoxLayout()
        self.input_field = QLineEdit()
        self.input_field.setPlaceholderText("Type a message...")
        self.input_field.returnPressed.connect(self.send_message)
        
        self.send_button = QPushButton("Send")
        self.send_button.clicked.connect(self.send_message)

        input_layout.addWidget(self.input_field)
        input_layout.addWidget(self.send_button)
        layout.addLayout(input_layout)

    def send_message(self):
        text = self.input_field.text().strip()
        if not text:
            return

        self.input_field.clear()
        self.append_to_chat("You", text, "#8A99B5")
        
        # Disable input while waiting
        self.input_field.setEnabled(False)
        self.send_button.setEnabled(False)
        
        # Process via Orchestrator (In a real app, this should be a QThread to not freeze UI)
        import threading
        def run_llm():
            response = self.orchestrator.process_message(text)
            # Back to UI thread to update
            from PySide6.QtCore import QMetaObject, Qt, Q_ARG
            QMetaObject.invokeMethod(self, "display_response", Qt.QueuedConnection, Q_ARG(str, response))

        threading.Thread(target=run_llm, daemon=True).start()

    from PySide6.QtCore import Slot
    @Slot(str)
    def display_response(self, response: str):
        self.append_to_chat("JARVIS", response, "#22D3EE")
        self.input_field.setEnabled(True)
        self.send_button.setEnabled(True)
        self.input_field.setFocus()

    def append_to_chat(self, sender: str, text: str, color: str):
        # Simple HTML formatting for chat
        html = f'<div style="margin-bottom: 10px;"><span style="color: {color}; font-weight: bold;">{sender}:</span> <br><span style="color: #E6ECF5;">{text}</span></div>'
        self.chat_display.append(html)