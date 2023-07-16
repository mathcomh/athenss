import tkinter as tk
from PIL import ImageTk, Image
import plotly.graph_objects as go

def homem():
    
    def enviar_dados():
        
        altura_puxar = float(altura.get())
        peso_puxar = float(peso.get())
        idade_puxar = float(idade.get())
        
        resul.destroy()
        resultado= tk.Tk()
        resultado.title("Resultados")

        calculo = 66 + (9.563 * peso_puxar) + (1.85 * altura_puxar) - (4.676 * idade_puxar)
        necessidade = (0.062 * peso_puxar + 2.036) * 239
        resultados_mostrar_tmb = tk.Label(resultado, text=f"Seu TMB deu: {calculo:.2f}")
        resultados_mostrar_tmb.pack()
        resultados_mostrar_necessidade = tk.Label(resultado, text=f"Sua necessidade calórica deu: {necessidade:.2f}")
        resultados_mostrar_necessidade.pack()
        
        # Generate a Plotly graph
        abs=['tmb', 'necessidade']
        fig = go.Figure([go.Bar(x=abs, y=[calculo, necessidade])])
        
        # Save the graph as an image
        graph_image = "graph.png"
        fig.write_image(graph_image)
        
        # Load the graph image
        image = Image.open(graph_image)

        # Convert the image to Tkinter-compatible format
        image_tk = ImageTk.PhotoImage(image)
    
        # Create a Tkinter label and display the image
        label = tk.Label(resultado, image=image_tk)
        label.image = image_tk
        label.pack()

        # Start the Tkinter event loop for the resultado window
        resultado.mainloop()

    window.destroy()

    resul = tk.Tk()
    resul.title("dados")

    altura_texto= tk.Label(resul, text="Digite sua altura:")
    altura_texto.pack()
    altura = tk.Entry(resul)
    altura.pack()

    peso_texto= tk.Label(resul, text="Digite seu peso:")
    peso_texto.pack()
    peso = tk.Entry(resul)
    peso.pack()
    
    idade_texto= tk.Label(resul, text="Digite sua idade:")
    idade_texto.pack()
    idade = tk.Entry(resul)
    idade.pack()
    
    calculo_butao = tk.Button(resul, text="enviar e calcular", command=enviar_dados)
    calculo_butao.pack()

def mulher():
    
    def enviar_dados():
        
        altura_puxar = float(altura.get())
        peso_puxar = float(peso.get())
        idade_puxar = float(idade.get())
        
        resul.destroy()
        resultado= tk.Tk()
        resultado.title("Resultados")

        calculo = 655.1 + (9.563 * peso_puxar) + (1.85 * altura_puxar) - (4.676 * idade_puxar)
        necessidade = (0.062 * peso_puxar + 2.036) * 239
        resultados_mostrar_tmb = tk.Label(resultado, text=f"Seu TMB deu: {calculo:.2f}")
        resultados_mostrar_tmb.pack()
        resultados_mostrar_necessidade = tk.Label(resultado, text=f"Sua necessidade calórica deu: {necessidade:.2f}")
        resultados_mostrar_necessidade.pack()
        
        # Generate a Plotly graph
        abs=['tmb', 'necessidade']
        fig = go.Figure([go.Bar(x=abs, y=[calculo, necessidade])])
        
        # Save the graph as an image
        graph_image = "graph.png"
        fig.write_image(graph_image)
        
        # Load the graph image
        image = Image.open(graph_image)

        # Convert the image to Tkinter-compatible format
        image_tk = ImageTk.PhotoImage(image)
    
        # Create a Tkinter label and display the image
        label = tk.Label(resultado, image=image_tk)
        label.image = image_tk
        label.pack()

        # Start the Tkinter event loop for the resultado window
        resultado.mainloop()

    window.destroy()

    resul = tk.Tk()
    resul.title("dados")

    altura_texto= tk.Label(resul, text="Digite sua altura:")
    altura_texto.pack()
    altura = tk.Entry(resul)
    altura.pack()

    peso_texto= tk.Label(resul, text="Digite seu peso:")
    peso_texto.pack()
    peso = tk.Entry(resul)
    peso.pack()
    
    idade_texto= tk.Label(resul, text="Digite sua idade:")
    idade_texto.pack()
    idade = tk.Entry(resul)
    idade.pack()
    
    calculo_butao = tk.Button(resul, text="enviar e calcular", command=enviar_dados)
    calculo_butao.pack()

# Create the Tkinter window
window = tk.Tk()
window.title("Menu")

opcao = tk.Label(window, text="Você é homem ou mulher?").place(x=40, y=60)
#opcao.pack()

homi = tk.Button(window, text="Homem", command=homem).place(x=40, y=100)
#homi.pack(ipadx=10, ipady=10)

muie = tk.Button(window, text="Mulher", command=mulher).place(x=40, y=130)
#muie.pack(ipadx=10, ipady=10)

# Start the Tkinter event look
window.mainloop()
