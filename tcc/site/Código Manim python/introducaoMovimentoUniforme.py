from manim import *

class introducaoMovimentoUniforme(Scene):
    # Sobrescrevendo método construct de Scene
    def construct(self):

        movimentoUniforme = Tex('Movimento uniforme')
        self.play(Write(movimentoUniforme))
        self.wait(2)
        self.add(movimentoUniforme)
        self.play(FadeOut(movimentoUniforme))
        fraseMovimentoUniforme = Text("No movimento uniforme a velocidade escalar instantânea", weight=BOLD, font_size=32)
        fraseMovimentoUniforme2 = Text("é constante e igual à velocidade escalar média", weight=BOLD, font_size = 32).next_to(fraseMovimentoUniforme, DOWN)
        self.play(FadeIn(fraseMovimentoUniforme, fraseMovimentoUniforme2))
        self.wait(4)