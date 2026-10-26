# dataset_schema.py
from typing import Literal
from pydantic import BaseModel, Field, field_validator


class SourceRef(BaseModel):
    doc: str
    page: int | None = None


class GoldenItem(BaseModel):
    id: str
    question: str = Field(min_length=3)
    expected_answer: str | None = None  # unanswerable হলে None
    expected_sources: list[SourceRef] = []  # unanswerable হলে empty
    category: Literal[
        "factual",
        "multi_hop",
        "vague",
        "typo",
        "follow_up",
        "out_of_scope",
        "no_answer",
        "adversarial",
    ]
    difficulty: Literal["easy", "medium", "hard"]
    answerable: bool
    language: Literal["bangla", "english", "banglish"]
    source_type: Literal["manual", "synthetic", "user"]

    # Consistency check: answerable হলে অবশ্যই answer + source থাকতে হবে
    @field_validator("expected_sources")
    @classmethod
    def sources_match_answerable(cls, v, info):
        if info.data.get("answerable") and not v:
            raise ValueError("answerable=True হলে expected_sources লাগবে")
        return v
