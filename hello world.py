from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QTextEdit, QScrollBar


class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        # Create a QTextEdit with fixed height
        self.text_edit = QTextEdit(self)
        self.text_edit.setReadOnly(True)

        # Set the fixed number of lines by adjusting the height
        font_metrics = self.text_edit.fontMetrics()
        line_height = font_metrics.lineSpacing()
        num_lines = 10  # Number of lines you want to display
        self.text_edit.setFixedHeight(line_height * num_lines)

        # Add some example content
        for i in range(50):
            self.text_edit.append(f"Line {i + 1}")

        layout.addWidget(self.text_edit)
        self.setLayout(layout)

        self.setWindowTitle('PyQt5 Fixed Lines Example')
        self.setGeometry(100, 100, 400, 300)


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
