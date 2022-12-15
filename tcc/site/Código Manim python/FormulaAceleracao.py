from manim import *

class Formula(Scene):
    def construct(self):
        eq2 = MathTex(
                r'a = \frac{V_{F}-V_{0}}{t_{F}-t_{0}').scale(2)
        self.play(Write(eq2))
        self.wait(10)