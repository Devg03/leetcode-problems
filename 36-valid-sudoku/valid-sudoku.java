class Solution {
    public boolean isValidSudoku(char[][] board) {
        int N = 9;
        HashSet<Character>[] rows = new HashSet[N];
        HashSet<Character>[] cols = new HashSet[N];
        HashSet<Character>[] boxes = new HashSet[N];

        for (int i = 0; i < N; i++) {
            rows[i] = new HashSet<Character>();
            cols[i] = new HashSet<Character>();
            boxes[i] = new HashSet<Character>();
        }

        for (int r = 0; r < N; r++) {
            for (int c = 0; c < N; c++) {
                char cell = board[r][c];

                if (cell == '.') continue;
                
                if (rows[r].contains(cell)) return false;
                rows[r].add(cell);

                if (cols[c].contains(cell)) return false;
                cols[c].add(cell);

                int idx = (r/3) * 3 + (c/3);
                if (boxes[idx].contains(cell)) return false;
                boxes[idx].add(cell);
            }
        }
        return true;
    }
}