class Move:
    def __init__(self, initial_pos, final_pos):
        self.initial_pos = initial_pos
        self.final_pos = final_pos

    def __repr__(self):
        return f"Move({self.initial_pos}, {self.final_pos})"
