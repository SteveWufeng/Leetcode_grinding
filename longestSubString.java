import java.util.HashSet;

// problem 3
public class longestSubString {
    public int lengthOfLongestSubstring(String s) {
        HashSet<Character> window = new HashSet<>();
        int lIndex = 0;
        int longestLen = 0;
        
        for (int rIndex = 0; rIndex < s.length(); rIndex++) {
            // as long as duplicate is found in window
            while (window.contains(s.charAt(rIndex))) {
                window.remove(s.charAt(lIndex));
                lIndex++;
            } // this is needed to guarantee our window does not contain duplicates
            window.add(s.charAt(rIndex));
            longestLen = (longestLen > window.size()) ? longestLen : window.size();
        }

        return longestLen;
    }

    public static void main(String[] args) {
        longestSubString solution = new longestSubString();
        int answer = solution.lengthOfLongestSubstring("abcabcdbb");
        System.out.println(answer);
    }
}
