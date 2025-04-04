from __future__ import annotations

import datetime
import json
from pathlib import Path
from typing import TYPE_CHECKING, cast

if TYPE_CHECKING:
    from collections.abc import Callable
import streamlit as st

from todo._dataclass import HistoryItem, Task
from todo._dictionary import LANGUAGES

if TYPE_CHECKING:
    from todo._typing import TaskType
from todo._dataclass import ToDoSettings
from todo.styles.global_style import style
from todo.utils.config import load_settings_file

# Load settings
settings: ToDoSettings = load_settings_file("todo.toml", ToDoSettings)


# ========================
# Filter Functions
# ========================
def filter_daily_tasks(task: Task) -> bool:
    return task.task_type == "daily" and not task.completed


def filter_weekly_tasks(task: Task) -> bool:
    return task.task_type == "weekly" and not task.completed


def filter_monthly_tasks(task: Task) -> bool:
    return task.task_type == "monthly" and not task.completed


def filter_completed_tasks(task: Task) -> bool:
    return task.completed


# ========================
# Sorting Functions
# ========================
def sort_tasks_by_due_date(task: Task) -> tuple[datetime.date, datetime.datetime]:
    """Sort key function for tasks - by due date (earliest first) then creation date (oldest first)"""
    # Handle due_date (primary sort key)
    if task.due_date is None:
        due_date = datetime.date.max
    else:
        safe_time = safe_strptime(task.due_date, "%Y-%m-%d")
        if safe_time is None:
            # Fallback to max date if parsing fails
            due_date = datetime.date.max
        else:
            due_date = safe_time.date()
    # Handle created_at (secondary sort key)
    created_at = safe_strptime(task.created_at, "%Y-%m-%d %H:%M") or datetime.datetime.min
    return (due_date, created_at)


def sort_completed_tasks(task: Task) -> tuple[datetime.datetime, datetime.datetime]:
    completed_at = safe_strptime(task.completed_at, "%Y-%m-%d %H:%M") or datetime.datetime.min
    created_at = safe_strptime(task.created_at, "%Y-%m-%d %H:%M") or datetime.datetime.min
    return (completed_at, created_at)


def sort_history_items(item: HistoryItem) -> datetime.datetime:
    return safe_strptime(item.timestamp, "%Y-%m-%d %H:%M") or datetime.datetime.min


# ========================
# Helper Functions
# ========================
def safe_strptime(date_string: str | None, format: str) -> datetime.datetime | None:
    if not date_string:
        return None
    try:
        return datetime.datetime.strptime(date_string, format)
    except (ValueError, TypeError):
        return None


def t(key: str) -> str:
    return LANGUAGES.get(st.session_state.get("language", "en"), {}).get(key, key)


def get_due_date_info(task: Task, lang: str, today: datetime.date) -> str:
    """返回任务的截止日期信息和状态"""
    if task.completed:
        if task.completed_at:
            try:
                completed_dt = datetime.datetime.strptime(task.completed_at, "%Y-%m-%d %H:%M")
                completed_str = completed_dt.strftime("%Y-%m-%d %H:%M" if lang == "en" else "%Y年%m月%d日 %H:%M")
                return f"✓ {t('Completed')} {completed_str}"
            except (ValueError, TypeError):
                return f"✓ {t('Completed')}"
        else:
            return f"✓ {t('Completed')}"
    elif task.due_date:
        try:
            due_date_obj = datetime.datetime.strptime(task.due_date, "%Y-%m-%d").date()
            days_diff = (due_date_obj - today).days
            if days_diff < 0:
                return f"🔥 {t('Overdue')} {-days_diff} {t('days')}"
            elif days_diff == 0:
                return f"⏰ {t('Due today')}"
            elif days_diff <= 3:
                return f"🗓️ {t('Due in')} {days_diff} {t('days')}"
            else:
                due_date_str = due_date_obj.strftime("%b %d, %Y" if lang == "en" else "%Y年%m月%d日")
                return f"🗓️ {t('Due')} {due_date_str}"
        except (ValueError, TypeError):
            return f"🗓️ {task.due_date} (Invalid)"

    return ""


# ========================
# Constants and Config
# ========================
DATA_FILE = Path(settings.history_file_path)


