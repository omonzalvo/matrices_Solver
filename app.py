def calculate_two_matrices(matrice_one, matrice_two):
    row_one = len(matrice_one)
    col_one = len(matrice_one[0])
    row_two = len(matrice_two)
    col_two = len(matrice_two[0])

    if col_one != row_two:
        raise ValueError("Number of columns in the first matrix must be equal to the number of rows in the second matrix.")

    result = [[0 for _ in range(col_two)] for _ in range(row_one)]

    for i in range(row_one):
        for j in range(col_two):
            for k in range(col_one):
                result[i][j] += matrice_one[i][k] * matrice_two[k][j]

    return result
def read_matrix(rows, cols, name):
    matrix = []
    for i in range(rows):
        row = list(map(int, input(f"Enter row {i + 1} (space-separated) for {name}: ").strip().split()))
        if len(row) != cols:
            raise ValueError(f"Row {i + 1} must have exactly {cols} elements.")
        matrix.append(row)
    return matrix

def main():

    row_one = int(input("Enter the number of rows for the first matrix: "))
    col_one = int(input("Enter the number of columns for the first matrix: "))
    row_two = int(input("Enter the number of rows for the second matrix: "))
    col_two = int(input("Enter the number of columns for the second matrix: "))


    matrice_one = read_matrix(row_one, col_one, "Matrix A")
    matrice_two = read_matrix(row_two, col_two, "Matrix B")

    result = calculate_two_matrices(matrice_one, matrice_two)

    print("Calculated Metrics:")

    for fila in result:
        print(fila)


if __name__ == "__main__":
    main()