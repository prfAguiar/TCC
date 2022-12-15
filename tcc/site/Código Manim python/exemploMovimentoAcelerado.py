from manim import *


class Formula(Scene):
    def construct(self):
        line = NumberLine(x_range=[0, 10, 1], length=10,
                          include_tip=True,
                          include_numbers=True)
        medida = Tex('m')
        medida.move_to(line).to_corner(RIGHT)
        velocidade1 = Tex(' V1=1 m/s')
        velocidade1.move_to(line).to_corner(UP)
        dot = Dot(color=RED).move_to(line.number_to_point(3))
        self.add(line, medida, velocidade1, dot)

        self.play(
            FadeIn(line, shift=DOWN),
            FadeIn(dot),
        )
        self.wait(2)
        dn = DecimalNumber(0)
        self.add(dn.next_to(line.number_to_point(0), LEFT, buff=0.5))
        self.clock = 0
        def update_timer(mob, dt):
            self.clock += dt
            if self.clock >= 3:
                self.clock = 3
            mob.set_value(self.clock)
    
        dn.add_updater(update_timer)

        self.add(dot)
        self.play(dot.animate.shift(RIGHT * 6), run_time=3, rate_func=rush_into)


        velocidade2 = Tex(' V2=2 m/s')
        velocidade2.move_to(line).to_corner(DOWN)
        self.add(velocidade2)

    
        self.play(FadeOut(line, medida, velocidade1, velocidade2, dot, dn))

        velocidadeInicial = MathTex(r'V_{0} = 1 m/s} ').scale(1).to_edge(DOWN)
        velocidadeFinal = MathTex(r'V_{f} = 2 m/s}').scale(1).to_edge(DOWN)
        velocidadeFinal.move_to(velocidadeInicial).to_corner(RIGHT)
        velocidades = Group(velocidadeInicial, velocidadeFinal)
        self.add(velocidades.next_to(line, DOWN))
        self.wait(4)
        tempoInicial = MathTex(r'T_{0} = 0 S} ').scale(1).to_edge(DOWN)
        tempoFinal = MathTex(r'T_{f} = 3 S}').scale(1).to_edge(DOWN)
        tempoFinal.move_to(tempoInicial).to_corner(RIGHT)
        tempos = Group(tempoInicial, tempoFinal)
        self.add(tempos.next_to(line, DOWN))
        deltaVelocidade = MathTex(r'\Delta V = 1 m/s}').scale(1).to_edge(DOWN)
        deltaTempo = MathTex(r'\Delta t = 3 s}').scale(1).next_to(deltaVelocidade, UP * 5)
        self.play(Transform(velocidades, deltaVelocidade), Transform(tempos, deltaTempo))

        self.wait(5)

      