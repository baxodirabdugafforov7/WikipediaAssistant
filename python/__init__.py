import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton

def process_data(input_data):
    # Function to process input data
    # For simplicity, let's just return the input data reversed
    return input_data[::-1]

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Data Processing App")
        self.setGeometry(100, 100, 400, 200)

        self.layout = QVBoxLayout()

        self.input_label = QLabel("Enter Data:")
        self.layout.addWidget(self.input_label)

        self.input_text = QLineEdit()
        self.layout.addWidget(self.input_text)

        self.output_label = QLabel("Processed Result:")
        self.layout.addWidget(self.output_label)

        self.output_text = QLabel()
        self.layout.addWidget(self.output_text)

        self.process_button = QPushButton("Process Data")
        self.process_button.clicked.connect(self.process_data)
        self.layout.addWidget(self.process_button)

        self.setLayout(self.layout)

    def process_data(self):
        input_data = self.input_text.text()
        result = process_data(input_data)
        self.output_text.setText(result)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
