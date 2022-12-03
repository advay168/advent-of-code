import Data.List (intersect)

main = do
  all_data <- readFile "./input.txt"
  print $ answerFunc all_data

answerFunc :: String -> Int
answerFunc all_data =
  let lined = lines all_data
      priorities = map (priority . common . split) lined
   in sum priorities

split :: String -> (String, String)
split lst = splitAt (length lst `div` 2) lst

common :: (String, String) -> Char
common (a, b) = head $ intersect a b

priority :: Char -> Int
priority 'a' = 1
priority 'b' = 2
priority 'c' = 3
priority 'd' = 4
priority 'e' = 5
priority 'f' = 6
priority 'g' = 7
priority 'h' = 8
priority 'i' = 9
priority 'j' = 10
priority 'k' = 11
priority 'l' = 12
priority 'm' = 13
priority 'n' = 14
priority 'o' = 15
priority 'p' = 16
priority 'q' = 17
priority 'r' = 18
priority 's' = 19
priority 't' = 20
priority 'u' = 21
priority 'v' = 22
priority 'w' = 23
priority 'x' = 24
priority 'y' = 25
priority 'z' = 26
priority 'A' = 27
priority 'B' = 28
priority 'C' = 29
priority 'D' = 30
priority 'E' = 31
priority 'F' = 32
priority 'G' = 33
priority 'H' = 34
priority 'I' = 35
priority 'J' = 36
priority 'K' = 37
priority 'L' = 38
priority 'M' = 39
priority 'N' = 40
priority 'O' = 41
priority 'P' = 42
priority 'Q' = 43
priority 'R' = 44
priority 'S' = 45
priority 'T' = 46
priority 'U' = 47
priority 'V' = 48
priority 'W' = 49
priority 'X' = 50
priority 'Y' = 51
priority 'Z' = 52
