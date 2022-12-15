from manim import *

class Formula(Scene):
    def construct(self):
        eq2 = MathTex(
                r'V = \frac{\Delta s}{\Delta t}=\frac{s-s_{0}}{t-t_{0}}').scale(2)
        self.play(Write(eq2))
        self.wait(10)