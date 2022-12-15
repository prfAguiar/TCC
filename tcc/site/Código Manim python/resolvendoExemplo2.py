from manim import *


class Formula(Scene):
    def construct(self):
        
        calculoparcialAceleracao = MathTex(r'a = \frac{V_{f} - V_{0}}{t_{f} - t_{0}} = \frac{2m/s - 1m/s}{3s - 0s}').scale(2)
        calculocompletoAceleracao = MathTex(r'a = \frac{1m/s}{3s} = 0.33 m/s^2').scale(2)
        self.play(Write(calculoparcialAceleracao))
        self.wait(7)
        resposta = Tex('A aceleração é de 0.33 m/s²')
        resposta.align_to(calculoparcialAceleracao, DOWN).to_edge(DOWN)
        self.play(Transform(calculoparcialAceleracao, calculocompletoAceleracao), Write(resposta))
        self.wait(4)