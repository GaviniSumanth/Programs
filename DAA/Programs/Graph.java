package Programs;

import java.util.Iterator;
import java.util.LinkedList;

public class Graph {
    private LinkedList<Integer> adj[];

    @SuppressWarnings("unchecked")
    public Graph(int size) {
        adj = new LinkedList[size];
        for (int i = 0; i < adj.length; i++) {
            adj[i] = new LinkedList<Integer>();
        }
    }

    public void addEdge(int src, int dest) {
        adj[src].add(dest);
    }

    public void bfs(int v) {
        boolean[] visited = new boolean[adj.length];
        visited[v] = true;
        LinkedList<Integer> queue = new LinkedList<Integer>();
        queue.add(v);
        System.out.println("BFS:");
        while (queue.size() != 0) {
            v = queue.poll();
            System.out.print(v + " ");
            Iterator<Integer> i = adj[v].listIterator();
            while (i.hasNext()) {
                int n = i.next();
                if (!visited[n]) {
                    visited[n] = true;
                    queue.add(n);
                }
            }
        }
        System.out.println();
    }

    private void dfs(int v, boolean[] visited) {
        visited[v] = true;
        System.out.print(v + " ");
        Iterator<Integer> i = adj[v].listIterator();
        while (i.hasNext()) {
            int n = i.next();
            if (!visited[n])
                dfs(n, visited);
        }
    }

    public void dfs(int v) {
        boolean[] visited = new boolean[adj.length];
        System.out.println("DFS:");
        dfs(v, visited);
        System.out.println();

    }

    public static void run() {
        Graph g = new Graph(4);
        g.addEdge(0, 1);
        g.addEdge(0, 2);
        g.addEdge(1, 2);
        g.addEdge(2, 0);
        g.addEdge(2, 3);
        g.addEdge(3, 3);
        // Breadth First Search
        g.bfs(2);
        // Depth First Search
        g.dfs(2);
    }
}
