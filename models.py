from pydantic import BaseModel
from datetime import datetime

class MCPModel(BaseModel):
    name: str
    description: str
    created_at: datetime

    def to_dict(self):
        return {
            "name": self.name,
            "description": self.description,
            "created_at": self.created_at.isoformat()
        }