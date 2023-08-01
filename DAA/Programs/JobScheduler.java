package Programs;

import java.util.ArrayList;
import java.util.Collections;

public class JobScheduler {
    static class Job implements Comparable<Job> {
        String id;
        int deadline, profit;

        public Job(String id, int deadline, int profit) {
            this.id = id;
            this.deadline = deadline;
            this.profit = profit;
        }

        public int compareTo(Job j) {
            return this.profit - j.profit;
        }
    }

    public static void showSchedule(ArrayList<Job> jobs, int t) {
        Collections.sort(jobs, Collections.reverseOrder());
        int job_count = jobs.size();

        String[] job = new String[t];
        boolean[] result = new boolean[t];
        for (int i = 0; i < job_count; i++) {
            for (int j = Math.min(t - 1, jobs.get(i).deadline - 1); j >= 0; j--)
                if (result[j] == false) {
                    result[j] = true;
                    job[j] = jobs.get(i).id;
                    break;
                }
        }
        for (String jb : job)
            System.out.print(jb + " ");
        System.out.println();
    }

}
