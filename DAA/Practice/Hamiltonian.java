public class Hamiltonian {
    static boolean isSafe(int[][] graph, int v, int[] path, int pos) {
        if (graph[path[pos - 1]][v] == 0)
            return false;
        for (int i = 0; i < path.length; i++) {
            if (v == path[i])
                return false;
        }
        return true;
    }

    static boolean solve(int[][] graph, int[] path, int pos) {
        if (pos >= graph.length)
            if (graph[path[pos - 1]][path[0]] == 1)
                return true;
            else
                return false;
        for (int i = 0; i < path.length; i++) {
            if (isSafe(graph, i, path, pos)) {
                path[pos] = i;
                if (solve(graph, path, pos + 1))
                    return true;
                path[pos] = 0;
            }
        }
        return false;
    }

    static void show(int[][] graph) {
        int[] path = new int[graph.length];
        for (int i = 0; i < path.length; i++)
            path[i] = -1;
        path[0] = 0;
        if (solve(graph, path, 1))
            display(path);
        else
            System.out.println("Hamiltonian Path does not exist.");
    }

    static void display(int[] path) {
        System.out.println("Hamiltonian Path:");
        for (int i : path)
            System.out.print(i + " ");
        System.out.println(0);
    }

    static void run() {
        int graph1[][] = { { 0, 1, 0, 1, 0 },
                { 1, 0, 1, 1, 1 },
                { 0, 1, 0, 0, 1 },
                { 1, 1, 0, 0, 1 },
                { 0, 1, 1, 1, 0 },
        };
        Hamiltonian.show(graph1);
    }

    public static void main(String[] args) {
        run();
    }
}
