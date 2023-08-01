package Programs;

import java.util.ArrayList;

class Articulation {
    private int[][] adjMat;
    private int time = 0;

    Articulation(int size) {
        adjMat = new int[size][size];
    }

    public void addEdge(int u, int v) {
        adjMat[u][v] = 1;
        adjMat[v][u] = 1;
    }

    private ArrayList<Integer> getAdj(int i) {
        ArrayList<Integer> list = new ArrayList<Integer>();
        for (int num = 0; num < adjMat.length; num++) {
            if (adjMat[i][num] == 1)
                list.add(num);
        }
        return list;
    }

    private void solve(int u, boolean visited[], int disc[], int low[], int parent, boolean isAP[]) {
        int children = 0;
        visited[u] = true;
        disc[u] = low[u] = ++time;
        for (int v : getAdj(u)) {
            if (!visited[v]) {
                children++;
                solve(v, visited, disc, low, u, isAP);
                low[u] = Math.min(low[u], low[v]);
                if (parent != -1 && low[v] >= disc[u])
                    isAP[u] = true;
            } else if (v != parent)
                low[u] = Math.min(low[u], disc[v]);
        }
        if (parent == -1 && children > 1)
            isAP[u] = true;
    }

    private void display(boolean[] isAP) {
        System.out.println("Articulation points:");
        for (int u = 0; u < isAP.length; u++)
            if (isAP[u])
                System.out.print(u + " ");
        System.out.println();
    }

    public void show() {
        int V = adjMat.length;
        boolean[] visited = new boolean[V];
        int[] disc = new int[V];
        int[] low = new int[V];
        boolean[] isAP = new boolean[V];
        int par = -1;
        for (int u = 0; u < V; u++)
            if (visited[u] == false)
                solve(u, visited, disc, low, par, isAP);
        display(isAP);
    }

    public static void run() {
        // Program 1
        Articulation art1 = new Articulation(5);
        art1.addEdge(1, 0);
        art1.addEdge(0, 2);
        art1.addEdge(2, 1);
        art1.addEdge(0, 3);
        art1.addEdge(3, 4);
        art1.show();

        // Program 2
        Articulation art2 = new Articulation(4);
        art2.addEdge(0, 1);
        art2.addEdge(1, 2);
        art2.addEdge(2, 3);
        art2.show();

        // Program 3
        Articulation art3 = new Articulation(7);
        art3.addEdge(0, 1);
        art3.addEdge(1, 2);
        art3.addEdge(2, 0);
        art3.addEdge(1, 3);
        art3.addEdge(1, 4);
        art3.addEdge(1, 6);
        art3.addEdge(3, 5);
        art3.addEdge(4, 5);
        art3.show();
    }
}
