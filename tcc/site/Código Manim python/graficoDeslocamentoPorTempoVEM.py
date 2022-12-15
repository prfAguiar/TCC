from manim import *


class Formula(Scene):
    def construct(self):
        ax = Axes(
                    x_range=[-1, 10],
                    y_range=[-1, 12],
                    tips=True,
                    axis_config={"include_numbers": True},
                )
        x = [0, 1, 2, 3, 4, 5]
        y = [2, 3, 4, 5, 6, 7]
        #plane = NumberPlane()
        y_label = ax.get_y_axis_label("s(cm)", edge = LEFT, direction= LEFT, buff=0.4)
        x_label = ax.get_x_axis_label("t(s)")
        graph = ax.plot_line_graph(x, y, add_vertex_dots=False)

        textoGraficoVelocidadeEscalar = Tex('Gráfico de deslocamento(s) pelo tempo(t)', color = RED).to_corner(UP)
        self.play(Create(ax), Create(graph), Create(textoGraficoVelocidadeEscalar), run_time = 3)
        self.play(Write(y_label), Write(x_label))
        self.wait(2)