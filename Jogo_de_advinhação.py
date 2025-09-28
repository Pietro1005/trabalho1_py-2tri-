import random

def jogo_adivinhacao():
    """
    Jogo de adivinhação onde o usuário tenta descobrir um número secreto.
    """
    print("🎯 Bem-vindo ao Jogo de Adivinhação!")
    print("=" * 40)
    print("Tente adivinhar o número secreto entre 1 e 100!")
    print("Digite 'sair' a qualquer momento para encerrar o jogo.")
    print("=" * 40)
    
    numero_secreto = random.randint(1, 100)
    tentativas = 0
    max_tentativas = 10
    
    print(f"\nVocê tem no máximo {max_tentativas} tentativas. Boa sorte!")
    
    while True:
        while True:
            palpite_input = input(f"\n🎲 Tentativa {tentativas + 1}: Digite seu palpite: ").strip()
            
            if not palpite_input:
                print("❌ Erro: Digite um valor!")
                continue
            
            if palpite_input.lower() == 'sair':
                print(f"\n👋 Obrigado por jogar! O número secreto era {numero_secreto}.")
                return
            
            if not palpite_input.isdigit():
                print("❌ Erro: Digite apenas números!")
                continue
            
            palpite = int(palpite_input)
            
            # Validação: verificar faixa de valores
            if palpite < 1 or palpite > 100:
                print("❌ Erro: Digite um número entre 1 e 100!")
                continue
            
            break
        
        tentativas += 1
        
        if palpite == numero_secreto:
            print(f"\n🎉 PARABÉNS! Você acertou em {tentativas} tentativa(s)!")
            print(f"O número secreto era realmente {numero_secreto}!")
            break
        elif palpite < numero_secreto:
            print("📈 Muito baixo! Tente um número maior.")
        else:
            print("📉 Muito alto! Tente um número menor.")
        
        if tentativas >= max_tentativas:
            print(f"\n💀 Fim de jogo! Você atingiu o limite de {max_tentativas} tentativas.")
            print(f"O número secreto era {numero_secreto}.")
            break
        
        if tentativas % 3 == 0:
            print("\n💡 Dica: O número está entre", 
                  max(1, numero_secreto - 20), "e", 
                  min(100, numero_secreto + 20))
    
    print(f"\n📊 Estatísticas:")
    print(f"• Número de tentativas: {tentativas}")
    print(f"• Tentativas restantes: {max_tentativas - tentativas}")
    
    while True:
        resposta = input("\n🔄 Deseja jogar novamente? (s/n): ").strip().lower()
        
        if resposta in ['s', 'sim', 'y', 'yes']:
            print("\n" + "=" * 40)
            jogo_adivinhacao()
            break
        elif resposta in ['n', 'não', 'nao', 'no']:
            print("\n👋 Obrigado por jogar! Até a próxima!")
            break
        else:
            print("❌ Digite 's' para sim ou 'n' para não.")

if __name__ == "__main__":
    jogo_adivinhacao()