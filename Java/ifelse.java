class ifelse {
    
    public static void main(String[] args) {
        int age;
        age = 9;
        if (age >= 18) {
            System.out.println("You are eligible to vote");
        }
        else {
            System.out.println("You are not eligible to vote");
        }
        
        System.out.println(age >=18 ? "You are eligible to vote" : "You are not eligible to vote");
    }
}