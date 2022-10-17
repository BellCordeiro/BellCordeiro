Gerador de NFTs em python

Esse é um projeto que desenvolvi no final do meu curso, e se trata de um gerador automático de NFTs, o que esse código faz é ler imagens png
de pastas distintas e mesclar essas imagens para gerar NFTs, o codigo é capaz de mudar a Hue de uma determinado arquivo png e automaticamente gerar varias 
versões de arquivo com cores diferentes.
Com esse código eu fui capaz de montar a seguinte loja no opensea:
https://opensea.io/collection/alienz-z

Índices:
1-7 bibliotecas
9-35 nomes que serão usados de maneira recorrente no projeto // chance de determinado itens aparecer
42-54  Criação dos diretórios para receber os arquivos png
56-68 Salva o novo arquivo png
71-171  menu provisório
173-184 ordena os arquivos por numero
188-198 deleta um arquivo e reordena os arquivos restantes
201-209 deleta arquivos em sequencia, e reordena os arquivos
211-214 Conta o numero de arquivos presentes em um diretorio
208- 264  Pequeno menu para escolher valores de hue e pastas para interação
269-380 Escolhe imagens randomicas de cada pasta e cria um nft com base nelas, salva as edições e fecha os diretorios abertos
383-427 Cria um nft usando arquivos especificos de cada pasta
430-550 O mesmo que acima mas varias vezes
561-617 Menu para criar um unico nft manualmente
624-668 converte padrão de cores rgb em hsv e converte hsv em rbg
670-805 gera novos padrões de cores para imagens png
812-870 calcula o numero de combinações possiveis e calcula o numero total de arquivos
874-1633 criação de tags para organização no site  (parte dispensavel)
1639-1641 Seleciona uma cor aleatória
1644-1651 tenta criar as pastas que são necessárias para rodar o arquivo


Desenvolvedor : BellCordeiro

Projeto em desenvolvimento 
