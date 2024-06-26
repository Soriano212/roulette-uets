from sqlalchemy import Column, ForeignKey, Integer, LargeBinary, String
from sqlalchemy.orm import relationship
from src.core.config.database import Base
from src.core.models.subject_model import SubjectModel


class QuestionModel(Base):
    """Question model class

    Args:
        question_id (int): Question ID
        subject_id (int): Subject ID
        question_text (str): Question text
        image_route (str): Image route
        subject (SubjectModel): Subject model
        options (list): List of options
        have_image (bool): Have image

    Returns:
        QuestionModel: Question model class
    """

    __tablename__ = "question"

    question_id = Column(Integer, primary_key=True, nullable=False)
    subject_id = Column(Integer, ForeignKey(SubjectModel.subject_id), nullable=False)
    question_text = Column(String(510), nullable=False)
    image = Column(LargeBinary)
    subject = relationship("SubjectModel", back_populates="questions")
    options = relationship("OptionModel", back_populates="question")

    @property
    def have_image(self) -> bool:
        return self.image is not None

    @property
    def option_count(self) -> int:
        return len(self.options)

    def __repr__(self) -> str:
        return self.question_text

    def model_to_dict(self, include_option_count=False) -> dict:
        data = {
            "question_id": self.question_id,
            "subject_id": self.subject_id,
            "question_text": self.question_text,
            "have_image": self.have_image,
        }

        if include_option_count:
            data["option_count"] = self.option_count

        return data
