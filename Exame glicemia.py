# Entrada de dados
glicose = int (input("Digite o nível de glicose do paciente: "))

# Método para verificar a glicose do paciente

if (glicose < 100):
    print("O paciente é Normoglicemico")

elif (glicose < 126):
    print("O paciente é pré-diabetico")

else :
    print(" O paciente é diabetico")