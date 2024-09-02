# * Ordenação Natural
def natural(names):
    names_sorted = sorted(names)
    return print("Ordenação Natural:",names_sorted)

# * Ordenação Customizada
def customizada(nums):
    def custom(n):
        # Retorna o número mais próximo do valor
        valor = 17
        return abs(valor - n)
    nums_sorted = sorted(nums, key=custom)
    return print("Ordenação Customizada:",nums_sorted)

natural(["Alessandro", "Lucas", "Cristiano", "Murilo"])
customizada([10,15,30,20,20,28])