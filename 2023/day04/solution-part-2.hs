import Data.List (intersect)
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

runGame :: [Int] -> [Int] -> Int
runGame _ [] = 0
runGame (n : ns) (w : ws) = n + runGame new ws
  where
    new = map (+ n) (take w ns) ++ drop w ns

answerFunc :: String -> Int
answerFunc = runGame (repeat 1) . map (uncurry common . parseLine) . lines
