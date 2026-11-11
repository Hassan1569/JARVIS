import sys
from PySide6.QtWidgets import QApplication
from app.config import setup_logging
from desktop.window import MainWindow
import logging

def main():
    # Setup Logging
    setup_logging()
    logger = logging.getLogger(__name__)
    logger.info("Starting JARVIS...")

    # Start UI
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    
    sys.exit(app.exec())

if __name__ == "__main__":
    main()