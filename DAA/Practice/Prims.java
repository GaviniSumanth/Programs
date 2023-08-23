class Prims {
    int vertices;

    Prims(int vertices) {
        this.vertices = vertices;
    }

    int minkey(int[] key, boolean[] mstSet) {
        int min = Integer.MAX_VALUE, min_index = -1;
        for (int v = 0; v < vertices; v++)
            if (mstSet[v] == false && key[v] < min) {
                min = key[v];
                min_index = v;
            }
        return min_index;
    }

    public void show(int[][] graph) {
        int[] key = new int[vertices], parent = new int[vertices];
        boolean[] mstSet = new boolean[vertices];

        for (int i = 0; i < vertices; i++) {
            key[i] = Integer.MAX_VALUE;
            mstSet[i] = false;
        }
        key[0] = 0;
        parent[0] = -1;

        for (int i = 0; i < vertices - 1; i++) {
            int u = minkey(key, mstSet);
            mstSet[u] = true;
            for (int v = 0; v < vertices; v++)
                if (graph[u][v] != 0 && mstSet[v] == false && graph[u][v] < key[v]) {
                    parent[v] = u;
                    key[v] = graph[u][v];
                }
        }
        display(parent, graph);
    }

    void display(int[] parent, int[][] graph) {
        System.out.println("Edge \t Weight");
        for (int v = 1; v < vertices; v++) {
            System.out.println(parent[v] + "-" + v + " \t" + graph[v][parent[v]]);
        }
    }

    public static void main(String[] args) {
        int graph[][] = new int[][] { { 0, 2, 0, 6, 0 },
                { 2, 0, 3, 8, 5 },
                { 0, 3, 0, 0, 7 },
                { 6, 8, 0, 0, 9 },
                { 0, 5, 7, 9, 0 } };

        Prims p = new Prims(graph.length);
        p.show(graph);
    }
}
