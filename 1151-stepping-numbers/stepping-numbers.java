class Solution {
    private List<Integer> results;

    public List<Integer> countSteppingNumbers(int low, int high) {
        results = new ArrayList<>();
        if (low == 0) {
            results.add(0);
        }

        Deque<Long> qu = new ArrayDeque<>();
        for (long i = 1; i < 10; i++) {
            qu.offer(i);
        }

        while (!qu.isEmpty()) {
            long currentNumber = qu.pollFirst();

            if (currentNumber > high) {
                break;
            }
            if (currentNumber >= low) {
                results.add((int) currentNumber);
            }

            int lastDigit = (int) (currentNumber % 10);

            if (lastDigit > 0) {
                qu.offer(currentNumber * 10 + lastDigit - 1);
            }
            if (lastDigit < 9) {
                qu.offer(currentNumber * 10 + lastDigit + 1);
            }
        }
        return results;
    }
}