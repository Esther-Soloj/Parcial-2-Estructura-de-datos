# María Esther Tigüilpa Soloj - 1627021

class Node:
    def __init__(self, data):
        # Constructor de la clase Node que inicializa el nodo con un dato y referencias a los nodos izquierdo y derecho.
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        # Constructor de la clase BinaryTree que inicializa el árbol con la raíz como None.
        self.root = None

    def insert(self, data):
        # Método para insertar un nuevo nodo en el árbol.
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert(data, self.root)

    def _insert(self, data, node):
        # Método auxiliar para la inserción recursiva de un nodo.
        if data <= node.data:
            if node.left is None:
                node.left = Node(data)
            else:
                self._insert(data, node.left)
        else:
            if node.right is None:
                node.right = Node(data)
            else:
                self._insert(data, node.right)

    def preorder_traversal(self, node):
        # Método para realizar un recorrido en preorden del árbol.
        if node is not None:
            print(node.data)
            self.preorder_traversal(node.left)
            self.preorder_traversal(node.right)

    def inorder_traversal(self, node):
        # Método para realizar un recorrido en inorden del árbol.
        if node is not None:
            self.inorder_traversal(node.left)
            print(node.data)
            self.inorder_traversal(node.right)

    def postorder_traversal(self, node):
        # Método para realizar un recorrido en postorden del árbol.
        if node is not None:
            self.postorder_traversal(node.left)
            self.postorder_traversal(node.right)
            print(node.data)

    def export_to_file(self, filename):
        # Método para exportar el árbol a un archivo externo.
        with open(filename, 'w') as f:
            f.write("Preorder: ")
            self._write_preorder(self.root, f)
            f.write("\nInorder: ")
            self._write_inorder(self.root, f)
            f.write("\nPostorder: ")
            self._write_postorder(self.root, f)

    def _write_preorder(self, node, file):
        if node is not None:
            file.write(str(node.data) + " ")
            self._write_preorder(node.left, file)
            self._write_preorder(node.right, file)

    def _write_inorder(self, node, file):
        if node is not None:
            self._write_inorder(node.left, file)
            file.write(str(node.data) + " ")
            self._write_inorder(node.right, file)

    def _write_postorder(self, node, file):
        if node is not None:
            self._write_postorder(node.left, file)
            self._write_postorder(node.right, file)
            file.write(str(node.data) + " ")

    def import_from_file(self, filename):
        # Método para importar el árbol desde un archivo externo.
        with open(filename, 'r') as f:
            lines = f.readlines()
            preorder = lines[0].split()[1:]
            inorder = lines[1].split()[1:]
            postorder = lines[2].split()[1:]

        self.root = self._build_tree(preorder, inorder, postorder)

    def _build_tree(self, preorder, inorder, postorder):
        if not preorder:
            return None

        root_data = preorder[0]
        root = Node(root_data)

        if len(preorder) == 1:
            return root

        root_index_inorder = inorder.index(root_data)

        left_inorder = inorder[:root_index_inorder]
        right_inorder = inorder[root_index_inorder + 1:]

        left_preorder = [elem for elem in preorder if elem in left_inorder]
        right_preorder = [elem for elem in preorder if elem in right_inorder]

        left_postorder = [elem for elem in postorder if elem in left_inorder]
        right_postorder = [elem for elem in postorder if elem in right_inorder]

        root.left = self._build_tree(left_preorder, left_inorder, left_postorder)
        root.right = self._build_tree(right_preorder, right_inorder, right_postorder)

        return root

def play_game(tree):
    # Función para jugar al juego de adivinanzas.
    node = tree.root
    while node.left and node.right:
        answer = input(node.data + " (s/n): ").lower()
        if answer == "s":
            node = node.right
        elif answer == "n":
            node = node.left
        else:
            print("Respuesta inválida. Inténtalo de nuevo.")

    print("¿Es " + node.data + "?")
    answer = input().lower()
    if answer == "s":
        print("¡Adiviné correctamente!")
    else:
        new_object = input("Ingresa el objeto/animal/personaje que tenías en mente: ")
        new_question = input(f"Ingresa una pregunta que distinga '{new_object}' de '{node.data}': ")
        new_answer = input(f"¿La respuesta a la pregunta '{new_question}' es sí o no para '{new_object}'? (s/n): ").lower()
        if new_answer == "s":
            node.data = new_question
            node.right = Node(new_object)
            node.left = Node(node.data)
        else:
            node.data = new_question
            node.left = Node(new_object)
            node.right = Node(node.data)

def learn_and_guess(tree):
    # Función para aprender y adivinar.
    new_object = input("Ingresa el objeto/animal/personaje que tienes en mente: ")
    node = tree.root
    while node.left and node.right:
        answer = input(node.data + " (s/n): ").lower()
        if answer == "s":
            node = node.right
        elif answer == "n":
            node = node.left
        else:
            print("Respuesta inválida. Inténtalo de nuevo.")

    if node.data == new_object:
        print("¡Adiviné correctamente!")
    else:
        new_question = input(f"Ingresa una pregunta que distinga '{new_object}' de '{node.data}': ")
        new_answer = input(f"¿La respuesta a la pregunta '{new_question}' es sí o no para '{new_object}'? (s/n): ").lower()
        if new_answer == "s":
            node.data = new_question
            node.right = Node(new_object)
            node.left = Node(node.data)
        else:
            node.data = new_question
            node.left = Node(new_object)
            node.right = Node(node.data)

def reset_game(tree):
    # Función para reiniciar el juego.
    tree.root = None
    tree.insert("¿Es un animal?")
    tree.root.left = Node("¿Es un perro?")
    tree.root.right = Node("¿Es un gato?")
    print("El juego ha sido reiniciado con el árbol inicial.")

# Menú de opciones
tree = BinaryTree()
tree.insert("¿Es un animal?")
tree.root.left = Node("¿Es un perro?")
tree.root.right = Node("¿Es un gato?")

while True:
    print("\n------BIENVENIDO-----")
    print("JUEGO DE ADIVINANZAS. 📦:")
    print('\nAcciones:')
    print('1- Iniciar el juego')
    print('2- Adivinar y aprender')
    print("3- Reiniciar el juego")
    print("4- Exportar árbol a archivo")
    print("5- Importar árbol desde archivo")
    print("6- Salir")
    opcion = int(input('Seleccione una acción: '))

    if opcion == 1:
        play_game(tree)
    elif opcion == 2:
        learn_and_guess(tree)
    elif opcion == 3:
        reset_game(tree)
    elif opcion == 4:
        filename = input("Ingrese el nombre del archivo para exportar: ")
        tree.export_to_file(filename)
        print("Árbol exportado exitosamente.")
    elif opcion == 5:
        filename = input("Ingrese el nombre del archivo para importar: ")
        tree.import_from_file(filename)
        print("Árbol importado exitosamente.")
    elif opcion == 6:
        print("¡Gracias por utilizar el juego de adivinanzas de Esther ! 😊")
        break
    else:
        print("Opción inválida. Por favor, seleccione una opción válida.")


# el archivo .txt adicional que esta en el repositorio es el que se exporta con los recorridos
# inorden postorden preorden
