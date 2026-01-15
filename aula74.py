"""
Closure a funções que retornam outras funções
"""

def criar_saudacao(saudacao, nome) :  
   def saudar():
      return f"{saudacao}, {nome}!"
   return saudar

falar_bom_dia = criar_saudacao("Bom dia", "Tulio")
falar_boa_tarde = criar_saudacao("Boa tarde", "Annie")

for nome in ['Tulio', 'Maria', 'Annie']:
   print(falar_bom_dia())
   print(falar_boa_tarde())