# ========================
# CSS Styling - 只保留布局相关的CSS
# ========================
def get_layout_css() -> str:
    return """
    <style>
    /* --- Task Card Styling --- */
    .task-card {
        padding: 1rem 1.2rem;
        border-radius: 8px;
        margin-bottom: 1rem;
        position: relative;
        overflow: hidden;
        transition: all 0.2s ease;
    }
    .task-card:hover {
        transform: translateY(-1px);
    }
    .task-card.completed-card {
        border-left-width: 4px;
        border-left-style: solid;
    }
    .task-card .task-content {
        font-size: 1rem;
        font-weight: 500;
        margin-bottom: 0.6rem;
        word-wrap: break-word;
        white-space: pre-wrap;
    }
    .task-card .task-content.completed {
        text-decoration: line-through;
        opacity: 0.8;
    }
    .task-card .meta-info {
        font-size: 0.8rem;
        margin-bottom: 0.8rem;
        display: flex;
        flex-wrap: wrap;
        gap: 0.4rem 1rem;
        align-items: center;
    }
    .meta-due-date {
        display: inline-flex;
        align-items: center;
        gap: 0.3em;
        white-space: nowrap;
    }
    /* --- Action Buttons Container --- */
    .task-actions {
        display: flex;
        justify-content: flex-end;
        align-items: center;
        gap: 0.5rem;
        padding-top: 0.5rem;
    }
    .task-actions .stButton>button {
        padding: 0.25rem 0.6rem !important;
        font-size: 0.85rem !important;
        min-height: auto !important;
        line-height: 1.3 !important;
        border-radius: 5px !important;
        width: auto;
        min-width: 35px;
        text-align: center;
        transition: transform 0.1s ease;
    }
    .task-actions .stButton>button:hover {
        transform: scale(1.05);
    }
    /* History item styling */
    .history-item {
        padding: 0.6rem 1rem;
        margin-bottom: 0.5rem;
        border-radius: 6px;
        border-left: 3px solid;
        font-size: 0.9rem;
        transition: background-color 0.2s ease;
    }
    .history-item .action-text {
        font-weight: 600;
        margin-right: 0.4em;
    }
    .history-item .history-task-preview {
        font-style: italic;
        opacity: 0.9;
    }
    .history-meta {
        font-size: 0.8rem;
        opacity: 0.8;
        margin-top: 0.2rem;
    }
    </style>
    """


