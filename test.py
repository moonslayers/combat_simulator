from cEngine import *
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import os
import copy


def run(main_combat,it):
    c1 = copy.deepcopy(main_combat.cs[0])  # Crear una copia independiente de c1
    c2 = copy.deepcopy(main_combat.cs[1])
    win=[]
    asalt=[]
    blood1=[]
    blood2=[]
    armor1=[]
    armor2=[]
    first1=[]
    first2=[]
    ataque1=[]
    ataque2=[]
    defensa1=[]
    defensa2=[]
    counter1=[]
    counter2=[]
    j=it
    print("Simulando combate...")
    for i in range(j):
        c1_copy = copy.deepcopy(c1)  # Crear una copia independiente de c1
        c2_copy = copy.deepcopy(c2)
        main_combat=Combate(c1_copy,c2_copy)
        while main_combat.ganador=='':
            main_combat.whofirst()
            main_combat.status()
        win.append(main_combat.ganador)
        asalt.append(main_combat.asaltos)
        blood1.append(sum(main_combat.cs[0].hemo)/main_combat.asaltos)
        blood2.append(sum(main_combat.cs[1].hemo)/main_combat.asaltos)
        armor1.append(sum(main_combat.cs[0].armorlost)/main_combat.asaltos)
        armor2.append(sum(main_combat.cs[1].armorlost)/main_combat.asaltos)
        first1.append(main_combat.cs[0].first/main_combat.asaltos)
        first2.append(main_combat.cs[1].first/main_combat.asaltos)
        ataque1.append(main_combat.cs[0].ataque/main_combat.asaltos)
        ataque2.append(main_combat.cs[1].ataque/main_combat.asaltos)
        defensa1.append(main_combat.cs[0].defensa/main_combat.asaltos)
        defensa2.append(main_combat.cs[1].defensa/main_combat.asaltos)
        counter1.append(main_combat.cs[0].counter/main_combat.asaltos)
        counter2.append(main_combat.cs[1].counter/main_combat.asaltos)
    print("Resultados: ")
    print("Asaltos promedio: ", sum(asalt)/j)
    print("empates: ", win.count(0))
    print("ganador 1: ", win.count(1))
    print("ganador 2: ", win.count(2))
    print("iniciativa 1: ", sum(first1)/j)
    print("iniciativa 2: ", sum(first2)/j)
    print("ataques 1: ", sum(ataque1)/j)
    print("ataques 2: ", sum(ataque2)/j)
    print("defensas 1: ", sum(defensa1)/j)
    print("defensas 2: ", sum(defensa2)/j)
    print("counter 1: ", sum(counter1)/j)
    print("counter 2: ", sum(counter2)/j)

    # Datos de ejemplo
    competidores = ['Combatiente 1', 'Combatiente 2']
    empates= [win.count(0),win.count(1), win.count(2)]
    ataques = [sum(ataque1), sum(ataque2)]
    iniciativas = [sum(first1), sum(first2)]
    defensas = [sum(first1), sum(first2)]
    counters = [sum(first1), sum(first2)]
    vida_promedio = [sum(blood1)/j,sum(blood2)/j ]
    armadura_perdida_promedio = [sum(armor1)/j,sum(armor2)/j]

    # Crear el directorio 'static/resultados/resultados' si no existe
    if not os.path.exists('static/resultados/'):
        os.makedirs('static/resultados/')

    # Colores personalizados para las gráficas de pastel
    colores = ['#FF6F00', '#FFD600']

    # Gráfica de número de asaltos promedio
    # Configuración del histograma
    num_bins = 10
    range_min = min(asalt)
    range_max = max(asalt)

    
    # Crear el histograma
    plt.figure(figsize=(8, 6))
    plt.hist(asalt, bins=num_bins, range=(range_min, range_max), color=colores[0])
    plt.xlabel('Asaltos Promedio')
    plt.ylabel('Frecuencia')
    plt.title('Distribución de Asaltos Promedio')
    plt.grid(True)

    plt.savefig('static/resultados/asaltos_promedio_histograma.png')
    plt.close()

    # Gráfica de empates vs ganadas vs perdidas
    plt.figure(figsize=(8, 6))
    plt.pie(empates, labels=["Empate", "Combatiente 1", "Combatiente 2" ], colors=['#FF6F00', '#FFD600', '#FA2051'], autopct='%1.1f%%')
    plt.title('Resultados del combate')
    plt.savefig('static/resultados/empates.png')
    plt.close()

    # Colores de las secciones
    colores = ['#FF5733', '#33FF99']

    # Gráfica de ataques
    plt.figure(figsize=(8, 6))
    plt.bar(competidores, ataques, color=colores)
    plt.title('Ataques exitosos en promedio')
    plt.xlabel('Combatientes')
    plt.ylabel('Ataques en Promedio')
    plt.savefig('static/resultados/ataques.png')
    plt.close()

    # Gráfica de defensas
    plt.figure(figsize=(8, 6))
    plt.bar(competidores, defensas,color=colores)
    plt.title('Defensas exitosas en promedio')
    plt.xlabel('Combatientes')
    plt.ylabel('Defensas')
    plt.savefig('static/resultados/defensas.png')
    plt.close()

    # Gráfica de inciativa
    plt.figure(figsize=(8, 6))
    plt.bar(competidores, iniciativas,color=colores)
    plt.title('Iniciativas en promedio')
    plt.xlabel('Combatientes')
    plt.ylabel('Iniciativas')
    plt.savefig('static/resultados/iniciativas.png')
    plt.close()

    # Gráfica de counters
    plt.figure(figsize=(8, 6))
    plt.bar(competidores, vida_promedio,color=colores)
    plt.title('Contraataques exitosos en promedio')
    plt.xlabel('Combatientes')
    plt.ylabel('Contraataques')
    plt.savefig('static/resultados/counters.png')
    plt.close()

    # Gráfica de vida promedio
    plt.figure(figsize=(8, 6))
    plt.bar(competidores, vida_promedio,color=colores)
    plt.title('Vida Promedio')
    plt.xlabel('Combatientes')
    plt.ylabel('sangre perdida en promedio')
    plt.savefig('static/resultados/vida_promedio.png')
    plt.close()

    # Gráfica de armadura perdida
    plt.figure(figsize=(8, 6))
    plt.bar(competidores, armadura_perdida_promedio,color=colores)
    plt.title('Armadura Perdida Promedio')
    plt.xlabel('Combatientes')
    plt.ylabel('Puntos de armadura')
    plt.savefig('static/resultados/armor.png')
    plt.close()


    print("Gráficas generadas y guardadas en la carpeta 'static/resultados'.")


