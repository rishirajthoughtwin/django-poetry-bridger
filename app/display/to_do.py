from typing import Optional

from bridger import display as dp
from bridger.display.metadata_config import DisplayConfig


class ToDoDisplayConfig(DisplayConfig):
    def get_instance_display(self) -> Optional[dp.InstanceDisplay]:
        return dp.InstanceDisplay(
            sections=(
                dp.Section(fields=dp.FieldSet(fields=("name", "student_details", "age",'religion'))),
            )
        )

    def get_list_display(self) -> Optional[dp.ListDisplay]:
        return dp.ListDisplay(
            fields=[
                dp.Field(key="name", label="Name"),
                dp.Field(key="student_details", label="Student Details"),
                dp.Field(key="age", label="Age"),
                dp.Field(key="religion", label="Religion"),
            ],
        )
        
class ToDoDisplayConfig(DisplayConfig):
    def get_instance_display(self) -> Optional[dp.InstanceDisplay]:
        return dp.InstanceDisplay(
            sections=(
                dp.Section(fields=dp.FieldSet(fields=("name", "student_details", "age",'religion'))),
            )
        )

    def get_list_display(self) -> Optional[dp.ListDisplay]:
        return dp.ListDisplay(
            fields=[
                dp.Field(key="name", label="Name"),
                dp.Field(key="student_details", label="Student Details"),
                dp.Field(key="age", label="Age"),
                dp.Field(key="religion", label="Religion"),
            ],
        )


