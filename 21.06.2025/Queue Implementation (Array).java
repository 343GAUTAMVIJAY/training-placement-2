public class Queue {
    private int maxSize;
    private int[] queueArray;
    private int front;
    private int rear;
    private int currentSize;
    
    public Queue(int size) {
        maxSize = size;
        queueArray = new int[maxSize];
        front = 0;
        rear = -1;
        currentSize = 0;
    }
    
    public void enqueue(int value) {
        if (currentSize < maxSize) {
            if (rear == maxSize - 1) rear = -1;
            queueArray[++rear] = value;
            currentSize++;
            System.out.println("Enqueued: " + value);
        } else {
            System.out.println("Queue is full!");
        }
    }
    
    public int dequeue() {
        if (currentSize > 0) {
            int value = queueArray[front++];
            if (front == maxSize) front = 0;
            currentSize--;
            System.out.println("Dequeued: " + value);
            return value;
        } else {
            System.out.println("Queue is empty!");
            return -1;
        }
    }
    
    public static void main(String[] args) {
        Queue queue = new Queue(5);
        queue.enqueue(10);
        queue.enqueue(20);
        queue.enqueue(30);
        queue.dequeue();
        queue.dequeue();
    }
}