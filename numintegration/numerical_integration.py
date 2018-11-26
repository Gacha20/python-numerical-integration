import numpy as np
import scipy.optimize as so

""" 
    Utilisation de la formule d'Euler pour la dérivation numérique 
    Paramètres : 
        f : la fonction à dériver
        epsilon : 
"""


def derivative(f, epsilon=1e-6):
    def g(x):
        return (f(x+epsilon) - f(x)) / epsilon
    return g


"""
    Classe pour l'intégration numérique via la méthode des trapèzes
"""


class Trapezoid:
    """
        Constructeur
        Paramètres :
            f : la fonction à intégrer
            a : la borne inférieure
            b : la borne supérieure
            n : le pas
    """
    def __init__(self, f, a, b, n):
        self.function = f
        self.a = a
        self.b = b
        self.n = n

    """
        Fonction de calcul de l'aire et de l'estimation de l'erreur
        Retour : Un tuple avec l'aire et l'erreur d'intégration
    """
    def compute(self):

        """
            Calcul de l'aire suivant la formule suivante

                Aire = h * [s + SOMME(1, n-1, f(xi))]

            1) on calcul la valeur d'une unité d'aire (ua) pour n (le pas) ua entre les valeurs a et b
            2) on calcul la valeur de f(x) avec x = (a + b) / 2, soit le milieu de la courbe aux bornes [a; b]
            3) on calcul la valeur de f(x) avec x allant de 1 jusqu'à n avec un pas égal à h
        """
        h = (self.b - self.a) / self.n
        s = 0
        try:
            s = (self.function(self.a) + self.function(self.b)) / 2
        except ZeroDivisionError:
            print("Erreur : la fonction ne convèrge pas")
            return (0,0)

        for i in range(1, self.n):
            s += self.function(self.a + i * h)
        integration = s * h

        """
            Calcul de l'estimation de l'erreur en :
            
                1) Calculant la dérivée seconde de la fonction
                2) En cherchant la valeur de x telle que f"(x) soit la plus grande valeur sur le domaine [a, b]
                3) Calcul de l'estimation de l'erreur via la formule suivante :
                    
                    - [ (b - a)^3 / (n² / 12) ] * M2
        """
        second_derivative = derivative(derivative(self.function))
        m2 = so.fmin(lambda x: -second_derivative(x), 0)[0]
        error = -(np.power((self.b - self.a), 3) / (np.power(self.n, 2) * 12)) * second_derivative(m2)

        return integration, error
