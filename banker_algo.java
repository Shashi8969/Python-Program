package Cloud_lab;

import java.util.Scanner;
import java.util.*;
import java.io.*;

public class banker_algo {

    private static void findNeedValue(int[][] needArray, int[][] maxArray, int[][] allocationArray, int totalProcess,int totalResources) 
    {
        for (int i = 0; i < totalProcess; i++) {
            for (int j = 0; j < totalResources; j++) {
                needArray[i][j] = maxArray[i][j] - allocationArray[i][j];
            }
        }
    }

    // create checkSafeSystem() method to determine whether the system is in safe state or not
    static boolean checkSafeSystem(int processes[], int availableArray[], int maxArray[][], int allocationArray[][],int totalProcess, int totalResources) 
    {
        int[][] needArray = new int[totalProcess][totalResources];

        // call findNeedValue() method to calculate needArray
        findNeedValue(needArray, maxArray, allocationArray, totalProcess, totalResources);

        // all the process should be infinished in starting
        boolean[] finishProcesses = new boolean[totalProcess];

        // initialize safeSequenceArray that store safe sequenced
        int[] safeSequenceArray = new int[totalProcess];

        // initialize workArray as a copy of the available resources
        int[] workArray = new int[totalResources];

        // use for loop to copy each available resource in the workArray
        for (int i = 0; i < totalResources; i++) 
            workArray[i] = availableArray[i];

        // initialize counter variable whose value will be 0 when the system is not in the safe state or when all the processes are not finished.
        int counter = 0;

        // use loop to iterate the statements until all the processes are not finished
        while (counter < totalProcess) {
            // find infinished process which needs can be satisfied with the current work resource.
            boolean foundSafeSystem = false;
            for (int m = 0; m < totalProcess; m++) {
                if (finishProcesses[m] == false) // when process is not finished
                {
                    int j;

                    // use for loop to check whether the need of each process for all the resources is less than the work
                    for (j = 0; j < totalResources; j++)
                        if (needArray[m][j] > workArray[j]) // check need of current resource for current process with work
                            break;

                    // the value of J and totalResources will be equal when all the needs of current process are satisfied
                    if (j == totalResources) {
                        for (int k = 0; k < totalResources; k++)
                            workArray[k] += allocationArray[m][k];

                        // add current process in the safeSequenceArray
                        safeSequenceArray[counter++] = m;

                        // make this process finished
                        finishProcesses[m] = true;

                        foundSafeSystem = true;
                    }
                }
            }

            // the system will not be in the safe state when the value of the foundSafeSystem is false
            if (foundSafeSystem == false) {
                System.out.print("The system is not in the safe state because lack of resources");
                return false;
            }
        }

        // print the safe sequence
        System.out.print("The system is in safe sequence and the sequence is as follows: ");
        for (int i = 0; i < totalProcess; i++)
            System.out.print("P" + safeSequenceArray[i] + " ");

        return true;
    }

    // Main Method
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        // get Total no. of resource from user
        System.out.println("Enter total no. of processor - ");
        int numberOfProcesses = sc.nextInt();

        System.out.println("Enter total no. of resources - ");
        int numberOfResources = sc.nextInt();

        int processes[] = new int[numberOfResources];

        for (int i = 0; i < numberOfProcesses; i++) {
            processes[i] = i;
        }

        int availableArray[] = new int[numberOfResources];
        for (int i = 0; i < numberOfResources; i++) {
            System.out.println("Enter the availability of resouce " + i + " :");
            availableArray[i] = sc.nextInt();
        }

        int maxArray[][] = new int[numberOfProcesses][numberOfResources];
        for (int i = 0; i < numberOfProcesses; i++) {
            for (int j = 0; j < numberOfResources; j++) {
                System.out.println("Enter the max no. of resource " + j + " for process " + i + " :");
                maxArray[i][j] = sc.nextInt();
            }
        }

        int allocationArray[][] = new int[numberOfProcesses][numberOfResources];
        for (int i = 0; i < numberOfProcesses; i++) {
            for (int j = 0; j < numberOfResources; j++) {
                System.out.println("How many instance " + j + " are allocated to process " + i + " ?");
                allocationArray[i][j] = sc.nextInt();
            }
        }

        checkSafeSystem(processes, availableArray, maxArray, allocationArray, numberOfProcesses, numberOfResources); //Calling the method to check safe system.
    }
}
