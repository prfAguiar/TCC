from manim import *

config.frame_width = 14.22
config.frame_height = 8

class Formula(Scene):
    # Sobrescrevendo método construct de Scene
    def construct(self):
        # Instanciando objetos MathTex, ou seja, chamando o construtor de MathTex
        # MathTex são objetos gráficos para expressões matemáticas
        # Delta em latex
        # title = Tex('Velocidade Escalar Média').to_edge(UP+LEFT)
        # eq2 = MathTex(
        #     r'V = \frac{\Delta s}{\Delta t}=\frac{S-S_{0}}{t-t_{0}}').scale(2)

        # # Chamando método play da superclasse Scene
        # # play é o método que anima os objetos gráficos
        # self.play(Write(title))                         # escrevendo equação
        # self.play(Write(eq2))  # manipulando equação passo 1
        # self.wait()  # manipulando equação passo 2
        # exemploText = Tex('Agora, vamos mostrar um exemplo')
        # exemploText.move_to(title).to_corner(UP+LEFT)
        # self.play(
        #     FadeOut(title),
        #     FadeIn(exemploText, shift=DOWN)
        # )
        # self.wait()
        # line = NumberLine(x_range=[0, 10, 1], length=10,
        #                   include_tip=True,
        #                   include_numbers=True)
        # medida = Tex('cm')
        # medida.move_to(line).to_corner(RIGHT)
        # title_line1 = Tex('Imagine uma formiga caminhando por esta linha. ')
        # title_line2 = Tex('Ela será o pontinho vermelho')
        # title_line1.move_to(exemploText).to_corner(UP+LEFT)
        # title_line2.next_to(title_line1, DOWN)
        # dot = Dot(color=RED).move_to(line.number_to_point(2))
        # self.add(line, medida, title_line1, title_line2, dot)
        # self.play(
        #     Transform(exemploText, title_line1),
        #     FadeIn(title_line2),
        #     FadeOut(eq2),
        #     FadeIn(line, shift=DOWN),
        #     FadeIn(dot),
        # )
        # self.wait(2)
        # self.play(
        #     FadeOut(title_line2)
        # )
        # title_desloc = Tex('Até onde ela caminhará? Este é o deslocamento dela').next_to(title_line1, DOWN)
        # group1 = Group(title_line1, title_desloc)

        # teste = 0
        # dn = DecimalNumber(0)
        # self.add(dn.next_to(line.number_to_point(0), LEFT, buff=0.5))
        # self.clock = 0
        # def update_timer(mob, dt):
        #     self.clock += dt
        #     if self.clock >= 5:
        #         self.clock = 5
        #     mob.set_value(self.clock)
    
        # dn.add_updater(update_timer)

        # self.add(dot)
        # self.play(dot.animate.shift(RIGHT * 5), run_time=5, rate_func=linear)
        # self.play(
        #     FadeIn(group1),
        # )
        # Double_arrow = DoubleArrow(start=line.number_to_point(2), end = line.number_to_point(7), buff=0 , color = BLUE)
        # self.play(Write(Double_arrow), run_time = 3)
        
        # self.play(FadeOut(line, medida, dot, title_line1, dn))
        # distancia = Tex("5 cm").next_to(Double_arrow, UP)
        # self.play(Write(distancia))
        # # group2 = Group(Double_arrow, distancia, dn)
        # deslocamentoInicial = MathTex(r'S_{0} = 2 cm} ').scale(1).to_edge(DOWN)
        # deslocamentoFinal = MathTex(r'S_{f} = 7 cm}').scale(1).to_edge(DOWN)
        # deslocamentoFinal.move_to(deslocamentoInicial).to_corner(RIGHT)
        # deslocamentos = Group(deslocamentoInicial, deslocamentoFinal)
        # self.add(deslocamentos.next_to(line, DOWN))
        # self.wait(4)
        # deltaDeslocamento = MathTex(r'\Delta s = 5 cm}').scale(1).to_edge(DOWN)
        # self.play(Transform(deslocamentos, deltaDeslocamento))

        # self.play(FadeOut(Double_arrow, distancia))
        # self.wait()
        # frase1 = Tex('Como foi percebido, a formiga percorreu 5 centímetros \linebreak em 5 segundos', color = RED).move_to(title_line1).to_edge(UP+LEFT)
        # frase2 = Tex('\nTendo como base o deslocamento inicial e final \linebreak podemos calcular a velocidade escalar média', color = RED).scale(1).next_to(frase1, DOWN)
        # self.play(Transform(exemploText, frase1), Transform(title_desloc, frase2), FadeOut(deslocamentos))
        # self.wait(5)
        # self.play(FadeOut(exemploText, title_desloc))
        # calculoparcialVelocidadeEscalar = MathTex(r'V = \frac{\Delta s}{\Delta t}=\frac{S-S_{0}}{t-t_{0}} = \frac{7 - 2}{5 - 0}').scale(2)
        # calculocompletoVelocidadeEscalar = MathTex(r'V = \frac{5}{5} = 1 cm/s').scale(2)
        # self.play(Write(calculoparcialVelocidadeEscalar))
        # self.wait(7)
        # resposta = Tex('A velocidade escalar média é 1 cm/s')
        # resposta.align_to(calculoparcialVelocidadeEscalar, DOWN).to_edge(DOWN);
        # self.play(Transform(calculoparcialVelocidadeEscalar, calculocompletoVelocidadeEscalar), Write(resposta))
        # self.wait(4)
        # self.play(FadeOut(calculoparcialVelocidadeEscalar, resposta))

        # ax = Axes(
        #     x_range=[-1, 10],
        #     y_range=[-1, 12],
        #     tips=True,
        #     axis_config={"include_numbers": True},
        # )
        # x = [0, 1, 2, 3, 4, 5]
        # y = [2, 3, 4, 5, 6, 7]
        # #plane = NumberPlane()
        # y_label = ax.get_y_axis_label("s(cm)", edge = LEFT, direction= LEFT, buff=0.4)
        # x_label = ax.get_x_axis_label("t(s)")
        # graph = ax.plot_line_graph(x, y, add_vertex_dots=False)

        # textoGraficoVelocidadeEscalar = Tex('Gráfico de deslocamento(s) pelo tempo(t)', color = RED).to_corner(UP)
        # self.play(Create(ax), Create(graph), Create(textoGraficoVelocidadeEscalar), run_time = 3)
        # self.play(Write(y_label), Write(x_label))
        # self.wait(5)
        # self.play(FadeOut(textoGraficoVelocidadeEscalar, ax, y_label, x_label, graph))

        
        movimentoUniforme = Tex('Movimento uniforme')
        self.play(Write(movimentoUniforme))
        self.wait(2)
        self.add(movimentoUniforme)
        self.play(FadeOut(movimentoUniforme))
        fraseMovimentoUniforme = Text("No movimento uniforme a velocidade escalar instantânea", weight=BOLD, font_size=32)
        fraseMovimentoUniforme2 = Text("é constante e igual à velocidade escalar média", weight=BOLD, font_size = 32).next_to(fraseMovimentoUniforme, DOWN)
        self.play(FadeIn(fraseMovimentoUniforme, fraseMovimentoUniforme2))
        self.wait(4)
        self.play(FadeOut(fraseMovimentoUniforme, fraseMovimentoUniforme2))
        fraseEquacao = Text("Uma fórmula importante para se lembrar é a equação de ", weight=BOLD, font_size=36).to_corner(UP+LEFT)
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
        fraseResolvendoEquacao_Tempo = Text("Descobrindo o tempo:", weight=BOLD, font_size=36).to_corner(UP+LEFT)
        equacaoMovimentoUniformeParcial = MathTex(r'7 = 2 + 1 * t').scale(2)
        self.play(Transform(frasesInfoEquacao, fraseResolvendoEquacao_Tempo), Transform(equacaoMovimentoUniforme, equacaoMovimentoUniformeParcial))
        self.wait(3)
        equacaoMovimentoUniformeParcial2 = MathTex(r't = \frac{5}{1}').scale(2)
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
        fraseGraficosMovimentoUniforme = Text("Vamos para os gráficos de velocidade por tempo", weight=BOLD, font_size=36).to_corner(UP+LEFT)
        self.play(FadeOut(fraseMotivadora, fraseVelocidadeConstante, formulaVelocidadeConstante),
                Write(fraseGraficosMovimentoUniforme))
        self.wait(2)
        graficoVelocidade_Tempo = Axes(
            x_range=[-1, 10],
            y_range=[-1, 12],
            tips=True,
            axis_config={"include_numbers": True},
        )
        x = [0, 1, 2, 3, 4, 5]
        y = [1, 1, 1, 1, 1, 1]
        #plane = NumberPlane()
        y_label = graficoVelocidade_Tempo.get_y_axis_label("v(cm/s)")
        x_label = graficoVelocidade_Tempo.get_x_axis_label("t(s)")
        lineVelocidade_Tempo = graficoVelocidade_Tempo.plot_line_graph(x, y, add_vertex_dots=False)
        textoGraficoVelocidade_Tempo = Tex('Gráfico de velocidade(v) pelo tempo(t)', color = RED).to_corner(UP)
        self.play(FadeOut(fraseGraficosMovimentoUniforme))
        self.play(Create(graficoVelocidade_Tempo), Create(lineVelocidade_Tempo), Create(textoGraficoVelocidade_Tempo), run_time=3)
        self.play(Write(y_label), Write(x_label))
        self.wait(5)


