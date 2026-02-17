class Solution {
    public boolean isValid(String s) {
        Stack<Character> stk = new Stack<>();
        HashMap<Character, Character> mappings = new HashMap<>();
        mappings.put('}', '{');
        mappings.put(']', '[');
        mappings.put(')', '(');

        for (char c : s.toCharArray()) {
            if (mappings.containsValue(c)) {
                stk.push(c);
            } else if (mappings.containsKey(c)) {
                if (stk.isEmpty() || mappings.get(c) != stk.pop()) {
                    return false;
                }
            }
        }

        return stk.isEmpty();
    }
}