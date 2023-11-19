from pygame import font


class Score:
    def __init__(self, x, y, font_name, font_size):
        self.font = font.Font(font_name, font_size)
        self.x = x
        self.y = y
        self.score = 0

    # Draw the score on the screen

    def draw(self, window):
        score_text = self.font.render(f"Score: {self.score}", True, (255, 255, 255))
        window.blit(score_text, (self.x, self.y))
        
    # Update the score

    def update(self, new_score):
        self.score = new_score
