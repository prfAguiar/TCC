from manim import *

class Formula(Scene):
    def construct(self):
        eq2 = MathTex(
                r'V = \omega * R').scale(2)
        self.play(Write(eq2))
        self.wait(10)