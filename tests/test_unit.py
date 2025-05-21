from app.models import Task

def test_task_model():
    task = Task(title="Test Task")
    assert task.title == "Test Task"
    assert not task.done
