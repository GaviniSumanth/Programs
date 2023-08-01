import java.util.Stack;

class SubSet {
    private int set[];
    private Stack<Integer> solutionSet = new Stack<Integer>();

    SubSet(int set[]) {
        this.set = set;
    }

    private void solve(int size, int s, int idx) {
        if (s > size)
            return;
        if (s == size) {
            display();
            return;
        }
        for (int i = idx; i < set.length; i++) {
            solutionSet.push(set[i]);
            solve(size, s + set[i], i + 1);
            solutionSet.pop();
        }
    }

    public void solve(int size) {
        solve(size, 0, 0);
    }

    private void display() {
        for (Integer item : solutionSet)
            System.out.print(item + " ");
        System.out.println();
    }
}

public class SubsetSum {
    public static void main(String[] args) {
        int set[] = { 10, 7, 5, 18, 12, 20, 15 };
        SubSet s = new SubSet(set);
        s.solve(30);
    }
}