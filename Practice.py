import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg


class MainWindow(qtw.QWidget):
    def __init__(self):
        super().__init__()
        #set title
        self.setWindowTitle("Practice Window")

        #set vertical layout
        self.setLayout(qtw.QVBoxLayout())

        #label
        my_label = qtw.QLabel("Whats your name you beautiful human?")
        #create font size
        my_label.setFont(qtg.QFont('Shanti', 18))
        self.layout().addWidget(my_label)

        #entry box
        my_entry = qtw.QLineEdit()
        my_entry.setObjectName("name-field")
        my_entry.setText("")
        self.layout().addWidget(my_entry)

        #button
        my_button = qtw.QPushButton("Submit", clicked = lambda: press_it())
        self.layout().addWidget(my_button)

        #open app
        self.show()

        def press_it():
            #display whatever that has been tped in entry box
            my_label.setText(f"Hello {my_entry.text()}")
            #clear the label field
            my_entry.setText("")




app = qtw.QApplication([])
mw=MainWindow()

#run the app
app.exec_()

