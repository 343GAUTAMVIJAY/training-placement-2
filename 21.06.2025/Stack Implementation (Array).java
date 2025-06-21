public class Stack {
    private int maxSize;
    private int[] stackArray;
    private int top;
    
    public Stack(int size) {
        maxSize = size;
        stackArray = new int[maxSize];
        top = -1;
    }
    
    public void push(int value) {
        if (top < maxSize - 1) {
            stackArray[++top] = value;
            System.out.println("Pushed: " + value);
        } else {
            System.out.println("Stack is full!");
        }
    }
    
    public int pop() {
        if (top >= 0) {
            int value = stackArray[top--];
            System.out.println("Popped: " + value);
            return value;
        } else {
            System.out.println("Stack is empty!");
            return -1;
        }
    }
    
    public static void main(String[] args) {
        Stack stack = new Stack(5);
        stack.push(1);
        stack.push(2);
        stack.push(3);
        stack.pop();
        stack.pop();
    }
}