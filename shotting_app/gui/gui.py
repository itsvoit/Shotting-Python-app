from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QFileDialog

widget_back_ground = "background-color: #505F72"
menu_button_style = '''
                    QPushButton{
                        background-color: #455364;
                    }

                    QPushButton:hover{
                        background-color: #5F7289;
                    }'''


class UiMainWindow(QMainWindow):

    def __init__(self, controller):
        super().__init__()
        self.main_window.setObjectName("Screen Recorder")
        self.main_window.resize(875, 612)
        self.main_window.setMinimumSize(QtCore.QSize(875, 612))
        self.main_window.setMaximumSize(QtCore.QSize(875, 612))

        self.controller = controller
        self.central_widget = self.make_central_widget()
        self.full_menu_widget = self.make_menu_widget()
        self.menu_vertica_layout = self.make_menu_layout()
        self.option_v_layout = self.make_vertical_layaut("verticalLayout_4", self.full_menu_widget)

        self.option_button = self.make_menu_button("option_button", ":/icons/settings_cogwheel_options_icon_149387.png")
        self.option_button.clicked.connect(self.select_option_widget())

        self.menu_vertica_layout.addWidget(self.option_button)

        self.video_button = self.make_menu_button("video_button",
                                                  ":/icons/movie-symbol-of-video-camera_icon-icons.com_72981.png")

        self.menu_vertica_layout.addWidget(self.video_button)

        self.editor_button = self.make_menu_button("editor_button",
                                                   ":/icons/iconfinder-videoeditingeditorslicecrop-3993845_112640.png")

        self.menu_vertica_layout.addWidget(self.editor_button)

        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.menu_vertica_layout.addItem(spacerItem)

        self.option_v_layout.addLayout(self.menu_vertica_layout)

        self.exit_button = self.make_menu_button("exit_button", ":/icons/powercircleandlinesymbol_118369.png")

        self.option_v_layout.addWidget(self.exit_button)
        self.exit_button.clicked.connect(self.close_app)

        self.main_widget = self.make_main_widget()
        self.main_stacked_widget = self.make_stacked_widget()

        self.option = QtWidgets.QWidget()
        self.option.setObjectName("option")

        self.resolution_combo_box = self.make_combo_box("resolution_combo_box", (270, 30))
        self.FPS_combo_box = self.make_combo_box('FPS_combo_box', (270, 80))
        self.codec_combo_box = self.make_combo_box('codec_combo_box', (270, 130))
        self.display_combo_box = self.make_combo_box('display_combo_box', (270, 530))

        self.s_storage_line = self.make_storage_line('s_storage_line', (270, 480))
        self.v_storage_line = self.make_storage_line("v_storage_line", (270, 430))

        self.quality_slider = self.make_slider("quality_slider", (270, 330), 0, 100)

        self.sounds_button = self.make_check_button("sounds_button", (350, 280))

        self.layout_widget_labels = self.make_layout_widget_for_label()

        self.menu_label_vertica_layout = self.make_vertical_layaut("menu_label_vertica_layout",
                                                                   self.layout_widget_labels)

        self.resolution_label = self.make_label("resolution_label", self.layout_widget_labels)
        self.menu_label_vertica_layout.addWidget(self.resolution_label)

        self.FPS_label = self.make_label("FPS_label", self.layout_widget_labels)
        self.menu_label_vertica_layout.addWidget(self.FPS_label)

        self.Codec_label = self.make_label("codec_label", self.layout_widget_labels)
        self.menu_label_vertica_layout.addWidget(self.Codec_label)

        self.v_hotkey = self.make_label("v_hotkey", self.layout_widget_labels)
        self.menu_label_vertica_layout.addWidget(self.v_hotkey)

        self.s_hotkey = self.make_label("s_hotkey", self.layout_widget_labels)
        self.menu_label_vertica_layout.addWidget(self.s_hotkey)

        self.sound_label = self.make_label("sound_label", self.layout_widget_labels)
        self.menu_label_vertica_layout.addWidget(self.sound_label)

        self.quality_label = self.make_label("quality_label", self.layout_widget_labels)
        self.menu_label_vertica_layout.addWidget(self.quality_label)

        self.duration_label = self.make_label("duration_label", self.layout_widget_labels)
        self.menu_label_vertica_layout.addWidget(self.duration_label)

        self.v_storage_label = self.make_label("v_storage_label", self.layout_widget_labels)
        self.menu_label_vertica_layout.addWidget(self.v_storage_label)

        self.s_storage_label = self.make_label("s_storage_label", self.layout_widget_labels)
        self.menu_label_vertica_layout.addWidget(self.s_storage_label)

        self.display_label = self.make_label("display_label", self.layout_widget_labels)
        self.menu_label_vertica_layout.addWidget(self.display_label)

        self.v_storage_browse = self.make_button("v_storage_button", (470, 430))
        self.v_storage_browse.clicked.connect(self.browse_v_storage)

        self.s_storage_browse = self.make_button("s_storage_button", (470, 480))
        self.s_storage_browse.clicked.connect(self.browse_s_storage)

        self.duration_display = self.make_lcd_display("duration_display", (470, 330), 91, 32)

        self.reset_button = self.make_button("reset_button", (470, 570))
        self.reset_button.clicked.connect(self.restart_settings)

        self.save_button = self.make_button("save_button", (590, 570))
        self.save_button = self.save_button.clicked.connect(self.save_settings)

        self.duration_horizontal_slider = self.make_horizontal_slider("duration_slider", (270, 380), 10, 120)

        self.v_dur_display = self.make_lcd_display("v_dur_display", (470, 380), 91, 32)

        self.video_hotkey = self.make_line("video_path", (270, 180))

        self.screen_hotkey = self.make_line("screen_path", (270, 230))

        self.ram_label = self.make_label("ram_req_label", self.option)
        self.ram_label.setGeometry(QtCore.QRect(480, 60, 201, 41))

        self.ram_display = self.make_lcd_display("ram_display", (480, 100), 210, 42)

        self.main_stacked_widget.addWidget(self.option)

        self.video = QtWidgets.QWidget()
        self.video.setObjectName("video")

        self.main_stacked_widget.addWidget(self.video)

        self.video_editor = QtWidgets.QWidget()
        self.video_editor.setObjectName("video_editor")

        self.main_stacked_widget.addWidget(self.video_editor)
        self.main_window.setCentralWidget(self.central_widget)

        self.retranslateUi()

        self.main_stacked_widget.setCurrentIndex(0)

        self.quality_slider.valueChanged['int'].connect(self.duration_display.display)

        self.duration_horizontal_slider.valueChanged['int'].connect(self.v_dur_display.display)

        QtCore.QMetaObject.connectSlotsByName(self.main_window)

    def make_central_widget(self):
        central_widget = QtWidgets.QWidget(self.main_window)
        central_widget.setObjectName("central_widget")

        return central_widget

    def make_menu_widget(self):
        full_menu_widget = QtWidgets.QWidget(self.central_widget)
        full_menu_widget.setGeometry(QtCore.QRect(0, 0, 151, 611))
        full_menu_widget.setAutoFillBackground(False)
        full_menu_widget.setStyleSheet(widget_back_ground)
        full_menu_widget.setObjectName("full_menu_widget")

        return full_menu_widget

    def make_vertical_layaut(self, name, widget):
        v_layout = QtWidgets.QVBoxLayout(widget)
        v_layout.setContentsMargins(0, 0, 0, 0)
        v_layout.setSpacing(0)
        v_layout.setObjectName(name)

        return v_layout

    def make_menu_layout(self):
        menu_vertica_layout = QtWidgets.QVBoxLayout()
        menu_vertica_layout.setObjectName("menu_vertica_layout")

        return menu_vertica_layout

    def make_menu_button(self, name, icon_path):
        button = QtWidgets.QPushButton(self.full_menu_widget)
        button.setStyleSheet(menu_button_style)
        font = QtGui.QFont()
        font.setPointSize(11)
        button.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(icon_path), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        button.setIcon(icon)
        button.setIconSize(QtCore.QSize(30, 30))
        button.setCheckable(True)
        button.setAutoExclusive(True)
        button.setObjectName(name)

        return button

    def make_main_widget(self):
        main_widget = QtWidgets.QWidget(self.central_widget)
        main_widget.setGeometry(QtCore.QRect(151, 0, 720, 611))
        main_widget.setMinimumSize(QtCore.QSize(720, 611))
        main_widget.setMaximumSize(QtCore.QSize(720, 611))
        main_widget.setObjectName("main_widget")

        return main_widget

    def make_stacked_widget(self):
        main_stacked_widget = QtWidgets.QStackedWidget(self.central_widget)
        main_stacked_widget.setGeometry(QtCore.QRect(160, 0, 713, 611))
        main_stacked_widget.setMinimumSize(QtCore.QSize(713, 611))
        main_stacked_widget.setMaximumSize(QtCore.QSize(713, 611))
        main_stacked_widget.setBaseSize(QtCore.QSize(0, 0))
        main_stacked_widget.setStyleSheet("\\")
        main_stacked_widget.setFrameShape(QtWidgets.QFrame.NoFrame)
        main_stacked_widget.setObjectName("main_stacked_widget")

        return main_stacked_widget

    def make_combo_box(self, name, geometry):
        combo_box = QtWidgets.QComboBox(self.option)
        combo_box.setGeometry(QtCore.QRect(geometry[0], geometry[1], 181, 32))
        font = QtGui.QFont()
        font.setPointSize(11)
        combo_box.setFont(font)
        combo_box.setObjectName(name)

        return combo_box

    def make_storage_line(self, name, geometry):
        storage_line = QtWidgets.QLineEdit(self.option)
        storage_line.setGeometry(QtCore.QRect(geometry[0], geometry[1], 181, 32))
        font = QtGui.QFont()
        font.setPointSize(11)
        storage_line.setFont(font)
        storage_line.setObjectName(name)

        return storage_line

    def make_slider(self, name, geometry, min, max):
        slider = QtWidgets.QSlider(self.option)
        slider.setGeometry(QtCore.QRect(geometry[0], geometry[1], 181, 32))
        font = QtGui.QFont()
        font.setPointSize(11)
        slider.setFont(font)
        slider.setMinimum(min)
        slider.setMaximum(max)
        slider.setOrientation(QtCore.Qt.Horizontal)
        slider.setObjectName(name)

        return slider

    def make_check_button(self, name, geometry):
        button = QtWidgets.QCheckBox(self.option)
        button.setGeometry(QtCore.QRect(geometry[0], geometry[1], 31, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        button.setFont(font)
        button.setText("")
        button.setObjectName(name)

        return button

    def make_layout_widget_for_label(self):
        layout_widget_labels = QtWidgets.QWidget(self.option)
        layout_widget_labels.setGeometry(QtCore.QRect(60, 20, 165, 551))
        layout_widget_labels.setObjectName("layout_widget_labels")

        return layout_widget_labels

    def make_label(self, name, widget):
        label = QtWidgets.QLabel(widget)
        font = QtGui.QFont()
        font.setPointSize(11)
        label.setFont(font)
        label.setObjectName(name)

        return label

    def make_button(self, name, geometry):
        button_browse = QtWidgets.QPushButton(self.option)
        button_browse.setGeometry(QtCore.QRect(geometry[0], geometry[1], 91, 32))
        button_browse.setCheckable(True)
        button_browse.setAutoExclusive(True)
        button_browse.setObjectName(name)

        return button_browse

    def make_lcd_display(self, name, geometry, height, width):
        display = QtWidgets.QLCDNumber(self.option)
        display.setGeometry(QtCore.QRect(geometry[0], geometry[1], height, width))
        display.setObjectName(name)

        return display

    def make_horizontal_slider(self, name, geometry, min, max):
        horizontal_slider = QtWidgets.QSlider(self.option)
        horizontal_slider.setGeometry(QtCore.QRect(geometry[0], geometry[1], 181, 32))
        font = QtGui.QFont()
        font.setPointSize(11)
        horizontal_slider.setFont(font)
        horizontal_slider.setMinimum(min)
        horizontal_slider.setMaximum(max)
        horizontal_slider.setProperty("value", 10)
        horizontal_slider.setOrientation(QtCore.Qt.Horizontal)
        horizontal_slider.setObjectName(name)

        return horizontal_slider

    def make_line(self, name, geomtery):
        path = QtWidgets.QLineEdit(self.option)
        path.setGeometry(QtCore.QRect(geomtery[0], geomtery[1], 182, 32))
        font = QtGui.QFont()
        font.setPointSize(11)
        path.setFont(font)
        path.setObjectName(name)

        return path

    def close_app(self):
        self.main_winow.close()

    def select_option_widget(self):
        self.main_stacked_widget.setCurrentIndex(0)

    def show_user_settings(self):
        self.show_settings(self.controller.get_user_settings())

    def show_settings(self, settings):
        self.resolution_combo_box.addItems(settings['resolution'])
        self.resolution_combo_box.setCurrentIndex(0)
        self.FPS_combo_box.addItems(settings['fps'])
        self.FPS_combo_box.setCurrentIndex(0)
        self.codec_combo_box.addItems(settings['codec'])
        self.codec_combo_box.setCurrentIndex(0)
        self.display_combo_box.addItems(settings['display'])
        self.display_combo_box.setCurrentIndex(0)

        self.video_hotkey.setText(settings['video_hotkey'])
        self.screen_hotkey.setText(settings['screen_hotkey'])
        self.sounds_button.setChecked(settings['save_sound'])
        self.quality_slider.setValue(settings['quality'])
        self.duration_horizontal_slider.setValue(settings['duration'])
        self.v_storage_line.setText(settings['video_path'])
        self.s_storage_line.setText(settings['screen_path'])

        self.ram_display.display(settings['ram_ussage'])

    def restart_settings(self):
        self.show_settings(self.controller.get_default_settings())

    def save_settings(self):
        new_settings = {'resolution': self.resolution_combo_box.currentText(),
                        'fps': self.FPS_combo_box.currentText(),
                        'codec': self.codec_combo_box.currentText(),
                        'display': self.display_combo_box.currentText(),
                        'video_hotkey': self.video_hotkey.text(),
                        'screen_hotkey': self.screen_hotkey.text(),
                        'save_sound': self.sounds_button.isChecked(),
                        'quality': self.quality_slider.value(),
                        'duration': self.duration_horizontal_slider.value(),
                        'video_path': self.v_storage_line.text(),
                        'screen_path': self.s_storage_line.text(),
                        'ram_ussage': 0}
        ram_ussage = self.controller.save_settings(new_settings)
        new_settings['ram_ussage'] = ram_ussage
        self.show_settings(new_settings)

    def browse_v_storage(self):
        folder = QFileDialog.getExistingDirectory(QMainWindow(), "Wybierz folder")
        self.v_storage_line.setText(folder)

    def browse_s_storage(self):
        folder = QFileDialog.getExistingDirectory(QMainWindow(), "Wybierz folder")
        self.s_storage_line.setText(folder)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.main_window.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.option_button.setText(_translate("MainWindow", "Option"))
        self.video_button.setText(_translate("MainWindow", "Video"))
        self.editor_button.setText(_translate("MainWindow", "Video editor"))
        self.exit_button.setText(_translate("MainWindow", "Exit"))
        self.resolution_label.setText(_translate("MainWindow", "Resolution"))
        self.FPS_label.setText(_translate("MainWindow", "FPS"))
        self.Codec_label.setText(_translate("MainWindow", "Codec"))
        self.v_hotkey.setText(_translate("MainWindow", "Video Hotkey"))
        self.s_hotkey.setText(_translate("MainWindow", "Screen Hotkey"))
        self.sound_label.setText(_translate("MainWindow", "Save with sounds"))
        self.quality_label.setText(_translate("MainWindow", "Bitrate/Quality"))
        self.duration_label.setText(_translate("MainWindow", "Video duration (s)"))
        self.v_storage_label.setText(_translate("MainWindow", "Video storage path"))
        self.s_storage_label.setText(_translate("MainWindow", "Screen storage path"))
        self.display_label.setText(_translate("MainWindow", "Display"))
        self.v_storage_browse.setText(_translate("MainWindow", "Browse"))
        self.s_storage_browse.setText(_translate("MainWindow", "Browse"))
        self.reset_button.setText(_translate("MainWindow", "Reset"))
        self.save_button.setText(_translate("MainWindow", "Save"))
        self.ram_label.setText(_translate("MainWindow", "RAM requirements (MB)"))