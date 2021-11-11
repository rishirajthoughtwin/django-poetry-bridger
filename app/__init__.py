from bridger.menus import ItemPermission, Menu, MenuItem, default_registry

default_app_config = "app.apps.AppConfig"

default_registry.alphabetical_sorted = True
default_registry.register(
    Menu(
        label="Views",
        items=[
            Menu(
                label="Sub Views",
                items=[
                    MenuItem(
                        label="STUDENT",
                        endpoint="student-list",
                        add=MenuItem(label="Add STUDENT", endpoint="student-list"),
                    ),
                ],
            ),
            MenuItem(
                label="Religion",
                endpoint="religion-list",
                add=MenuItem(label="Add Religion", endpoint="religion-list"),
            ),
        ],
        index=1,
    ),
)
