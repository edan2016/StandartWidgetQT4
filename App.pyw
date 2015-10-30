from PyQt4.QtGui import QApplication, QMainWindow
from widget import *
# ------------------------------

# -------------------------------
if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    Form = QMainWindow()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())