import streamlit as st


def levenshtein_distance(token1, token2):

    m = len(token1) + 1    # row
    n = len(token2) + 1    # column
    matrix = [[0] * n for _ in range(m)]

    for i in range(m):
        matrix[i][0] = i
    for j in range(n):
        matrix[0][j] = j

    for i in range(1, m):
        for j in range(1, n):
            if token1[i - 1] == token2[j - 1]:
                cost = 0
            else:
                cost = 1

            ins_cost = matrix[i][j - 1] + 1
            del_cost = matrix[i - 1][j] + 1
            sub_cost = matrix[i - 1][j - 1] + cost
            matrix[i][j] = min(ins_cost, del_cost, sub_cost)

    return matrix[m - 1][n - 1]


def load_vocab(file_path):
    with open(file_path, 'r') as f:
        lines = f.readlines()
    words = sorted(set([line.strip().lower() for line in lines]))
    return words


vocabs = load_vocab(file_path='data/colors_vocab.txt')


def main():
    st.title("Word Correction using Levenshtein Distance - Learning Colors for Kids")
    word = st.text_input('Enter a color:')

    if st.button("Compute"):

        # compute levenshtein distance
        leven_distances = dict()
        for vocab in vocabs:
            leven_distances[vocab] = levenshtein_distance(word, vocab)

        # sorted by distance
        sorted_distences = dict(
            sorted(leven_distances.items(), key=lambda item: item[1]))
        correct_word = list(sorted_distences.keys())[0]
        st.write('Correct word: ', correct_word)

        col1, col2 = st.columns(2)
        col1.write('Vocabulary:')
        col1.write(vocabs)

        col2.write('Distances:')
        col2.write(sorted_distences)


if __name__ == "__main__":
    main()
