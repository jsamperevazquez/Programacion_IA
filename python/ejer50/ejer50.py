class Adn:
    ADN_COMPONENT = ['A', 'C', 'G', 'T']

    def __init__(self, dna_chain):
        # Chequeo que sea de tipo str
        if not isinstance(dna_chain, str):
            raise TypeError('Los datos deben ser string')
        for component in dna_chain:
            # Valido la secuencia de ADN
            if component not in self.ADN_COMPONENT:
                raise ValueError("Componente no válido para ADN")
        self.dna_chain = dna_chain


def hamming_distance(sequence_a, sequence_b):
    # Valido la misma longitud de ambas secuencias
    if len(sequence_a) != len(sequence_b):
        raise ValueError('los datos deben tener la misma longitud')
    # Combino ambas secuencias con zip y sumo los 1 de sum() que devuelve la expresión
    return sum(s1 != s2 for s1, s2, in zip(sequence_a, sequence_b))


if __name__ == '__main__':
    try:
        adn1 = Adn('ACTG')
        adn2 = Adn('ACTG')
        print(hamming_distance(adn1.dna_chain, adn2.dna_chain))
    except ValueError as error:
        print(f"Error en los datos proporcionados: {error}")
    except TypeError as error:
        print(f"Error en los datos proporcionados: {error}")
