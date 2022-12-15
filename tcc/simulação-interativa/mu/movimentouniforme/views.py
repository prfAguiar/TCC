import asyncio
import os
from wsgiref.util import FileWrapper

from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.
from manim import *


def home(request):
    
    return render(request, 'mu.html')

def processa(request):  
    tempo =  request.POST.get('tempo')
    posInicial = request.POST.get('posInicial')
    print(posInicial)
    posFinal = request.POST.get('posFinal')
    deslocamento = int(posFinal) - int(posInicial)
    velocidade = deslocamento / int(tempo)
    print(deslocamento)

    with open("C:\\Users\\Samukinha\\Desktop\\video\\mu\\movimentouniforme\\response.py", "w") as f:
        f.write("from manim import * \n")
        f.write("class VelocidadeEscalarMedia(Scene): \n")
        f.write("\tdef construct(self): \n")
        f.write("\t\tline = NumberLine(x_range=[0, 10, 1], length=10, include_tip=True, include_numbers=True)\n")
        f.write("\t\tmedida = Tex('cm')\n")
        f.write("\t\tmedida.move_to(line).to_corner(RIGHT)\n")
        f.write("\t\tdot = Dot(color=RED).move_to(line.number_to_point("+posInicial+"))\n")
        f.write("\t\tself.add(line, medida, dot)\n")
        f.write("\t\tself.play(FadeIn(line, shift=DOWN), FadeIn(dot))\n")
        f.write("\t\tself.wait(2)\n")
        f.write("\t\tdn = DecimalNumber(0)\n")
        f.write("\t\tself.add(dn.next_to(line.number_to_point(0), LEFT, buff=0.5))\n")
        f.write("\t\tself.clock = 0\n")
        f.write("\t\tdef update_timer(mob, dt):\n")
        f.write("\t\t\tself.clock += dt\n")
        f.write("\t\t\tif self.clock >= "+tempo+":\n")
        f.write("\t\t\t\tself.clock = "+tempo+"\n")
        f.write("\t\t\tmob.set_value(self.clock)\n")
        f.write("\t\tdn.add_updater(update_timer)\n")
        f.write("\t\tself.add(dot)\n")
        f.write("\t\tself.play(dot.animate.shift(RIGHT * "+str(deslocamento)+"), run_time="+tempo+", rate_func=linear)\n")
        f.write("\t\tDouble_arrow = DoubleArrow(start=line.number_to_point("+posInicial+"), end = line.number_to_point("+posFinal+"), buff=0 , color = BLUE)\n")
        f.write("\t\tself.play(Write(Double_arrow), run_time = 3)\n")
        f.write("\t\tself.play(FadeOut(line, medida, dot, dn))\n")
        f.write("\t\tdistancia = Tex('"+ str(deslocamento)+" cm').next_to(Double_arrow, UP)\n")
        f.write("\t\tself.play(Write(distancia))\n")
        f.write("\t\tdeslocamentoInicial = MathTex(r'S_{0} = "+posInicial+" cm} ').scale(1).to_edge(DOWN)\n")
        f.write("\t\tdeslocamentoFinal = MathTex(r'S_{f} = "+posFinal+" cm} ').scale(1).to_edge(DOWN)\n")
        f.write("\t\tdeslocamentoFinal.move_to(deslocamentoInicial).to_corner(RIGHT)\n")
        f.write("\t\tdeslocamentos = Group(deslocamentoInicial, deslocamentoFinal)\n")
        f.write("\t\tself.add(deslocamentos.next_to(line, DOWN))\n")
        f.write("\t\tself.wait(4)\n")
        f.write("\t\tdeltaDeslocamento = MathTex(r'\Delta s = "+ str(deslocamento)+" cm}').scale(1)\n")
        f.write("\t\tdeltaTempo = MathTex(r'\Delta t = "+tempo+" s}').scale(1).next_to(deltaDeslocamento, UP * 5)\n")
        f.write("\t\tself.play(Transform(deslocamentos, deltaDeslocamento), Write(deltaTempo))\n")
        f.write("\t\tself.play(FadeOut(Double_arrow, distancia))\n")
        f.write("\t\tself.wait(5)\n")
    os.system("manim -ql C:\\Users\\Samukinha\\Desktop\\video\\mu\\movimentouniforme\\response.py VelocidadeEscalarMedia")

    with open("C:\\Users\\Samukinha\\Desktop\\video\\mu\\media\\videos\\response\\480p15\\VelocidadeEscalarMedia.mp4", 'rb') as f:
        response = HttpResponse(f, content_type='video/mp4')
        response['Content-Disposition'] = 'attachment; filename="video.mp4"'
        return response
