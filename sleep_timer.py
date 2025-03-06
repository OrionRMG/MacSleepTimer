import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QMessageBox
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
from PyQt5.QtSvg import QSvgWidget
from datetime import datetime, timedelta
import subprocess

class SleepScheduler(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        mainFont = QFont("Arial", 16)
        mainFont.setBold(True)


        scheduled_events = self.get_existing_schedule()

        self.setWindowTitle("Schedule Sleep")
        self.activeSchedLabel = QLabel("Active sleep schedules:")
        self.activeSchedListLabel = QLabel(scheduled_events)
        self.label = QLabel("Enter minutes until sleep:")
        self.line_edit = QLineEdit()
        self.new_sched_button = QPushButton("Set")
        self.new_sched_button.clicked.connect(self.schedule_sleep)
        self.clear_sched_button = QPushButton("Clear sleep schedules")
        self.clear_sched_button.clicked.connect(self.clear_sleep_schedules)
        self.icon = QSvgWidget()

        fontColor = "#9133a6"
        backgroundColor = "#d0b0ff"
        hoverDark = "#a43fba"
        hoverLight = "#c599f2"
        activeDark = "#832d96"
        activeLight = "#b175d9"
        primaryButtonStyles = f"""
            QPushButton {{
                border: 2px solid;
                border-color: {fontColor};
                background-color: {fontColor};
                color: {backgroundColor};
                font-weight: bold;
                padding: 5px 32px;
            }}
            QPushButton:hover {{
                background-color: {hoverDark}
            }}
            QPushButton:pressed {{
                background-color: {activeDark}
            }}
        """
        secondaryButtonStyles = f"""
            QPushButton {{
                border: 2px solid;
                border-color: {fontColor};
                color: {fontColor};
                font-weight: bold;
                padding-top: 4px;
                padding-bottom: 4px;
                margin-top: 8px
            }}
            QPushButton:hover {{
                background-color: {hoverLight}
            }}
            QPushButton:pressed {{
                background-color: {activeLight}
            }}
        """
        textBoxStyles = f"""
            border: 2px solid;
            border-color: {fontColor};
            color: {fontColor};
            font-weight: bold;
            padding-top: 4px;
            padding-bottom: 4px;
            padding-left: 4px;
            padding-right: 4px;
        """
        self.activeSchedLabel.setFont(mainFont)
        self.label.setFont(mainFont)
        self.activeSchedLabel.setStyleSheet(f"color: {fontColor}")
        self.activeSchedListLabel.setStyleSheet(f"color: {fontColor}")
        self.label.setStyleSheet(f"color: {fontColor}")
        self.new_sched_button.setStyleSheet(primaryButtonStyles)
        self.clear_sched_button.setStyleSheet(secondaryButtonStyles)
        self.line_edit.setStyleSheet(textBoxStyles)
        self.new_sched_button.setCursor(Qt.PointingHandCursor)
        self.clear_sched_button.setCursor(Qt.PointingHandCursor)

        iconData = f"""
            <svg  xmlns="http://www.w3.org/2000/svg"  width="24"  height="24"  viewBox="0 0 24 24"  fill="none"  stroke="{fontColor}"  stroke-width="2"  stroke-linecap="round"  stroke-linejoin="round"  class="icon icon-tabler icons-tabler-outline icon-tabler-moon-stars"><path stroke="none" d="M0 0h24v24H0z" fill="none"/><path d="M12 3c.132 0 .263 0 .393 0a7.5 7.5 0 0 0 7.92 12.446a9 9 0 1 1 -8.313 -12.454z" /><path d="M17 4a2 2 0 0 0 2 2a2 2 0 0 0 -2 2a2 2 0 0 0 -2 -2a2 2 0 0 0 2 -2" /><path d="M19 11h2m-1 -1v2" /></svg>
        """
        self.icon.load(bytearray(iconData, encoding='utf-8'))
        self.icon.setFixedSize(32, 32)

        inputLayout = QHBoxLayout()
        inputLayout.addWidget(self.line_edit)
        inputLayout.addWidget(self.new_sched_button, alignment=Qt.AlignTop)

        formLayout = QVBoxLayout()
        formLayout.addWidget(self.label)
        formLayout.addLayout(inputLayout)
        formLayout.setContentsMargins(0, 12, 0, 8)

        activeSchedLayout = QVBoxLayout()
        activeSchedLayout.addWidget(self.activeSchedLabel)
        activeSchedLayout.addWidget(self.activeSchedListLabel, alignment=Qt.AlignTop)
        activeSchedLayout.addWidget(self.clear_sched_button)

        layout = QVBoxLayout()
        layout.addWidget(self.icon)
        layout.addLayout(formLayout)
        layout.addLayout(activeSchedLayout)

        self.setLayout(layout)
        self.setStyleSheet("background-color: #d0b0ff")
        self.resize(300, 200)

    def schedule_sleep(self):
        # Calculate the future date and time
        try:
            minutes = int(self.line_edit.text())
        except ValueError:
            QMessageBox.critical(self, "Input Error", "Please enter a valid number.")
            return
        
        future_time = datetime.now() + timedelta(minutes=minutes)
        future_time_str = future_time.strftime("%m/%d/%y %H:%M:%S")

        # Prepare the shell command (without sudo)
        shell_command = f"pmset schedule sleep '{future_time_str}'"
        
        # Build the AppleScript command to run the shell command with admin privileges
        applescript = f'do shell script "{shell_command}" with administrator privileges'
        
        # Execute the AppleScript using osascript
        try:
            subprocess.run(["osascript", "-e", applescript], check=True)
            newSched = self.get_existing_schedule()
            self.activeSchedListLabel.setText(newSched)
        except subprocess.CalledProcessError as e:
            QMessageBox.critical(self, "Error", f"Failed to schedule sleep:\n{e}")
        
        self.line_edit.setText("")

    def clear_sleep_schedules(self):
        shell_command = "pmset schedule cancelall"
        applescript = f'do shell script "{shell_command}" with administrator privileges'

        # Execute the AppleScript using osascript
        try:
            subprocess.run(["osascript", "-e", applescript], check=True)
            newSched = self.get_existing_schedule()
            self.activeSchedListLabel.setText(newSched)
        except subprocess.CalledProcessError as e:
            QMessageBox.critical(self, "Error", "Failed to clear schedules")

    def get_existing_schedule(self):
        res = subprocess.check_output(["pmset", "-g", "sched"], text=True)
        lines = res.splitlines()
        scheduled_events = []
        for line in lines:
            if "]  sleep" in line:
                scheduled_events.append(line[15:34])
        
        self.activeSchedList = ""
        
        if len(scheduled_events) > 0:
            for index, event in enumerate(scheduled_events):
                twelveHourTime = datetime.strptime(event, "%m/%d/%Y %H:%M:%S").strftime("%a, %b %d %I:%M %p")
                if index == len(scheduled_events) - 1:
                    self.activeSchedList = self.activeSchedList + f"{twelveHourTime}"
                else:
                    self.activeSchedList = self.activeSchedList + f"{twelveHourTime}\n"
        else:
            self.activeSchedList = "None"

        return self.activeSchedList

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = SleepScheduler()
    window.show()
    sys.exit(app.exec_())

