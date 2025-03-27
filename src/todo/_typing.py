# _typing.py
from __future__ import annotations

from typing import Literal, TypedDict  # 保留TypedDict和Literal

TaskType = Literal["daily", "weekly", "monthly"]
ActionType = Literal["Added", "Completed_action", "Deleted", "Uncompleted"]


class TaskDict(TypedDict):
    id: str
    task: str
    task_type: TaskType
    color: str
    created_at: str
    completed: bool
    completed_at: str | None
    due_date: str | None


class HistoryItemDict(TypedDict):
    id: str
    action: ActionType
    task_description: str
    task_type: str
    timestamp: str


class DataDict(TypedDict):
    tasks: list[TaskDict]
    history: list[HistoryItemDict]
    last_updated: str


LanguageDict = dict[str, dict[str, str]]
