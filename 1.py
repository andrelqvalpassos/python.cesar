import math

def graus_para_radianos(graus):
    radianos = graus * (math.pi / 180)
    return radianos

graus = float(input("Digite o valor do ângulo em graus: "))
radianos = graus_para_radianos(graus)
print(f"O ângulo em radianos é: {radianos:.4f}")
