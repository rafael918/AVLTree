# main.py

from avl_tree import AVLTree, Node

def main():
    avl_tree = AVLTree()
    root = None
    pacientes = [
        ("Alice", 30, "A123"),
        ("Bob", 25, "B456"),
        ("Charlie", 35, "C789"),
        ("David", 20, "D012"),
        ("Eva", 28, "E345"),
        ("Frank", 40, "F678"),
        ("Grace", 32, "G901"),
        ("Helen", 45, "H234"),
        ("Ivan", 27, "I567"),
        ("Jack", 38, "J890"),
        ("Kate", 29, "K123"),
        ("Liam", 33, "L456"),
        ("Megan", 42, "M789"),
        ("Nora", 26, "N012"),
        ("Oliver", 37, "O345"),
        ("Patricia", 31, "P678"),
        ("Quinn", 44, "Q901"),
        ("Ryan", 36, "R234"),
        ("Candido", 39, "C5")
    ]

    for paciente in pacientes:
        nome, idade, codigo = paciente
        root = avl_tree.insert(root, idade)

    print("Preorder traversal da Árvore AVL:")
    avl_tree.pre_order(root)

if __name__ == "__main__":
    main()
