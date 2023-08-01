import java.util.*;

class Item {
    float weight;
    int value;
    int idx;

    public Item(int value, float weight, int idx) {
        this.value = value;
        this.weight = weight;
        this.idx = idx;
    }
}

class Node {
    float ub, lb;
    float tv, tw;
    boolean flag;
    int level;

    public Node() {
    }

    public Node(Node cp) {
        this.tv = cp.tv;
        this.tw = cp.tw;
        this.ub = cp.ub;
        this.lb = cp.lb;
        this.level = cp.level;
        this.flag = cp.flag;
    }
}

class sortByC implements Comparator<Node> {
    public int compare(Node a, Node b) {
        return (a.lb > b.lb) ? 1 : -1;
    }
}

class sortByRatio implements Comparator<Item> {
    public int compare(Item a, Item b) {
        return (a.value / a.weight > b.value / b.weight) ? -1 : 1;
    }
}

public class Knapsack {
    private static float capacity;

    private static float upperBound(float tv, float tw, int idx, Item arr[]) {
        float value = tv, weight = tw;
        for (int i = idx; i < arr.length; i++) {
            if (weight + arr[i].weight <= capacity) {
                weight += arr[i].weight;
                value -= arr[i].value;
            } else {
                value -= (float) (capacity - weight) / arr[i].weight * arr[i].value;
                break;
            }
        }
        return value;
    }

    private static float lowerBound(float tv, float tw, int idx, Item arr[]) {
        float value = tv, weight = tw;
        for (int i = idx; i < arr.length; i++)
            if (weight + arr[i].weight <= capacity) {
                weight += arr[i].weight;
                value -= arr[i].value;
            } else
                break;
        return value;
    }

    private static void assign(Node a, float ub, float lb, int level, boolean flag, float tv, float tw) {
        a.ub = ub;
        a.lb = lb;
        a.level = level;
        a.flag = flag;
        a.tv = tv;
        a.tw = tw;
    }

    private static void solve(Item arr[]) {
        Arrays.sort(arr, new sortByRatio());
        Node current = new Node(), left = new Node(), right = new Node();
        float minLB = 0, finalLB = Integer.MAX_VALUE;
        current.tv = current.tw = current.ub = current.lb = 0;
        current.level = 0;
        current.flag = false;
        PriorityQueue<Node> pq = new PriorityQueue<Node>(new sortByC());
        pq.add(current);
        boolean currPath[] = new boolean[arr.length];
        boolean finalPath[] = new boolean[arr.length];
        while (!pq.isEmpty()) {
            current = pq.poll();
            if (current.ub > minLB || current.ub >= finalLB) {
                continue;
            }
            if (current.level != 0)
                currPath[current.level - 1] = current.flag;
            if (current.level == arr.length) {
                if (current.lb < finalLB) {
                    for (int i = 0; i < arr.length; i++)
                        finalPath[arr[i].idx] = currPath[i];
                    finalLB = current.lb;
                }
                continue;
            }
            int level = current.level;
            assign(right, upperBound(current.tv, current.tw, level + 1, arr),
                    lowerBound(current.tv, current.tw, level + 1, arr), level + 1, false, current.tv, current.tw);
            if (current.tw + arr[current.level].weight <= capacity) {
                left.ub = upperBound(
                        current.tv - arr[level].value,
                        current.tw + arr[level].weight,
                        level + 1,
                        arr);
                left.lb = lowerBound(
                        current.tv - arr[level].value,
                        current.tw + arr[level].weight,
                        level + 1,
                        arr);
                assign(left, left.ub, left.lb, level + 1, true, current.tv - arr[level].value,
                        current.tw + arr[level].weight);
            } else
                left.ub = left.lb = 1;
            minLB = Math.min(minLB, left.lb);
            minLB = Math.min(minLB, right.lb);
            if (minLB >= left.ub)
                pq.add(new Node(left));
            if (minLB >= right.ub)
                pq.add(new Node(right));
        }
        display(finalPath, finalLB);
    }

    private static void display(boolean[] finalPath, float finalLB) {
        System.out.println("Items taken into the knapsack are");
        for (int i = 0; i < finalPath.length; i++)
            System.out.print(finalPath[i] ? "1 " : "0 ");
        System.out.println("\nMaximum profit is " + (-finalLB));
    }

    public static void show(int capacity) {
        Knapsack.capacity = capacity;
        Item arr[] = new Item[4];
        arr[0] = new Item(10, 2, 0);
        arr[1] = new Item(10, 4, 1);
        arr[2] = new Item(12, 6, 2);
        arr[3] = new Item(18, 9, 3);
        solve(arr);
    }

    public static void main(String args[]) {
        show(15);
    }
}