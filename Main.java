public class Main {
    public static void main(String[] args) {
        System.out.println("=== ClassAverageCalculation Tests ===");
        
        // Test ClassAverageCalculation with 2 scores
        ClassAverageCalculation calc1 = new ClassAverageCalculation();
        double avg2 = calc1.calculateClassAverage(85.5, 92.0);
        System.out.println("Average of 2 scores (85.5, 92.0): " + avg2);
        
        // Test ClassAverageCalculation with 3 scores
        double avg3 = calc1.calculateClassAverage(75.0, 82.5, 90.0);
        System.out.println("Average of 3 scores (75.0, 82.5, 90.0): " + avg3);
        
        // Test ClassAverageCalculation with array of scores
        double[] scores = {70.0, 85.0, 90.0, 95.0, 80.0};
        double avgArray = calc1.calculateClassAverage(scores);
        System.out.println("Average of array " + java.util.Arrays.toString(scores) + ": " + avgArray);
        
        System.out.println("\n=== StudentGrading Tests ===");
        
        // Test StudentGrading with different scores
        StudentGrading grading = new StudentGrading();
        
        double[] testScores = {95.0, 82.5, 72.0, 65.0, 55.0, 48.0, 42.0, -5.0};
        
        for (double score : testScores) {
            System.out.print("Score: " + score + " -> ");
            grading.executeGradeReport(score);
        }
    }
}

