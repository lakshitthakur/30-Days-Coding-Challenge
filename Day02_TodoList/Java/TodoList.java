import java.util.ArrayList;
import java.util.Scanner;

class Task {
    String name;
    boolean done;

    Task(String name) {
        this.name = name;
        this.done = false;
    }
}

public class TodoList {
    static ArrayList<Task> tasks = new ArrayList<>();
    static Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) {
        while (true) {
            System.out.println("\n1. Add Task\n2. View Tasks\n3. Mark as Done\n4. Delete Task\n5. Exit");
            String choice = scanner.nextLine();

            switch (choice) {
                case "1": addTask(); break;
                case "2": viewTasks(); break;
                case "3": markDone(); break;
                case "4": deleteTask(); break;
                case "5": return;
                default: System.out.println("Invalid choice!");
            }
        }
    }

    static void addTask() {
        System.out.print("Enter a new task: ");
        String taskName = scanner.nextLine();
        tasks.add(new Task(taskName));
        System.out.println("Task added!");
    }

    static void viewTasks() {
        if (tasks.isEmpty()) {
            System.out.println("No tasks found.");
            return;
        }
        for (int i = 0; i < tasks.size(); i++) {
            String status = tasks.get(i).done ? "✓" : "✗";
            System.out.println((i + 1) + ". [" + status + "] " + tasks.get(i).name);
        }
    }

    static void markDone() {
        viewTasks();
        System.out.print("Enter task number to mark as done: ");
        try {
            int index = Integer.parseInt(scanner.nextLine()) - 1;
            tasks.get(index).done = true;
            System.out.println("Task marked as done.");
        } catch (Exception e) {
            System.out.println("Invalid task number.");
        }
    }

    static void deleteTask() {
        viewTasks();
        System.out.print("Enter task number to delete: ");
        try {
            int index = Integer.parseInt(scanner.nextLine()) - 1;
            tasks.remove(index);
            System.out.println("Task deleted.");
        } catch (Exception e) {
            System.out.println("Invalid task number.");
        }
    }
}
