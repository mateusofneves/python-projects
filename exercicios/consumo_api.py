# função retorna % de sucesso
def verifica_sucesso():
    
    for i in range(len(endpoint)):
            
        total = 0
        sucesso = 0
        
        for codigo in status[i]:
            
            total += 1
            
            if codigo >= 200 and codigo < 300:
                sucesso += 1
                
        porcentagem = (sucesso / total) * 100
        
        print(f"{endpoint[i]}: {porcentagem:.2f}%.")
                
# função retorna endpoint com maior numero de erros
def endpoint_maior_erros():
    
    maior_erros = 0
    endpoint_maior = ""
    
    for i in range(len(endpoint)):
        erros = 0
        
        for codigo in status[i]:
            if codigo >= 400:
                erros += 1
                
        if erros > maior_erros:
            maior_erros = erros
            
            endpoint_maior = endpoint[i]
                
    print(f"O endpoint com mais erros é: {endpoint_maior} com {maior_erros} erros.")
        
# função verifica endpoint com erros seguidos
def erros_seguidos():
    
    for i in range(len(endpoint)):
        
        for j in range(len(status[i]) - 1):
            
            if status[i][j] >= 400 and status[i][j + 1] >= 400:
                print(f"Erros consecutivos encontrados em: {endpoint[i]}.")
                
                break
    
# função classifica endpoint    
def classifica_endpoint():

    for i in range(len(endpoint)):

        total = len(status[i])

        sucesso = 0

        critico = False

        for j in range(total):

            if 200 <= status[i][j] < 300:
                sucesso += 1

            if j < total - 1:
                if status[i][j] >= 400 and status[i][j+1] >= 400:
                    critico = True

        porcentagem = (sucesso / total) * 100

        if critico:
            classificacao = "CRÍTICO"

        elif porcentagem >= 80:
            classificacao = "ESTÁVEL"

        else:
            classificacao = "INSTÁVEL"

        print(f"{endpoint[i]} -> {classificacao}")
    
# função relatório com dados organizados
def relatorio():
    print("================")
    print("RELATÓRIO DA API")
    print("================")
    
    print("\n1. Percentual de sucesso")
    verifica_sucesso()

    print("\n2. Endpoint com mais erros")
    endpoint_maior_erros()

    print("\n3. Erros consecutivos")
    erros_seguidos()

    print("\n4. Classificação")
    classifica_endpoint()
 
endpoint = ["/login", "/produtos", "/pedidos"]
 
status = [
    [200, 200, 401, 200, 500],
    [200, 200, 200, 200, 200],
    [201, 500, 502, 201, 500]
]

relatorio()
