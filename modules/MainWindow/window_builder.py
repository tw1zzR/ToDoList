from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

def setup_UI(main_window):
    setup_main_window(main_window)

    setup_layouts(main_window)
    setup_scroll_area(main_window)
    setup_alignments(main_window)

    setup_buttons(main_window)
    setup_tool_menu(main_window)
    setup_connections(main_window)

    setup_object_sizes(main_window)
    setup_object_names(main_window)

def setup_main_window(main_window):
    main_window.setWindowTitle("To Do List")
    main_window.setWindowIcon(QIcon("assets/MainWindow/todolist_icon.png"))
    main_window.setGeometry(900, 400, 800, 700)

def setup_buttons(main_window):
    main_window.completed_task_open_button.setLayoutDirection(Qt.RightToLeft)
    main_window.completed_task_open_button.setIconSize(QSize(25, 25))
    main_window.change_theme_button.setLayoutDirection(Qt.RightToLeft)
    main_window.change_theme_button.setIconSize(QSize(35, 20))
    main_window.add_task_plus_button.setToolTip("Add new task")
    main_window.add_task_plus_button.setIconSize(QSize(30, 30))
    main_window.user_login_button.setIconSize(QSize(50, 50))
    main_window.tool_button.setIconSize(QSize(50, 50))
    main_window.tool_button.setPopupMode(QToolButton.InstantPopup)

def setup_scroll_area(main_window):
    main_window.scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
    main_window.scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
    main_window.scroll_area.setWidgetResizable(True)
    main_window.task_widget.setLayout(main_window.tasks_layout)
    main_window.scroll_area.setWidget(main_window.task_widget)
    main_window.main_window_task_layout.addWidget(main_window.scroll_area)

def setup_layouts(main_window):
    main_window.setCentralWidget(main_window.central_widget)
    main_window.central_widget.setLayout(main_window.main_layout)

    main_window.main_layout.setAlignment(Qt.AlignTop)
    main_window.main_layout.setContentsMargins(0, 0, 0, 0)
    main_window.main_layout.setSpacing(0)

    main_window.main_layout.addLayout(main_window.header_layout, 1)
    main_window.main_layout.addLayout(main_window.main_window_task_layout, 4)
    main_window.main_layout.addLayout(main_window.statusbar_layout, 1)

    main_window.header_layout.addWidget(main_window.tool_button)
    main_window.header_layout.addWidget(main_window.title_label)
    main_window.header_layout.addWidget(main_window.user_login_button)

    main_window.tasks_layout.setAlignment(Qt.AlignTop)
    main_window.tasks_layout.setContentsMargins(75, 25, 75, 25)
    main_window.tasks_layout.setSpacing(30)

    main_window.statusbar_layout.addWidget(main_window.status_label)

def setup_connections(main_window):
    main_window.add_task_button.clicked.connect(main_window.on_click_controller.on_click_task_button)
    main_window.del_tasks_button.clicked.connect(main_window.on_click_controller.on_click_task_button)
    main_window.change_theme_button.clicked.connect(main_window.on_click_controller.on_click_change_theme_button)
    main_window.about_button.clicked.connect(main_window.on_click_controller.on_click_about_button)
    main_window.add_task_plus_button.clicked.connect(main_window.on_click_controller.on_click_task_button)
    main_window.completed_task_open_button.clicked.connect(main_window.on_click_controller.on_click_completed_tasks_button)

    main_window.user_login_button.clicked.connect(main_window.print_dicts)  # test column (delete)

def setup_tool_menu(main_window):
    for button in main_window.menu_buttons:
        action = QWidgetAction(main_window)
        action.setDefaultWidget(button)
        main_window.menu.addAction(action)
    main_window.tool_button.setMenu(main_window.menu)

def setup_object_names(main_window):
    main_window.title_label.setObjectName("title_label")
    main_window.title_tasks_label.setObjectName("title_tasks_label")
    main_window.status_label.setObjectName("status_label")
    main_window.user_login_button.setObjectName("user_login_button")
    main_window.tool_button.setObjectName("tool_button")
    main_window.add_task_plus_button.setObjectName("add_task_plus_button")
    main_window.add_task_button.setObjectName("add_task_button")
    main_window.del_tasks_button.setObjectName("del_tasks_button")
    main_window.change_theme_button.setObjectName("change_theme_button")
    main_window.about_button.setObjectName("about_button")
    main_window.completed_task_open_button.setObjectName("completed_task_open_button")

def setup_object_sizes(main_window):
    main_window.title_tasks_label.setFixedHeight(50)
    main_window.tool_button.setFixedSize(100, 100)
    main_window.tool_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    main_window.user_login_button.setFixedSize(100, 100)
    main_window.user_login_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    main_window.title_label.setFixedHeight(100)
    main_window.title_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    main_window.status_label.setFixedHeight(25)

def setup_alignments(main_window):
    main_window.title_label.setAlignment(Qt.AlignCenter)
    main_window.title_tasks_label.setAlignment(Qt.AlignCenter)
    main_window.status_label.setAlignment(Qt.AlignCenter)