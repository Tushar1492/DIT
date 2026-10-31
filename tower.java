
import java.util.*;

public class tower {

    static class State {
        List<List<Integer>> pegs;
        List<String> path;

        State(List<List<Integer>> pegs, List<String> path) {
            this.pegs = pegs;
            this.path = path;
        }
    }

    static List<List<Integer>> getInitialState(int numDisks) {

        List<List<Integer>> pegs = new ArrayList<>();

        List<Integer> pegA = new ArrayList<>();

        for (int i = numDisks; i >= 1; i--) {
            pegA.add(i);
        }

        pegs.add(pegA);
        pegs.add(new ArrayList<>());
        pegs.add(new ArrayList<>());

        return pegs;
    }

    static List<List<Integer>> getGoalState(int numDisks) {

        List<List<Integer>> pegs = new ArrayList<>();

        pegs.add(new ArrayList<>());
        pegs.add(new ArrayList<>());

        List<Integer> pegC = new ArrayList<>();

        for (int i = numDisks; i >= 1; i--) {
            pegC.add(i);
        }

        pegs.add(pegC);

        return pegs;
    }

    static List<State> getSuccessors(State current) {

        List<State> successors = new ArrayList<>();

        for (int source = 0; source < 3; source++) {

            for (int target = 0; target < 3; target++) {

                if (source == target) {
                    continue;
                }

                List<Integer> sourcePeg =
                    current.pegs.get(source);

                List<Integer> targetPeg =
                    current.pegs.get(target);

                if (sourcePeg.isEmpty()) {
                    continue;
                }

                int movingDisk =
                    sourcePeg.get(sourcePeg.size() - 1);

                if (!targetPeg.isEmpty() &&
                    targetPeg.get(targetPeg.size() - 1) < movingDisk) {
                    continue;
                }

                List<List<Integer>> newPegs =
                    new ArrayList<>();

                for (List<Integer> peg : current.pegs) {
                    newPegs.add(new ArrayList<>(peg));
                }

                newPegs.get(source).remove(
                    newPegs.get(source).size() - 1
                );

                newPegs.get(target).add(movingDisk);

                String action =
                    "Peg " + (char) ('A' + source)
                    + " -> Peg " + (char) ('A' + target);

                List<String> newPath =
                    new ArrayList<>(current.path);

                newPath.add(action);

                successors.add(new State(newPegs, newPath));
            }
        }

        return successors;
    }

    static boolean isGoalState(
            List<List<Integer>> current,
            List<List<Integer>> goal) {

        return current.equals(goal);
    }

    static List<String> solveHanoiStateSpace(int numDisks) {

        List<List<Integer>> startState =
            getInitialState(numDisks);

        List<List<Integer>> goalState =
            getGoalState(numDisks);

        Queue<State> queue = new ArrayDeque<>();

        Set<List<List<Integer>>> visited = new HashSet<>();

        queue.add(new State(startState, new ArrayList<>()));

        visited.add(startState);

        while (!queue.isEmpty()) {

            State current = queue.poll();

            if (isGoalState(current.pegs, goalState)) {
                return current.path;
            }

            for (State next : getSuccessors(current)) {

                if (!visited.contains(next.pegs)) {

                    visited.add(next.pegs);

                    queue.add(next);
                }
            }
        }

        return null;
    }

    static void printSolution(int numDisks, List<String> path) {

        if (path == null) {
            System.out.println("No solution found.");
            return;
        }

        System.out.println(
            "--- Solved Tower of Hanoi for "
            + numDisks + " Disks ---"
        );

        System.out.println(
            "Minimum moves required: " + path.size()
        );

        for (int i = 0; i < path.size(); i++) {

            System.out.println(
                "Step " + (i + 1) + ": " + path.get(i)
            );
        }
    }

    public static void main(String[] args) {

        int disks = 3;

        List<String> solutionPath =
            solveHanoiStateSpace(disks);

        printSolution(disks, solutionPath);
    }
}
