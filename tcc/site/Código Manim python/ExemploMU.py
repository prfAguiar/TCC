from manim import *

config.frame_width = 14.22
config.frame_height = 8

class Formula(Scene):
    # Sobrescrevendo método construct de Scene
    def construct(self):
        equacaoMovimentoUniforme = MathTex(r'S = S_{0} + v * t').scale(2)
        fraseInfoEquacao = Text("Resolvendo a equação de acordo com as informações", weight=BOLD, font_size=36)
        fraseInfoEquacao2 = Text("obtidas, podemos obter o deslocamento, velocidade", weight=BOLD, font_size = 36).next_to(fraseInfoEquacao, DOWN)
        fraseInfoEquacao3 = Text("ou até o tempo", weight=BOLD, font_size = 36).next_to(fraseInfoEquacao2, DOWN)
        frasesInfoEquacao = Group(fraseInfoEquacao, fraseInfoEquacao2, fraseInfoEquacao3).to_corner(UP+LEFT)
        fraseResolvendoEquacao_Tempo = Text("Descobrindo o tempo:", weight=BOLD, font_size=36).to_corner(UP+LEFT)
        equacaoMovimentoUniformeParcial = MathTex(r'7cm = 2cm + 1cm/s * t').scale(2)
        self.play(Transform(frasesInfoEquacao, fraseResolvendoEquacao_Tempo), Transform(equacaoMovimentoUniforme, equacaoMovimentoUniformeParcial))
        self.wait(3)
        equacaoMovimentoUniformeParcial2 = MathTex(r't = \frac{5cm}{1cm/s}').scale(2)
        self.play(Transform(equacaoMovimentoUniforme, equacaoMovimentoUniformeParcial2))
        self.wait(3)
        equacaoMovimentoUniformeCompleto = MathTex(r't = 5 segundos').scale(2)
        self.play(Transform(equacaoMovimentoUniforme, equacaoMovimentoUniformeCompleto))
        self.wait(3)
        fraseMotivadora = Text("Bem fácil não é?", weight=BOLD, font_size=36).to_corner(UP+LEFT)
        fraseVelocidadeConstante = Text("Podemos perceber que a velocidade é constante", weight=BOLD, font_size = 36)
        formulaVelocidadeConstante = MathTex(r'V = V_{0}').scale(2).next_to(fraseVelocidadeConstante, DOWN)
        self.play(FadeOut(equacaoMovimentoUniforme, frasesInfoEquacao),
                FadeIn(fraseMotivadora, fraseVelocidadeConstante, formulaVelocidadeConstante))
        self.wait(5)