class GraphColor {
    static boolean isSafe(int[][] graph, int v, int[] color, int c) {
        for (int i = 0; i < graph.length; i++)
            if (graph[v][i] == 1 && color[i] == c)
                return false;
        return true;
    }

    static boolean solve(int[][] graph, int v, int[] color, int m) {
        if (v >= graph.length)
            return true;
        for (int c = 1; c <= m; c++) {
            if (isSafe(graph, v, color, c)) {
                color[v] = c;
                if (solve(graph, v + 1, color, m))
                    return true;
                color[v] = 0;
            }
        }
        return false;
    }

    static void show(int[][] graph, int m) {
        int[] color = new int[graph.length];
        if (solve(graph, 0, color, m))
            display(color);
        else
            System.out.println("Colors are not sufficient.");
    }

    static void display(int[] color) {
        System.out.println("Graph Colors:");
        for (int i : color)
            System.out.print(i + " ");
        System.out.println();
    }

    static void run() {
        int[][] graph = {
                { 0, 1, 1, 1 },
                { 1, 0, 1, 0 },
                { 1, 1, 0, 1 },
                { 1, 0, 1, 0 },
        };
        int m = 3;
        show(graph, m);
    }

    public static void main(String[] args) {
        run();
    }
}