package Programs;

public class Practice {
    public static class GraphColor {
        private static boolean isSafe(int v, int[][] graph, int[] color, int c) {
            for (int i = 0; i < graph.length; i++) {
                if (graph[v][i] == 1 && c == color[i])
                    return false;
            }
            return true;
        }

        private static boolean solve(int[][] graph, int v, int[] color, int m) {
            if (v == graph.length)
                return true;
            for (int c = 1; c <= color.length; c++) {
                if (isSafe(v, graph, color, c)) {
                    color[v] = c;
                    if (solve(graph, v + 1, color, m))
                        return true;
                    color[v] = 0;
                }
            }
            return false;
        }

        private static void display(int[] color) {
            System.out.println("Solution:");
            for (int i = 0; i < color.length; i++)
                System.out.println("Vertex: " + (i + 1) + " -> Color: " + color[i]);
        }

        public static boolean show(int[][] graph, int m) {
            int[] color = new int[graph.length];
            if (solve(graph, 0, color, m)) {
                display(color);
                return true;
            }
            System.out.println("No Solution");
            return false;
        }

    }

    public static class NQueens {
        private static boolean isSafe(int[][] board, int row, int col) {
            for (int i = row; i >= 0; i--)
                if (board[i][col] == 1)
                    return false;
            for (int i = row, j = col; i >= 0 && j >= 0; i--, j--)
                if (board[i][j] == 1)
                    return false;
            for (int i = row, j = col; i >= 0 && j < board.length; i--, j++)
                if (board[i][j] == 1)
                    return false;
            return true;
        }

        private static boolean solve(int[][] board, int row) {
            if (row >= board.length)
                return true;
            for (int i = 0; i < board.length; i++) {
                if (isSafe(board, row, i)) {
                    board[row][i] = 1;
                    if (solve(board, row + 1))
                        return true;
                    board[row][i] = 0;
                }
            }
            return false;
        }

        private static boolean solve(int[][] board) {
            return solve(board, 0);
        }

        private static void display(int[][] board) {
            for (int[] row : board) {
                for (int i : row) {
                    System.out.print(i == 1 ? "Q " : "_ ");
                }
                System.out.println();
            }
        }

        public static void show(int n) {
            int[][] board = new int[n][n];
            if (solve(board))
                display(board);
        }
    }

    public static class Hamiltonian {
        private static boolean isSafe(int[][] graph, int v, int[] path, int pos) {
            if (graph[path[pos - 1]][v] == 0)
                return false;
            for (int i = 0; i < pos; i++)
                if (path[i] == v)
                    return false;
            return true;
        }

        private static boolean solve(int[][] graph, int[] path, int pos) {
            if (pos == graph.length)
                if (graph[path[pos - 1]][path[0]] == 1)
                    return true;
                else
                    return false;
            for (int v = 0; v < path.length; v++)
                if (isSafe(graph, v, path, pos)) {
                    path[pos] = v;
                    if (solve(graph, path, pos + 1))
                        return true;
                    path[pos] = -1;
                }
            return false;
        }

        private static void display(int[] path) {
            System.out.println("Hamiltonian Cycle Path:");
            for (int i : path)
                System.out.print(i + " ");
            System.out.println();
        }

        public static boolean show(int[][] graph) {
            int[] path = new int[graph.length];
            for (int i = 0; i < path.length; i++)
                path[i] = -1;
            path[0] = 0;
            if (solve(graph, path, 1)) {
                display(path);
                return true;
            }
            System.out.println("No Solution");
            return false;
        }
    }

    public static void main(String[] args) {
        // Graph Coloring
        // int[][] graph = {
        // { 0, 1, 1, 1 },
        // { 1, 0, 1, 0 },
        // { 1, 1, 0, 1 },
        // { 1, 0, 1, 0 },
        // };
        // int m = 3;
        // GraphColor.show(graph, m);
        // N Queens
        // NQueens.show(8);
        // Hamiltonian Cycle
        int graph1[][] = { { 0, 1, 0, 1, 0 },
                { 1, 0, 1, 1, 1 },
                { 0, 1, 0, 0, 1 },
                { 1, 1, 0, 0, 1 },
                { 0, 1, 1, 1, 0 },
        };
        Hamiltonian.show(graph1);
    }
}
