def convertStringToBoard(board):
    row = 9
    col = 9

    convertedBoard = []

    offset = 0

    for r in range(row):
        convertedBoard.append([])
        for c in range(col):
            convertedBoard[r].append(board[offset])
            offset = offset + 1

    return convertedBoard

def solve(convertedBoard):

    def isInRow(listOfPossibleValues, convertedBoard, indexRow):
        col = 9

        for c in range(col):
            if convertedBoard[indexRow][c] in listOfPossibleValues:
                listOfPossibleValues.remove(convertedBoard[indexRow][c])

        return listOfPossibleValues

    def isInCol(listOfPossibleValues, convertedBoard, indexCol):
        row = 9

        for r in range(row):
            if convertedBoard[r][indexCol] in listOfPossibleValues:
                listOfPossibleValues.remove(convertedBoard[r][indexCol])

        return listOfPossibleValues

    def isInBox(listOfPossibleValues, convertedBoard, indexRow, indexCol):
        row = indexRow - indexRow % 3
        col = indexCol - indexCol % 3

        for r in range(row, row + 3):
            for c in range(col, col + 3):
                if convertedBoard[r][c] in listOfPossibleValues:
                    listOfPossibleValues.remove(convertedBoard[r][c])

        return listOfPossibleValues

    isThereEmptyCell = True

    while isThereEmptyCell:
        row = len(convertedBoard)
        col = len(convertedBoard[0])

        for r in range(row):
            for c in range(col):
                if convertedBoard[r][c] == "0":
                    indexRow = r
                    indexCol = c

                    listOfPossibleValues = ["1","2","3","4","5","6","7","8","9"]

                    listOfPossibleValues = isInRow(listOfPossibleValues, convertedBoard, indexRow)

                    listOfPossibleValues = isInCol(listOfPossibleValues, convertedBoard, indexCol)

                    listOfPossibleValues = isInBox(listOfPossibleValues, convertedBoard, indexRow, indexCol)

                    if len(listOfPossibleValues) == 1:
                        convertedBoard[indexRow][indexCol] = listOfPossibleValues[0]
                     
                        break

                if r == 8 and c == 8:
                    isThereEmptyCell = False
                    
            else:
                continue
            break

    solution = convertedBoard

    return solution

def convertBoardToString(solution):

    result = ""

    row = len(solution)
    col = len(solution[0])

    for r in range(row):
        for c in range(col):
            result = result + solution[r][c]

    return result

