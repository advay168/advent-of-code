import Data.List (foldl', intersect)
import System.IO

main = do
  all_data <- readFile "./input.txt"
  print $ answerFunc all_data

split :: Char -> String -> [String]
split delimeter xs = case break (== delimeter) xs of
  (word, "") -> [word]
  (word, _ : rs) -> word : split delimeter rs

parseLine :: String -> ([Int], [Int])
parseLine line =
  let [_, draw] = split ':' line
      [winners, mine] = map words $ split '|' draw
   in (map read winners, map read mine)

common :: [Int] -> [Int] -> Int
common = (length .) . intersect

answerFunc :: String -> Int
answerFunc all_data =
  let lined = lines all_data
      wins = map (uncurry common . parseLine) lined
   in foldl' (\s w -> s + (if w > 0 then 2 ^ (w - 1) else 0)) 0 wins
