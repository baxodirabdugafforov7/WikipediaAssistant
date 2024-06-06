#importing all necessary libraries

from PyQt5.QtGui import QFontMetricsF, QFont
from PyQt5.QtWidgets import *
import sys
import wikipedia

# function to output text with fixed lines

def fixed_lines(text, num_lines, line_length):
    words = text.split()
    lines = []
    current_line = ""
    for word in words:
        if len(current_line) + len(word) <= line_length:
            current_line += (word + " ")
        else:
            lines.append(current_line.strip())
            current_line = " " + word
        if len(lines) == num_lines:
            break

    if len(lines) < num_lines:
        lines.append(current_line.strip())

    while len(lines) < num_lines:
        lines.append("")

    return "\n".join(lines[:num_lines])

#class to create window and objects inside it

class mainwindow(QWidget):
    def __init__(self):
        super().__init__()

#settings of window

        self.setWindowTitle("oneLine_Calculator")
        self.layout = QVBoxLayout()

#label for input

        self.input_label = QLabel("Enter your topic")
        self.layout.addWidget(self.input_label)
        self.input_label.setFont(QFont("Arial", 24))
        self.input_text = QLineEdit()
        self.layout.addWidget(self.input_text)
        self.input_text.setFont(QFont("Arial", 24))

#label for output

        self.output_label = QLabel("Result: ")
        self.layout.addWidget(self.output_label)
        self.output_label.setFont(QFont("Arial", 24))
        self.output_text = QLabel()
        self.layout.addWidget(self.output_text)
        self.output_text.setFont(QFont("Arial", 16))

#button for processing data

        self.process_button = QPushButton("Search")
        self.process_button.clicked.connect(self.process_data)
        self.layout.addWidget(self.process_button)
        self.process_button.setFont(QFont("Arial", 20))
        self.process_button.setGeometry(200,150,100,50)

#setting the layouts

        self.setLayout(self.layout)
        self.showMaximized()


#function to process datas given

    def process_data(self):
        input_data = self.input_text.text()
        try:
            result = wikipedia.summary(input_data)
            result = fixed_lines(str(result), 30,150)

            self.output_text.setText(str(result))
            self.input_text.clear()

        except Exception as e:
            self.output_text.setText(str(fixed_lines(str(e),10,100)))

#main function to call all the functions and run the program

if __name__ == "__main__":
    app = QApplication([sys.argv])
    window = mainwindow()
    window.show()
    sys.exit(app.exec_())