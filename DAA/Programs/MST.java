package Programs;

import java.util.List;

public class MST {
    static class Prims {
        private final int vertices;

        Prims(int vertices) {
            this.vertices = vertices;
        }

        private int minKey(int[] key, boolean[] mstSet) {
            int min = Integer.MAX_VALUE, min_index = -1;
            for (int v = 0; v < vertices; v++) {
                if (mstSet[v] == false && key[v] < min) {
                    min = key[v];
                    min_index = v;
                }
            }
            return min_index;
        }

        private void display(int[] parent, int[][] graph) {
            System.out.println("Edge \tWeight");
            for (int v = 1; v < vertices; v++)
                System.out.println(
                        parent[v] + " - " + v + "\t" + graph[v][parent[v]]);
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
                int u = minKey(key, mstSet);
                mstSet[u] = true;
                for (int v = 0; v < vertices; v++) {
                    if (graph[u][v] != 0 &&
                            mstSet[v] == false &&
                            graph[u][v] < key[v]) {
                        parent[v] = u;
                        key[v] = graph[u][v];
                    }
                }
            }
            display(parent, graph);
        }
    }

    static class Kruskals {
        private final int vertices;

        Kruskals(int vertices) {
            this.vertices = vertices - 1;
        }

        public static class Edge implements Comparable<Edge> {
            int src, dest, weight;

            public Edge(int src, int dest, int weight) {
                this.src = src;
                this.dest = dest;
                this.weight = weight;
            }

            public int compareTo(Edge e) {
                return this.weight - e.weight;
            }
        }

        private static class Subset {
            int parent, rank;

            public Subset(int parent, int rank) {
                this.parent = parent;
                this.rank = rank;
            }
        }

        private static void display(Edge[] results, int edge_count) {
            int minCost = 0;
            for (int i = 0; i < edge_count; i++) {
                System.out.println(results[i].src + " -- "
                        + results[i].dest + " == "
                        + results[i].weight);
                minCost += results[i].weight;
            }
            System.out.println("Total cost of MST: " + minCost);
        }

        public void show(List<Edge> edges) {
            Subset[] subsets = new Subset[vertices];
            Edge[] results = new Edge[vertices];
            for (int v = 0; v < vertices; v++) {
                subsets[v] = new Subset(v, 0);
            }

            int edge_count = 0, i = 0;
            while (edge_count < vertices - 1) {
                Edge nextEdge = edges.get(i);
                int x = findRoot(subsets, nextEdge.src);
                int y = findRoot(subsets, nextEdge.dest);
                if (x != y) {
                    results[edge_count] = nextEdge;
                    union(subsets, x, y);
                    edge_count++;
                }
                i++;
            }
            display(results, edge_count);
        }

        private static void union(Subset[] subsets, int x, int y) {
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

        private static int findRoot(Subset[] subsets, int i) {
            if (subsets[i].parent == i)
                return subsets[i].parent;
            subsets[i].parent = findRoot(subsets, subsets[i].parent);
            return subsets[i].parent;
        }
    }
}