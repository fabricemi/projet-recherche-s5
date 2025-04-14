def lire_graphe(nom_du_fichier):
    graphe = {}
    with open(nom_du_fichier, 'r') as fichier:
        for ligne in fichier:
            sommet1, sommet2 = map(int, ligne.strip().split())
            if sommet1 not in graphe:
                graphe[sommet1] = set()
            if sommet2 not in graphe:
                graphe[sommet2] = set()
            graphe[sommet1].add(sommet2)
            graphe[sommet2].add(sommet1)

    return graphe


def initialiser_communautes(graphe):
    """Initialiser chaque sommet dans sa propre communauté."""
    communautes = {}
    for sommet in graphe:
        communautes[sommet] = sommet  # Chaque sommet commence dans sa propre communauté
    return communautes


def main():
    nom_du_fichier = "base.txt"
    graphe = lire_graphe(nom_du_fichier)

    communautes = initialiser_communautes(graphe)

    print("Graphe chargé avec succès !")
    print("Nombre de sommets :", len(graphe))
    nombre_aretes = sum(len(voisins) for voisins in graphe.values()) // 2
    print("Nombre d'arêtes :", nombre_aretes)
    print("Nombre initial de communautés :", len(set(communautes.values())))

    """print("\nVoici un petit aperçu du graphe 😊
    compteur = 0
    for sommet in graphe:
        print("Sommet", sommet, "est connecté à :", graphe[sommet])
        compteur += 1
        if compteur == 5:
            break  """


if __name__ == '__main__':
    main()