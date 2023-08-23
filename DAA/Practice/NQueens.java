class NQueens {
    static boolean isSafe(int[][] board, int row, int col) {
        for (int i = row; i >= 0; --i)
            if (board[i][col] == 1)
                return false;
        for (int i = row, j = col; i >= 0 && j >= 0; --i, --j)
            if (board[i][j] == 1)
                return false;
        for (int i = row, j = col; i >= 0 && j < board.length; --i, j++)
            if (board[i][j] == 1)
                return false;
        return true;

    }

    static boolean solve(int[][] board, int row) {
        if (row >= board.length)
            return true;
        for (int col = 0; col < board.length; col++) {
            if (isSafe(board, row, col)) {
                board[row][col] = 1;
                if (solve(board, row + 1))
                    return true;
                board[row][col] = 0;
            }
        }
        return false;
    }

    static boolean solve(int[][] board) {
        return solve(board, 0);
    }

    static void show(int size) {
        int[][] board = new int[size][size];
        if (solve(board))
            display(board);
        else
            System.out.println("No Solution found.");
    }

    static void display(int[][] board) {
        for (int row = 0; row < board.length; row++) {
            for (int col = 0; col < board.length; col++)
                if (board[row][col] == 1) {
                    System.out.print("\u2655 ");
                } else {
                    if (row % 2 == col % 2)
                        System.out.print("\u25A1 ");
                    else
                        System.out.print("\u25A0 ");
                }
            System.out.println();
        }
    }

    static void run() {
        int size = 4;
        show(size);
    }

    public static void main(String[] args) {
        run();
    }
}