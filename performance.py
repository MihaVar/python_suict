from abc import ABC, abstractmethod

class AcademicPerformance(ABC):

    def __init__(self, subjects: list[str], scores: list[int]):
        self._subjects = subjects
        self._scores = scores

    def get_subjects(self) -> list[str]:
        return self._subjects

    def get_scores(self) -> list[int]:
        return self._scores

    @abstractmethod
    def calculate_average_score(self) -> float:
        pass
