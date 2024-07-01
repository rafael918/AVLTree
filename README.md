# AVLTree
Nesta tarefa você deverá implementar uma árvore AVL. Uma Árvore AVL é uma árvore balanceada, ela se auto-organiza sempre que o Fator de Balanceamento atinge um limiar. Você deverá implementar uma versão desta árvore utilizando os dados que estão sendo utilizandos como base (Utilize o dado de Idade para inserir na AVL).
Travessia Pré-Ordem (Preorder Traversal)
A travessia pré-ordem é uma das maneiras de percorrer (ou "visitar") os nós de uma árvore binária. Ela segue a seguinte ordem:

Visita o nó atual.
Visita o nó da subárvore esquerda.
Visita o nó da subárvore direita.
Na saída que você forneceu:

Copiar código
30 27 25 20 26 28 29 37 35 32 31 33 36 40 38 39 44 42 45
Isso significa que os nós foram visitados de acordo com a travessia pré-ordem. Vamos interpretar isso:

30 é o nó raiz da árvore AVL.
27 é o nó à esquerda do nó 30.
25 é o nó à esquerda do nó 27.
20 é o nó à esquerda do nó 25.
26 é o nó à direita do nó 25.
28 é o nó à direita do nó 27.
29 é o nó à direita do nó 28.
Depois disso, a árvore continua a ser percorrida:

37 é o nó à direita do nó 30.
35 é o nó à esquerda do nó 37.
32 é o nó à esquerda do nó 35.
31 é o nó à esquerda do nó 32.
33 é o nó à direita do nó 32.
36 é o nó à direita do nó 35.
E assim por diante, até que todos os nós tenham sido visitados na ordem correta de travessia pré-ordem.

Significado na Árvore AVL
Uma Árvore AVL é uma árvore binária de busca balanceada, onde o fator de balanceamento (diferença entre a altura das subárvores esquerda e direita de qualquer nó) é mantido para garantir que a altura da árvore seja minimizada. Isso ajuda a manter o desempenho das operações de busca, inserção e remoção em tempo logarítmico em relação ao número de nós na árvore.

Portanto, a travessia pré-ordem que você observou reflete a estrutura da Árvore AVL após a inserção dos valores de idade dos pacientes. Cada número representa um nó na árvore e a ordem em que esses números são exibidos reflete a ordem de visita durante a travessia pré-ordem.
