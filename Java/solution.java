// class solution {
//     public boolean zoho(String s) {
//         int i = 0;
//         int j = s.length();
//         while (i<=j) {
//             if (s.charAt(i) == s.charAt(j)) {
//                 i++;
//                 j--;
//             }
//             else {
//                 return help(s, i + 1, j) || help(s, i, j - 1);
//                 System.out.println(i);
//                 System.out.println(j);
//             }
//             return true;
//         }
//     }
// }

// public boolean help(String s, int i, int j) {
//     while (i <= j) {
//         if (s.charAt(i) == s.charAt(j)) {
//             i++;
//             j--;
//         } else {
//             return false;
//         }
//         return true;
//     }
// }

// public static void main(String[] args) {
//     solution S = new solution();
//     S.zoho("abca");
// }