# ========================
# Data Persistence
# ========================
def save_data(tasks: list[Task], history: list[HistoryItem]) -> None:
    data = {
        "tasks": [t.to_dict() for t in tasks],
        "history": [h.to_dict() for h in history],
        "last_updated": datetime.datetime.now().strftime("%Y-%m-%d %H:%M"),
    }
    try:
        DATA_FILE.parent.mkdir(exist_ok=True)
        with DATA_FILE.open("w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
    except Exception as e:
        st.error(f"Error saving data: {e}")


def load_data() -> tuple[list[Task], list[HistoryItem]]:
    if DATA_FILE.exists():
        try:
            with DATA_FILE.open("r", encoding="utf-8") as f:
                data = json.load(f)
                tasks = [Task.from_dict(t) for t in data.get("tasks", [])]
                history = [HistoryItem.from_dict(h) for h in data.get("history", [])]
                return tasks, history
        except Exception as e:
            st.error(f"Error loading data: {e}")
    return [], []


# ========================
# UI Components
# ========================
def display_task_list(tasks: list[Task], list_context: str, lang: str) -> None:
    today = datetime.date.today()
    for task in tasks:
        completed_class_card = "completed-card" if task.completed else ""
        card_style = f"background-color: {task.color}1A; border-left-color: {task.color if task.completed else ''};"
        safe_task_desc = task.task
        completed_class_content = "completed" if task.completed else ""

        st.markdown(
            f"""
            <div class='task-card {completed_class_card}' style='{card_style}'>
                <div class='task-content {completed_class_content}'>{safe_task_desc}</div>
            """,
            unsafe_allow_html=True,
        )

        col_meta, col_spacer, col_actions = st.columns([6, 2, 2])

        with col_spacer:
            pass

        with col_meta:
            due_info = get_due_date_info(task, lang, today)
            if due_info:
                st.markdown(
                    f"<div class='meta-info'><span class='meta-due-date'>{due_info}</span></div>",
                    unsafe_allow_html=True,
                )
            else:
                st.markdown("<div class='meta-info'>&nbsp;</div>", unsafe_allow_html=True)

        with col_actions:
            st.markdown("<div class='task-actions'>", unsafe_allow_html=True)
            button_key_base = f"button_{list_context}_{task.id}"
            cols_buttons = st.columns([1, 1])

            with cols_buttons[0]:
                if not task.completed:
                    if st.button(
                        "✓", key=f"complete_{button_key_base}", help=t("mark_complete"), use_container_width=True
                    ):
                        task.completed = True
                        task.completed_at = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
                        st.session_state.history.insert(0, HistoryItem("Completed_action", task.task, task.task_type))
                        save_data(st.session_state.tasks, st.session_state.history)
                        st.rerun()
                else:
                    if st.button(
                        "↩", key=f"undo_{button_key_base}", help=t("mark_incomplete"), use_container_width=True
                    ):
                        task.completed = False
                        task.completed_at = None
                        st.session_state.history.insert(0, HistoryItem("Uncompleted", task.task, task.task_type))
                        save_data(st.session_state.tasks, st.session_state.history)
                        st.rerun()

            with cols_buttons[1]:
                if st.button("🗑️", key=f"delete_{button_key_base}", help=t("delete"), use_container_width=True):
                    st.session_state.tasks = [t for t in st.session_state.tasks if t and t.id != task.id]
                    st.session_state.history.insert(0, HistoryItem("Deleted", task.task, task.task_type))
                    save_data(st.session_state.tasks, st.session_state.history)
                    st.rerun()

            st.markdown("</div>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)


def display_history_items(history_items: list[HistoryItem]) -> None:
    for record in history_items[:30]:
        action_class = record.action.lower().replace("_", "-")
        st.markdown(
            f"""<div class='history-item history-{action_class}'>
                <span class='action-text'>{t(record.action)}:</span>
                <span class='history-task-preview'>"{record.task_description}"</span>
                <div class='history-meta'>{t("task_type")}: {t(record.task_type) if record.task_type in ["daily", "weekly", "monthly"] else record.task_type} | {record.timestamp}</div>
            </div>""",
            unsafe_allow_html=True,
        )


# ========================
# Main Application
# ========================
# Initialize session state
if "tasks" not in st.session_state:
    st.session_state.tasks, st.session_state.history = load_data()
    st.session_state.tasks.sort(key=sort_tasks_by_due_date)
    st.session_state.history.sort(key=sort_history_items, reverse=True)

if settings.as_package:
    pass
else:
    st.set_page_config(page_title="✓ 轻简待办", page_icon="✓", layout="wide")
    style()  # 应用全局样式

# 应用布局CSS
st.markdown(get_layout_css(), unsafe_allow_html=True)

# UI Layout
with st.container():
    cols = st.columns([0.9, 0.1])
    with cols[0]:
        st.title(t("title"))
    with cols[1]:
        st.selectbox(
            "Language/语言",
            options=list(LANGUAGES.keys()),
            format_func=lambda lang_code: "English" if lang_code == "en" else "中文",
            key="language",
            label_visibility="collapsed",
        )
    st.divider()

# Sidebar
with st.sidebar:
    st.header(f"{t('add_task')}")
    with st.form("add_task_form", clear_on_submit=True):
        task_desc = st.text_area(t("task_desc"), placeholder=t("task_placeholder"), key="new_task_desc")
        col_s1, col_s2 = st.columns(2)
        with col_s1:
            task_type: TaskType = cast(
                "TaskType",
                st.radio(
                    t("task_type"),
                    options=["daily", "weekly", "monthly"],
                    format_func=lambda x: t(x),
                    key="new_task_type",
                    horizontal=False,
                ),
            )
        with col_s2:
            task_color = st.color_picker(t("color"), value="#007AFF", key="new_task_color")
        due_date_option = st.date_input(
            t("due_date"), value=None, min_value=datetime.date.today(), key="new_task_due_date"
        )
        submitted = st.form_submit_button(f"✓ {t('add_task')}")
        if submitted and task_desc.strip():
            new_task = Task(
                task=task_desc.strip(),
                task_type=task_type,
                color=task_color,
                due_date=due_date_option.strftime("%Y-%m-%d") if due_date_option else None,
            )
            st.session_state.tasks.insert(0, new_task)
            st.session_state.history.insert(0, HistoryItem("Added", new_task.task, new_task.task_type))
            save_data(st.session_state.tasks, st.session_state.history)
            st.rerun()

# Main Tabs
tab_keys = ["daily", "weekly", "monthly", "completed"]
tabs = st.tabs([t(key) for key in tab_keys])
task_filters: dict[str, Callable[[Task], bool]] = {
    "daily": filter_daily_tasks,
    "weekly": filter_weekly_tasks,
    "monthly": filter_monthly_tasks,
    "completed": filter_completed_tasks,
}

for i, key in enumerate(tab_keys):
    with tabs[i]:
        filtered_tasks = [task for task in st.session_state.tasks if task_filters[key](task)]

        if key == "completed":
            filtered_tasks.sort(key=sort_completed_tasks, reverse=True)
        else:
            filtered_tasks.sort(key=sort_tasks_by_due_date)

        if not filtered_tasks:
            st.info(f"🎉 {t('no_tasks')}")
        else:
            display_task_list(filtered_tasks, key, st.session_state.get("language", "en"))

        if key == "completed":
            st.markdown("---")
            with st.expander(f"📜 {t('history')}", expanded=False):
                if not st.session_state.history:
                    st.info(t("no_history"))
                else:
                    display_history_items(st.session_state.history)
