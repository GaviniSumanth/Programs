import java.util.ArrayList;
import java.util.Comparator;

public class Kruskals {
    int vertices;

    Kruskals(int vertices) {
        this.vertices = vertices - 1;
    }

    static class Edge implements Comparable<Edge> {
        int src, dest, weight;

        Edge(int src, int dest, int weight) {
            this.src = src;
            this.dest = dest;
            this.weight = weight;
        }

        public int compareTo(Edge e) {
            return this.weight - e.weight;
        }
    }

    static class Subset {
        int parent, rank;

        Subset(int parent, int rank) {
            this.parent = parent;
            this.rank = rank;
        }
    }

    void display(Edge[] results, int edge_count) {
        int minCost = 0;
        for (int i = 0; i < edge_count; i++) {
            Edge e = results[i];
            System.out.println(e.src + " -> " + e.dest + " -- " + e.weight);
            minCost += e.weight;
        }
        System.out.println("Total cost of MST: " + minCost);
    }

    void show(ArrayList<Edge> edges) {
        Subset[] subsets = new Subset[vertices];
        Edge[] results = new Edge[vertices];
        for (int v = 0; v < vertices; v++) {
            subsets[v] = new Subset(v, 0);
        }
        int edge_count = 0, i = 0;
        while (edge_count < vertices - 1) {
            Edge e = edges.get(i);
            int rootX = findRoot(subsets, e.src);
            int rootY = findRoot(subsets, e.dest);
            if (rootX != rootY) {
                results[edge_count] = e;
                union(subsets, rootX, rootY);
                edge_count++;
            }
            i++;
        }
        display(results, edge_count);
    }

    void union(Subset[] subsets, int x, int y) {
        int rootX = findRoot(subsets, x);
        int rootY = findRoot(subsets, y);

        if (subsets[rootY].rank < subsets[rootX].rank) {
            subsets[rootY].parent = rootX;
        } else if (subsets[rootX].rank < subsets[rootY].rank) {
            subsets[rootX].parent = rootY;
        } else {
            subsets[rootY].parent = rootX;
            subsets[rootX].rank++;
        }
    }

    int findRoot(Subset[] subsets, int i) {
        if (subsets[i].parent == i)
            return subsets[i].parent;
        subsets[i].parent = findRoot(subsets, subsets[i].parent);
        return subsets[i].parent;
    }

    static void run() {
        ArrayList<Edge> edges = new ArrayList<Edge>();
        edges.add(new Edge(0, 1, 10));
        edges.add(new Edge(0, 2, 6));
        edges.add(new Edge(0, 3, 5));
        edges.add(new Edge(1, 3, 15));
        edges.add(new Edge(2, 3, 4));
        edges.sort(new Comparator<Edge>() {
            @Override
            public int compare(Edge o1, Edge o2) {
                return o1.weight - o2.weight;
            }
        });
        Kruskals k = new Kruskals(edges.size());
        k.show(edges);

    }

    public static void main(String[] args) {
        run();
    }
}
