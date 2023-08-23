public class MergeSort {
    static void merge(int[] arr, int left, int mid, int right) {
        int leftSize = mid - left + 1, rightSize = right - mid;
        int[] L = new int[leftSize], R = new int[rightSize];

        for (int i = 0; i < leftSize; i++)
            L[i] = arr[left + i];
        for (int i = 0; i < rightSize; i++)
            R[i] = arr[mid + 1 + i];

        int i, j, k;
        i = j = 0;
        k = left;
        while (i < leftSize && j < rightSize) {
            if (L[i] < R[j]) {
                arr[k] = L[i];
                i++;
            } else {
                arr[k] = R[j];
                j++;
            }
            k++;
        }
        while (i < leftSize) {
            arr[k] = L[i];
            i++;
            k++;
        }
        while (j < rightSize) {
            arr[k] = R[j];
            j++;
            k++;
        }
    }

    static void sort(int[] arr, int left, int right) {
        if (left < right) {
            int mid = (left + right) / 2;
            sort(arr, left, mid);
            sort(arr, mid + 1, right);
            merge(arr, left, mid, right);
        }

    }

    public static void main(String[] args) {
        int[] arr = { 12, 11, 13, 5, 6, 7 };
        sort(arr, 0, arr.length - 1);
        for (int i : arr)
            System.out.print(i + " ");
        System.out.println();
    }
}
