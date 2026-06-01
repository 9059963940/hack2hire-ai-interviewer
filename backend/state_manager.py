class InterviewState:
    def __init__(self):
        self.difficulty = "Easy"
        self.scores = []

    def update_difficulty(self, latest_score):
        if latest_score >= 8:
            self.difficulty = "Hard"

        elif latest_score >= 5:
            self.difficulty = "Medium"

        else:
            self.difficulty = "Easy"

        return self.difficulty
    
    def check_early_termination(self):
    if len(self.scores) < 3:
        return False

    last_3 = self.scores[-3:]

    if sum(last_3) / 3 < 4:
        return True

    return False