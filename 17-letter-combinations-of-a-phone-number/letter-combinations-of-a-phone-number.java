class Solution {
    private Map<Character, String> mappings = Map.of(
    '2',"abc",
    '3',"def",
    '4',"ghi",
    '5',"jkl",
    '6',"mno",
    '7',"pqrs",
    '8',"tuv",
    '9',"wxyz"
    );

    private List<String> combos = new ArrayList<>();
    private String phoneDigits;
    public List<String> letterCombinations(String digits) {
        if (digits.isEmpty()) return combos;
        this.phoneDigits = digits;

        backtrack(0, new StringBuilder());
        return combos;
    }

    public void backtrack(int index, StringBuilder path) {
        if (path.length() == phoneDigits.length()) {
            combos.add(path.toString());
            return;
        }

        String possibleLetters = mappings.get(phoneDigits.charAt(index));
        for (char letter : possibleLetters.toCharArray()) {
            path.append(letter);
            backtrack(index + 1, path);
            path.deleteCharAt(path.length() - 1);
        }
    }
}