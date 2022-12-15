from manim import *


class resolvendoExemplo3(Scene):
    def construct(self):
        
        calculoparcialDesaceleracao = MathTex(r'a = \frac{V_{f} - V_{0}}{t_{f} - t_{0}} = \frac{2m/s - 5m/s}{4s - 0s}').scale(2)
        calculocompletoDesaceleracao = MathTex(r'a = \frac{-3m/s}{4s} = -0.75 m/s^2').scale(2)
        self.play(Write(calculoparcialDesaceleracao))
        self.wait(7)
        resposta = Tex('A desaceleração é de 0.75 m/s²')
        resposta.align_to(calculoparcialDesaceleracao, DOWN).to_edge(DOWN)
        self.play(Transform(calculoparcialDesaceleracao, calculocompletoDesaceleracao), Write(resposta))
        self.wait(4)