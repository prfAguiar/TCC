from manim import *

config.frame_width = 14.22
config.frame_height = 8

class formulaMovimentoUniforme(Scene):
    # Sobrescrevendo método construct de Scene
    def construct(self):
        fraseEquacao = Text("Uma fórmula importante do", weight=BOLD, font_size=36).to_corner(UP+LEFT)
        fraseEquacao2 = Text("movimento uniforme", weight=BOLD, font_size = 36).next_to(fraseEquacao, DOWN)
        #
        self.play(FadeIn(fraseEquacao, fraseEquacao2))
        self.wait(2)
        equacaoMovimentoUniforme = MathTex(r'S = S_{0} + v * t').scale(2)
        self.add(equacaoMovimentoUniforme)
        self.play(Write(equacaoMovimentoUniforme))
        self.wait(4)
        self.play(FadeOut(fraseEquacao, fraseEquacao2))
        fraseInfoEquacao = Text("Resolvendo a equação de acordo com as informações", weight=BOLD, font_size=36)
        fraseInfoEquacao2 = Text("obtidas, podemos obter o deslocamento, velocidade", weight=BOLD, font_size = 36).next_to(fraseInfoEquacao, DOWN)
        fraseInfoEquacao3 = Text("ou até o tempo", weight=BOLD, font_size = 36).next_to(fraseInfoEquacao2, DOWN)
        frasesInfoEquacao = Group(fraseInfoEquacao, fraseInfoEquacao2, fraseInfoEquacao3).to_corner(UP+LEFT)
        self.play(FadeIn(frasesInfoEquacao))
        self.wait(4)