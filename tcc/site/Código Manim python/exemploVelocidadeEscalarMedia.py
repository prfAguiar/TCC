from manim import *


class Formula(Scene):
    def construct(self):
        line = NumberLine(x_range=[0, 10, 1], length=10,
                          include_tip=True,
                          include_numbers=True)
        medida = Tex('cm')
        medida.move_to(line).to_corner(RIGHT)
        dot = Dot(color=RED).move_to(line.number_to_point(2))
        self.add(line, medida, dot)

        self.play(
            FadeIn(line, shift=DOWN),
            FadeIn(dot),
        )
        self.wait(2)

        teste = 0
        dn = DecimalNumber(0)
        self.add(dn.next_to(line.number_to_point(0), LEFT, buff=0.5))
        self.clock = 0
        def update_timer(mob, dt):
            self.clock += dt
            if self.clock >= 5:
                self.clock = 5
            mob.set_value(self.clock)
    
        dn.add_updater(update_timer)

        self.add(dot)
        self.play(dot.animate.shift(RIGHT * 5), run_time=5, rate_func=linear)

        Double_arrow = DoubleArrow(start=line.number_to_point(2), end = line.number_to_point(7), buff=0, color = BLUE)
        self.play(Write(Double_arrow), run_time = 3)

        self.play(FadeOut(line, medida, dot, dn))
        distancia = Tex("5 cm").next_to(Double_arrow, UP)
        self.play(Write(distancia))

        deslocamentoInicial = MathTex(r'S_{0} = 2 cm} ').scale(1).to_edge(DOWN)
        deslocamentoFinal = MathTex(r'S_{f} = 7 cm}').scale(1).to_edge(DOWN)
        deslocamentoFinal.move_to(deslocamentoInicial).to_corner(RIGHT)
        deslocamentos = Group(deslocamentoInicial, deslocamentoFinal)
        self.add(deslocamentos.next_to(line, DOWN))
        self.wait(4)
        deltaDeslocamento = MathTex(r'\Delta s = 5 cm}').scale(1)
        deltaTempo = MathTex(r'\Delta t = 5 s}').scale(1).next_to(deltaDeslocamento, UP * 5)
        self.play(Transform(deslocamentos, deltaDeslocamento), Write(deltaTempo))
        self.play(FadeOut(Double_arrow, distancia))
        self.wait(5)