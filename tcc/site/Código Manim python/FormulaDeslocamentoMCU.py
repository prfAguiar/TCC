from manim import *

class Formula(Scene):
    def construct(self):
        eq2 = MathTex(
                r'S = 2*\pi*R').scale(2)
        self.play(Write(eq2))
        self.wait(10)