import java.util.*;

public class Job {
    String id;
    int deadline, profit;

    public Job() {
    }

    public Job(String id, int deadline, int profit) {
        this.id = id;
        this.deadline = deadline;
        this.profit = profit;
    }

    void showSchedule(ArrayList<Job> jobs, int t) {
        Collections.sort(jobs, (a, b) -> b.profit - a.profit);

        boolean[] result = new boolean[t];
        String[] job = new String[t];
        for (int i = 0; i < jobs.size(); i++)
            for (int j = Math.min(t, jobs.get(i).deadline) - 1; j >= 0; j--)
                if (result[j] == false) {
                    result[j] = true;
                    job[j] = jobs.get(i).id;
                    break;
                }

        for (String j : job)
            System.out.print(j + " ");
        System.out.println();
    }

    public static void main(String[] args) {
        ArrayList<Job> jobs = new ArrayList<Job>();

        jobs.add(new Job("a", 2, 100));
        jobs.add(new Job("b", 1, 19));
        jobs.add(new Job("c", 2, 27));
        jobs.add(new Job("d", 1, 25));
        jobs.add(new Job("e", 3, 15));
        new Job().showSchedule(jobs, 3);
    }
}
