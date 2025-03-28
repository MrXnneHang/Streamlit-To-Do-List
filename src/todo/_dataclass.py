from __future__ import annotations

import datetime
import uuid
from typing import TYPE_CHECKING, Annotated

from pydantic import BaseModel, Field

if TYPE_CHECKING:
    from todo._typing import ActionType, HistoryItemDict, TaskDict, TaskType


# ========================
# Data Models
# ========================
class Task:
    def __init__(
        self,
        task: str,
        task_type: TaskType = "daily",
        color: str = "#007AFF",
        due_date: str | None = None,
    ):
        self.id = str(uuid.uuid4())
        self.task = task
        self.task_type: TaskType = task_type
        self.color = color if color else "#007AFF"
        self.created_at = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
        self.completed = False
        self.completed_at: str | None = None
        self.due_date = due_date

    def to_dict(self) -> TaskDict:
        return {
            "id": self.id,
            "task": self.task,
            "task_type": self.task_type,
            "color": self.color,
            "created_at": self.created_at,
            "completed": self.completed,
            "completed_at": self.completed_at,
            "due_date": self.due_date,
        }

    @classmethod
    def from_dict(cls, data: TaskDict) -> Task:
        task = cls(
            task=data["task"],
            task_type=data["task_type"],
            color=data.get("color", "#007AFF"),
            due_date=data.get("due_date"),
        )
        task.id = data["id"]
        task.created_at = data["created_at"]
        task.completed = data["completed"]
        task.completed_at = data.get("completed_at")
        return task


class HistoryItem:
    def __init__(self, action: ActionType, task_description: str, task_type: str):
        self.id = str(uuid.uuid4())
        self.action: ActionType = action
        self.task_description = task_description[:50] + ("..." if len(task_description) > 50 else "")
        self.task_type = task_type if task_type else "unknown"
        self.timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")

    def to_dict(self) -> HistoryItemDict:
        return {
            "id": self.id,
            "action": self.action,
            "task_description": self.task_description,
            "task_type": self.task_type,
            "timestamp": self.timestamp,
        }

    @classmethod
    def from_dict(cls, data: HistoryItemDict) -> HistoryItem:
        return cls(
            action=data["action"],
            task_description=data["task_description"],
            task_type=data["task_type"],
        )


class ToDoSettings(BaseModel):
    history_file_path: Annotated[str, Field("./config/todo_data_simplified.json", title="历史文件路径")]
    as_package: Annotated[bool, Field(False, title="是否作为子项目")]
