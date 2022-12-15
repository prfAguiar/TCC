from manim import *

config.frame_width = 14.22
config.frame_height = 8

class Formula(Scene):
    # Sobrescrevendo método construct de Scene
    def construct(self):
        fraseGraficosMovimentoUniforme = Text("Vamos para o gráfico de velocidade por tempo", weight=BOLD, font_size=36).to_corner(UP+LEFT)
        self.play(Write(fraseGraficosMovimentoUniforme))
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
        y_label = graficoVelocidade_Tempo.get_y_axis_label("v(cm/s)", direction= LEFT, buff=0.4)
        x_label = graficoVelocidade_Tempo.get_x_axis_label("t(s)")
        lineVelocidade_Tempo = graficoVelocidade_Tempo.plot_line_graph(x, y, add_vertex_dots=False)
        textoGraficoVelocidade_Tempo = Tex('Gráfico de velocidade(v) pelo tempo(t)', color = RED).to_corner(UP)
        self.play(FadeOut(fraseGraficosMovimentoUniforme))
        self.play(Create(graficoVelocidade_Tempo), Create(lineVelocidade_Tempo), Create(textoGraficoVelocidade_Tempo), run_time=3)
        self.play(Write(y_label), Write(x_label))
        self.wait(5)