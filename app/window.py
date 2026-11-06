
import json
import sys
from pathlib import Path

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QListWidget,
    QListWidgetItem,
    QListView
)

from rpc.presence import DiscordRPC


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.discord_rpc = DiscordRPC()

        self.default_button_1_label = "GitHub"
        self.default_button_1_url = "https://github.com/witchblxvdes/custom_ds_rpc"
        self.default_button_2_label = "Tap on me ^^"
        self.default_button_2_url = "https://www.youtube.com/watch?v=vZIXSQlzJKA"

        self.setWindowTitle("Custom DS RPC")
        self.resize(650, 750)

        self.layout = QVBoxLayout()
        self.layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.layout.setSpacing(12)
        self.layout.setContentsMargins(25, 25, 25, 25)
        self.setLayout(self.layout)

        self.title = QLabel("Custom DS RPC")
        self.title.setObjectName("windowTitle")
        self.layout.addWidget(self.title)

        self.details_label = QLabel("Activity Details")
        self.layout.addWidget(self.details_label)

        self.details_input = QLineEdit()
        self.details_input.setPlaceholderText("Enter activity details...")
        self.layout.addWidget(self.details_input)

        self.state_label = QLabel("Activity State")
        self.layout.addWidget(self.state_label)

        self.state_input = QLineEdit()
        self.state_input.setPlaceholderText("Enter activity state...")
        self.layout.addWidget(self.state_input)

        self.images_layout = QHBoxLayout()
        self.images_layout.setSpacing(15)

        self.large_image_layout = QVBoxLayout()

        self.large_image_label = QLabel("Large Image")
        self.large_image_layout.addWidget(self.large_image_label)

        self.large_image_gallery = QListWidget()
        self.large_image_gallery.setViewMode(QListView.ViewMode.ListMode)
        self.large_image_gallery.setFixedHeight(85)

        large_winter = QListWidgetItem("Winter")
        large_winter.setData(Qt.ItemDataRole.UserRole, "mc_winter")

        large_view = QListWidgetItem("Player View")
        large_view.setData(Qt.ItemDataRole.UserRole, "mc_view")

        self.large_image_gallery.addItem(large_winter)
        self.large_image_gallery.addItem(large_view)
        self.large_image_gallery.setCurrentRow(0)

        self.large_image_layout.addWidget(self.large_image_gallery)

        self.small_image_layout = QVBoxLayout()

        self.small_image_label = QLabel("Small Image")
        self.small_image_layout.addWidget(self.small_image_label)

        self.small_image_gallery = QListWidget()
        self.small_image_gallery.setViewMode(QListView.ViewMode.ListMode)
        self.small_image_gallery.setFixedHeight(85)

        small_winter = QListWidgetItem("Winter")
        small_winter.setData(Qt.ItemDataRole.UserRole, "mc_winter")

        small_view = QListWidgetItem("Player View")
        small_view.setData(Qt.ItemDataRole.UserRole, "mc_view")

        self.small_image_gallery.addItem(small_winter)
        self.small_image_gallery.addItem(small_view)
        self.small_image_gallery.setCurrentRow(1)

        self.small_image_layout.addWidget(self.small_image_gallery)

        self.images_layout.addLayout(self.large_image_layout)
        self.images_layout.addLayout(self.small_image_layout)

        self.layout.addLayout(self.images_layout)

        self.custom_buttons_label = QLabel("Custom Buttons")
        self.custom_buttons_label.setObjectName("sectionTitle")
        self.layout.addWidget(self.custom_buttons_label)

        self.button_1_label = QLabel("Button 1 Label")
        self.layout.addWidget(self.button_1_label)

        self.button_1_label_input = QLineEdit()
        self.button_1_label_input.setText(self.default_button_1_label)
        self.layout.addWidget(self.button_1_label_input)

        self.button_1_url_label = QLabel("Button 1 URL")
        self.layout.addWidget(self.button_1_url_label)

        self.button_1_url_input = QLineEdit()
        self.button_1_url_input.setText(self.default_button_1_url)
        self.layout.addWidget(self.button_1_url_input)

        self.button_2_label = QLabel("Button 2 Label")
        self.layout.addWidget(self.button_2_label)

        self.button_2_label_input = QLineEdit()
        self.button_2_label_input.setText(self.default_button_2_label)
        self.layout.addWidget(self.button_2_label_input)

        self.button_2_url_label = QLabel("Button 2 URL")
        self.layout.addWidget(self.button_2_url_label)

        self.button_2_url_input = QLineEdit()
        self.button_2_url_input.setText(self.default_button_2_url)
        self.layout.addWidget(self.button_2_url_input)

        self.buttons_layout = QHBoxLayout()
        self.buttons_layout.setSpacing(10)

        self.update_button = QPushButton("Update Activity")
        self.reset_button = QPushButton("Reset Settings")

        self.buttons_layout.addWidget(self.update_button)
        self.buttons_layout.addWidget(self.reset_button)

        self.layout.addLayout(self.buttons_layout)

        self.update_button.clicked.connect(self.update_activity)
        self.reset_button.clicked.connect(self.reset_settings)

        self.setStyleSheet("""
            QWidget {
                background-color: #202225;
                color: #f2f3f5;
                font-family: Segoe UI;
                font-size: 14px;
            }

            QLabel {
                color: #dbdee1;
            }

            QLabel#windowTitle {
                color: #ffffff;
                font-size: 24px;
                font-weight: bold;
                padding-bottom: 10px;
            }

            QLabel#sectionTitle {
                color: #ffffff;
                font-size: 17px;
                font-weight: bold;
                padding-top: 8px;
            }

            QLineEdit {
                background-color: #2b2d31;
                border: 1px solid #3f4147;
                border-radius: 6px;
                padding: 9px;
                color: #ffffff;
            }

            QLineEdit:focus {
                border: 1px solid #5865f2;
            }

            QListWidget {
                background-color: #2b2d31;
                border: 1px solid #3f4147;
                border-radius: 8px;
                padding: 5px;
                outline: none;
            }

            QListWidget::item {
                color: #dbdee1;
                border-radius: 6px;
                padding: 6px;
            }

            QListWidget::item:selected {
                background-color: #363a70;
                color: #ffffff;
            }

            QPushButton {
                background-color: #5865f2;
                color: #ffffff;
                border: none;
                border-radius: 6px;
                padding: 10px;
                font-weight: bold;
            }

            QPushButton:hover {
                background-color: #4752c4;
            }

            QPushButton:pressed {
                background-color: #3c45a5;
            }
        """)

        self.load_settings()

    def get_settings_path(self):
        if getattr(sys, "frozen", False):
            return Path(sys.executable).parent / "settings.json"

        return Path(__file__).resolve().parent.parent / "settings.json"

    def update_activity(self):
        details = self.details_input.text()
        state = self.state_input.text()

        large_image = self.large_image_gallery.currentItem().data(
            Qt.ItemDataRole.UserRole
        )

        small_image = self.small_image_gallery.currentItem().data(
            Qt.ItemDataRole.UserRole
        )

        buttons = [
            {
                "label": self.button_1_label_input.text(),
                "url": self.button_1_url_input.text()
            },
            {
                "label": self.button_2_label_input.text(),
                "url": self.button_2_url_input.text()
            }
        ]

        self.discord_rpc.update(
            details=details,
            state=state,
            large_image=large_image,
            small_image=small_image,
            buttons=buttons
        )

        self.save_settings()

        print("Activity updated successfully!")

    def reset_settings(self):
        self.details_input.clear()
        self.state_input.clear()

        self.large_image_gallery.setCurrentRow(0)
        self.small_image_gallery.setCurrentRow(1)

        self.button_1_label_input.setText(self.default_button_1_label)
        self.button_1_url_input.setText(self.default_button_1_url)
        self.button_2_label_input.setText(self.default_button_2_label)
        self.button_2_url_input.setText(self.default_button_2_url)

        self.save_settings()

    def save_settings(self):
        settings = {
            "details": self.details_input.text(),
            "state": self.state_input.text(),
            "large_image": self.large_image_gallery.currentItem().data(
                Qt.ItemDataRole.UserRole
            ),
            "small_image": self.small_image_gallery.currentItem().data(
                Qt.ItemDataRole.UserRole
            ),
            "button_1_label": self.button_1_label_input.text(),
            "button_1_url": self.button_1_url_input.text(),
            "button_2_label": self.button_2_label_input.text(),
            "button_2_url": self.button_2_url_input.text()
        }

        with open(self.get_settings_path(), "w", encoding="utf-8") as file:
            json.dump(settings, file, indent=4, ensure_ascii=False)

    def load_settings(self):
        settings_path = self.get_settings_path()

        if not settings_path.exists():
            return

        with open(settings_path, "r", encoding="utf-8") as file:
            settings = json.load(file)

        self.details_input.setText(settings.get("details", ""))
        self.state_input.setText(settings.get("state", ""))

        self.button_1_label_input.setText(
            settings.get("button_1_label", self.default_button_1_label)
        )
        self.button_1_url_input.setText(
            settings.get("button_1_url", self.default_button_1_url)
        )
        self.button_2_label_input.setText(
            settings.get("button_2_label", self.default_button_2_label)
        )
        self.button_2_url_input.setText(
            settings.get("button_2_url", self.default_button_2_url)
        )

        large_image = settings.get("large_image")
        small_image = settings.get("small_image")

        for index in range(self.large_image_gallery.count()):
            item = self.large_image_gallery.item(index)

            if item.data(Qt.ItemDataRole.UserRole) == large_image:
                self.large_image_gallery.setCurrentRow(index)

        for index in range(self.small_image_gallery.count()):
            item = self.small_image_gallery.item(index)

            if item.data(Qt.ItemDataRole.UserRole) == small_image:
                self.small_image_gallery.setCurrentRow(index)

    def closeEvent(self, event):
        self.save_settings()
        self.discord_rpc.close()
        event.accept()