import java.util.ArrayList;

public class Articulation {
    int[][] adjMat;
    int time = 0;

    Articulation(int size) {
        adjMat = new int[size][size];
    }

    void addEdge(int v1, int v2) {
        adjMat[v1][v2] = adjMat[v2][v1] = 1;
    }

    ArrayList<Integer> getAdj(int num) {
        ArrayList<Integer> list = new ArrayList<Integer>();
        for (int i = 0; i < adjMat.length; i++) {
            if (adjMat[num][i] == 1)
                list.add(i);
        }
        return list;
    }

    void solve(int u, boolean[] visited, int[] disc, int[] low, int parent, boolean[] isAP) {
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

    void show() {
        int V = adjMat.length;
        boolean[] visited = new boolean[V];
        int[] disc = new int[V], low = new int[V];
        boolean[] isAP = new boolean[V];
        int parent = -1;
        for (int u = 0; u < isAP.length; u++)
            if (visited[u] == false)
                solve(u, visited, disc, low, parent, isAP);
        display(isAP);
    }

    void display(boolean[] isAP) {
        System.out.print("Articulation Points: ");
        for (int i = 0; i < adjMat.length; i++) {
            if (isAP[i])
                System.out.print(i + " ");
        }
        System.out.println();
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

    public static void main(String[] args) {
        run();
    }
}
