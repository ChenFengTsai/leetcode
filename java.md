1. HashMap:

Map<Character, Integer> map = new HashMap<>();
map.add("Age", 30);
map.remove("Age");
map.get("Age");
map.containsKey("Age");

2. Stack: 

Stack<Character> stack = new Stack<>();
stack.push(30);
stack.pop();
stack.peek();

3. List:

List<Integer> myList = new ArrayList<>();
myList.add(30);
myList.add(0, 25); ## Add at index 0 position
myList.remove(30);
myList.size(); //length of the list
myList.subList(1, myList.size());

4. Array:

int[]{1,2,3}
int[] myArray = {1, 2, 3, 4, 5}; //not assign value before
myArray = new int[]{3,4,5,6,7}; //assigned value already
int length = myArray.length; // length is 5
int second = myArray[2];

5. Set:
Set<Integer> mySet = new HashSet<>();
mySet.add(30);
mySet.remove(30);

6. String:
s.length();
char currentChar = s.charAt(i);
s.insert(5, ", ");

## create String
StringBuilder result = new StringBuilder();
for (char ch : stack) {
    result.append(ch);
}
result.toString();

s.toCharArray(); # make string to char array

7. Priority Queue (Heap):
MinHeap:
PriorityQueue<Integer> minHeap = new PriorityQueue<>();

MaxHeap:
PriorityQueue<Integer> maxHeap = new PriorityQueue<>(Collections.reverseOrder());

Save list in Heap node:
PriorityQueue<int[]> heap = new PriorityQueue<>((a, b) -> a[0] - b[0]);

# push onto heap 
heap.offer(ele);
heap.offer(new int[]{total_time, t, i}); # save multiple element in heap node

# pop the smallest in minheap
heap.poll();

# look at the min value
heap.peek()

8. Deque:
Deque<int> q = new ArrayDeque<>();
q.offer(3); # push to deque
p = q.pollFirst(); # pop out

100. Misc
myList.isEmpty();
mySet.isEmpty();
map.isEmpty();
stack.isEmpty();