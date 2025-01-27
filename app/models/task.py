from app import db

class Task(db.Model):
    task_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String)
    description = db.Column(db.String)
    completed_at = db.Column(db.DateTime, nullable=True)
    goal_id = db.Column(db.Integer, db.ForeignKey("goal.goal_id"), nullable=True)
    goal = db.relationship("Goal", back_populates="tasks")
    
    @classmethod
    def from_dict(cls, task_data):
        new_task = Task(title=task_data["title"],
                        description=task_data["description"],
                        completed_at=None,
        )
        return new_task

    def to_dict(self):
        return {
            "id": self.task_id,
            "title": self.title,
            "description": self.description,
            "is_complete": self.task_complete()}
    
    def task_complete(self):
        if self.completed_at is None:
            return False
        else:
            return True

    def task_with_goal_to_dict(self):
        return {
        "id": self.task_id,
        "goal_id": self.goal_id,
        "title": self.title,
        "description": self.description,
        "is_complete": self.task_complete()}