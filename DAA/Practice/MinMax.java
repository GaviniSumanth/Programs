class MM {
    int min, max;
}

public class MinMax {
    static MM solve(int[] arr, int low, int high) {
        MM minmax = new MM();
        if (low == high) {
            minmax.min = minmax.max = arr[low];
        } else if (low + 1 == high) {
            if (arr[low] > arr[high]) {
                minmax.min = arr[high];
                minmax.max = arr[low];
            } else {
                minmax.min = arr[low];
                minmax.max = arr[high];
            }
        } else {
            int mid = (low + high) / 2;
            MM mml = solve(arr, low, mid);
            MM mmr = solve(arr, mid + 1, arr.length - 1);
            if (mml.min < mmr.min)
                minmax.min = mml.min;
            else
                minmax.min = mmr.min;
            if (mml.max > mmr.max)
                minmax.max = mml.max;
            else
                minmax.max = mmr.max;
        }
        return minmax;
    }

    static void show(int[] arr) {
        MM minmax = solve(arr, 0, arr.length - 1);
        display(minmax);
    }

    static void display(MM minmax) {
        System.out.println("Min:" + minmax.min);
        System.out.println("Max:" + minmax.max);
    }

    static void run() {
        int arr[] = { 1000, 11, 445, 1, 330, 3000 };
        show(arr);
    }

    public static void main(String[] args) {
        run();
    }
}
