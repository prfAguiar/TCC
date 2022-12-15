from manim import *


class Formula(Scene):
    def construct(self):
        
        calculoparcialVelocidadeEscalar = MathTex(r'V = \frac{\Delta s}{\Delta t}=\frac{s-s_{0}}{t-t_{0}} = \frac{7cm - 2cm}{5s - 0s}').scale(2)
        calculocompletoVelocidadeEscalar = MathTex(r'V = \frac{5}{5} = 1 cm/s').scale(2)
        self.play(Write(calculoparcialVelocidadeEscalar))
        self.wait(7)
        resposta = Tex('A velocidade escalar média é 1 cm/s')
        resposta.align_to(calculoparcialVelocidadeEscalar, DOWN).to_edge(DOWN)
        self.play(Transform(calculoparcialVelocidadeEscalar, calculocompletoVelocidadeEscalar), Write(resposta))
        self.wait(4)