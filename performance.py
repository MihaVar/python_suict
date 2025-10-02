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

class RealPerformance(AcademicPerformance):

    def calculate_average_score(self) -> float:
        if not self._scores:
            return 0.0
        return sum(self._scores) / len(self._scores)


class DesiredPerformance(AcademicPerformance):

    def __init__(self, subjects: list[str], desired_scores: list[int], desired_avg_score: float):
        super().__init__(subjects, desired_scores)
        self.__desired_avg_score = desired_avg_score

    def calculate_average_score(self) -> float:
        return self.__desired_avg_score

    def get_desired_scores(self) -> list[int]:
        return self._scores