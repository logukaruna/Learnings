

import java.time.*;
import java.time.format.DateTimeFormatter;
import java.time.format.DateTimeParseException;
import java.time.temporal.ChronoUnit;
import java.util.*;
public class Days {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        LocalDate dt1 = null;
        LocalDate dt2 = null;
        DateTimeFormatter formatter = DateTimeFormatter.ofPattern("d/M/yyyy");
        System.out.println("Enter Date 1: ");
        while (dt1 == null) {
            String date1 = input.nextLine();
            try {
                dt1 = LocalDate.parse(date1, formatter);
            } catch (DateTimeParseException e) {
                System.out.println("Invaild Date Format, Enter date in this format DD/MM/YYYY");
            }
        }
        System.out.println("Enter Date 2: ");
        while (dt2 == null) {
            String date2 = input.nextLine();
            try {
                dt2 = LocalDate.parse(date2, formatter);
            } catch (DateTimeParseException e) {
                System.out.println("Invaild Date Format, Enter Date in this format DD/MM/YYYY");
            }
        }

        long days = ChronoUnit.DAYS.between(dt1, dt2);
        System.out.println("The days between " + dt1 +" and " + dt2 + " is: " + days);
    }
}
