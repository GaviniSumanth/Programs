class Knapsack {
    static int max(int a, int b) {
        return (a > b) ? a : b;
    }

    static int solve(int M, int[] weights, int[] profits, int n) {
        if (n == 0 || M == 0)
            return 0;
        if (weights[n] > M)
            return solve(M, weights, profits, n - 1);
        else
            return max(profits[n] + solve(M - weights[n], weights, profits, n - 1), solve(M, weights, profits, n - 1));
    }

    static void show(int M, int[] weights, int[] profits) {
        int profit = solve(M, weights, profits, profits.length - 1);
        System.out.println("Max. Profit: " + profit);
    }

    public static void main(String[] args) {
        int profits[] = { 60, 100, 120 };
        int weights[] = { 10, 20, 30 };
        int M = 50;
        show(M, weights, profits);
    }
}