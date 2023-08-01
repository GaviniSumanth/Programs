package Programs;

public class MinMax {
    static class Pair {
        int min, max;
    }

    private static Pair get(int[] arr, int low, int high) {
        Pair minmax = new Pair();
        if (low == high) {
            minmax.min = arr[low];
            minmax.max = arr[low];
            return minmax;
        } else if (low + 1 == high) {
            if (arr[low] < arr[high]) {
                minmax.min = arr[low];
                minmax.max = arr[high];
            } else {
                minmax.min = arr[high];
                minmax.max = arr[low];
            }
        }
        int mid = (low + high) / 2;
        Pair mml = get(arr, low, mid), mmr = get(arr, mid + 1, high);
        if (mml.max > mmr.max)
            minmax.max = mml.max;
        else
            minmax.max = mmr.max;
        if (mml.min < mmr.min)
            minmax.min = mml.min;
        else
            minmax.min = mmr.min;
        return minmax;
    }

    public static int[] get(int[] arr) {
        Pair p = get(arr, 0, arr.length - 1);
        int[] a = { p.min, p.max };
        return a;
    }
}