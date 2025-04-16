import random

def rolar_dado():
    input("🎲 Pressione Enter para rolar o dado de 20 lados...")
    resultado = random.randint(1, 20)
    print(f"🎲 Dado rolado: {resultado}")
    return resultado
