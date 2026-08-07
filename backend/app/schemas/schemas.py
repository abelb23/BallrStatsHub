from enum import Enum
from pydantic import BaseModel, Field
from typing import Optional, List

class IssueStatus(str, Enum):
    open = "open"
    IN_PROGRESS = "in_progress"
    CLOSED = "closed"

class IssuePriority(str, Enum):
    low = "low"
    medium = "medium"
    high = "high"

class IssueCreate(BaseModel):
    title: str = Field(min_length=3, max_length=100)
    description: str = Field(min_length=5, max_length=1000)
    priority: IssuePriority = Field(default=IssuePriority.medium)

class IssueUpdate(BaseModel):
    title: Optional[str] = Field(min_length=None, max_length=100)
    description: Optional[str] = Field(min_length=None, max_length=1000)
    status: Optional[IssueStatus]
    priority: Optional[IssuePriority]

class IssueOut(BaseModel):
    id: str
    title: str
    description: str
    status: IssueStatus
    priority: IssuePriority