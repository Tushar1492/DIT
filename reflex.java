import java.util.ArrayList;
import java.util.List;

class SimpleReflexVacuumAgent {

    String location = "A";

    List<String[]> perceptSequence = new ArrayList<>();
    List<String> actions = new ArrayList<>();

    void addPercept(String location, boolean isDirty) {
        perceptSequence.add(
            new String[]{location, String.valueOf(isDirty)}
        );
    }

    void addAction(String action) {
        actions.add(action);
    }

    void executeActions() {
        for (int i = 0; i < actions.size(); i++) {

            String[] percept = perceptSequence.get(i);
            String action = actions.get(i);

            System.out.println(
                "Percept: (" + percept[0] + ", "
                + percept[1] + ") - Action: " + action
            );

            if (action.equals("Suck")) {
                System.out.println("Vacuuming dirt.");

            } else if (action.equals("MoveLeft")) {
                location = "A";
                System.out.println("Moving left to location A.");

            } else if (action.equals("MoveRight")) {
                location = "B";
                System.out.println("Moving right to location B.");

            } else if (action.equals("DoNothing")) {
                System.out.println("Doing nothing.");
            }
        }
    }

    static SimpleReflexVacuumAgent simpleReflexVacuumAgent(
            String[][] perceptSequence) {

        SimpleReflexVacuumAgent agent =
            new SimpleReflexVacuumAgent();

        for (String[] percept : perceptSequence) {

            String location = percept[0];
            boolean isDirty = Boolean.parseBoolean(percept[1]);

            agent.addPercept(location, isDirty);

            if (isDirty) {
                agent.addAction("Suck");
            } else {
                if (location.equals("A")) {
                    agent.addAction("MoveRight");
                } else if (location.equals("B")) {
                    agent.addAction("MoveLeft");
                }
            }
        }

        return agent;
    }

    public static void main(String[] args) {

        String[][] perceptSequence = {
            {"A", "true"},
            {"A", "false"},
            {"B", "true"},
            {"B", "false"}
        };

        SimpleReflexVacuumAgent agent =
            simpleReflexVacuumAgent(perceptSequence);

        agent.executeActions();
    }
}