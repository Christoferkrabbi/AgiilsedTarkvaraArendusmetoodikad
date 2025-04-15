class Task:
    def __init__(self, title, status="to-do"):
        self.title = title
        self.status = status

    def mark_done(self):
        self.status = "done"
        
        'from task import Task

def test_mark_done():
    task = Task("Testi ülesanne")
    task.mark_done()
    assert task.status == "done"